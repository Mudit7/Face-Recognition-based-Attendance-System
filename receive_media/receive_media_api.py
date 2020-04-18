from flask import Flask, request
from flask_cors import CORS

from receive_trigger import ReceiveTrigger
from receive_observer import ReceiveObserver

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods = ['POST'])
def receiveGroup():
    if request.method == 'POST':
        media = request.files['media']
        subject_code = request.get_json()['subject_code']
        receive_trigger.group = (subject_code, media)

if __name__ == "__main__":
    receive_trigger = ReceiveTrigger()

    receive_observer = ReceiveObserver(receive_trigger)

    app.run(host='0.0.0.0')