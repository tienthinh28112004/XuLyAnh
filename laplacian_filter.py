# laplacian_filter.py
import numpy as np

def laplacian_filter(gray: np.ndarray) -> np.ndarray:
    """
    Bộ lọc Laplacian + làm mượt nhẹ trước, phát hiện biên rõ hơn.
    Trả về ảnh float32 (0..255) cùng kích thước đầu vào.

    - gray: ảnh xám 2D numpy (H, W)
    - return: ảnh float32 (H, W)
    """

    if gray.ndim != 2:
        raise ValueError("laplacian_filter chỉ xử lý ảnh xám 2D.")

    g = gray.astype(np.float32)
    H, W = g.shape

    # ===== 1. Làm mờ nhẹ bằng Gaussian 3x3 (tự code) =====
    gauss_kernel = np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ], dtype=np.float32)
    gauss_kernel /= gauss_kernel.sum()  # tổng = 1

    pad = 1  # cho kernel 3x3
    padded_g = np.pad(g, pad_width=pad, mode="edge")

    blurred = np.zeros_like(g, dtype=np.float32)
    for i in range(H):
        for j in range(W):
            region = padded_g[i:i+3, j:j+3]
            blurred[i, j] = np.sum(region * gauss_kernel)

    # ===== 2. Laplacian 3x3 trên ảnh đã làm mờ =====
    lap_kernel = np.array([
        [ 0, -1,  0],
        [-1,  4, -1],
        [ 0, -1,  0]
    ], dtype=np.float32)

    padded_blur = np.pad(blurred, pad_width=pad, mode="edge")
    lap = np.zeros_like(g, dtype=np.float32)

    for i in range(H):
        for j in range(W):
            region = padded_blur[i:i+3, j:j+3]
            lap[i, j] = np.sum(region * lap_kernel)

    # ===== 3. Lấy trị tuyệt đối + chuẩn hóa về 0..255 =====
    lap = np.abs(lap)
    max_val = lap.max()
    if max_val > 0:
        lap = lap / max_val * 255.0

    return lap.astype(np.float32)
