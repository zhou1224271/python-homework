import itertools


class Allergies(object):

    def __init__(self, score):

        self.score = score

    def is_allergic_to(self, item):

        return item in self.lst

    @property
    def lst(self):

        allergies_lst = {'1': 'eggs',
                         '2': 'peanuts',
                         '4': 'shellfish',
                         '8': 'strawberries',
                         '16': 'tomatoes',
                         '32': 'chocolate',
                         '64': 'pollen',
                         '128': 'cats'}

        tmp_ls = list()

        int_a = [2 ** x for x in range(0, 8)]

        ls = self.get_keyls(self.score, int_a)

        for x in range(1, len(ls) + 1):

            tmp_l = itertools.combinations(ls, x)

            for l in tmp_l:

                summ = 0

                for a in l:

                    summ += int(a)

                if summ == self.score:

                    tmp_ls.append(l)

        rst = list()

        for x in tmp_ls:

            for a in x:

                rst.append(allergies_lst.get(str(a)))

        return rst

    def get_keyls(self, in_key, in_ls):

        if in_key - 128 <= max(in_ls):

            self.score = in_key

            return [x for x in in_ls if x <= in_key]

        else:

            n = 8

            stopFlg = True

            while stopFlg:

                if in_key >= 2 ** n:

                    n += 1

                else:

                    n = n - 1

                    stopFlg = False

            return self.get_keyls((in_key - 2 ** n), in_ls)
