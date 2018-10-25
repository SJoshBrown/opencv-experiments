#! /usr/bin/python3

from sys import argv, exit
import cv2
import numpy as np


def gaussian_noise(path, sigma):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) / 255

    x, y = img.shape

    noise = np.random.rand(x, y) * sigma

    gaussed = img + noise

    cv2.imshow('image', gaussed)
    cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    if len(argv) < 3:
        print("Invalid Arguments")
        exit()

    gaussian_noise(argv[1], float(argv[2]))
