def sum_of_multiples(limit, multiples):
    s = set()
    for n in multiples:
        for i in range(1, limit):
            mul = n * i
            if mul >= limit:
                break
            else:
                s.add(mul)
    return sum(s)
