import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image

IMG_SIZE = 128
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Wahi model structure
model = models.resnet18(weights=None)
num_ftrs = model.fc.in_features
model.fc = nn.Sequential(
    nn.Linear(num_ftrs, 128),
    nn.ReLU(),
    nn.Dropout(0.3),
    nn.Linear(128, 1),
    nn.Sigmoid()
)
model.load_state_dict(torch.load('flood_image_model.pth', map_location=DEVICE))
model = model.to(DEVICE)
model.eval()

# Image transform
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def predict(image_path):
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0).to(DEVICE)
    
    with torch.no_grad():
        output = model(image)
    
    prob = output.item()
    if prob < 0.5:
        print(f"Result: FLOOD - {(1-prob)*100:.2f}% confident")
    else:
        print(f"Result: NO FLOOD - {prob*100:.2f}% confident")  
predict('test.jpg')