# from string import ascii_lowercase


# def base_trans(text):
#     dest = ''
#     for c in text:
#         if c.isalnum():
#             dest += c
#     return dest.lower().translate(str.maketrans(ascii_lowercase, ascii_lowercase[::-1]))


# def encode(plain):
#     LENGHT = 5
#     cipher = base_trans(plain)
#     l = [(cipher[i:i + LENGHT]) for i in range(0, len(cipher), LENGHT)]
#     return " ".join(l)


# def decode(ciphered):
#     return base_trans(ciphered)

from string import ascii_lowercase, digits


def convert(c):
    if c in ascii_lowercase:
        return chr(ord('z') - (ord(c) - ord('a')))
    elif c in digits:
        return c
    else:
        return ""


def punctuate(src, n):
    dest = ""
    for i, c in enumerate(src):
        dest += c
        if (i + 1) % n == 0:
            dest += " "
    return dest.rstrip()


def encode(plain_text):
    enc = (convert(c) for c in plain_text.lower())
    return punctuate("".join(enc), 5)


def decode(ciphered_text):
    dec = (convert(c) for c in ciphered_text)
    return "".join(dec)
