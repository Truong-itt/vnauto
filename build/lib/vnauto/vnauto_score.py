from .data_loader import load_all_data
from .convert_number import convert_number
from .convert_win1252_to_utf8 import covert_unicode
from .convert_datetime import process_text_with_date
from .convert_total import convert_total, convert_total_currency
from .remove_token import remove_token
from .remove_stopword import remove_stopWord
from .remove_character import remove_character
from .remove_duplicate_emoji import clean_text_emmoji
from underthesea import text_normalize
from .standardize_total import *

class Vnauto:
    def __init__(self, base_dir):
        self.data = load_all_data(base_dir)

    def normalize(self, text, features=None):
        """
        Thực hiện chuẩn hóa văn bản dựa trên dữ liệu.
        """
        if features is None:
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
        # format chu
        if features.get("unicode"):
            text = covert_unicode(text)

        # format lower
        if features.get("lowercase"):
            text = text.lower()

        # xu li currencyUnit
        if features.get("currencyUnit"):
            text = convert_total_currency(text, self.data["currencyUnit"])

        # xu li acronyms
        if features.get("acronyms"):
            text = convert_total(text, self.data["acronyms"])

        # xu li acronyms_shorten
        if features.get("acronymsShorten"):
            text = convert_total(text, self.data["acronymsShorten"])

        # xu li teencode
        if features.get("teencode"):
            text = convert_total(text, self.data["teencode"])

        # xu li ngay thang
        if features.get("date"):
            text = process_text_with_date(text)

        # xu li so thanh chu
        if features.get("numbers"):
            text = convert_number(text, self.data["numbers"])

        # xoa stopword trong cau
        if features.get("stopwords"):
            text = remove_stopWord(text, self.data["stopwords"])
        
        # xu li symbol
        if features.get("symbols"):
            text = convert_total(text, self.data["symbol"])

        # xu li prefixUnit
        if features.get("prefixUnit"):
            text = convert_total(text, self.data["prefixUnit"])

        # romove token
        if features.get("token"):
            text = remove_token(text)

        # remove charactor
        if features.get("character"):
            text = remove_character(text)
        
        # remove emoji and duplicate in text
        if features.get("emoji"):
            text = clean_text_emmoji(text, self.data["emojicon"])
        
        if features.get("fix_punct_space"):
            text = fix_punct_space(text)
        
        if features.get("dedup_punct"):
            text = dedup_punct(text)
        
        if features.get("trim_extra_chars"):
            text = trim_extra_chars(text)
        
        if features.get("remove_punct"):
            text = remove_punct(text)

        if features.get("fix_whitespace"):
            text = fix_whitespace(text)
        
        if features.get("clean_underscores"):
            text = clean_underscores(text)

        text = text_normalize(text) 
        return text
    