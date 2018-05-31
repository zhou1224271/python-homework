from string import ascii_lowercase, ascii_uppercase


def yell(phrase):
    seen = set()
    for c in phrase:
        if c in ascii_lowercase:
            return False
        elif c in ascii_uppercase:
            seen.add(c)
    if len(seen) > 0:
        return True
    else:
        return False


def hey(phrase):
    if len(phrase.strip()) == 0:
        return "Fine. Be that way!"
    elif phrase.strip()[-1] == "?":
        if yell(phrase):
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    elif yell(phrase):
        return "Whoa, chill out!"
    else:
        return "Whatever."
