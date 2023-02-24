from sys import path
from tkinter import *
from PIL import Image
import os
import cv2
from tkinter import messagebox
import numpy as np
import pickle
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "My_Dataset")

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
face_cascade2 = cv2.CascadeClassifier('cascades/data/haarcascade_profileface.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):
			path = os.path.join(root, file)
			label = os.path.basename(root).replace(" ", "-").lower()
			if not label in label_ids:
				label_ids[label] = current_id
				current_id += 1
			id_ = label_ids[label]
			pil_image = Image.open(path).convert("L")
			size = (550, 550)
			final_image = pil_image.resize(size, Image.ANTIALIAS)
			image_array = np.array(final_image, "uint8")
			faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.4, minNeighbors=5)
			facess = face_cascade2.detectMultiScale(image_array, scaleFactor=1.1, minNeighbors=5)
            
			for (x,y,w,h) in facess:
				roi = image_array[y:y+h, x:x+w]
				x_train.append(roi)
				y_labels.append(id_)
				
			for (xi,yi,wi,hi) in faces:
				roi = image_array[yi:yi+hi, xi:xi+wi]
				x_train.append(roi)
				y_labels.append(id_)
            

with open("abels.pickle", 'wb') as f:
	pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")