# SOFA-cable-controlled finger-Khuat-Hung-Anh
để sau
# Mô Phỏng Ngón Tay Robot Điều Khiển Bằng Dây (Cable-Controlled Finger)

## 1. Mục tiêu mô phỏng
Xây dựng mô hình mô phỏng chuyển động của ngón tay softrobot được điều khiển bằng cơ cấu dây kéo trong phần mềm SOFA framework.


## 2. Giới thiệu ngắn gọn về phần mềm
Dự án sử dụng:
- **SOFA Framework**: Nền tảng mô phỏng mã nguồn mở chuyên về cơ học vật thể biến dạng và tương tác thời gian thực.
- **SoftRobots Plugin**: Plugin mở rộng cho SOFA hỗ trợ mô phỏng các cấu trúc robot mềm và các bộ truyền động
  
  
## 3. Hình ảnh hoặc video kết quả
<img width="1904" height="1062" alt="image" src="https://github.com/user-attachments/assets/dec1e5d0-7452-496d-81d1-971acd12181e" />


## 4. Phiên bản phần mềm và thư viện
- **Python**: 3.12.1
- **SOFA**: v26.06 
- **Plugin SOFA bắt buộc**:
  - `SoftRobots` (Plugin mô phỏng robot mềm và cơ cấu dây cáp)
  - `SofaPython3` (Plugin chạy Python 3 trong SOFA)
- **Thư viện phụ thuộc (Python & Module)**:
  - `Sofa.Core`, `Sofa.constants` (Thư viện Python có sẵn trong SofaPython3)
  - `os` (Thư viện chuẩn có sẵn của Python)
 

## 5. Hướng dẫn cài đặt
1. **Clone repository về máy:**
để sau

## 6. Lệnh chạy chương trình
1. Khởi động phần mềm **SOFA GUI** (hoặc gõ `runSofa` trong cửa sổ cmd).
2. Trên thanh menu, chọn **File** $\rightarrow$ **Open Simulation**.
3. Tìm và chọn file: Finger.py (hoặc Finger nếu máy không hiển thị đuôi file
4. Nhấn nút **Animate** (biểu tượng hình tam giác ở phía trên chính giữa màn hình) để bắt đầu tính toán mô phỏng.
   
<p align="center">
  <img width="800" alt="Ảnh 1" src="https://github.com/user-attachments/assets/8fadba13-4d43-4fc1-92c9-ab5e887f7654" />
  <br>
  <em>Hình 1: Cách khởi động phần mềm qua file (có thể tạo shortcut trên desktop)</em>
</p>
<br><br>
<p align="center">
  <img width="800" alt="Ảnh 2" src="https://github.com/user-attachments/assets/d81e5f6a-7111-44db-a671-db92cd41c209" />
  <br>
  <em>Hình 2: Khởi động phần mềm qua cửa sổ cmd</em>
</p>
<br><br>
<p align="center">
  <img width="800" alt="Ảnh 3" src="https://github.com/user-attachments/assets/232a8f44-b44b-46e6-92d7-f9242558a5f5" />
  <br>
  <em>Hình 3: Cách chạy chương trình</em>
</p>


