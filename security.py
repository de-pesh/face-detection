def check_name(t):
    result = False
    if ord(t[0]) < 65:
        result = True
    elif ord(t[0]) > 122:
        result = True
    elif ord(t[0]) < 97 and ord(t[0]) > 90:
        result = True
    return result