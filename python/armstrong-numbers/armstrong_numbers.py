def is_armstrong(number):
    keta = len(str(number))
    l = [int(n) ** keta for n in str(number)]
    return sum(l) == number
