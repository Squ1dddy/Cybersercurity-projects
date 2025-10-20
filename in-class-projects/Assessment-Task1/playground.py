import csv

def clear_terminal():
    print("\n")

def identify_triangle(a,b,c):
    values = [a, b, c]
    values.sort() #SORT IN ASCENDING ORDER
    #print(values) Debug to double check they are in order
    if a + b <= c: 
        clear_terminal()
        print("This is an impossible triangle.")
    elif a == b and a == c:
        clear_terminal()
        print("This is an equilateral trianle.")
    elif a == b or a == c or b == c:
        clear_terminal()
        print("This is an isosceles triangle.")
    else:
        clear_terminal()
        print("This trianle is a scalene triangle.")
    if (c**2) == (a**2 + b**2):
        clear_terminal()
        print("This is a right angle triangle.")


