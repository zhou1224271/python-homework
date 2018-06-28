class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ","")

    def is_valid(self):
        if self.card_num == "0":
            return False
        total = 0
        for i, d in enumerate(self.card_num[::-1]):
            try: 
                d = int(d)
            except Exception:
                return False
            if i % 2 == 1:
                d =  2 * d
                if d >= 9:
                    d = d - 9
            total += d
        return total % 10 == 0