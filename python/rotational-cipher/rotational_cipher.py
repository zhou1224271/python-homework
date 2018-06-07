from string import ascii_lowercase, ascii_uppercase


# def shift_char(c, l, k):
#     new_ord = ord(c) + k
#     if new_ord > ord(l[-1]):
#         new_ord = new_ord - len(l)
#     return chr(new_ord)


# def rotate(text, key):
#     new_str = ""
#     for c in text:
#         if c in ascii_lowercase:
#             new_str += shift_char(c, ascii_lowercase, key)
#         elif c in ascii_uppercase:
#             new_str += shift_char(c, ascii_uppercase, key)
#         else:
#             new_str += c
#     return new_str

def rotate(text, key):
    l = ascii_lowercase * 2 + ascii_uppercase * 2
    ret = ""
    for c in text:
        i = l.find(c)
        if i >= 0:
            ret += l[i+key]
        else:
            ret += c
    return ret
