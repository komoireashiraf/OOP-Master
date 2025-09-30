class Student:
    def _init_(self, Name):
        self.name = Name  # public
        self._gpa = 3.5  # protected (has one underscore "_")
        self.__password = "12345"  # private (has two underscore "__")
