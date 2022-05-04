from model.Student import Student


class StudentManager:

    def __init__(self):
        pass

    @staticmethod
    def show(file_name):
        with open(file_name, 'a', encoding='utf-8') as file:
            pass
        with open(file_name, 'r', encoding='utf-8') as file:
            students = file.readlines()
            print()
            for student in students:
                information_list = student.split('|')
                print('{}\t{}\t{}\t{}'.format(information_list[0], information_list[1], information_list[2],
                                              information_list[3]), end='')
        print()

    @staticmethod
    def add(file_name, school_no, name, last_name):
        with open(file_name, 'r+', encoding='utf-8') as file:
            students = file.readlines()
            if len(students) > 0:
                end_student = students[len(students) - 1].split('|')
                student_id = int(end_student[0]) + 1
            else:
                student_id = 1
            student = Student(student_id, school_no, name, last_name)
            file.seek(0)
            content = file.read()
            file.seek(0)
            content = content + str(student)
            file.write(content)
        print("Başarıyla oluşturuldu.")
        print()

    @staticmethod
    def delete(file_name, student_id):
        with open(file_name, 'r+', encoding='utf-8') as file:
            students = file.readlines()
            for student in students:
                if student[0] == student_id:
                    students.remove(student)
                    print()
                    print("Başarı ile silindi.")
                    print()
                    break

            with open(file_name, 'w', encoding='utf-8') as file2:
                file2.writelines(students)

    @staticmethod
    def edit(file_name, student_id, school_no, name, last_name):
        with open(file_name, 'r+', encoding='utf-8') as file:
            students = file.readlines()
            counter = 0
            for student in students:
                if student[0] == student_id:
                    students.remove(student)
                    student = Student(student_id, school_no, name, last_name)
                    students.insert(counter, str(student))
                    print()
                    print("Başarı ile düzenlendi.")
                    print()
                    break
                counter = counter + 1

            with open(file_name, 'w', encoding='utf-8') as file2:
                file2.writelines(students)