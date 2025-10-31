import numpy as np
from PIL import Image

def mean_filter(image_array):
    height, width = image_array.shape
    result = np.zeros((height-2, width-2))

    kernel = np.ones((3,3)) / 9.0   # kernel 3x3 trung bình đều

    for i in range(height-2):
        for j in range(width-2):
            region = image_array[i:i+3, j:j+3]
            result[i,j] = np.sum(region * kernel)
    
    return result

# Demo
img = Image.open("input/mean_filter.jpg").convert("L")
img_array = np.array(img, dtype=np.float32)

mean_img = mean_filter(img_array)
mean_img_out = Image.fromarray(mean_img.astype(np.uint8))
mean_img_out.show()

