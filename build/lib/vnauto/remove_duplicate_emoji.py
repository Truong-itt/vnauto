import re
import string
# from underthesea import text_normalize

def clean_text_emmoji(text, data):
    # Thay thế emoji bằng chuỗi rỗng để loại bỏ
    emoji_dict = data
    for emoji, _ in emoji_dict.items():
        text = text.replace(emoji, " _ ")

    # Loại bỏ các ký tự không mong muốn còn sót từ emoji (như ký tự `️`)
    text = re.sub(r"[️]+", " ", text)  # Xóa các ký tự còn sót
    return text