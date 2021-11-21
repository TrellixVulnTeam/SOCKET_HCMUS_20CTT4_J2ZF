

                ---------------------------------
                |      process (tiến trình)     |
                |                               |
    ------------|         client                |-----------
    
    input stream                                sendall

    ------------|                               |------------
                |                               |
                |                               |
    ------------|                               |-------------

    output stream                               recieve

    ------------|                               |--------------
                |                               |
                |                               |
                ---------------------------------
    - input{
        - Khởi tạo kết nối đến server
            1. Tạo socket
            2. Tạo connect tới server
        - Thông tin đăng nhập
            1. Send mã "loginUsr"
            2. Send các thông tin sau khi nhận phản hồi mã "loginUsr"
            3. lấy các thông tin {
                + Thông tin đăng nhập: 
                + Thông tin đăng ký
            }
            4. Send lại thông tin đăng nhập nếu lỗi sai
        - Thông tin đăng ký
            1. Send mã "signUpUsr"
            2. Send các thông tin sau khi nhận phản hồi mã "loginUsr"
            3. lấy các thông tin {
                + Thông tin đăng nhập: 
                + Thông tin đăng ký
            }
        - Thông tin tra cứu
            1. Send mã "searchCov"
            2. Send các thông tin sau khi nhận phản hồi 
        - Đóng kết nối
            1. Thực thi lệnh close
    }
    - output {
        - 
    }