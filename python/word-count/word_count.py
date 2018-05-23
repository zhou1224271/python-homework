from collections import defaultdict


def add_word(d, w):
    word = w.strip("'")
    if word:
        d[word] += 1


def word_count(phrase):
    word_count = defaultdict(int)
    new_word = ""
    for c in phrase.lower():
        if c == "," or c == "_" or c.isspace():
            add_word(word_count, new_word)
            new_word = ""
        elif (c >= 'a' and c <= 'z') or (c >= '1' and c <= '9') or c == "'":
            new_word += c
    # 最後の単語忘れないよに
    add_word(word_count, new_word)
    return word_count
