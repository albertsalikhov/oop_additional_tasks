"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число
- Оценки - список из целых чисел, может быть пустым

Опишите класс Student и метод avg_rate так, чтобы считалась средняя оценка, а при пустом списке оценок возвращался 0

"""


class Student:

    def __init__(self, name, course, assessments=None):
        self.name = name
        self.course = course
        self.assessments = assessments

    def avg_rate(self):
        if not self.assessments:
            return 0
        avg = sum(self.assessments) / len(self.assessments)
        return avg


# код для проверки
student = Student('Ivan', 'Python', [5, 4, 5, 5])
print(student.avg_rate()) # 4.75

student = Student('Ivan', 'Python', [])
print(student.avg_rate()) # 0.0
