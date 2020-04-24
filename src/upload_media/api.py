from send_media_strategy import SendMediaStrategy

def send_media(destination_address, subject, sending_strategy = None):
    try:
        send_media_interface = SendMediaStrategy(destination_address, sending_strategy)
        send_media_interface.send(subject.subjectCode, subject.groupImage)
    except:
        print("Media not sent!")