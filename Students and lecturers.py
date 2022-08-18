import math


class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name 
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_process = []
        self.grades = {}
        self.grades_list = []
        
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)    
 
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_process and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        for item in self.grades:
            for i in self.grades[item]:
                self.grades_list.append(i)
        if len(self.grades_list) == 0:        
            print(f"У студента {self.name} еще нет оценок")
            return
        else:
            self.average_grade = sum(self.grades_list) / len(self.grades_list)
            courses = ""
            for item in self.courses_in_process:
                courses += item + " "
            return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {format(self.average_grade, '.2f')} \nКурсы в процессе изучения: {courses} \nЗавершенные курсы: Введение в программирование"

      
class Mentor:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
             
class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.list = []
        self.average_grade = True
        
    def __str__(self):
        for item in self.grades:
            for i in self.grades[item]:
                self.list.append(i)
        self.average_grade = sum(self.list) / len(self.list)    
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {format(self.average_grade, '.2f')}"
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f"{other} не является лектором!")
            return 
        return self.average_grade < other.average_grade
                
        
class Reviewer(Mentor):
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_process:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
        
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"


def students_grade_count(course, students_list):
    grades_list = []
    for item in students_list:
        if course in item.grades:
            for i in item.grades[course]:
                grades_list.append(i)
    average_grade = sum(grades_list) / len(grades_list)    
    item_names = [] 
    empty_string = " "
    for item in students_list:
        item_names.append(item.name)
    for item in item_names:
        empty_string += item + " "
    return f"Средняя оценка по курсу {course} для студентов:{empty_string}составляет: {format(average_grade, '.2f')}"


def lecturer_grade_count(course, lecturer_list):
    grades_list = []
    for item in lecturer_list:
        if course in item.grades:
            for i in item.grades[course]:
                grades_list.append(i)
    average_grade = sum(grades_list) / len(grades_list)    
    item_names = [] 
    empty_string = " "
    for item in lecturer_list:
        item_names.append(item.name)
    for item in item_names:
        empty_string += item + " "
    return f"Средняя оценка по курсу {course} для преподавателей:{empty_string}составляет: {format(average_grade, '.2f')}"    
          
          
vova = Reviewer("Владимир", "Левченко")     
vova.courses_attached.append("Ruby")
vova.courses_attached.append("Git")

alyona = Reviewer("Алёна", "Батицкая")
alyona.courses_attached.append("Ruby")
alyona.courses_attached.append("Git")


petya = Lecturer("Пётр", "Столыпин")     
petya.courses_attached.append("Python")
petya.courses_attached.append("C#")   
petya.courses_attached.append("Ruby")    
petya.courses_attached.append("Git")   

kolya = Lecturer("Николай", "Гоголь")   
kolya.courses_attached.append("Python")
kolya.courses_attached.append("C#")   
kolya.courses_attached.append("Ruby")    
kolya.courses_attached.append("Git")         

vasya = Student("Васлий", "Тёркин", "мужской")
vasya.courses_in_process.append("Python")
vasya.courses_in_process.append("C#")
vasya.courses_in_process.append("Ruby")
vasya.courses_in_process.append("Git")

dima = Student("Дмиртий", "Донской", "мужской")
dima.courses_in_process.append("Python")
dima.courses_in_process.append("C#")
dima.courses_in_process.append("Ruby")
dima.courses_in_process.append("Git")



vasya.rate_lecturer(petya, "Python", 10)
vasya.rate_lecturer(petya, "Python", 7)
vasya.rate_lecturer(petya, "Python", 9)
vasya.rate_lecturer(petya, "C#", 7)
vasya.rate_lecturer(petya, "C#", 6)
vasya.rate_lecturer(petya, "C#", 9)

vasya.rate_lecturer(kolya, "Python", 8)
vasya.rate_lecturer(kolya, "Python", 3)
vasya.rate_lecturer(kolya, "Python", 2)
vasya.rate_lecturer(kolya, "C#", 10)
vasya.rate_lecturer(kolya, "C#", 6)
vasya.rate_lecturer(kolya, "C#", 9)


vova.rate_hw(vasya, "Ruby", 9)
vova.rate_hw(vasya, "Ruby", 5)
vova.rate_hw(vasya, "Ruby", 10)
vova.rate_hw(vasya, "Git", 4)
vova.rate_hw(vasya, "Git", 7)
vova.rate_hw(vasya, "Git", 5)

alyona.rate_hw(dima, "Ruby", 3)
alyona.rate_hw(dima, "Ruby", 10)
alyona.rate_hw(dima, "Ruby", 7)
alyona.rate_hw(dima, "Git", 8)
alyona.rate_hw(dima, "Git", 8)
alyona.rate_hw(dima, "Git", 9)


print(vasya)
print(petya)
print(alyona)
print(kolya)
print(dima)
print(vova)
print(petya < kolya)
print(kolya < petya)

vasya.add_courses("GitHub")
print(vasya.finished_courses)

print(vasya.grades)
print(dima.grades)

print(students_grade_count("Ruby", [vasya, dima]))
print(students_grade_count("Git", [vasya, dima]))

print(petya.grades)
print(kolya.grades)

print(lecturer_grade_count("Python", [petya, kolya]))
print(lecturer_grade_count("C#", [petya, kolya]))