import cv2

# Load the facial image
image_path = "images/00000.png"  # Replace with the path to your facial image
image = cv2.imread(image_path)

# Load the pre-trained Haar cascade classifier for eye detection
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# Convert the image to grayscale for eye detection
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform eye detection
eyes = eye_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Iterate over the detected eyes
for (x, y, w, h) in eyes:
    # Draw a rectangle around each eye
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the result
cv2.imshow("Facial Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()



