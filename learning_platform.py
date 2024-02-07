class Student:
    """Represents a student on learning platform with such attributes as name, surnmame, gender, etc."""

    def __init__(self, name, surname, gender):
        """Initialize a Student instance with the given name, surname, and gender."""
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def student_rate(self, lecturer, course, grade):
        """Rate a student by a lecturer for a specific course with a given grade."""
        if (isinstance(lecturer, Lecturer)
                and course in lecturer.courses_attached
                and course in self.courses_in_progress
                and 0 <= grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calculate_average_grade(self):
        """Calculate the average grade for all courses the student is enrolled in."""
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
        """Return a string representation of the student, including name, surname, and average grade."""
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за домашние задания: {self.calculate_average_grade()} \n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        return self.calculate_average_grade() < other.calculate_average_grade()

    def __le__(self, other):
        return self.calculate_average_grade() <= other.calculate_average_grade()

    def __eq__(self, other):
        return self.calculate_average_grade() == other.calculate_average_grade()

    def __ne__(self, other):
        return self.calculate_average_grade() != other.calculate_average_grade()

    def __gt__(self, other):
        return self.calculate_average_grade() > other.calculate_average_grade()

    def __ge__(self, other):
        return self.calculate_average_grade() >= other.calculate_average_grade()


class Mentor:
    """Represents a mentor with attributes such as name and surname."""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Represents a lecturer, inheriting from Mentor, with additional attributes for courses and grades."""

    def __init__(self, name, surname):
        """Initialize a Lecturer instance with the given name and surname."""
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def calculate_average_grade(self):
        """Calculate the average grade for all courses the lecturer is attached to."""
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
        """Return a string representation of the lecturer, including name, surname, and average grade."""
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за лекции: {self.calculate_average_grade()}')

    def __lt__(self, other):
        return self.calculate_average_grade() < other.calculate_average_grade()

    def __le__(self, other):
        return self.calculate_average_grade() <= other.calculate_average_grade()

    def __eq__(self, other):
        return self.calculate_average_grade() == other.calculate_average_grade()

    def __ne__(self, other):
        return self.calculate_average_grade() != other.calculate_average_grade()

    def __gt__(self, other):
        return self.calculate_average_grade() > other.calculate_average_grade()

    def __ge__(self, other):
        return self.calculate_average_grade() >= other.calculate_average_grade()


class Reviewer(Mentor):
    """Represents a reviewer, inheriting from Mentor, with additional method for reviewing students."""

    def reviewer_rate(self, student, course, grade):
        """Rate a student for a specific course with a given grade."""
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
        """Return a string representation of the reviewer, including name and surname."""
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}')


def hw_avg_total_grade(students, course):
    """Calculate the average grade of homework for a specific course among a group of students."""
    total_grade = 0
    total_students = 0

    for student in students:
        if course in student.courses_in_progress and course in student.grades:
            total_grade += sum(student.grades[course])
            total_students += len(student.grades[course])

    if total_students > 0:
        average_grade = total_grade / total_students
    else:
        average_grade = 0

    return average_grade


def lecture_avg_total_grade(lecturers, course):
    """Calculate the average grade for a specific course among a group of lecturers."""
    total_grade = 0
    total_lecturers = 0

    for lecturer in lecturers:
        if course in lecturer.courses_attached and course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            total_lecturers += len(lecturer.grades[course])

    if total_lecturers > 0:
        average_grade = total_grade / total_lecturers
    else:
        average_grade = 0

    return average_grade


student_1 = Student('Евгений', 'Истомин', 'м')
student_1.courses_in_progress = ['Программирование на Python']
student_1.finished_courses = ['HTML']

student_2 = Student('Иван', 'Иванов', 'м')
student_2.courses_in_progress = ['Программирование на Python']


lecturer_1 = Lecturer('Алена', 'Горшкова')
lecturer_1.courses_attached = ['Программирование на Python']

lecturer_2 = Lecturer('Александр', 'Сапелкин')
lecturer_2.courses_attached = ['Программирование на Python']


reviewer_1 = Reviewer('Ярослав', 'Козлов')
reviewer_1.courses_attached = ['Программирование на Python']

reviewer_2 = Reviewer('Милана', 'Белоусова')
reviewer_2.courses_attached = ['Программирование на Python']


student_1.student_rate(lecturer_1, 'Программирование на Python', 10)
student_2.student_rate(lecturer_1, 'Программирование на Python', 9)
student_1.student_rate(lecturer_2, 'Программирование на Python', 6)
student_2.student_rate(lecturer_2, 'Программирование на Python', 7)

reviewer_1.reviewer_rate(student_1, 'Программирование на Python', 8)
reviewer_2.reviewer_rate(student_1, 'Программирование на Python', 7)
reviewer_1.reviewer_rate(student_2, 'Программирование на Python', 6)
reviewer_2.reviewer_rate(student_2, 'Программирование на Python', 10)


print(student_1, '\n')
print(lecturer_1, '\n')
print(reviewer_1, '\n')


print(student_1 > student_2)
print(lecturer_1 > lecturer_2, '\n')


print(f'Средняя оценка среди студентов: {hw_avg_total_grade([student_1, student_2], "Программирование на Python")}')
print(f'Средняя оцена за лекцию: {lecture_avg_total_grade([lecturer_1, lecturer_2], "Программирование на Python")}')
