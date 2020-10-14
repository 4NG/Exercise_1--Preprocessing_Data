# Exercise_1--Preprocessing_Data
# CS313.K21 Exercise 
Xây dựng chương trình console với định dạng:
  <program_name> <op tion> <input_data> <output_data> <data_log>
 
1.<program_name> : tên chương trình tùy đặt

2.<op tion> : các tùy chọn
  
 a. Tóm tắt dữ liệu: <summary>
  
      - số mẫu
  
      - số thuộc tính
      
      - <data_log> -> <thuộc tính> : <tên> <kiểu dữ liệu>
      
  
 b. Điền giá trị bị thiếu: <replace>
  
      - thay thế "?" bằng giá trị mới: nominal -> popular value, numeric -> mean value
  
      - <data_log> -> <thuộc tính> : <tên thuộc tính>, <số giá trị thiếu>, <giá trị mới>
      
  
 c. Chia giỏ một hoặc nhiều thuộc tính numeric:  <discretize>
  
      - Nhập số giỏ cần chia, phương pháp chia (chiều sâu hoặc chiều rộng)
  
      - <data_log> -> <thuộc tính> : <tên thuộc tính> <miền giá trị giỏ 1> : <số mẫu> ... 
                                        <miền giá trị giỏ K> : <số mẫu>
      

                                          
 d. Chuẩn hóa các thuộc tính có kiểu numeric: <normalize>
  
      - Min-max, Z-score
  
      - <data_log> -> <thuộc tính>: <tên thuộc tính> <miền giá trị mới>
      

  
3.<input_data> : 

    - Dòng đầu: danh sách <thuộc tính>, cách nhau bởi dấu ","
    
    - Các dòng tiếp: mỗi dòng là 1 mẫu, cách nhau bởi dấu ","
    
    - nominal: chữ cái hoặc chuỗi
    
    - numeric: chữ số
    
4. <output_data> : dữ liệu đã xử lí

5. <data_log> : ghi lại những thay đổi cụ thể trong từng function.

** Cập nhật tình hình làm việc:

1. Sử dụng file .csv làm định dạng file input và output.
2. Tất cả lịch sử thay đổi khi sử dụng các function lên data được lưu lại trong file log - định dạng .txt.
3. Ba bộ dữ liệu test được tách từ file Indian_Liver_Patient_Dataset.csv ở bài tập 1.

6. Hướng dẫn sử dụng:

  - Chạy Preprocessing_Data.
  - Chạy main.
  - Nhập file dữ liệu cần xử lí vào console ở phần yêu cầu.
  - Nhập tên file output (định dạng .csv)
  - Nhập tên file log (định dạng .txt)
  - Sử dụng các options trong console (thứ tự 1, 2, 3, 4, 5).
  - Sau khi sử dụng 1 option, các thay đổi sẽ hiển thị trên màn hình console.
  - Sau khi exit, các thay đổi cũng như dữ liệu đầu ra sẽ được lưu vào file output và log.
  
