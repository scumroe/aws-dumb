import math

def get_sides(a=0, b=0, c=0, o=1):
    if o == 1:
        c = round(math.sqrt(a**2+b**2), 2)
        print("The hypotenuse (side c )is:\nThe square root of: %s^2 + %s^2 = %s" % (a , b, c))
    elif o == 2:
        a = round(math.sqrt(c**2-b**2), 2)
        print("Side a is:\n The square root of %s^2 - %s^2 = %s" % (c, b, a))
        print(a)
    elif o == 3:
        b = round(math.sqrt(c**2-a**2), 2)
        print("Side b is:\n The square root of %s^2 - %s^2 = %s" % (c, a, b))
    else:
        print("No can do.")
    return

def Menu():

    menu = ['Pythagoras','1. Find side c','2. Find side a',
            '3. Find side b']
    for menu in menu:
        print(menu)
    option = int(input("Choose an option:"))

    if option == 1:
        side_a = int(input("Enter side a: "))
        side_b = int(input("Enter side b: "))
        get_sides(side_a, side_b, 1)
    elif option == 2:
        side_b = int(input("Enter side b: "))
        side_c = int(input("Enter side c: "))
        get_sides(0, side_b, side_c, 2)
    elif option == 3:
        side_a = int(input("Enter side a: "))
        side_c = int(input("Enter side c: "))
        get_sides(side_a, side_c, 3)
    else:
        print("Bad choice.")
    return

def main():
    try:
        Menu()
    except ValueError:
        print("Bad value.")

if __name__ == "__main__":
    main()
