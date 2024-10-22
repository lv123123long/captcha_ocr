import os
from captcha.image import ImageCaptcha
import random
import time

captcha_array = list("1234567890abcdefghijklmnopquvwxyz")
captcha_size = 4

if __name__ == "__main__":
    current = os.path.dirname(os.path.abspath(__file__))

    image = ImageCaptcha()
    

    for i in range(10000):
        image_text = "".join(random.sample(captcha_array, captcha_size))
        image_path = os.path.join(current, "./datasets/train/{}_{}.png".format(image_text, int(time.time())))
        image.write(image_text, image_path)
    