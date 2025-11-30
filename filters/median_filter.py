import numpy as np

def median_filter(gray: np.ndarray, ksize: int = 3) -> np.ndarray:

    if gray.ndim != 2:
        raise ValueError("median_filter chỉ xử lý ảnh xám 2D (H, W).")

    # đảm bảo kernel là số lẻ >=3
    if ksize % 2 == 0:
        ksize += 1
    if ksize < 3:
        ksize = 3

    g = gray.astype(np.float32)
    H, W = g.shape
    
    pad = ksize // 2

    # padding replicate để không bị viền đen
    padded = np.pad(g, pad_width=pad, mode="edge")

    out = np.zeros_like(g, dtype=np.float32)

    for i in range(H):
        for j in range(W):
            region = padded[i:i+ksize, j:j+ksize]
            out[i, j] = np.median(region)

    return out
