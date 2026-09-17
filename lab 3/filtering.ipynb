import cv2
import numpy as np
import urllib.request
from matplotlib import pyplot as plt
url = 'https://raw.githubusercontent.com/hassam-ur-rehman/Computer_Vision/83fc0208c23ceaa3103e5587b10ebd1d8f6891c6/images/cat%201.webp'
resp = urllib.request.urlopen(url)
img_array = np.asarray(bytearray(resp.read()), dtype=np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

if img is None:
    raise ValueError("Image failed to load — check the URL or file format.")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def modify_pixel(image, x, y, value):
    modified = image.copy()
    modified[y, x] = value
    return modified
modified_img = modify_pixel(gray_img, 50, 50, 255)
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(gray_img, cmap='gray'); axes[0].set_title('Original'); axes[0].axis('off')
axes[1].imshow(modified_img, cmap='gray'); axes[1].set_title('Pixel (50,50) → 255'); axes[1].axis('off')
plt.show()


# task 2

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
R, G, B = cv2.split(img_rgb)
G_modified = np.zeros_like(G)
modified_rgb = cv2.merge([R, G_modified, B])
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(img_rgb); axes[0].set_title('Original'); axes[0].axis('off')
axes[1].imshow(modified_rgb); axes[1].set_title('Green channel removed'); axes[1].axis('off')
plt.show()


# task 3
smoothed = cv2.blur(img_rgb, (5, 5))
details = cv2.subtract(img_rgb, smoothed)
sharpened = cv2.add(img_rgb, details)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(img_rgb); axes[0].set_title('Original'); axes[0].axis('off')
axes[1].imshow(details); axes[1].set_title('Details'); axes[1].axis('off')
axes[2].imshow(sharpened); axes[2].set_title('Sharpened'); axes[2].axis('off')
plt.show()


# lab journal 5 task:
smoothed = cv2.blur(img_rgb, (5, 5))
details = cv2.subtract(img_rgb, smoothed)
sharpened = cv2.add(img_rgb, details)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(img_rgb); axes[0].set_title('Original'); axes[0].axis('off')
axes[1].imshow(details); axes[1].set_title('Details'); axes[1].axis('off')
axes[2].imshow(sharpened); axes[2].set_title('Sharpened'); axes[2].axis('off')
plt.show()
