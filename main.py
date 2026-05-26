from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from routes import upload, analysis

app = Flask(__name__)
CORS(app)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max

os.makedirs(app.config['UPLOAD_FOLDER'], isfile=False)

# Routes
app.register_blueprint(upload.bp)
app.register_blueprint(analysis.bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
