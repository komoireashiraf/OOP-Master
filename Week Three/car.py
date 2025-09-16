class car:
    def __init__(self, name, year, brand):
        self.name = name
        self.year = year
        self.brand = brand


car1 = car("Corolla", 2020, "Toyota")
car2 = car("Civic", 2019, "Honda")
car3 = car("Mustang", 2022, "Ford")

print(car1.name)
print(car2.year)
print(car3.brand)
