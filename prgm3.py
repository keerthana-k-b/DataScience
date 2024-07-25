import math

a = int(input("Enter the co-efficient of x2 : "))
b = int(input("Enter the co-efficient of x : "))
c = int(input("Enter the constant value : "))

discriminant = (b * b) - 4 * a * c

if discriminant > 0:
    print("Two distinct roots exists.")
    n1 = ((-1 * b) + math.sqrt(discriminant)) / (2 * a)
    n2 = ((-1 * b) - math.sqrt(discriminant)) / (2 * a)
    prt = f"Root 1 = {n1:.2f}"
    print(prt)
    prt = f"Root 2 = {n2:.2f}"
    print(prt)
elif discriminant == 0:
    print("Only one root exists.")
    n1 = (-1 * b) / (2 * a)
    prt = f"Root = {n1:.2f}"
    print(prt)
else:
    print("Two imaginary roots exists.")
    real = (-1 * b) / (2 * a)
    img = (math.sqrt(-discriminant) / (2 * a))
    prt = f"Root 1 = {real:.2f} + {img:.2f}i"
    print(prt)
    prt = f"Root 1 = {real:.2f} - {img:.2f}i"
    print(prt)