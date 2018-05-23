def verify(isbn):
    digits = []
    for c in isbn:
        if c != '-':
            digits.append(c)
    if len(digits) != 10:
        return False

    sum = 0

    for i, d in enumerate(digits):
        if i == 9 and d == 'X':
            value = 10
        else:
            try:
                value = int(d)
            except Exception:
                return False
        sum += (len(digits) - i) * value
    return sum % 11 == 0
