import numpy as np
import scipy.ndimage
from scipy import signal, misc
import matplotlib.pyplot as plt
import cv2
from pylab import *

def BoxcarZeroPadding(image,k):
    kernel = np.ones((k,k))
    kernel_1 = kernel/pow(k,2)
    #print(kernel_1)
    output = scipy.signal.convolve2d(image,kernel_1,mode='same',boundary='fill')
    return output

img = cv2.imread('characterTestPattern688.tif',cv2.IMREAD_GRAYSCALE)

output = BoxcarZeroPadding(img,35)/255
cv2.imshow('input',img)
cv2.imshow('output',output)
cv2.waitKey()




