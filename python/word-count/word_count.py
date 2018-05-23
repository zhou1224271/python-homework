from collections import defaultdict


def word_count(phrase):
    word_count = defaultdict(int)
    new_word = ""
    for c in phrase:
        c = c.lower()
        if c == "," or c == "_" or c.isspace():
            word_count[new_word.strip("'")] += 1
            new_word = ""
        elif (c >= 'a' and c <= 'z') or (c >= '1' and c <= '9') or c == "'":
            new_word += c
    word_count[new_word.strip("'")] += 1
    word_count.pop("", None)
    return word_count
