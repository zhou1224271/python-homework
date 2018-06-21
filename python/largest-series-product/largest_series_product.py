def largest_product(series, size):
    if size < 0 or size > len(series):
        raise ValueError("bad value")
    elif size == 0:
        return 1
    elif not series.isdigit():
        raise ValueError("bad value")
    max_value = 0
    for i in range(0, len(series) - size + 1):
        value = 1
        for v in map(lambda x: int(x), series[i:size + i]):
            value *= v
        if value > max_value:
            max_value = value
    return max_value
