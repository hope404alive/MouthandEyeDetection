import cv2

#  find a cool face to work with
image_path = "images/00000.png"  # Put your awesome face image here
image = cv2.imread(image_path)

# use some special tools to find faces, eyes, and mouths
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
mouth_cascade = cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")  # Shhh, it's a secret file!

#  make the image simpler by removing colors
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Now it's time to find faces!
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# go through each face we found
for (x, y, w, h) in faces:
    # Time to highlight the face with a rectangle
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Now we focus on the cool parts inside the face
    roi_gray = gray_image[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    
    #  find the eyes within the face
    eyes = eye_cascade.detectMultiScale(roi_gray)
    
    # Time to put rectangles around the eyes
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
    
    # we're searching for the mouth, the gateway to laughter and food
    mouths = mouth_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=11, minSize=(25, 15))
    
    # draw rectangles around the mouths we find
    for (mx, my, mw, mh) in mouths:
        cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (0, 0, 255), 2)


cv2.imshow("Facial Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
