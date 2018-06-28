import collections


def flatten(iterable):
    result = []
    for item in iterable:
        if item is None:
            pass
        elif isinstance(item, tuple) or isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
