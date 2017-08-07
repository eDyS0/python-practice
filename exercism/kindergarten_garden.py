PLANTS = {'V': 'Violets', 'G': 'Grass', 'C': 'Clover', 'R': 'Radishes'}
STUDENTS = [
        'Alice',
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
        'Larry',
    ]


class Garden(object):
    def __init__(self, rows, students=STUDENTS):
        self.students = sorted(students)
        self.rows1, self.rows2 = rows.split('\n')

    def plants(self, student):
        pos = self.students.index(student) * 2
        return [PLANTS[self.rows1[pos]],
                PLANTS[self.rows1[pos + 1]],
                PLANTS[self.rows2[pos]],
                PLANTS[self.rows2[pos + 1]]]
