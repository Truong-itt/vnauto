def remove_stopWord(x, data):
    # Tách chuỗi văn bản `x` thành danh sách các từ
    # data = data["stopwords"]
    words = x.split()  # Tách từ dựa trên khoảng trắng
    # Loại bỏ các từ trong danh sách `y`
    filtered_words = [word for word in words if word not in data]
    # Gộp các từ lại thành chuỗi
    result = ' '.join(filtered_words)
    return result
