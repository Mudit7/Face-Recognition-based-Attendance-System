import requests
import json

class ReceiveObserver(object):
    """
    Receive Observer which receives media and calls
    executes desired function accordingly
    """

    def __init__(self, trigger):
        self.trigger = trigger
        self.trigger.bind_to(self.extract_faces)
    
    def sendForExtraction(self, subject_code, group_media):
        DESTINATION_ADDRESS = '127.0.0.1:8080'

        image = group_media

        data = {
            'subject_code' : subject_code
        }

        files = {'media': image}
        
        requests.post(url = DESTINATION_ADDRESS, files=files, data = json.dumps(data))