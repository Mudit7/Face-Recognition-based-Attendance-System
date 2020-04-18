import face_extract

class ReceiveObserver(object):
    """
    Receive Observer which receives media and calls
    executes desired function accordingly
    """

    def __init__(self, trigger):
        self.trigger = trigger
        self.trigger.bind_to(self.extract_faces)

    def extractFacesMedia(self, subject_code, group_media):
        image = group_media

        gray_image = face_extract.rgbToGrayscale(image)

        faces = face_extract.cropFaces(gray_image)

        return faces