import pandas as pd
import cv2
import urllib.request
import numpy as np
import os
from datetime import datetime
import face_recognition

# Path to the folder containing images of known faces
path = r'E:\major\Attendance\image_folder'

# URL for the video stream (IP camera)
url = 'http://192.168.5.243/cam-hi.jpg'

# Check if Attendance.csv exists, if yes, delete it
attendance_file = "Attendance.csv"
if os.path.isfile(attendance_file):
    os.remove(attendance_file)

# Initialize an empty DataFrame for attendance
df = pd.DataFrame(columns=['Name', 'Time'])
df.to_csv(attendance_file, index=False)

# Load images and corresponding class names
images = []
classNames = []
myList = os.listdir(path)
print("Loaded images:")
print(myList)
for cl in myList:
    curImg = cv2.imread(os.path.join(path, cl))
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print("Class names:")
print(classNames)

# Encode the known faces
def findEncodings(images):
    encodeList = []
    for img in images:
        if img is None:
            print("Error: Unable to load one or more images.")
            continue
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)
print('Encoding Complete')

# Function to mark attendance
def markAttendance(name):
    now = datetime.now()
    dtString = now.strftime('%H:%M:%S')
    with open(attendance_file, 'a') as f:
        f.write(f'{name},{dtString}\n')

# Main loop for face recognition
while True:
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)

    # Resize image for faster processing
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Find faces in the current frame
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    # Compare faces with known faces
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            # Draw rectangle around the face and mark attendance
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

    cv2.imshow('Webcam', img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
