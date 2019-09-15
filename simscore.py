# import the necessary packages
# from skimage.measure import structural_similarity as ssim
from skimage import measure
import numpy as np
import cv2
import os
import shutil

# cat1 = cv2.imread("cat11.jpeg")
# cat2 = cv2.imread("cat12.jpeg")
def compare_frame(f1, f2):
    ff1 = cv2.imread(f1)
    ff2 = cv2.imread(f2)
    return measure.compare_ssim(ff1, ff2, multichannel=True)

def compare_videos():
    og_image_folder = 'data/target/train/train_img/'

    og_images = [img for img in os.listdir(og_image_folder) if img.endswith(".png")]
    og_images = sorted(og_images)

    mod_image_folder = 'results/target/test_latest/images/'
    mod_images = [img for img in os.listdir(mod_image_folder) if img.endswith("image.jpg")]
    mod_images = sorted(mod_images)

    print(len(og_images))
    print(len(mod_images))

    avg = 0
    N = min(len(og_images), len(mod_images))
    for i in range(N):
        avg += compare_frame('%s/%s' %(mod_image_folder, mod_images[i]), '%s/%s' %(og_image_folder, og_images[i]))

    return avg / N

score = compare_videos()

f= open("score.py","w+")
f.write(str(score))
