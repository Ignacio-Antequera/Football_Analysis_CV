from ultralytics import YOLO
import torch

# Check if GPU is available
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU Device: {torch.cuda.get_device_name(0)}")
    device = 0  # Use GPU
else:
    print("Running on CPU")
    device = 'cpu'

model = YOLO("yolov8x.pt")  # load a pretrained YOLOv8x model

# Run inference on GPU if available
results = model.predict(source="input_videos/08fd33_4.mp4", save=True, device=device)
print(results[0])
print("==============================")
for box in results[0].boxes:
    print(box)