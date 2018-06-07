def square_of_sum(count):
    total = sum(range(count + 1))
    return total ** 2


def sum_of_squares(count):
    l = [x ** 2 for x in range(count + 1)]
    return sum(l)


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
