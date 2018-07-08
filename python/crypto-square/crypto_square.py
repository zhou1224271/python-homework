import string
import re

alphabets = string.ascii_lowercase


def encode(plain_text):

    ptn = r"\w"
    alphas_lst = re.findall(ptn, plain_text.lower())
    alphas = "".join(alphas_lst)

    if alphas == "":
        return ""

    cxr = rectangle(alphas)

    if cxr[3] > 0:
        alphas = alphas + " " * (cxr[0] - cxr[3])

    rt = [alphas[i:i + cxr[0]] for i in range(0, cxr[2], cxr[0])]
    first_rt_len = len(rt[0])
    rst_lst = list()

    for x in range(0, first_rt_len):
        tmp_rst = ""
        for y in rt:
            tmp_rst = tmp_rst + y[x:x+1]
        rst_lst.append(tmp_rst)

    if cxr[1] == 1:
        rst = rst_lst[0]
    else:
        rst = " ".join(rst_lst)

    return rst


def rectangle(in_param):

    rst = list()
    str_len = len(in_param)
    if str_len == 1:
        return [1, 1, 1, 0]

    b = str_len // 2 + 1

    sum_a = 0
    sum_b = 0
    lst_a = [[x, x + 1] for x in range(0, b)]
    lst_b = [[x, x] for x in range(0, b)]
    min_a = list()
    min_b = list()

    for x in lst_a:
        sum_a = x[0] * x[1]
        if sum_a >= str_len:
            min_a = x
            break

    for x in lst_b:
        sum_b = x[0] * x[1]
        if sum_b >= str_len:
            min_b = x
            break

    if sum_a >= sum_b:
        rst.append(min_b[1])
        rst.append(min_b[0])
    else:
        rst.append(min_a[1])
        rst.append(min_a[0])

    rst.append(str_len)
    rst.append(str_len % rst[0])

    return rst
