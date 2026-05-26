from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os

bp = Blueprint('upload', __name__, url_prefix='/api/upload')

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv', 'flv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('', methods=['POST'])
def upload_video():
    """Upload une vidéo pour analyse"""
    
    if 'video' not in request.files:
        return jsonify({'error': 'Aucune vidéo fournie'}), 400
    
    file = request.files['video']
    
    if file.filename == '':
        return jsonify({'error': 'Nom de fichier vide'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Format vidéo non supporté'}), 400
    
    filename = secure_filename(file.filename)
    timestamp = str(int(time.time()))
    filename = f"{timestamp}_{filename}"
    
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    return jsonify({
        'success': True,
        'video_id': timestamp,
        'filename': filename,
        'message': 'Vidéo uploadée avec succès'
    }), 200
