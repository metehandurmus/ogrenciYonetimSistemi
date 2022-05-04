from manager.StudentManager import StudentManager


class Main:
    def __init__(self, file_name):
        self.file_name = file_name

    def run(self):

        student_manager = StudentManager()
        print("Hoşgeldiniz, yapmak istediğiniz işlemi seçin")
        while True:
            print("1) Öğrenci oluştur")
            print("2) Öğrenci sil")
            print("3) Öğrencileri göster")
            print("4) Öğrenci düzenle")
            print("5) Çıkış Yap")
            choise = input('-> ')

            if choise == '1':
                school_no = input("Okul no: ")
                name = input("Öğrenci adı: ")
                last_name = input("Soyadı: ")
                student_manager.add(self.file_name, school_no, name, last_name)
                print()

            if choise == '2':
                student_manager.show(self.file_name)
                student_id = input("ID: ")
                student_manager.delete(self.file_name, student_id)

            if choise == '3':
                student_manager.show(self.file_name)

            if choise == '4':
                student_manager.show(self.file_name)
                student_id = input("ID: ")
                school_no = input("Okul no: ")
                name = input("Öğrenci adı: ")
                last_name = input("Soyadı: ")
                student_manager.edit(self.file_name, student_id, school_no, name, last_name)

            if choise == '5':
                break
