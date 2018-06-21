english = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
           "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
           "twenty"]
english2 = ["zero", "ten", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety", ]


def split_by_scale(number, scale):
    return divmod(number, scale)  # number//scale, number % scale


def say_digit(digit):
    return english[digit]


def say_double_digit(double_digit):
    assert (double_digit < 100)
    t, rest = split_by_scale(double_digit, 10)
    parts = []
    if t > 1:
        parts.append(english2[t])
        if rest != 0:
            parts.append(english[rest])
    else:
        parts.append(english[int(double_digit)])
    return "-".join(parts)


def say_part(part):
    assert (part < 1000)
    h, rest = split_by_scale(part, 100)
    # t, digit = split_by_scale(rest, 10)
    parts = []
    if h != 0:
        parts.append(say_digit(h) + " hundred")
    if rest != 0:
        parts.append(say_double_digit(rest))

    return " and ".join(parts)


def say(number):
    if number >= 1000 ** 4 or number < 0:
        raise ValueError("bad value")
    b, rest = split_by_scale(number, 1000 ** 3)
    m, rest = split_by_scale(rest, 1000 ** 2)
    t, rest = split_by_scale(rest, 1000)
    sentence = ""
    parts = []
    if b != 0:
        parts.append(say_part(b) + " billion")
    if m != 0:
        parts.append(say_part(m) + " million")
    if t != 0:
        parts.append(say_part(t) + " thousand")
    if rest != 0:
        parts.append(say_part(rest))
    if len(parts) != 0:
        if t == 0:
            return " and ".join(parts)
        else:
            return " ".join(parts)
    else:
        return "zero"
