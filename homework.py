class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_ww(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rat(self):
        total = 0
        length = 0
        if len(self.grades) != 0:
            for val in self.grades.values():
                for i in val:
                    total += i
                    length += 1
            return round(total / length, 2)
        else:
            return 0

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.average_rat()}\n' \
               f'Курсы в процессе обчуения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        res = self.average_rat() < other.average_rating()
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        total = 0
        length = 0
        if len(self.grades) != 0:
            for val in self.grades.values():
                for i in val:
                    total += i
                    length += 1
            return round(total / length, 2)
        else:
            return 0

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.average_rating()}'

    def __lt__(self, other):
        res = self.average_rating() < other.average_rat()
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_student = Student('Ruy', 'Eman', 'Man')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
print(some_reviewer)
print()
some_student.rate_ww(some_lecturer, 'Python', 10)
some_student.rate_ww(some_lecturer, 'Python', 7)
some_student.rate_ww(some_lecturer, 'Python', 9)
print(some_lecturer)
print()
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
print(some_student)
print()
print(some_lecturer < some_student)
print(some_student < some_lecturer)

student_1 = Student('Jon', 'Brown', 'Man')
student_2 = Student('Rob', 'Williams', 'Man')
students_list = [student_1, student_2]
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Din', 'Jons')
lecturer_2 = Lecturer('Maikel', 'Tyson')
lecturers_list = [lecturer_1, lecturer_2]
lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2.courses_attached += ['Python', 'Git']

some_student.rate_ww(lecturer_1, 'Python', 10)
some_student.rate_ww(lecturer_1, 'Python', 7)
some_student.rate_ww(lecturer_1, 'Python', 9)

some_student.rate_ww(lecturer_2, 'Python', 10)
some_student.rate_ww(lecturer_2, 'Python', 7)
some_student.rate_ww(lecturer_2, 'Python', 9)

some_reviewer.rate_hw(student_1, 'Python', 6)
some_reviewer.rate_hw(student_1, 'Python', 10)
some_reviewer.rate_hw(student_1, 'Python', 9)

some_reviewer.rate_hw(student_2, 'Python', 10)
some_reviewer.rate_hw(student_2, 'Python', 10)
some_reviewer.rate_hw(student_2, 'Python', 9)


def grades_everage_of_students_courses(students, name_course):
    length = 0
    total = 0
    for student in students_list:
        if name_course in student.grades:
            length += len(student.grades[name_course])
            total += sum(student.grades[name_course])

    return round((total / length), 2)


print(grades_everage_of_students_courses(students_list, 'Python'))


def grades_everage_of_lectures_courses(lecturers, course_name):
    counter = 0
    sum_grade = 0
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            counter += len(lecturer.grades[course_name])
            sum_grade += sum(lecturer.grades[course_name])

    return round((sum_grade / counter), 2)


print(grades_everage_of_lectures_courses(lecturers_list, 'Python'))