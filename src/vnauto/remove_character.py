import re
def remove_character(x):
    return re.sub(r'(.)\1+', r'\1', x)