import cv2
import numpy as np

images = []
images.append(cv2.imread(r'img\a1.png', cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread(r'img\a2.png', cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread(r'img\b1.png', cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread(r'img\b2.png', cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread(r'img\c1.png', cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread(r'img\c2.png', cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread(r'img\d1.png', cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread(r'img\d2.png', cv2.IMREAD_GRAYSCALE))

labels = [0, 0, 1, 1, 2, 2, 3, 3]
# print(labels)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(images, np.array(labels))
predict_image = cv2.imread(r'img\b2.png', cv2.IMREAD_GRAYSCALE)
label, confidence = recognizer.predict(predict_image)
print("label=", label)
print("confidence=", confidence)
