

# Automatic Face Recognition Attendance System Using ESP32-CAM Module

## Overview

This project is a face recognition-based attendance system developed using the ESP32-CAM module and Python's OpenCV library. The system detects faces in real-time and marks attendance for recognized individuals. This project aims to automate the attendance marking process, making it more efficient and less prone to errors.

## Features

- **Real-Time Face Detection**: The system can detect faces in real-time using the ESP32-CAM module.
- **Face Recognition**: The system identifies individuals from the detected faces using a pre-trained model.
- **Automated Attendance Marking**: Attendance is automatically marked for recognized individuals and stored in a database or file.
- **User-Friendly Interface**: The project includes a simple interface for monitoring and managing attendance records.

## Components

- **ESP32-CAM Module**: The core hardware component responsible for capturing images and streaming video.
- **Python**: Used for developing the face recognition and attendance marking logic.
- **OpenCV**: A computer vision library used for face detection and recognition.

## How It Works

1. **Image Capture**: The ESP32-CAM module captures images or streams video.
2. **Face Detection**: The captured images are processed using OpenCV to detect faces.
3. **Face Recognition**: Detected faces are compared against a pre-trained model to identify the individual.
4. **Attendance Marking**: Once a face is recognized, the system automatically marks the attendance for that individual by logging the time and date.
5. **Data Storage**: The attendance data is stored in a database or file for future reference.

## Prerequisites

- **Hardware**: 
  - ESP32-CAM module
  - USB to TTL converter for programming
  - Power supply (5V)
- **Software**:
  - Arduino IDE or PlatformIO for programming the ESP32-CAM
  - Python 3.x
  - OpenCV library (`opencv-python`)
  - Any additional Python libraries needed for data handling and storage

## Setup Instructions

### Hardware Setup

1. **Connect the ESP32-CAM module** to the USB to TTL converter for programming. Connect the power supply as well.
2. **Upload the ESP32-CAM code** using Arduino IDE or PlatformIO. Ensure that the camera and Wi-Fi settings are correctly configured.
3. **Deploy the ESP32-CAM module** at the desired location for capturing faces.

### Software Setup

1. **Install Python and OpenCV**:
    ```bash
    pip install opencv-python
    ```
2. **Clone the project repository** and navigate to the project directory:
    ```bash
    git clone <your-repo-link>
    cd face-recognition-attendance-system
    ```
3. **Run the Python script** to start the face detection and recognition process:
    ```bash
    python attendance_system.py
    ```
4. **View the attendance records** stored in the specified file or database.

## Customization

- **Training the Model**: If you want to use your own dataset, you can train a new face recognition model using OpenCV or any other machine learning framework.
- **Data Storage**: Modify the data storage logic in the Python script to store attendance records in a database, CSV file, or any other format as per your requirement.

## Future Improvements

- **Enhanced Recognition Accuracy**: Implement advanced machine learning algorithms to improve face recognition accuracy.
- **Multiple Camera Support**: Extend the system to support multiple ESP32-CAM modules for larger areas.
- **Mobile App Integration**: Develop a mobile app for easier access to attendance records.

## Conclusion

This ESP32-CAM based face recognition attendance system is an efficient and automated solution for tracking attendance. By leveraging the power of Python and OpenCV, it provides a robust method for real-time face recognition and attendance marking.

## Author

- [Mausam Raj]

---

