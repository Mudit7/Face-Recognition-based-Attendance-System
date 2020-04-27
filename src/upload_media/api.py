from send_media_strategy import SendMediaStrategy

def send_media(destination_address, subject_code, media_path, sending_strategy = None):
    try:
        send_media_interface = SendMediaStrategy(destination_address, sending_strategy)
        send_media_interface.send(subject_code, media_path)
    except:
        print("Media not sent!")