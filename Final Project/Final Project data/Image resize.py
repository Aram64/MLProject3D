import cv2
import os
from PIL import Image



files = os.listdir("./images/")

for i in range(len(files)):

    print(files[i])
    img = cv2.imread("./images/"+files[i], cv2.IMREAD_UNCHANGED)

    # get dimensions of image
    dimensions = img.shape
    # height, width, number of channels in image
    height = img.shape[0]
    width = img.shape[1]

    print(str(width) + " and " + str(height)+ "\n")
    if (width or height < 500):
        width *= 7
        height *= 7
        print(str(width)+" and "+ str(height) + "\n")

    dim = (width, height)
    # # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    status = cv2.imwrite('./resized/' + str(i) + '.jpg', resized)
