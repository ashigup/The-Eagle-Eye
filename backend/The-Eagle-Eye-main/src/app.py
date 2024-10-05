from flask import Flask, request, jsonify
from controllers.video_controller import VideoController
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

video_controller = VideoController()

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        video_url = data.get('url')
        location = data.get('location')
    
        if not video_url:
            raise KeyError('URL is required')
        if not location:
            raise KeyError('Location is required')
        
        response = video_controller.generate_response(data)
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)