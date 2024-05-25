# import os
# import cv2
# import numpy as np
# import pytesseract
# from flask import Flask, render_template, request
# from pymongo import MongoClient
# import re

# # Set the path for Tesseract executable if necessary
# # pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# app = Flask(__name__)

# # MongoDB connection
# client = MongoClient('mongodb+srv://123:123@cluster0.kdydgz2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # Update with your MongoDB URI
# db = client['license_plate_db']
# collection = db['plates']

# def preprocess_image(image_path):
#     image = cv2.imread(image_path)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#     edged = cv2.Canny(blurred, 30, 200)
#     return image, edged

# def find_license_plate_contour(edged):
#     contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
#     for c in contours:
#         perimeter = cv2.arcLength(c, True)
#         approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
#         if len(approx) == 4:
#             return approx
#     return None

# def extract_license_plate(image, contour):
#     mask = cv2.drawContours(np.zeros_like(image), [contour], -1, (255, 255, 255), thickness=cv2.FILLED)
#     license_plate = cv2.bitwise_and(image, mask)
#     x, y, w, h = cv2.boundingRect(contour)
#     cropped_plate = license_plate[y:y + h, x:x + w]
#     return cropped_plate

# def recognize_text_from_image(image):
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     text = pytesseract.image_to_string(gray_image, config='--psm 8')
#     return text.strip()

# def clean_text(text):
#     cleaned_text = re.sub(r'[^A-Z0-9]', '', text)
#     return cleaned_text

# @app.route('/', methods=['GET', 'POST'])
# def upload_image():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return 'No file part'
#         file = request.files['file']
#         if file.filename == '':
#             return 'No selected file'
#         if file:
#             file_path = os.path.join('static', file.filename)
#             file.save(file_path)
#             license_plate_text = main(file_path)
#             plate_exists = check_plate_in_db(license_plate_text)
#             return render_template('index.html', license_plate_text=license_plate_text, file_path=file_path, plate_exists=plate_exists)
#     return render_template('index.html')

# def check_plate_in_db(plate_text):
#     # Check if the license plate exists in MongoDB
#     if collection.find_one({"plate_number": plate_text}):
#         return True
#     return False

# def main(image_path):
#     image, edged = preprocess_image(image_path)
#     plate_contour = find_license_plate_contour(edged)
#     if plate_contour is None:
#         return "License plate not found"
#     license_plate_image = extract_license_plate(image, plate_contour)
#     plate_text = recognize_text_from_image(license_plate_image)
#     cleaned_text = clean_text(plate_text)
#     return cleaned_text

# if __name__ == "__main__":
#     if not os.path.exists('static'):
#         os.makedirs('static')
#     app.run(debug=True)



import os
import cv2
import numpy as np
import pytesseract
from flask import Flask, render_template, request
from pymongo import MongoClient
import re

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb+srv://123:123@cluster0.kdydgz2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # Update with your MongoDB URI
db = client['license_plate_db']
collection = db['plates']

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 200)
    return image, edged

def find_license_plate_contour(edged):
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    for c in contours:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        if len(approx) == 4:
            return approx
    return None

def extract_license_plate(image, contour):
    mask = cv2.drawContours(np.zeros_like(image), [contour], -1, (255, 255, 255), thickness=cv2.FILLED)
    license_plate = cv2.bitwise_and(image, mask)
    x, y, w, h = cv2.boundingRect(contour)
    cropped_plate = license_plate[y:y + h, x:x + w]
    return cropped_plate

def recognize_text_from_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray_image, config='--psm 8')
    return text.strip()

def clean_text(text):
    cleaned_text = re.sub(r'[^A-Z0-9]', '', text)
    return cleaned_text

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            file_path = os.path.join('static', file.filename)
            file.save(file_path)
            license_plate_text = main(file_path)
            plate_exists = check_plate_in_db(license_plate_text)
            return render_template('index.html', license_plate_text=license_plate_text, file_path=file_path, plate_exists=plate_exists)
    return render_template('index.html')

def check_plate_in_db(plate_text):
    if collection.find_one({"plate_number": plate_text}):
        return True
    return False

def main(image_path):
    image, edged = preprocess_image(image_path)
    plate_contour = find_license_plate_contour(edged)
    if plate_contour is None:
        return "License plate not found"
    license_plate_image = extract_license_plate(image, plate_contour)
    plate_text = recognize_text_from_image(license_plate_image)
    cleaned_text = clean_text(plate_text)
    return cleaned_text

if __name__ == "__main__":
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)
