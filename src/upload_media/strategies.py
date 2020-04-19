import requests
import json

class PostRequest:

    def execute(self, destination_address, subject_code, media_path):
        data = {
            'subject_code' : subject_code
        }
        files = {'media': open(media_path, 'rb')}
        requests.post(url = destination_address, files=files, data = json.dumps(data))