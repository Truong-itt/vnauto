import re

def convert_total(text, data): 
    # for key, value in data["teencode"].items():
    for key, value in data.items():
        text = re.sub(rf"\b{re.escape(key)}\b", f" {value} ", text) 
    return text

def convert_total_currency(text, data): 
    for key, value in data.items():
        # Loại bỏ \b và thay thế trực tiếp ký hiệu
        text = re.sub(rf"{re.escape(key)}", f" {value} ", text)
    # Xóa khoảng trắng thừa
    text = ' '.join(text.split())
    return text