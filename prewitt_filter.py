import numpy as np
from PIL import Image

def prewitt_filter(image_array):
    height, width = image_array.shape
    result = np.zeros((height - 2, width - 2))

    kernel_x = np.array([[-1, 0, 1],
                         [-1, 0, 1],
                         [-1, 0, 1]])

    kernel_y = np.array([[-1, -1, -1],
                         [0, 0, 0],
                         [1, 1, 1]])

    for i in range(height - 2):
        for j in range(width - 2):
            region = image_array[i:i + 3, j:j + 3]
            prewitt_x = np.sum(region * kernel_x)
            prewitt_y = np.sum(region * kernel_y)
            result[i, j] = np.sqrt(prewitt_x ** 2 + prewitt_y ** 2)

    return result


# Đọc ảnh xám
img = Image.open('input/prewitt_filter.jpg').convert('L')
img_array = np.array(img, dtype=np.float32)

# Áp dụng Prewitt filter
prewitt_edges = prewitt_filter(img_array)

# Hiển thị kết quả
prewitt_edges_image = Image.fromarray(prewitt_edges.astype(np.uint8))
prewitt_edges_image.show()
