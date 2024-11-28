import re
def remove_token(x):
    # x = x.lower()
    # giu lai cac ky tu dac biet trong tieng viet
    reg=r'[a-zA-Zàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ ]+'
    y = re.findall(reg,x)
    x = ' '.join(y)
    return x