class Person:
    my_school = "Ahmed"
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def show(self,new_age):
        self.age = new_age
        print(self.age,self.name,sep=" and ")

    @classmethod
    def school(cls,mynew_school):
        cls.my_school = mynew_school

#creating an object
myobject = Person("Ahmed",23)
myobject.show(21)

