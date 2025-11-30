import numpy as np

def laplacian_filter(gray: np.ndarray) -> np.ndarray:
    if gray.ndim != 2:
        raise ValueError("laplacian_filter chỉ xử lý ảnh xám 2D.")
    g = gray.astype(np.float32)
    H, W = g.shape
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
    lap = np.abs(lap)
    max_val = lap.max()
    if max_val > 0:
        lap = lap / max_val * 255.0

    return lap.astype(np.float32)
