import numpy as np

class SkillAssessment:
    def __init__(self):
        self.skills = {
            'stance': 0,
            'footwork': 0,
            'punch_accuracy': 0,
            'defense': 0,
            'speed': 0,
            'endurance': 0
        }
    
    def assess_stance(self, landmarks):
        """Évalue la position de combat"""
        if not landmarks:
            return 0
        
        # Points clés
        left_ankle = landmarks.get(27, {})
        right_ankle = landmarks.get(28, {})
        left_hip = landmarks.get(23, {})
        right_hip = landmarks.get(24, {})
        
        # Distance entre les pieds
        if left_ankle and right_ankle:
            foot_distance = abs(left_ankle['x'] - right_ankle['x'])
            
            # Largeur optimale des pieds : 0.15-0.25 de la largeur d'image
            if 0.15 <= foot_distance <= 0.25:
                stance_score = 95
            elif 0.1 <= foot_distance <= 0.3:
                stance_score = 75
            else:
                stance_score = 50
            
            return min(100, stance_score)
        
        return 0
    
    def assess_footwork(self, landmarks_sequence):
        """Évalue la technique des pieds"""
        if len(landmarks_sequence) < 10:
            return 0
        
        movements = 0
        for i in range(1, len(landmarks_sequence)):
            prev = landmarks_sequence[i-1]
            curr = landmarks_sequence[i]
            
            if prev and curr:
                # Détecte les mouvements de pieds
                prev_ankle = prev.get(28, {})
                curr_ankle = curr.get(28, {})
                
                if prev_ankle and curr_ankle:
                    movement = abs(prev_ankle['x'] - curr_ankle['x'])
                    if movement > 0.02:
                        movements += 1
        
        # Score basé sur la fréquence des mouvements
        score = min(100, (movements / len(landmarks_sequence)) * 200)
        return score
    
    def assess_punch_accuracy(self, punches):
        """Évalue la précision des coups"""
        if not punches:
            return 0
        
        # Coups avec vitesse constante = plus précis
        consistent_punches = sum(
            1 for p in punches 
            if 40 <= p.get('speed', 0) <= 100
        )
        
        accuracy = (consistent_punches / len(punches)) * 100
        return min(100, accuracy)
    
    def assess_defense(self, landmarks_sequence):
        """Évalue les techniques défensives"""
        if not landmarks_sequence:
            return 0
        
        defense_moves = 0
        
        for landmarks in landmarks_sequence:
            if landmarks:
                # Garde haute (mains près du visage)
                left_wrist = landmarks.get(15, {})
                right_wrist = landmarks.get(16, {})
                nose = landmarks.get(0, {})
                
                if left_wrist and right_wrist and nose:
                    left_dist = abs(left_wrist['y'] - nose['y'])
                    right_dist = abs(right_wrist['y'] - nose['y'])
                    
                    if left_dist < 0.1 and right_dist < 0.1:
                        defense_moves += 1
        
        score = min(100, (defense_moves / len(landmarks_sequence)) * 100)
        return score
    
    def calculate_overall_score(self, assessment_data):
        """Calcule le score global"""
        weights = {
            'stance': 0.2,
            'footwork': 0.2,
            'punch_accuracy': 0.25,
            'defense': 0.2,
            'speed': 0.1,
            'endurance': 0.05
        }
        
        total_score = sum(
            assessment_data.get(skill, 0) * weight
            for skill, weight in weights.items()
        )
        
        return min(100, total_score)
