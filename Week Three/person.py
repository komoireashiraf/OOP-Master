class Person:
    def _init_(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


class Student(Person):
    def _init_(self, name, program, year):
        super()._init_(name)
        self.program = program
        self.year = year

    def introduce(self):
        super().introduce() + f" I am studying {self.program} in year {self.year}."


class Lecturer(Person):
    def _init_(self, name, program, department):
        super()._init_(name)
        self.program = program
        self.department = department

    def introduce(self):
        (
            super().introduce()
            + f" I teach {self.program} in the {self.department} department."
        )


p = Person("Ashiraf")
s = Student("Ezrah", "Computer Science", 2)
l = Lecturer("Destiny", "Computer Science")

p.introduce()
s.introduce()
l.introduce()
