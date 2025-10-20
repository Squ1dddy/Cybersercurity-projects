import math
#THIS IS THE HARNESS AND TESTING PROCESS FOR IDENTIFYING THE UNKNOWN SIDE LENGTH

#FINDING THE SIDE LENGTH
def side_length_finder(a, c): #MAKE SURE YOU CALL C SECOND IN THE FUNCTION
    if a <= 0 or c <= 0:
       print("Please enter positive numbers...")
    elif a > c:
        print("Your side length cannot be greater than the hypotenuse...")
    else:
        return math.sqrt(c**2 - a**2)
    

#TESTING HARNESS
print("\n")
print("Testing...")
print("Testing the math correctly produces the right answer... Expected 17.32")
result = side_length_finder(10,20)
print(f"recived {result}")
print("\n")
print("Testing the borders of positive intergers... Expected please enter positive numbers")
side_length_finder(0,0)
print("\n")

print("Testing when only one interger is equal to zero... Expected please enter positive numbers")
side_length_finder(0,1)
print("\n")

print("Testing if the side length is larger than the hypotenuse... Expected your side length cannot be larger than your hypotense")
side_length_finder(10,2)
print("\n")

print("Testing when the hypotenuse is barely larger than the side length... Expected 4.58")
result = side_length_finder(10,11)
print(f"Recivied {result}")
print("\n")

print("Testing negative number inputs... Expected please enter positive numbers")
side_length_finder(-10,-11)
print("\n")

print("Testing very large inputs... Expected 22586545.0")
result = side_length_finder(20202020,30303030)
print(f"Recived {result}")





