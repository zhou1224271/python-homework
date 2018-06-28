def get_display(h, one, five, ten):
    return ["", one, one * 2, one * 3, one + five, five, five + one, five + one * 2, five + one * 3, one + ten][h]


def numeral(number):
    result = ""

    m, rest = number // 1000, number % 1000
    h, rest = rest // 100, rest % 100
    t, d = rest // 10, rest % 10

    if m != 0:
        result += "M" * m
    result += get_display(h, "C", "D", "M")
    result += get_display(t, "X", "L", "C")
    result += get_display(d, "I", "V", "X")
    return result
