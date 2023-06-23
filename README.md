# Face Detection Intern Project

This is an intern project focused on face detection using OpenCV. The project utilizes Haar cascade classifiers to detect faces, eyes, and mouths in an image.

## Requirements

- Python 3
- OpenCV 4

## Installation

1. Clone the repository:

```
git clone https://github.com/hope404alive/MouthandEyeDetection.git
```

2. Install the required packages:

```
pip install opencv-python
```

3. Download the pre-trained Haar cascade classifiers:

- [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
- [haarcascade_eye.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml)
- haarcascade_mcs_mouth.xml (contact project owner for access)

4. Place the downloaded cascade XML files in the project directory.

## Usage

1. Put your desired facial image in the "images" directory.

2. Update the `image_path` variable in the code (line 6) with the path to your facial image.

3. Run the script:

```
python main.py
```

4. The script will display the original image with rectangles around the detected faces, eyes, and mouths.


![image](https://github.com/hope404alive/MouthandEyeDetection/assets/94454699/7f2e5ff5-8186-4d24-81ad-b474ef721d36)


