import re
import string

# Chuẩn hóa khoảng trắng xung quanh dấu câu
# example : "Hello ,world ! This is a test :example."
# output : "Hello , world ! This is a test : example."
def fix_punct_space(text):
    # Thêm khoảng trắng xung quanh dấu câu
    text = re.sub(r"(\w)\s*([" + string.punctuation + "])\s*(\w)", r"\1 \2 \3", text)
    text = re.sub(r"(\w)\s*([" + string.punctuation + "])", r"\1 \2", text)
    return text

# Giảm bớt các dấu câu liên tiếp
# example: "Hello,,, world!! This is a test::: example.."
# output: "Hello, world! This is a test: example."
def dedup_punct(text):
    # Rút gọn các dấu câu liên tiếp
    text = re.sub(f"([{string.punctuation}])([{string.punctuation}])+", r"\1", text)
    return text

# Loại bỏ ký tự thừa ở đầu và cuối văn bản
# example: "!!!Hello, world!!!"
# output: "Hello, world"
def trim_extra_chars(text):
    # Loại bỏ dấu câu và khoảng trắng ở đầu và cuối
    text = text.strip(string.punctuation + string.whitespace)
    return text

# Loại bỏ toàn bộ dấu câu còn lại
# example: "Hello, world! This is a test: example."
# output: "Hello world This is a test example"
def remove_punct(text):
    # Loại bỏ toàn bộ dấu câu
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

# Chuẩn hóa khoảng trắng
# example: "Hello     world!   This  is    a test."
# output: "Hello world! This is a test."
def fix_whitespace(text):
    # Chuẩn hóa khoảng trắng thừa trong văn bản
    text = " ".join(text.split())
    return text

# Loại bỏ các dấu _ liên tiếp
# example: "Hello ___ world _ This __ is _ a test."
# output: "Hello world This is a test."
def clean_underscores(text):
    # Loại bỏ chuỗi dấu gạch dưới liên tiếp
    text = re.sub(r"(_\s*)+", "", text)
    return text
