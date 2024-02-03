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

    def __str__(self):
        return (f'Имя: {self.name} '
                f'Фамилия: {self.surname} '
                f'Средняя оценка за домашние задания: {sum(self.grades) / len(self.grades)} '
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} '
                f'Завершенные курсы: {", ".join(self.finished_courses)} ')

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

    def __str__(self):
        return (f'Имя: {self.name} '
                f'Фамилия: {self.surname}'
                f'Средняя оценка за лекции: {sum(self.grades) / len(self.grades)}')

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
        return (f'Имя: {self.name}'
                f'Фамилия: {self.surname}')








