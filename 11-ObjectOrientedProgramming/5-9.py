class C():
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = int(age)
        self.seniority = int(seniority)

    def __str__(self):
        if self.age >= 18:
            return f"{self.surname}{self.name[0]}{self.seniority}".upper()
        else:
            return f"{self.surname}{self.name[0]}{self.seniority}".lower()
        
def main():
    object1 = C("Anna", "May", "17", "7")
    object2 = C("George", "Brown", "21", "4")
    print(object1)
    print(object2)

if __name__ == "__main__":
    main()