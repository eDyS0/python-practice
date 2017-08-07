import operator


class School(object):
    """
    Given students' names along with the grade that they are in,
    create a roster for the school.

    add: add a student name to the roster for a grade
        -> doesn't work with tuples
    grade: returns a list of all the students enrolled for a grade
    sort: returns a sorted list of all students in all grades
        -> not fully implemented, it doesn't sort alphabetically atm.

    I don't think using a dictionary is the best way to handle that exercise.
    """

    def __init__(self, school_name):
        self.roster = {}
        self.school_name = school_name

    def add(self, name, grade):
        self.roster.setdefault(grade, [])
        self.roster[grade] += [name]

    def grade(self, school_grade):
        if self.roster:
            return self.roster[school_grade]
        else:
            return []

    def sort(self):
        sort = sorted(self.roster.items(), key=operator.itemgetter(0))
        return (sort)
