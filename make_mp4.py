import imageio
import os

image_folder = 'results/target/test_latest/images/'

images = [img for img in os.listdir(image_folder) if img.endswith("image.jpg")]
images = sorted(images)

s_folder = 'data/target/train/train_label/'

s_images = [img for img in os.listdir(s_folder) if img.endswith(".png")]
s_images = sorted(s_images)

writer = imageio.get_writer('test.mp4', fps=30)
s_writer = imageio.get_writer('test2.mp4', fps=30)

for im in images:
    writer.append_data(imageio.imread(image_folder+im))

for im in s_images:
    s_writer.append_data(imageio.imread(s_folder+im))
    
writer.close()
