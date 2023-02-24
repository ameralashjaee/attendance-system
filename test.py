import cv2
import os
from PIL import Image
import numpy as np
import pickle
from sys import path
# Load the label IDs from the pickle file


# Load the label IDs from the pickle file
with open("abels.pickle", 'rb') as f:
    label_ids = pickle.load(f)
    labels = {v: k for k, v in label_ids.items()}
    print(labels)
# Load the trained face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

# Load the cascade classifier for detecting faces
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

# Load the test image

test_image = cv2.imread('C:\\Users\\amera\\OneDrive\Desktop\\attendance system based on face recognition\\test\\1234567899\\WIN_20230118_14_09_41_Pro.jpg')

gray_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# Detect faces in the test image
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.4, minNeighbors=5)
print(faces)
# Iterate over each detected face
for (x, y, w, h) in faces:
    roi = gray_image[y:y+h, x:x+w]
    id_, conf = recognizer.predict(roi)
    print("confidence: ", conf)
    if conf >= 45 and conf <= 85:
        # Print the label of the recognized face
        print(labels[id_])
    else:
        print("unknown")