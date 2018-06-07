def square_of_sum(count):
    total = sum([x + 1 for x in range(count)])
    return total ** 2


def sum_of_squares(count):
    l = [(x + 1) ** 2 for x in range(count)]
    return sum(l)


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
