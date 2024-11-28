import re

def convert_number(text, data):
    def number_to_words(num):
        length = len(num)

        def two_digits_to_words(n):
            if n[0] == '1':  # Hàng chục là 1
                if n[1] == '0':  # Trường hợp đặc biệt: "10"
                    return "mười"
                elif n[1] == '5':  # Trường hợp đặc biệt: "15"
                    return "mười lăm"
                else:
                    return "mười " + data[n[1]]
            else:  # Hàng chục khác 1
                tens = data[n[0]] + " mươi"
                units = data[n[1]]
                if n[1] == '0':  # Tròn chục
                    return tens
                elif n[0] == '2' and n[1] == '1':  # Trường hợp đặc biệt: "21"
                    return "hai mốt"
                elif n[1] == '5':  # Lăm thay vì năm
                    return tens + " lăm"
                else:
                    return tens + " " + units

        def three_digits_to_words(n):
            hundreds = data[n[0]] + " trăm"
            if n[1] == '0' and n[2] == '0':  # Tròn trăm
                return hundreds
            if n[1] == '0':  # Trường hợp hàng chục là 0
                return hundreds + " lẻ " + data[n[2]]
            return hundreds + " " + two_digits_to_words(n[1:])

        def large_number_to_words(n):
            thousands = data[n[0]] + " nghìn"
            remainder = n[1:]
            if remainder == "000":  # Tròn nghìn
                return thousands
            if len(remainder) == 3:
                return thousands + " " + three_digits_to_words(remainder)
            if len(remainder) == 2:
                return thousands + " " + two_digits_to_words(remainder)
            return thousands + " lẻ " + data[remainder[0]]

        # Xử lý từng trường hợp dựa vào độ dài
        if length == 1:  # Một chữ số
            return data[num]
        elif length == 2:  # Hai chữ số
            return two_digits_to_words(num)
        elif length == 3:  # Ba chữ số
            return three_digits_to_words(num)
        elif length == 4:  # Bốn chữ số
            return large_number_to_words(num)
        else:
            return num  # Giữ nguyên nếu vượt quá giới hạn

    def process_date(match):
        day, month, year = match.group(1), match.group(2), match.group(3)
        day_text = number_to_words(day)  # Xử lý ngày
        month_text = number_to_words(month)  # Xử lý tháng
        year_text = number_to_words(year)  # Xử lý năm
        return f"ngày {day_text} tháng {month_text} năm {year_text}"

    # Thay thế ngày tháng năm
    text = re.sub(r"ngày (\d{1,2}) tháng (\d{1,2}) năm (\d{4})", process_date, text)

    # Áp dụng thay thế cho tất cả các số
    text = re.sub(r'\b\d+\b', lambda match: number_to_words(match.group(0)), text)
    return text
