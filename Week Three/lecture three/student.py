class Student:
    def __init__(self, Name):
        self.name = Name  # public
        self._gpa = 4.5  # protected attribute (denoted by a single underscore)
        self.__password = "12345"  # private attribute (denoted by a double underscore)


Student_One = Student("Komoire Ashiraf")

# Change name to Muyima Ezrah
Student_One.name = "Muyima Ezrah"
# Change GPA to 5.0
Student_One._gpa = "5.0"
# Change password to 2025
Student_One.__password = "2015"

print(Student_One.name)
print(Student_One._gpa)
