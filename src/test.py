import time
from vnauto import get_vnauto_instance  

def test_normalization():
    vnauto = get_vnauto_instance()
    text = "bchbp Hai £ 2 mm mik ko bít mai có đi học k, mà chắc là oki! bùl 19/10/2004"
    start_time = time.time()
    result = vnauto.normalize(text)
    end_time = time.time()
    print("Kết quả chuẩn hóa văn bản:", result)
    print(f"Thời gian hoạt động: {end_time - start_time:.6f} giây")

if __name__ == "__main__":
    test_normalization()


