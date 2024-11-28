# **VnAuto**

**VnAuto** là một thư viện Python mạnh mẽ dành cho xử lý ngôn ngữ tự nhiên tiếng Việt. Thư viện này được thiết kế để hỗ trợ các nhà phát triển trong việc chuẩn hóa văn bản, loại bỏ stopwords, xử lý emoji, chuyển đổi số thành chữ, chuẩn hóa ngày tháng, và nhiều tính năng khác.

---

## **Tính năng nổi bật**
- **Chuẩn hóa văn bản tiếng Việt**: Chuyển đổi văn bản không dấu, viết tắt, teencode về dạng chuẩn.
- **Xử lý stopwords**: Loại bỏ các từ không cần thiết trong tiếng Việt.
- **Chuyển đổi số thành chữ**: Hỗ trợ chuyển đổi các số (bao gồm ngày, tháng, năm) sang dạng chữ.
- **Xử lý emoji**: Phát hiện và chuẩn hóa emoji trong văn bản.
- **Xử lý ký tự đặc biệt**: Loại bỏ hoặc chuẩn hóa các ký tự đặc biệt và dấu câu.
- **Tùy chỉnh linh hoạt**: Người dùng có thể bật/tắt từng tính năng theo nhu cầu.

---

## **Cài đặt**

Cài đặt thư viện dễ dàng bằng pip:

```bash
pip install vnauto
```

---

## **Hướng dẫn sử dụng**

### **Khởi tạo thư viện**
```python
from vnauto import get_vnauto_instance

# Tạo đối tượng xử lý
vnauto = get_vnauto_instance()

# Văn bản cần chuẩn hóa
text = "Xin chào mn! Hnay là ngày 21/10/2024 :D"

# Chuẩn hóa văn bản
result = vnauto.normalize(text)
print(result)
```

### **Đầu vào mẫu:**
```plaintext
"Xin chào mn! Hnay là ngày 21/10/2024 :D"
```

### **Kết quả đầu ra:**
```plaintext
"xin chào mọi người! hôm nay là ngày hai mốt tháng mười năm hai nghìn không trăm hai mươi bốn :D"
```

---

## **Các chức năng chi tiết**

### **1. Chuẩn hóa văn bản**
Chuyển đổi teencode, từ viết tắt, và các từ sai chính tả về dạng chuẩn.
```python
text = "Ko bít mai có đi học k?"
result = vnauto.normalize(text)
# Kết quả: "không biết mai có đi học không?"
```

### **2. Chuyển đổi số thành chữ**
Chuyển đổi số sang dạng chữ tiếng Việt.
```python
text = "Hôm nay là ngày 21 tháng 10 năm 2024"
result = vnauto.normalize(text)
# Kết quả: "hôm nay là ngày hai mốt tháng mười năm hai nghìn không trăm hai mươi bốn"
```

### **3. Xử lý stopwords**
Loại bỏ các từ không cần thiết (ví dụ: "là", "của", "và", ...).
```python
text = "Đây là một ví dụ về stopwords"
result = vnauto.normalize(text)
# Kết quả: "Đây ví dụ stopwords"
```

### **4. Xử lý emoji**
Chuẩn hóa hoặc loại bỏ emoji trong văn bản.
```python
text = "Xin chào 😊! Tôi rất vui 😍"
result = vnauto.normalize(text)
# Kết quả: "xin chào! tôi rất vui"
```

### **5. Chuẩn hóa ký tự đặc biệt**
Loại bỏ hoặc chuẩn hóa các ký tự không cần thiết như dấu chấm câu liên tiếp, khoảng trắng thừa.
```python
text = "Hello!!!    Đây là văn   bản  . ."
result = vnauto.normalize(text)
# Kết quả: "hello đây là văn bản"
```

---

## **Tùy chỉnh tính năng**

Thư viện cho phép bật/tắt từng tính năng qua tham số `features` trong phương thức `normalize`.
```python
features = {
    "unicode": True,
    "lowercase": True,
    "currencyUnit": True, 
    "acronyms": True,
    "acronymsShorten": True,
    "teencode": True,
    "date": True,
    "numbers": True,
    "stopwords": False,
    "symbols": True,
    "prefixUnit": True,
    "token": True,
    "character": True,
    "emoji": True,
    "fix_punct_space": True,
    "dedup_punct": True,
    "trim_extra_chars": True,
    "remove_punct": True,
    "fix_whitespace": True,
    "clean_underscores": True,
}
result = vnauto.normalize(text, features=features)
```

---

## **Tài liệu**
Tham khảo tài liệu đầy đủ tại [GitHub VnAuto](https://github.com/Truong-itt/vnauto).

---

## **Đóng góp**
Nếu bạn có ý tưởng hoặc muốn đóng góp cho thư viện, hãy mở Pull Request hoặc Issue tại [GitHub Repository](https://github.com/Truong-itt/vnauto).

---

## **Thông tin liên hệ**
- **Tác giả**: [TruongItt](https://github.com/Truong-itt), [Vien Vien](https://github.com/VienVien123) 
- **Email**: hoduytruong280220@gmail.com

---

Hãy sử dụng **VnAuto** để chuẩn hóa và xử lý văn bản tiếng Việt dễ dàng hơn bao giờ hết! 😊
