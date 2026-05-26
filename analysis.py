from flask import Blueprint, request, jsonify
import cv2
from models.pose_detection import PoseDetector
from models.punch_analysis import PunchAnalyzer
from models.skill_assessment import SkillAssessment
from utils.improvement_plan import ImprovementPlan
import os

bp = Blueprint('analysis', __name__, url_prefix='/api/analysis')

@bp.route('/process', methods=['POST'])
def process_video():
    """Analyse une vidéo uploadée"""
    
    data = request.get_json()
    video_id = data.get('video_id')
    filename = data.get('filename')
    
    if not filename:
        return jsonify({'error': 'Vidéo non trouvée'}), 400
    
    filepath = os.path.join('uploads', filename)
    
    if not os.path.exists(filepath):
        return jsonify({'error': 'Fichier vidéo non trouvé'}), 404
    
    # Initialisation des analyseurs
    pose_detector = PoseDetector()
    punch_analyzer = PunchAnalyzer()
    skill_assessor = SkillAssessment()
    
    # Traitement de la vidéo
    cap = cv2.VideoCapture(filepath)
    
    landmarks_sequence = []
    punches = []
    frame_count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Détection de pose
        results = pose_detector.detect_pose(frame)
        landmarks = pose_detector.get_landmarks(results)
        
        if landmarks:
            landmarks_sequence.append(landmarks)
        
        frame_count += 1
        
        # Traiter tous les 5 frames pour les punches
        if frame_count % 5 == 0:
            if len(landmarks_sequence) > 1:
                new_punches = punch_analyzer.calculate_punch_speed(
                    landmarks_sequence[-2:]
                )
                punches.extend(new_punches)
    
    cap.release()
    
    # Évaluation des compétences
    assessment_data = {
        'stance': skill_assessor.assess_stance(landmarks_sequence[-1] if landmarks_sequence else {}),
        'footwork': skill_assessor.assess_footwork(landmarks_sequence),
        'punch_accuracy': skill_assessor.assess_punch_accuracy(punches),
        'defense': skill_assessor.assess_defense(landmarks_sequence),
        'speed': min(100, (len(punches) / (frame_count / fps)) * 10) if frame_count > 0 else 0,
        'endurance': min(100, (frame_count / fps) / 180 * 100)  # Score sur 3 min
    }
    
    # Plan d'amélioration
    improvement_planner = ImprovementPlan(assessment_data)
    improvement_plan = improvement_planner.generate_plan()
    timeline = improvement_planner.get_timeline()
    
    overall_score = skill_assessor.calculate_overall_score(assessment_data)
    
    return jsonify({
        'success': True,
        'video_id': video_id,
        'analysis': {
            'duration_seconds': frame_count / fps,
            'total_frames': frame_count,
            'fps': fps,
            'punches_detected': len(punches),
            'average_punch_speed': np.mean([p['speed'] for p in punches]) if punches else 0
        },
        'skills': assessment_data,
        'overall_score': overall_score,
        'punches': punches[:20],  # Les 20 premiers coups
        'improvement_plan': improvement_plan,
        'timeline': timeline
    }), 200
