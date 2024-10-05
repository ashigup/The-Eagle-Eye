
from services.video_service import VideoService
from services.custom_video_service import CustomVideoService

class VideoController:
    def __init__(self):
        self.video_service = VideoService()
        self.custom_video_service = CustomVideoService()

    def generate_response(self, data):
        video_url = data.get('url')
        location = data.get('location')
        response_data = self.custom_video_service.process_video_url(video_url, location)
        return response_data