# BÀI TẬP LỚN: XỬ LÝ ẢNH  


**Tên nhóm:** Nhóm 24 – Môn xử lý ảnh-02  
**Chủ đề đã đăng ký:** Bộ lọc ảnh nâng cao chất lượng ảnh số

## THÔNG TIN NHÓM

| STT | Họ và Tên | MSSV | Email |
|-----|-----------|------|-------|
| 1 | Bùi Tiến Thịnh | B22DCCN829 | tienthinh28112004@gmail.com |
---

## MÔ TẢ HỆ THỐNG
Hệ thống hỗ trợ người dùng **xử lý và nâng cao chất lượng ảnh số** thông qua hai nhóm bộ lọc chính: **bộ lọc làm mịn** và **bộ lọc phát hiện biên**.

Giao diện được xây dựng bằng **HTML/CSS**, cho phép hiển thị **ảnh gốc** và **ảnh sau xử lý** song song. Backend sử dụng **Flask** để nhận ảnh từ người dùng, chuyển đổi sang mảng **NumPy** và thực thi các thuật toán xử lý được lập trình **thuần bằng NumPy** (không dùng OpenCV).

Hệ thống hỗ trợ **ba bộ lọc làm mịn** gồm **Mean**, **Median**, **Gaussian** nhằm giảm nhiễu và làm mượt ảnh; cùng với **ba bộ lọc phát hiện biên** gồm **Laplacian**, **Prewitt**, **Sobel** để xác định đường biên và các vùng biến đổi mạnh.

Quy trình hoạt động: **người dùng tải ảnh → Flask xử lý ảnh theo bộ lọc đã chọn → giao diện hiển thị kết quả**. Nhờ thiết kế module hóa, mỗi bộ lọc nằm trong **một file riêng**, giúp hệ thống **dễ mở rộng** và **dễ bảo trì**.




## HƯỚNG DẪN CHẠY DỰ ÁN

### 1. Clone repository
```bash
git clone https://github.com/tienthinh28112004/XuLyAnh.git
cd XuLyAnh
```

### 2. Chạy cấu hình dự án ban đầu
```bash
pip install -r requirements.txt

```
### 3. Chạy dự án
```bash
python main.py

```

## CẤU TRÚC DỰ ÁN


```
├── filters
│   ├── __init__.py
│   ├── gaussian_filter.py      #Bộ lọc làm mịn Gaussian Filter 
│   ├── laplacian_filter.py     #Bộ lọc phát hiện biên Laplacian Filter
│   ├── mean_filter.py          #Bộ lọc làm mịn Mean Filter
│   ├── median_filter.py        #Bộ lọc làm mịn Median Filter
│   ├── prewitt_filter.py       #Bộ lọc phát hiện biên Prewitt Filter
│   └── sobel_filter.py         #Bộ lọc phát hiện boeen Sobel Filter
├── static
├── templates
│   └── index.html
├── Báo cáo xử lý ảnh.pdf       #File báo cáo
├── Slide xử lý ảnh.pdf         #File Silde
├── main.py                     #File main chính
└── requirements.txt
```
---
