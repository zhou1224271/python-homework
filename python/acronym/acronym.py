def abbreviate(words):
    return "".join(map(lambda x: x[0:1].upper(), words.replace("-", " ").split()))
