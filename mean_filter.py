# mean_filter.py (phiên bản tự viết, không dùng cv2)
import numpy as np

def mean_filter(gray: np.ndarray, ksize: int = 3) -> np.ndarray:
    if gray.ndim != 2:
        raise ValueError("mean_filter chỉ xử lý ảnh xám 2D (H, W).")

    if ksize % 2 == 0:
        ksize += 1
    if ksize < 3:
        ksize = 3

    g = gray.astype(np.float32)
    pad = ksize // 2

    # Padding ảnh ở biên bằng replicate (lặp biên)
    padded = np.pad(g, pad_width=pad, mode="edge")

    H, W = g.shape
    out = np.zeros_like(g, dtype=np.float32)

    kernel = np.ones((ksize, ksize), dtype=np.float32) / (ksize * ksize)

    for i in range(H):
        for j in range(W):
            region = padded[i:i+ksize, j:j+ksize]
            out[i, j] = np.sum(region * kernel)

    return out
