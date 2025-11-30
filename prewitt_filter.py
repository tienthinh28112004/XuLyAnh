# prewitt_filter.py
import numpy as np

def prewitt_filter(gray: np.ndarray) -> np.ndarray:
    """
    Bộ lọc Prewitt phát hiện biên theo hướng x và y.
    Trả về ảnh float32 cùng kích thước đầu vào.

    - gray: ảnh xám 2D numpy (H, W)
    - return: ảnh float32 (H, W)
    """

    if gray.ndim != 2:
        raise ValueError("prewitt_filter chỉ xử lý ảnh xám 2D.")

    g = gray.astype(np.float32)
    H, W = g.shape

    # Kernel Prewitt
    kernel_x = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ], dtype=np.float32)

    kernel_y = np.array([
        [ 1,  1,  1],
        [ 0,  0,  0],
        [-1, -1, -1]
    ], dtype=np.float32)

    pad = 1
    padded = np.pad(g, pad_width=pad, mode="edge")

    out = np.zeros_like(g, dtype=np.float32)

    # Tính gradient theo Prewitt
    for i in range(H):
        for j in range(W):
            region = padded[i:i+3, j:j+3]

            gx = np.sum(region * kernel_x)
            gy = np.sum(region * kernel_y)

            out[i, j] = np.sqrt(gx**2 + gy**2)

    return out.astype(np.float32)
