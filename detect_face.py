import cv2gpu

# Load the cascade
face_cascade = cv2gpu.CascadeClassifier('cascade_frontalface_gpu.xml')
# To capture video from webcam. 
cap = cv2gpu.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2gpu.cvtColor(img, cv2gpu.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2gpu.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    cvgpu2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2gpu.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()
