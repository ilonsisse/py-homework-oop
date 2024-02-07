class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def student_rate(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and self.courses_in_progress in lecturer.courses_attached
                and course in self.courses_in_progress
                and 0 <= grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calculate_average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            for grade in grades_list:
                all_grades.append(grade)

        if all_grades:
            average_grade = sum(all_grades) / len(all_grades)
        else:
            average_grade = 0

        return average_grade

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за домашние задания:{self.calculate_average_grade()} \n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        return sum(self.grades) / len(self.grades) < sum(other.grades) / len(other.grades)

    def __le__(self, other):
        return sum(self.grades) / len(self.grades) <= sum(other.grades) / len(other.grades)

    def __eq__(self, other):
        return sum(self.grades) / len(self.grades) == sum(other.grades) / len(other.grades)

    def __ne__(self, other):
        return sum(self.grades) / len(self.grades) != sum(other.grades) / len(other.grades)

    def __gt__(self, other):
        return sum(self.grades) / len(self.grades) > sum(other.grades) / len(other.grades)

    def __ge__(self, other):
        return sum(self.grades) / len(self.grades) >= sum(other.grades) / len(other.grades)


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def calculate_average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            for grade in grades_list:
                all_grades.append(grade)

        if all_grades:
            average_grade = sum(all_grades) / len(all_grades)
        else:
            average_grade = 0

        return average_grade

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за лекции: {self.calculate_average_grade()}')

    def __lt__(self, other):
        return sum(self.grades) / len(self.grades) < sum(other.grades) / len(other.grades)

    def __le__(self, other):
        return sum(self.grades) / len(self.grades) <= sum(other.grades) / len(other.grades)

    def __eq__(self, other):
        return sum(self.grades) / len(self.grades) == sum(other.grades) / len(other.grades)

    def __ne__(self, other):
        return sum(self.grades) / len(self.grades) != sum(other.grades) / len(other.grades)

    def __gt__(self, other):
        return sum(self.grades) / len(self.grades) > sum(other.grades) / len(other.grades)

    def __ge__(self, other):
        return sum(self.grades) / len(self.grades) >= sum(other.grades) / len(other.grades)


class Reviewer(Mentor):

    def reviewer_rate(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}')


student_1 = Student('Евгений', 'Истомин', 'м')
student_1.courses_in_progress = ['Программирование на Python']
student_1.finished_courses = ['HTML']

student_2 = Student('Иван', 'Иванов', 'м')


lecturer_1 = Lecturer('Алена', 'Горшкова')
lecturer_1.courses_attached = ['Программирование на Python']

lecturer_2 = Lecturer('Александр', 'Сапелкин')


reviewer_1 = Reviewer('Ярослав', 'Козлов')
reviewer_1.courses_attached = ['Программирование на Python']

reviewer_2 = Reviewer('Милана', 'Белоусова')


student_1.student_rate(lecturer_1, 'Программирование на Python', 10)
student_2.student_rate(lecturer_1, 'Программирование на Python', 9)

reviewer_1.reviewer_rate(student_1, 'Программирование на Python', 8)
reviewer_2.reviewer_rate(student_1, 'Программирование на Python', 7)

print(student_1)
print(lecturer_1)
print(reviewer_1)
