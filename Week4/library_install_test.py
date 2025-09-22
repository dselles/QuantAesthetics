import torch 
import numpy as np 
import cv2 
import clip 
from PIL import Image 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

device = torch.device("cuda" if torch.cuda.is_available() else "cpu") 
print(f"Using device: {device}") 
version = torch.__version__ 
print(f"PyTorch version: {version}") 
arr = np.array([1, 2, 3]) 
tensor = torch.from_numpy(arr).to(device) 
print(tensor) 
print(tensor.dtype) 
model, preprocess = clip.load("ViT-B/32", device=device) 
text = clip.tokenize(["a diagram", "a dog", "a cat"]).to(device) 
with torch.no_grad(): 
    text_features = model.encode_text(text) 
print(text_features)