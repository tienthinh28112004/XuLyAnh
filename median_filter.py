import numpy as np
from PIL import Image

def median_filter(image,kernel_size):
    height,width = image.shape
    result = np.zeros_like(image)

    pad = kernel_size // 2
    padded_image = np.pad(image,pad,mode='constant')

    for i in range(height):
        for j in range(width):
            window = padded_image[i:i+kernel_size,j:j+kernel_size]
            result[i,j] = np.median(window)

    return result

img = Image.open('input/median_filter.jpg').convert('L')
img_array = np.array(img)

median_filtered_img = median_filter(img_array,kernel_size=3)

filtered_img = Image.fromarray(median_filtered_img.astype(np.uint8))
filtered_img.show()
