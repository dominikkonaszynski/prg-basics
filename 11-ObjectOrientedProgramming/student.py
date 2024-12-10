# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.index_number = 0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.index_number = 236678
    student2.name = "Olivia"
    student2.age = 21
    student2.index_number = 245456
    student3.name = "John"
    student3.age = 20
    student3.index_number = 345293

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, Index number: {student1.index_number}')
    print(f'{student2.name}, {student2.age} years old, Index Number: {student2.index_number}')
    print(f'{student3.name}, {student3.age} years old, Index Number: {student3.index_number}')

if __name__ == "__main__":
    main()