class Student:
    def __init__(self):
        print("my students")
    def student_type(self):
        print("fresher")
class Teacher:
    def __init__(self):
        print("My teacher")
    def student_type(self):
        print("the teacher teaches math")
# normal function
def school_details(mr):
    mr.student_type()
    mr.student_type()

student = Student()
teacher = Teacher()

school_details(student)
school_details(teacher)