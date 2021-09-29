import cv2

def to_gray(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(image_path, img)