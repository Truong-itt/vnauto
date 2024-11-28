from datetime import datetime
import re

def process_text_with_date(text):
    # Tìm ngày tháng trong câu
    date_pattern = r"\b(\d{2}/\d{2}/\d{4})\b"
    match = re.search(date_pattern, text)
    if match:
        # Lấy chuỗi ngày tháng
        date_string = match.group(0)
        # Chuyển đổi sang datetime
        date_obj = datetime.strptime(date_string, "%d/%m/%Y")
        # Tính toán (ví dụ: ngày trong tuần)
        weekday_vietnamese = {
            "Monday": "thứ hai",
            "Tuesday": "thứ ba",
            "Wednesday": "thứ tư",
            "Thursday": "thứ năm",
            "Friday": "thứ sáu",
            "Saturday": "thứ bảy",
            "Sunday": "chủ nhật"
        }
        weekday = weekday_vietnamese[date_obj.strftime("%A")]
        # Định dạng ngày đẹp
        formatted_date = date_obj.strftime("ngày %d tháng %m năm %Y")
        # Thay thế trong câu gốc
        updated_text = text.replace(date_string, f"{formatted_date} ({weekday})")
        return updated_text
    else:
        return text