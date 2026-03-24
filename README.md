#  Object Detection System using YOLOv8

##  Project Title

Object Detection System using YOLOv8 and Python

---

##  Problem Statement

Object detection is a key task in computer vision that involves identifying and locating objects within an image. The objective of this project is to develop a system capable of detecting multiple objects in an image and drawing bounding boxes around them using deep learning techniques.

---

##  Objectives

* To implement an object detection system using YOLOv8
* To detect multiple objects in an image
* To display bounding boxes with labels and confidence scores
* To save the output image with detected objects

---

## 🛠️ Tools & Technologies Used

* Python 3.x
* OpenCV (cv2)
* Ultralytics YOLOv8
* NumPy
* Git & GitHub
* Linux (Ubuntu / WSL)

---

## ⚙️ Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/Thensinck/ObjectDetection_94.git
cd ObjectDetection_94
```

### 2. Create Virtual Environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Execution Procedure

### Step 1: Run the program

```bash
python detect.py
```

### Step 2: Enter image path

Example:

```bash
/mnt/c/Users/USER/Downloads/dog.jpg
```

### Step 3: Output

* Detected objects will be displayed in terminal
* Output image will be saved as:

```bash
result.jpg
```

---

## 📸 Output Screenshots

### Input Image

(Add your input image screenshot here)

### Output Image

(Add your result image screenshot here)

---

## 🧠 Methodology

* Load YOLOv8 pre-trained model
* Read input image using OpenCV
* Perform object detection using the model
* Extract detected objects and confidence scores
* Draw bounding boxes on image
* Save the output image

---

## ⚠️ Challenges Faced

* Handling file path issues in Linux (WSL)
* Managing large files in GitHub
* Installing and configuring dependencies
* Understanding YOLO model behavior

---

## ✅ Results

The system successfully detects multiple objects such as cars, dogs, persons, etc., with good accuracy and saves the output image with bounding boxes.

---

## 🔮 Future Scope

* Real-time object detection using webcam
* Video-based object detection
* Custom dataset training
* Integration with web or mobile applications

---

##  References

* https://docs.ultralytics.com/
* https://opencv.org/
* https://pytorch.org/

---

## Author

**Name:** Thensin CK
**Project:** Object Detection System
**GitHub:** https://github.com/Thensinck

