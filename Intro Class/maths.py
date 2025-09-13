def area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius


r = float(input("Enter the radius of the circle: "))
area = area_of_circle(r)

print("The area of the circle is:", area)
