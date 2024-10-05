
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting
import vonage
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

class CustomVideoService:
    def __init__(self):
        # self.video1 = Part.from_uri(
        #     mime_type="video/mp4",
        #     uri="https://www.youtube.com/watch?v=spV1PDKf9Rk",
        # )
        # self.location = "Camera in parking lot Helios Tech park, Bellandur"
        self.promptGenerator = """Look through each frame in the video carefully and answer the question.
        Only base your answers strictly on what information is available in the video attached.
        Do not make up any information that is not part of the video and do not be too verbose.
        Location of the video is location = "{location}"
        Questions:
        - Is there any crime happening, return an array having two elements : First element represents YES/No , and second element is the exact message that can forwarded over voice call to local police and add location as well"""

        self.generation_config = {
            "max_output_tokens": 8192,
            "temperature": 1,
            "top_p": 0.95,
        }

        self.safety_settings = []

        
    def process_video_url(self, video_url, location):
        prompt = self.promptGenerator.format(location = location)
        response = self.generate(video_url, prompt)
        print("============================Here is your response==================================")
        print(response)

        if response[0].strip().lower().startswith("yes"):
            self.sendSMSAlert(response[1])
            self.sendVoiceAlert(response[1])
        # Logic to process the video URL and extract relevant information
        # For demonstration, we will return a mock response
        return {
            "title": "Sample Video Title",
            "description": "This is a sample description for the video.",
            "url": video_url,
            "location": location,
            "prompt_response": response
        }

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    def sendVoiceAlert(self, message):
        account_sid = "xxxxx"  #key1
        auth_token = "xxxxx"     #key2
        client = Client(account_sid, auth_token)
        twiml="<Response><Say>"+ message+"</Say></Response>",
        call = client.calls.create(
            twiml=twiml,
            to="+917080516237",
            from_="+15153208864",
        )

        print(call.sid)

    def sendSMSAlert(self, message):
        account_sid = "xxxxx"  #key3
        auth_token = "xxxxx"     #key4
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_="+15153208864",
            to="+917080516237",
        )
        print(message.body)

    def parseResult(self, text):
        start_index = text.find('[')
        end_index = text.find(']') + 1
        
        # Extract and return the array as a string
        if start_index != -1 and end_index != -1:
            return eval(text[start_index:end_index])
        return []
    

    def generate(self, videoUrl, textPrompt):
        videoObjectReq = Part.from_uri(
            mime_type="video/mp4",
            uri=videoUrl,
        )
        vertexai.init(project="true-love-dev", location="us-central1")
        model = GenerativeModel(
            "gemini-1.5-flash-002",
        )
        responses = model.generate_content(
            [videoObjectReq, textPrompt],
            generation_config=self.generation_config,
            safety_settings=self.safety_settings,
            stream=True,
        )
        
        result = ""

        for response in responses:
            result += response.text
        return self.parseResult(result)



    