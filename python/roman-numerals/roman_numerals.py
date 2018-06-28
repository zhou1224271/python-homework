# def numeral(number):
#     num_list=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#     str_list=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
#     res=''
#     for i in range(len(num_list)):
#         while number>=num_list[i]:
#             number-=num_list[i]
#             res+=str_list[i]
#     return res


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
