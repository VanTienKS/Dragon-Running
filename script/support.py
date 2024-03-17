import os
import pygame

BASE_IMG_PATH = "assets\\images\\"

def load_image(path):
    image = pygame.image.load(BASE_IMG_PATH + path)
    return image

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + "\\" + img_name))
    return images

