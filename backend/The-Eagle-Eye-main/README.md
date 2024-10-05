# Python API Server

This project is a simple API server built using Flask that accepts a video URL and generates a similar response. 

## Project Structure

```
python-api-server
├── src
│   ├── app.py
│   ├── controllers
│   │   └── video_controller.py
│   ├── services
│   │   └── video_service.py
│   ├── models
│   │   └── video_model.py
│   └── utils
│       └── __init__.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-api-server
   ```

2. Install venv 
   ```
   brew install python3.11-venv
   python3.11 -m venv venv
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Deploy using gcloud 
   ```
   gcloud init
   gcloud app deploy
   ```
## Usage

1. Start the server:
   ```
   python src/app.py
   ```

2. Send a POST request to the `/generate` endpoint with a JSON body containing the video URL:
   ```json
   {
    "url": "https://www.youtube.com/watch?v=spV1PDKf9Rk",
    "location": "Camera in parking lot Helios Tech park, Bellandur"
   }
   ```

3. The server will respond with a similar video response.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.