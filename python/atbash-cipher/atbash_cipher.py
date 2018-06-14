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
