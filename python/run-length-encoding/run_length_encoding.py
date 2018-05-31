def decode(string):
    dec = []
    cnt = ""
    for c in string:
        if (c >= "A" and c <= "z") or c == " ":
            if cnt == "":
                dec.append(c)
            else:
                dec.extend(c * int(cnt))
            cnt = ""
        else:
            cnt += c
    return "".join(dec)


def encode(string):
    last_seen = ""
    cnt = 0
    enc = ""
    for c in string:
        if last_seen == "":
            pass
        elif c == last_seen:
            cnt += 1
        else:
            if cnt == 0:
                enc += last_seen
            else:
                enc += str(cnt+1)
                enc += last_seen
                cnt = 0
        last_seen = c
    if cnt == 0:
        enc += last_seen
    else:
        enc += str(cnt+1)
        enc += last_seen
    return enc
