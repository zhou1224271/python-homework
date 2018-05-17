def is_isogram(string):
    seen = set()
    for x in string.lower():
        if x != " " and x != "-":
            if x in seen:
                return False
            else:
                seen.add(x)
    return True
