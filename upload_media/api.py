from send_media_strategy import SendMediaStrategy

def send_media(destination_ip, subject_code, media, strategy = None):
    try:
        send_media_interface = SendMediaStrategy(destination_ip, subject_code, strategy)
        send_media_interface.send(media)
    except:
        print("Media not sent!")