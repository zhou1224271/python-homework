def get_name(c):
    if c == "R":
        return "Radishes"
    elif c == "G":
        return "Grass"
    elif c == "C":
        return "Clover"
    elif c == "V":
        return "Violets"
    else:
        raise ValueError("bad value")


def chunks(l):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), 2):
        yield l[i:i + 2]


class Garden(object):
    def __init__(self, diagram, students=['Alice',
                                          'Bob',
                                          'Charlie',
                                          'David',
                                          'Eve',
                                          'Fred',
                                          'Ginny',
                                          'Harriet',
                                          'Ileana',
                                          'Joseph',
                                          'Kincaid',
                                          'Larry']):

        diagram = zip(*map(chunks, diagram.splitlines()))
        diagram = ("".join(t) for t in diagram)  # flatten
        self.students = sorted(students)
        self.diagram = dict(zip(self.students, diagram))

    def plants(self, student):
        return [get_name(x) for x in self.diagram[student]]


if __name__ == "__main__":
    garden = Garden("VCRRGVRG\nRVGCCGCV",
                    students="Samantha Patricia Xander Roger".split())
    print(garden.plants("Patricia"))
    print(garden.plants("Xander"))
