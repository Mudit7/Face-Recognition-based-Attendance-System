import cv2
import numpy as np
import matplotlib.pyplot as plt

from .config import *
import os
def loadClassifier():
    """ 
    Load Pre-Trained/Trained Face Dectector
    """
    #for testing use this, otherwise prefer abs path
    CASCADE_CLASSIFIER
    return cv2.CascadeClassifier(CASCADE_CLASSIFIER)

def rgbToGrayscale(image):
    """
    Convert RGB image to Grayscale
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray_image

def readImage(image_path):
    """
    Read Image
    """
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def saveImage(image, image_path):
    """
    Save {image} at {image_path} location
    """
    cv2.imwrite(image_path, image) 

def showImage(image):
    """
    Show Image
    PRESS 0 for next image
    """
    cv2.imshow("Image",image)
    cv2.waitKey(0)


def cropFaces(image):
    """
    Crop faces detected from the image
    """

    face_cascade = loadClassifier()
    faces = face_cascade.detectMultiScale(image, 1.25, 6)

    # Print number of faces found
    print('Number of faces detected:', len(faces))

    extracted_faces = []

    for face in faces:
        x, y, w, h = [ v for v in face ]
        cv2.rectangle(image, (x,y), (x+w, y+h), GRAY_CODE, CHANNELS)
        extracted_faces.append(image[y:y+h, x:x+w] )
    
    return extracted_faces
 
if __name__ == "__main__":

    # SAMPLE USAGE CODE FOR HELP

    image = readImage('test_images/test-2.jpg')

    gray_image = rgbToGrayscale(image)

    cropFaces(gray_image)