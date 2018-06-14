def shake_out(prime, candidates):
    n = 1
    last = candidates[-1]
    dummy = prime
    while dummy < last:
        n = n + 1
        dummy = prime * n
        if dummy in candidates:
            i = candidates.index(dummy)
            del candidates[i]
    return candidates


def sieve(limit):
    candidates = list(range(2, limit + 1))
    for i in range(2, limit + 1):
        if i ** 2 < limit + 1:
            candidates = shake_out(candidates[i - 2], candidates)
    return candidates

# def sieve(limit):
#     linum = [num for num in range(2, limit + 1)]
#     prime = []
#     for pri in linum:
#         pri_ele = [i for i in range(1, pri + 1) if pri % i == 0]
#         if len(pri_ele) == 2:
#             prime.append(pri)
#         else:
#             pass
#     return prime


if __name__ == "__main__":
    assert sieve(1000) == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
        61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
        131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
        193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
        263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331,
        337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401,
        409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
        479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563,
        569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631,
        641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709,
        719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
        809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877,
        881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967,
        971, 977, 983, 991, 997
    ]
