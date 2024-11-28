import os
import pandas as pd
def load_mapping_file(file_path):
    """
    Đọc một file mapping (có định dạng key#value) và trả về dictionary.
    """
    mapping = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if "#" in line:
                key, value = line.strip().split("#", 1)
                mapping[key] = value
    return mapping

def load_list_file(file_path):
    """
    Đọc một file danh sách (mỗi dòng là một phần tử) và trả về danh sách.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

def load_emoji_dict(file_path):
    emoji_dict = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("\t")  # Tách emoji và ý nghĩa
            if len(parts) == 2:
                emoji, meaning = parts
                emoji_dict[emoji] = meaning
    return emoji_dict

def load_stopwords(file_path):
    stopWord = pd.read_csv(file_path, header=None, encoding="utf-8")
    stopwords_list = stopWord[0].tolist()
    return stopwords_list



def load_all_data(base_dir):
    """
    Tải tất cả dữ liệu từ thư mục chỉ định.
    """
    data = {     
        "acronyms": load_mapping_file(os.path.join(base_dir, "Acronyms.txt")),
        "acronymsShorten": load_mapping_file(os.path.join(base_dir, "Acronyms_shorten.txt")),
        "baseUnit": load_mapping_file(os.path.join(base_dir, "BaseUnit.txt")),
        "currencyUnit": load_mapping_file(os.path.join(base_dir, "CurrencyUnit.txt")),
        "prefixUnit": load_mapping_file(os.path.join(base_dir, "PrefixUnit.txt")),
        "symbol": load_mapping_file(os.path.join(base_dir, "Symbol.txt")),
        "teencode": load_mapping_file(os.path.join(base_dir, "Teencode.txt")),
        "numbers": load_mapping_file(os.path.join(base_dir, "Number.txt")),
        "emojicon": load_emoji_dict(os.path.join(base_dir, "emojicon.txt")),
        "stopwords": load_stopwords(os.path.join(base_dir, "vietnamese-stopwords.txt")),
    }
    return data
