import numpy as np

def gaussian_filter(gray: np.ndarray, ksize: int = 3, sigma: float = 1.0) -> np.ndarray:
    if gray.ndim != 2:
        raise ValueError("gaussian_filter chỉ xử lý ảnh xám 2D (H, W).")
    # đảm bảo ksize là số lẻ >= 3
    if ksize % 2 == 0:
        ksize += 1
    if ksize < 3:
        ksize = 3

    g = gray.astype(np.float32)
    H, W = g.shape

    k = ksize // 2
    x = np.arange(-k, k + 1, 1, dtype=np.float32)
    y = np.arange(-k, k + 1, 1, dtype=np.float32)
    X, Y = np.meshgrid(x, y)

    kernel = np.exp(-(X**2 + Y**2) / (2 * sigma**2))
    kernel /= np.sum(kernel)   # chuẩn hóa tổng = 1

    padded = np.pad(g, pad_width=k, mode="edge")
    out = np.zeros_like(g, dtype=np.float32)

    for i in range(H):
        for j in range(W):
            region = padded[i:i+ksize, j:j+ksize]
            out[i, j] = np.sum(region * kernel)

    return out
