import numpy as np
from PIL import Image

def laplacian_filter(image_array):
    height, width = image_array.shape
    result = np.zeros((height-2, width-2))

    # Kernel Laplacian cơ bản
    kernel = np.array([[0, -1, 0],
                       [-1, 4, -1],
                       [0, -1, 0]])

    for i in range(height-2):
        for j in range(width-2):
            region = image_array[i:i+3, j:j+3]
            result[i,j] = np.sum(region * kernel)

    # Chuẩn hóa về 0-255
    result = np.clip(result, 0, 255)
    return result

# Demo
img = Image.open("input/laplacian_filter.jpg").convert("L")
img_array = np.array(img, dtype=np.float32)

lap_img = laplacian_filter(img_array)
lap_img_out = Image.fromarray(lap_img.astype(np.uint8))
lap_img_out.show()
