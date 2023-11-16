from matplotlib import  pyplot as plt
import os
import cv2


images_name = os.listdir(os.path.join(os.getcwd(), "images"))

images = {image_name[:image_name.index(".")] : cv2.imread(os.path.join(os.getcwd(), "images", image_name)) for image_name in images_name}
