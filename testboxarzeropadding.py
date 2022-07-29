import cv2
from pylab import *


def BoxFilter(Imge, dim, dim2, flag):  # Image为待处理图像，dim为滤波器的大小dim*dim2
    im = array(Imge)
    # 序列化
    sigema = 0
    # 滤波求和

    for i in range(int(dim / 2), im.shape[0] - int(dim / 2)):
        for j in range(int(dim2 / 2), im.shape[1] - int(dim2 / 2)):
            for a in range(-int(dim / 2), -int(dim / 2) + dim):
                for b in range(-int(dim2 / 2), -int(dim2 / 2) + dim2):
                    sigema = sigema + img[i + a, j + b]
                    # 对于滤波范围内求和，从左到右，从上到下扫

            if (flag):
                im[i, j] = sigema / (dim * dim2)

            else:
                im[i, j] = min(sigema, 255)
            # 归一化则与均值滤波一致，不归一化的话超过255用255表示
            sigema = 0
            # 滤波移动
    return im


img = cv2.imread('characterTestPattern688.tif', 0)
print(img)
# 读取图像
x = int(input("输入滤波长度：\n"))
y = int(input("输入滤波宽度:\n"))
flag = int(input("是否归一化(1/0)?\n"))

im = BoxFilter(img, x, y, flag)
# im= cv2.boxFilter(img, -1, (3, 3), normalize=False)
# im= cv2.blur(source, (3, 3))

# 第一个为手写的方框滤波，第二个为opencv调包的方框滤波，第三个为调包的均值滤波

cv2.imshow('output', im)
#cv2.imshow('Origin', img)
cv2.waitKey()
cv2.destroyAllWindows()
