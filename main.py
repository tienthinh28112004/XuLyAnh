from weighted_average_filter import apply_mean_filter, apply_gaussian_filter
from median_filter import apply_median_filter
from sobel_filter import apply_sobel
from prewitt_operator import apply_prewitt
from laplacian_filter import apply_laplacian

# Đường dẫn ảnh input
input_path = "input/test.jpg"

# 1. Bộ lọc làm mịn
apply_mean_filter(input_path, save_path="output/mean.jpg")
apply_gaussian_filter(input_path, save_path="output/gaussian.jpg")
apply_median_filter(input_path, save_path="output/median.jpg")

# 2. Phát hiện biên
apply_sobel(input_path, save_path="output/sobel.jpg")
apply_prewitt(input_path, save_path="output/prewitt.jpg")
apply_laplacian(input_path, save_path="output/laplacian.jpg")

print("Xử lý xong! Kết quả nằm trong thư mục output/")
