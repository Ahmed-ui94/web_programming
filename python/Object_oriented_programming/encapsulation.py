class Student:
    def __init__(self,name,roll_no,age):
        self.name = name
        self.__roll_no = roll_no
        self.__age = age
    
    def show(self):
        print("student details: ",self.name,self.__roll_no)
    def get_roll_no(self):
        return self.__roll_no
    def set_roll_no(self, number):
        if number>50:
            print("invalid roll number please set correct roll number")
        else:
            self.__roll_no = number


student1 = Student("Ahmed",23,22)
#calling the object
student1.show()

student1.set_roll_no(22)
print("age:",student1.get_roll_no())



