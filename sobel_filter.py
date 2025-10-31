import numpy as np
from PIL import Image

def sobel_filter(image_array):
    height, width = image_array.shape
    result = np.zeros((height - 2, width - 2))

    kernel_x = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])
    
    kernel_y = np.array([[-1, -2, -1],
                         [0,  0,  0],
                         [1,  2,  1]])
    
    for i in range(height - 2):
        for j in range(width - 2):
            region = image_array[i:i+3, j:j+3]
            sobel_x = np.sum(region * kernel_x)
            sobel_y = np.sum(region * kernel_y)
            result[i, j] = np.sqrt(sobel_x**2 + sobel_y**2)
    
    return result

# Đọc ảnh
img = Image.open('input/sobel_filter.jpg').convert('L')
img_array = np.array(img, dtype=np.float32)

# Áp dụng Sobel filter
sobel_edges = sobel_filter(img_array)

# Hiển thị kết quả
sobel_edges_image = Image.fromarray(sobel_edges.astype(np.uint8))
sobel_edges_image.show()
