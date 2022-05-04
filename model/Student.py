class Student:
    def __init__(self, student_id, school_no, name, last_name):
        self.student_id = student_id
        self.school_no = school_no
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return '{}|{}|{}|{}\n'.format(self.student_id, self.school_no, self.name, self.last_name)
