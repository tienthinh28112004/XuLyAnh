# main.py (fixed)
import io, uuid
from pathlib import Path
import numpy as np
from PIL import Image
from flask import Flask, render_template, request, url_for, redirect, flash

from mean_filter import mean_filter
from gaussian_filter import gaussian_filter
from median_filter import median_filter
from sobel_filter import sobel_filter
from prewitt_filter import prewitt_filter
from laplacian_filter import laplacian_filter

FILTERS = {
    "mean":      ("Mean",      mean_filter),
    "gaussian":  ("Gaussian",  gaussian_filter),
    "median":    ("Median",    median_filter),
    "sobel":     ("Sobel",     sobel_filter),
    "prewitt":   ("Prewitt",   prewitt_filter),
    "laplacian": ("Laplacian", laplacian_filter),
}

app = Flask(__name__)
app.secret_key = "change-me"
BASE = Path(__file__).resolve().parent
OUT  = BASE / "static" / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

# -------- helpers I/O ----------

def read_image_bytes_color(b: bytes) -> np.ndarray:
    img = Image.open(io.BytesIO(b)).convert("RGB")
    return np.array(img, dtype=np.float32)

def rgb_to_gray(rgb: np.ndarray) -> np.ndarray:
    if rgb.ndim == 2:
        return rgb
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    return 0.299*r + 0.587*g + 0.114*b

def read_csv_bytes(b: bytes, H: int | None, W: int | None) -> np.ndarray:
    import io as _io
    data = np.loadtxt(_io.BytesIO(b), delimiter=",", dtype=np.float32)
    if H is not None and W is not None:
        if data.size != H * W:
            raise ValueError(f"CSV có {data.size} phần tử, không khớp với H×W = {H * W}.")
        data = data.reshape((H, W))
    else:
        if data.ndim == 1:
            raise ValueError("CSV là vector 1D, hãy nhập chiều cao (H) và chiều rộng (W).")
    return data

def save_img(arr: np.ndarray) -> str:
    arr8 = np.clip(arr, 0, 255).astype(np.uint8)
    name = f"{uuid.uuid4().hex}.png"
    Image.fromarray(arr8).save(OUT / name)
    return name

def call_filter(fn, gray: np.ndarray):
    return fn(gray)

# -------- routes ----------

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mode   = request.form.get("mode", "image")      # "image" | "csv"
        filt_k = request.form.get("filter", "mean")
        H      = request.form.get("height", type=int)
        W      = request.form.get("width",  type=int)

        f = request.files.get("file")
        if not f or f.filename.strip() == "":
            flash("Vui lòng chọn tệp đầu vào.")
            return redirect("/")

        data = f.read()

        try:
            if mode == "csv":
                src_gray = read_csv_bytes(data, H, W)
                src_color_for_show = src_gray
            else:
                src_color = read_image_bytes_color(data)
                src_gray  = rgb_to_gray(src_color)
                src_color_for_show = src_color
        except Exception as e:
            flash(f"Lỗi đọc dữ liệu: {e}")
            return redirect("/")

        if filt_k not in FILTERS:
            flash("Bộ lọc không hợp lệ.")
            return redirect("/")

        label, fn = FILTERS[filt_k]

        try:
            out_gray = call_filter(fn, src_gray)
        except Exception as e:
            flash(f"Lỗi xử lý {label}: {e}")
            return redirect("/")

        left_name  = save_img(src_color_for_show)
        right_name = save_img(out_gray)

        return render_template(
            "index.html",
            filters=FILTERS, selected=filt_k,
            src_url=url_for("static", filename=f"outputs/{left_name}"),
            out_url=url_for("static", filename=f"outputs/{right_name}"),
            note=f"Đã xử lý bằng {label} (lọc chạy trên ảnh xám, ảnh gốc hiển thị giữ nguyên).",
        )

    # GET
    return render_template(
        "index.html",
        filters=FILTERS,
        selected="mean",
        src_url=None,
        out_url=None,
        note=None,
    )

if __name__ == "__main__":
    app.run(debug=True)
