def slices(series, length):
    if length > len(series):
        raise ValueError("too long")
    elif length == 0:
        raise ValueError("too short")
    else:
        results = []
        for i in range(len(series)):
            if len(series[i:]) >= length:
                result = series[i:i + length]
                results.append([int(x) for x in result])
            else:
                break
        return results
