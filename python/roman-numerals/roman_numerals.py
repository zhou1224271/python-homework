def get_display(h, one, five, ten):
    if h == 9:
        return one + ten
    elif h == 8:
        return five + one * 3
    elif h == 7:
        return five + one * 2
    elif h == 6:
        return five + one
    elif h == 5:
        return five
    elif h == 4:
        return one + five
    elif h == 3:
        return one * 3
    elif h == 2:
        return one * 2
    elif h == 1:
        return one * 1
    elif h == 0:
        return ""


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
