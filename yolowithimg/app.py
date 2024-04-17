from ultralytics import YOLO


model = YOLO('yolov8l.pt')
results = model('car_img.jpg', show=True)
