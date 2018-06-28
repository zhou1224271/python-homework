import collections


def flatten(iterable):
    result = []
    for item in iterable:
        if item == None:
            pass
        elif isinstance(item, tuple):
            result.extend(flatten(item))
        elif isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
