from collections import defaultdict


class School(object):
    def __init__(self, name):
        self.name = name
        self._grades = defaultdict(list)

    def add(self, name, nth):
        self._grades[nth].append(name)

    def grade(self, nth):
        return sorted(self._grades[nth])

    def sort(self):
        return [(k, tuple(sorted(self._grades[k]))) for k in sorted(self._grades.keys())]
