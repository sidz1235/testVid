
from flask import Flask, request, send_file, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'videos'
UPLOAD_FOLDER = 'videos/'


@app.route('/sendvideo')
def send_video():
    video_name = request.args.get('video_name')
    video_file_path = os.path.join('videos', video_name , f"{video_name}.mp4")

    if os.path.exists(video_file_path):
        return send_file(video_file_path, mimetype='video/mp4')
    else:
        return jsonify({'error': 'Video not found'}), 404

    
@app.route('/videos')
def get_video_names():
    """
    Get the list of available video names.

    Returns:
        list: List of video names.
    """
    video_names = []

    # Getting all the video files in the 'videos' directory
    for root, dirs, files in os.walk('videos'):
        for file in files:
            if file.endswith('.mp4'):
                # Convert file name to human-readable format
                human_readable_name = ' '.join(part.capitalize() for part in os.path.splitext(file)[0].split('-'))
                video_names.append(human_readable_name)

    return jsonify(video_names)


@app.route('/sendvideo')
def send_video():
    """
    Send a video file.

    Returns:
        dict: Video file data.
    """
    video_name_req = request.args.get('video_name')
    # Convert the input video name to the expected format (e.g., "kobe-bryant")
    video_name = '-'.join(video_name_req.lower().split())

    video_file_path = os.path.join('videos', video_name, f"{video_name}.mp4")

    if os.path.exists(video_file_path):
        return send_file(video_file_path, mimetype='video/mp4')
    else:
        return jsonify({'error': 'Video not found'})


@app.route('/sendtext')
def send_text():
    """
    Send a text file.

    Returns:
        dict: Text file data.
    """
    text_name_req = request.args.get('text_name')
    # Convert the input text name to the expected format (e.g., "john-f-kennedy")
    text_name = '-'.join(text_name_req.lower().split())

    text_file_path = os.path.join('videos', text_name, f"{text_name}.txt")

    if os.path.exists(text_file_path):
        with open(text_file_path, 'r') as f:
            text_data = f.read()

        text_info = {
            'text_data': text_data
        }

        return jsonify(text_info)
    else:
        return jsonify({'error': 'Text file not found'})



