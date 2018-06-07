from string import ascii_lowercase, ascii_uppercase


def shift_char(c, l, k):
    new_ord = ord(c) + k
    if new_ord > ord(l[-1]):
        new_ord = new_ord - len(l)
    return chr(new_ord)


def rotate(text, key):
    new_str = ""
    for c in text:
        if c in ascii_lowercase:
            new_c = shift_char(c, ascii_lowercase, key)
            new_str += new_c
        elif c in ascii_uppercase:
            new_c = shift_char(c, ascii_uppercase, key)
            new_str += new_c
        else:
            new_str += c
    return new_str
