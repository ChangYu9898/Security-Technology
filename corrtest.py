import numpy
import numpy as np
import scipy.ndimage
from scipy.ndimage import correlate

kernel = numpy.array(
    [[1,2,1],
    [2,4,2],
    [1,2,1]])

input  = numpy.array(
    [[1,5,9,13],
    [2,6,10,14],
    [3,7,11,15],
    [4,8,12,16]])

output = scipy.ndimage.correlate(input,kernel,mode='reflect',cval=0.0,origin=0)
print(output)
