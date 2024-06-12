
from flask import Flask, request, send_file, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'videos'
UPLOAD_FOLDER = 'videos/'

@app.route('/videos')
def get_video_names():
    video_names = []
    for root, dirs, files in os.walk('videos'):
        for file in files:
            if file.endswith('.mp4'):
                video_names.append(os.path.splitext(file)[0])
    return jsonify(video_names)


@app.route('/sendvideo')
def send_video():
    video_name = request.args.get('video_name')
    video_file_path = os.path.join('videos', f"{video_name}.mp4")

    if os.path.exists(video_file_path):
        return send_file(video_file_path, mimetype='video/mp4')
    else:
        return jsonify({'error': 'Video not found'}), 404

    
@app.route('/sendtext')
def send_text():
    text_name = request.args.get('text_name')
    text_file_path = os.path.join('videos', text_name, f"{text_name}.txt")

    if os.path.exists(text_file_path):
        with open(text_file_path, 'r') as f:
            text_data = f.read()

    text_info = {
        'text_data': text_data
    }

    return jsonify(text_info)



