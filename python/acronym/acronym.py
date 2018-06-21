def abbreviate(words):
    return "".join(map(lambda x: x[0].upper(), words.replace(",", " ").replace("-", " ").split()))
