from ultralytics import YOLO
import cv2
import os

# Step 1: Load model
model = YOLO("yolov8n.pt")

# Step 2: Get image from user

image_path = input("Enter image path: ").strip().replace("\\", "/")

if not os.path.exists(image_path):
    print("❌ Image not found!")
    exit()

# Step 3: Read image
img = cv2.imread(image_path)

# Step 4: Detect objects
results = model(img)

# Step 5: Draw boxes
output = results[0].plot()

# Step 6: Save result
cv2.imwrite("result.jpg", output)

print("Detection completed! Check result.jpg")
print("Objects detected:", len(results[0].boxes))

# Print results
for box in results[0].boxes:
    cls = int(box.cls)
    conf = float(box.conf)
    print(model.names[cls], ":", conf)
