from ultralytics import YOLO

model = YOLO("models\\best.pt")

# if your PC has no GPU use colab
results = model.predict('input\\input_video.mp4', save=True)

print(results[0])
