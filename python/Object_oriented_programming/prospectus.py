class Prospectus:
  def __init__(self):
    self.lecturers = []
    self.courses = []
  
  def add_lecturer(self, *lecturers):
    for lecturer in lecturers:
        self.lecturers.append(lecturer)
  
  def remove_lecturer(self, lecturer):
    self.lecturers.remove(lecturer)
  
  def find_lecturer(self, name):
    for lecturer in self.lecturers:
      if lecturer.name == name:
        return lecturer
    return None
  
  def add_course(self, *courses):
    for course in courses:
        self.courses.append(course)
  
  def remove_course(self, course):
    self.courses.remove(course)
  
  def find_course(self, name):
    for course in self.courses:
      if course.name == name:
        return course
    return None

class Lecturer:
  def __init__(self, name, office, email):
    self.name = name
    self.office = office
    self.email = email
  
  def __str__(self):
    return f"{self.name}, Office: {self.office}, Email: {self.email}"

class Course:
  def __init__(self, name, units, leader):
    self.name = name
    self.units = units
    self.leader = leader
  
  def __str__(self):
    return f"{self.name}, Units: {self.units}, Leader: {self.leader.name}"

# Create a Prospectus object
prospectus = Prospectus()

# Add some lecturers to the prospectus
lecturer1 = Lecturer("John Smith", "123", "john.smith@college.edu")
lecturer2 = Lecturer("Jane Doe", "456", "jane.doe@college.edu")
lecturer3 = Lecturer("Bob Johnson", "789", "bob.johnson@college.edu")

prospectus.add_lecturer(lecturer1,lecturer2, lecturer3)

# Add some courses to the prospectus
course1 = Course("Computer Science", ["CS101", "CS102", "CS103"], lecturer1)
course2 = Course("English Literature", ["EL101", "EL102", "EL103"], lecturer2)
course3 = Course("Mathematics", ["MATH101", "MATH102", "MATH103"], lecturer3)

prospectus.add_course(course1, course2, course3)

print(prospectus.find_course("Computer Science"))
