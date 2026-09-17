import cv2

# Path to the image, relative to this script's location (../Images/)
image_path = "../Images/sample_gradient.jpg"
image = cv2.imread(image_path)
if image is None:
    print(f"Could not load image at: {image_path}")
else:
    print(f"Loaded image: {image_path}")
    print(f"Shape (height, width, channels): {image.shape}")
    cv2.imshow("Loaded Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
