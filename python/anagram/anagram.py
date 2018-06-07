from collections import defaultdict


def to_dict(word):
    d = defaultdict(int)
    for c in word:
        d[c] += 1
    return d


def detect_anagrams(word, candidates):
    targets = []
    word = word.lower()
    for target in candidates:
        lower_target = target.lower()
        if lower_target == word:
            pass
        elif to_dict(word) == to_dict(lower_target):
            targets.append(target)
    return targets
