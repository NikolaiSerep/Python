class Student():
    def __init__(self, name, surname, grades):
        self.name = name 
        self.surname = surname 
        self.grades = grades
    def statistics(self):
        maximum = 0
        summa = 0
        for grade in self.grades:
            if grade > maximum:
                maximum = grade
            summa += grade 
        print('Максимальный балл', maximum ) 
        print('Сумма баллов', summa)
        print('Средний балл',  round(summa/len(self.grades),) )
student = Student(input('Name:'), input ('Surname: '), list (map(int, input ('Grades ').split())))
student.statistics()