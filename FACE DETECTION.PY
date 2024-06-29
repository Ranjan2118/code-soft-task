import cv2

# Load the pre-trained DNN model
net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'res10_300x300_ssd_iter_140000.caffemodel')

# Read an image
image = cv2.imread('path/to/image.jpg')
(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

# Detect faces
net.setInput(blob)
detections = net.forward()

# Draw rectangles around faces
for i in range(0, detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.5:
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype('int')
        cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 2)

# Show the image
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import Normalizer

# Load the pre-trained FaceNet model
model = load_model('facenet_keras.h5')

# Function to preprocess the face for recognition
def preprocess_face(face):
    face = cv2.resize(face, (160, 160))
    face = face.astype('float32')
    mean, std = face.mean(), face.std()
    face = (face - mean) / std
    face = np.expand_dims(face, axis=0)
    return face

# Load and preprocess the image
image = cv2.imread('path/to/image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Recognize faces
for (x, y, w, h) in faces:
    face = image[y:y+h, x:x+w]
    face = preprocess_face(face)
    embedding = model.predict(face)
    # Here you can compare the embedding with stored embeddings for recognition

# Display the image
cv2.imshow('Face Recognition', image)
cv2.waitKey(0)
cv2.destroyAllWindows()