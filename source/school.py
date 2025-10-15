class TooManyStudents(Exception):
    pass

class Classroom:
    def __init__(self, teacher, student, course_title):
        self.teacher = teacher
        self.student = student
        self.course_title = course_title
        
    def add_student(self, student):
        if len(self.student)<= 10:
            self.student.append(student)
        else:
            raise TooManyStudents
        
    def remove_student(self, name):
        for student in self.student:
            if student.name == name:
                self.student.remove(student)
                break
                
            
            
    def change_teacher(self, new_teacher):
        self.teacher = new_teacher
        
    class Person:
        def __init__(self, name):
            self.name = name
            
    class Teacher(Person):
        pass
    
    class Student(Person):
        pass
        
        
        
        