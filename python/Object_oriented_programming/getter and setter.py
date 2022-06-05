class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("missing name value")
        self.name = name
        self.__house = house
    def __str__(self):
        return f"{self.name} from {self.__house}"
    @property
    def get_house(self):
        return self.__house
    @get_house.setter
    def set_house(self, house):
        if house not in ["Ahmed","Abde","bare","yare"]:
            raise ValueError("invaled house")
        self__house = house
        
def get_student():
    name = input("Your name: ")
    house = input("provide your house: ")
    return Student(name,house)

def main():
    student = get_student()
    print(student) 

if __name__ == "__main__":
    main()
