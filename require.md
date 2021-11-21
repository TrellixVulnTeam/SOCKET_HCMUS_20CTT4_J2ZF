------------------------------------------Lưu ý----------------------------------------------------
Sau khi clone về
* Khi dùng python:
- với windows thì dùng lệnh:
Set-ExecutionPolicy -ExecutionPolicy RemoteSign -Scope Process
sau đó
.\venvWinDows\Scripts\activate
* Sau khi dùng lệnh pip để tải thư viện gì thì sau khi tải thư viện về thì dùng tiếp lệnh
pip freeze > requirements.txt
* Sau khi kéo (pull) về thì dùng lệnh sau để update thư viện
pip install -r .\requirements.txt
---------------------------------------------------------------------------------------------------
1 Xử lý socket
KẾT NỐI NHIỀU THIẾT BỊ - Khải
SOCKET (CLIENT) - MÁY THẬT MÁY KHÁC - Luật
SOCKET (SERVER) - WIN SERVER - Khánh

(deadline CN tuần này)

2 Xử lý giao diện
PHẦN GIAO DIỆN CLIENT (ĐĂNG NHẬP ĐĂNG KÝ + DIALOG VỀ LỖI)
GIAO DIỆN SERVER (STATUS KẾT NỐI + THÔNG TIN CỦA HOST) HỎI CÔ

3. Quảng lý dữ liệu thông tin của SERVER
DATA (LƯU JSON)
THÔNG TIN ĐĂNG NHẬP (XONG)

CLIENT {
    SOCKET (OK)
    Giao diện (Kết nối tới server + Đăng nhập - Đăng ký + Query + LOG OUT (ngắt kết nối server) + Hiển thị lỗi (LỖI KẾT NỐI + LỖI ĐĂNG NHẬP KHÔNG THÀNH CÔNG + LỖI NHẬP TÊN SAI)) (Khải Khánh)
    Chức năng chuẩn hóa dữ liệu tên tỉnh (Viết tắt + Gợi ý) ()
    MESSAGE ?? (GUI xử lý sự kiện) (cuối)
}

SERVER {
    SOCKET (OK)
    Chứa THÔNG TIN TÀI KHOẢN, DATA COVID (OK)
    Giao diện (status (nó đang kết nối với ai IP PORT + Status (đang kết nối + mất kết nối) + Server (on/off)) (Luật)
    MESSAGE ?? (GUI xử lý sự kiện) (cuối)
}

(T5 25/11/2021)

Cộng nghệ quản lý đồ án:
github
GIAO DIỆN code bằng thư viện kivy của python
SOCKET code bằng thư viện socket của python
DATA lưu trong file json
