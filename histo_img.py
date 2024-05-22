import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('I:/LIM2second_semestre/traitement_iamge/cam_men.jpg',cv.IMREAD_GRAYSCALE)
plt.hist(img); plt.show()
plt.hist(img.ravel(),256,[0,256]); plt.show()