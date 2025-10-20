import math
import random

MAIN_SYSTEM_LOOP = True
pythag_finder = False
area_finder = False
triangle_identify = False
area_quiz = False
quiz = False
end_quiz = False
exit_system = False
valid_input = False



#CLEAR THE TERMINAL
def clear_terminal():
    print("\n" * 150)
    

#LEAVE SOME SPACE BETWEEN THE MENUS
def minor_clear():
    print("\n" * 2)
    

#NUMBER VERIFY SYSTEM
def number_verify(num):
    if num < 0:
        print("You cannot enter negative numbers...")
        return False
    else:
        return num

#PYTHAGORUS SYSTEM
#FINDING THE HYPOTENUSE 
def hypotenuse_finder(a, b):
    if a <= 0 or b <= 0:
        print("Please enter positive numbers...")
    else:
        return math.sqrt(a**2 + b**2)

#FINDING THE SIDE LENGTH
def side_length_finder(a, c): #MAKE SURE YOU CALL C SECOND IN THE FUNCTION
    if a <= 0 or c <= 0:
       print("Please enter positive numbers...")
    elif a > c:
        print("Your side length cannot be greater than the hypotenuse...")
    else:
        return math.sqrt(c**2 - a**2)
    
def random_shape(): #PICKS A RANDOM NUMBER AND ASSIGNS IT TO A SHAPE STORED AS A STRING
    random_number = random.randint(1, 3)
    if random_number == 1:
        return "Square"
    elif random_number == 2:
        return "Triangle"
    else:
        return "Rectangle"

def random_num(): #RANDOM NUMBER USED AS THE LENGTHS OF SHAPES IN THE QUIZ
    randomNumber = random.randint(1,100)
    return randomNumber

#AREA SYSTEM
#SQUARE AREA CALCULATOR
def area_square(num):
    area = num * num
    return area 

#RECTANGLE AREA CALCULATOR
def area_rectangle(length,width):
    area = length * width
    return area

#TRIANGLE AREA CALCULATOR
def area_triangle(base, height):
    area = 0.5 * base * height
    return area

#CIRCLE AREA CALCULATOR
def area_circle(radius):
    area = math.pi * radius **2
    return area

#THE WHOLE SYSTEM IS COMPOSED IN HERE
while MAIN_SYSTEM_LOOP:
    clear_terminal()
    print("\n")
    print("Welcome to the main menu...")
    print("What would you like to do?")
    print("1. Pythagorus Calculator\n2. Area Calculator\n3. Identifying Triangles\n4. Area Quiz")
    print("\n")
    main_nav = input("Select 1 - 4:\n").strip()
    
    if main_nav == "1":
        pythag_finder = True
    elif main_nav == "2":
        area_finder = True
    elif main_nav == "3":
        triangle_identify = True
    elif main_nav == "4":
        area_quiz = True
    else:
        print("Enter a number from 1 - 4")

    #THIS IS THE PYTHAGORUS LOOP
    while pythag_finder:
        minor_clear()
        print("\nWelcome to the Pythagorean theorem calculator")
        print("Would you like to find the...")
        print("1. Hypotenuse")
        print("2. Side Length")
        print("3. Exit pythagorus finder")
        pythag_nav = input("Choose 1, 2 or 3: ").strip() #CLEAR ANY WHITESPACE TO BE SAFE
    

    #FINDING THE HYPOTENSE
        if pythag_nav == "1":
            print("Please enter the side lengths of your triangle.")
            try:
                a = int(input("Side length a: "))
                b = int(input("Side length b: "))
                if a <= 0 or b <= 0:
                    print("Please enter positive numbers.")
                else:
                    result = hypotenuse_finder(a, b)
                    clear_terminal()
                    rounded = round(result, 2)
                    print(f"Your hypotenuse is: {rounded}")
            except ValueError:
                print("Invalid input. Please enter whole numbers")

        #FINDING THE SIDE LENGTH
        elif pythag_nav == "2":
            print("Please enter your side length and hypotenuse")
            try:
                a = int(input("What is the side length of your triangle? "))
                c = int(input("What is the hypotenuse of your triangle? "))
                if a <= 0 or c <= 0:
                    print("Please enter positive numbers")
                elif a >= c:
                     print("Your side length cannot be greater than or equal to your hypotenuse.")
                else: 
                    result = side_length_finder(a,c)
                    clear_terminal()
                    rounded = round(result, 2)
                    print(f"The side length of your triangle is: {rounded}")
            except ValueError:
                print("Invalid input. Please enter whole numbers")
        elif pythag_nav == "3":
            pythag_finder = False
        else: #INCASE THE USER DOESNT PICK 1 OR 2
            print("Please pick 1, 2 or 3...")

     #MAIN AREA LOOP   
    while area_finder:
        while area_nav == "0":
            print("\nWelcome to the area finder...")
            print("Select what you want to calculate")
            print("1. Square\n2. Rectangle\n3. Triangle\n4. Cirlce\n5. Exit")
            area_nav = input(" ").strip()

        #FIND SQUARE
        if area_nav == "1":
            valid_input = False
            while valid_input == False:
                try:
                    num = int(input("What is the side length of your square? "))
                    valid_input = True
                except Exception:
                    print("Invalid input. Please enter whole numbers")
                    valid_input = False
            if num < 0:
                minor_clear()
                print("Your side length should'nt be a negative number")
                area_nav = "0"
            else:
                area = area_square(num)
                area = round(area,2)
                minor_clear()
                print(f"The area of your square is {area}")
                area_nav = "0"
                
        #FIND RECTANGLE
        elif area_nav == "2":
            valid_input = False
            while valid_input == False:
                try:
                    length = int(input("What is the first side length to your rectangle? "))
                    width = int(input("What is the second side length of your rectangle? "))
                    valid_input = True
                except Exception:
                    print("Invalid input. Please enter whole numbers")
                    valid_input = False
            if length < 0 or width < 0:
                minor_clear()
                print("Your side length cannot be a negative")
                area_nav = "0"
            else:
                area = area_rectangle(length,width)
                minor_clear()
                area = round(area,2)
                print(f"The area of your rectangle is {area}")
                area_nav = "0"
                
        #FIND TRIANGLE
        elif area_nav == "3":
            valid_input = False
            while valid_input == False:
                try:
                    base = int(input("What is the base of your triangle? "))
                    height = int(input("What is the height of your triangle? "))
                    valid_input = True
                except Exception:
                    print("Invalid input. Please enter whole numbers")
                    valid_input = False
            if base <= 0 or height <= 0:
                minor_clear()
                print("Your values must be greater than zero...")
                area_nav = "0"
            else:
                area = area_triangle(base,height)
                minor_clear()
                area = round(area,2)
                print(f"The area of your triangle is {area}")
                area_nav = "0"
                
        #FIND CIRLCE
        elif area_nav == "4":
            valid_input = False
            while valid_input == False:
                try:
                    radius = int(input("What is the radius of your circle? "))
                    valid_input = True
                except Exception:
                    print("Invalid input. Please enter whole numbers")
                    valid_input = False
            if radius < 0:
                minor_clear()
                print("Your radius cannot be less than zero")
                area_nav = "0"
            else:
                area = area_circle(radius)
                minor_clear()
                rounded = round(area, 2)
                print(f"The area of your circle is:{rounded}")
                area_nav = "0"
        #EXIT THE LOOP
        elif area_nav == "5":
            area_finder = False
            area_nav = "0"
        else: 
            minor_clear()
            print("Please enter a number from 1 to 5")
            area_nav = "0"

    #IDENTIFYING TRIANGLES MAIN LOOP
    while triangle_identify:
        print("\nWelcome to the triangle identifyer...")
        print("1. Continue")
        print("2. Exit")
        tri_nav = input(" ").strip()
        
        #CONTINUING ON WITH IDENTIFYING THE TRIANGLE
        if tri_nav == "1":
            valid_input = False
            while valid_input == False: #CHECK THE USER ENTERS A NUMBER NOT A STRING
                try:
                    a = int(input("What is your first side length? "))
                    b = int(input("What is your second side length? "))
                    c = int(input("What is your third side length? "))
                    valid_input = True
                except ValueError:
                    print("Invalid input. Please enter whole numbers")
                    valid_input = False
            if a <= 0 or b <= 0 or c <= 0:
                print("Your sides cannot be negative or zero")
            else:
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
            

        #EXIT THE LOOP
        elif tri_nav == "2":
            triangle_identify = False
            minor_clear()

    #AREA QUIZ SECTION
    while area_quiz:
        print("Welcome to the area quiz")
        print("1. Begin")
        print("2. Exit")
        nav_quiz = input(" ").strip()

        if nav_quiz == "2": #CANCEL THE QUIZ
            area_quiz = False

        elif nav_quiz == "1": #CONTINUE FORWARD
            quiz = True
            score = 0
            attempts = 0
            end_quiz = False

            while quiz: #GENERATE THE RANDOM SHAPE AND SIDES VALUES
                minor_clear()
                shape = random_shape()
                num1 = random_num()
                num2 = random_num()

                if shape == "Square":
                    print(f"What is the area of a Square with the side length of {num1}?")
                    compAnswer = num1**2 #THE COMPUTER SOLVES THE QUESTION USING THE FORMULA
                    #print(compAnswer) DEBUGGING TO SEE THE REAL ANSWER

                    valid_input = False
                    while not valid_input: #CHECK THE USER USED A NUMBER
                        try:
                            userAnswer = int(input("What is the answer? "))
                            valid_input = True
                        except ValueError:
                            print("Invalid input. Please whole numbers.")
                            valid_input = False

                    if compAnswer == userAnswer: #COMPARE THE ACTUAL ANSWER TO THE USERS ANSWER
                        score += 1 #SCORE ONLY GOES UP WHEN YOU GET IT RIGHT
                        attempts += 1
                        minor_clear()
                        print("Well done that is correct")
                    else:
                        minor_clear()
                        print(f"Nice try that was incorrect, the correct answer was {compAnswer}")
                        attempts += 1

                    print("Do you want to continue?")
                    print("1. Yes\n2. No")

                    valid_cont = False #CHECKING IF THE USER WANTS TO CONTINUE WITH THE TEST
                    while not valid_cont: #CHECKING THE USER PICKED 1 OR 2
                        cont = input(" ").strip()
                        if cont == "1" or cont == "2": 
                            valid_cont = True
                        else:
                            print("Please enter 1 or 2.")

                    if cont == "2": #ENDING THE QUIZ
                        quiz = False
                        end_quiz = True

                elif shape == "Rectangle": #HANDLING THE CASE IF ITS A RECTANGLE
                    minor_clear()
                    print(f"What is the area of a Rectangle with the side lengths of {num1} and {num2}?")
                    compAnswer = num1 * num2 #COMPUTER ANSWER / REAL ANSWER
                    #print(compAnswer) #DEBUGGING LINE TO GET THE ANSWER

                    valid_input = False
                    while not valid_input: #CHECKS THE USER USED AN ACTUAL IMPUT
                        try:
                            userAnswer = int(input("What is the answer? "))
                            valid_input = True
                        except ValueError:
                            print("Invalid input. Please enter whole numbers.")
                            valid_input = False

                    if compAnswer == userAnswer: #COMPARES THE ANSWER TO THE USER ANSWER
                        score += 1
                        attempts += 1
                        minor_clear()
                        print("Well done that is correct")
                    else:
                        minor_clear()
                        print(f"Nice try that was incorrect, the correct answer was {compAnswer}")
                        attempts += 1

                    print("Do you want to continue?")
                    print("1. Yes\n2. No")

                    valid_cont = False
                    while not valid_cont:
                        cont = input(" ").strip()
                        if cont == "1" or cont == "2":
                            valid_cont = True
                        else:
                            print("Please enter 1 or 2.")

                    if cont == "2":
                        quiz = False
                        end_quiz = True

                elif shape == "Triangle": #HANDLES IF THE SHAPE IS A TRIANGLE
                    minor_clear()
                    print(f"What is the area of a Triangle with the height of {num1} and the base of {num2} to two decimal places?")
                    compAnswer = 0.5 * num2 * num1 #THE COMPUTER FINDS THE REAL ANSWER
                    compAnswer = round(compAnswer, 2)
                    #print(compAnswer) #DEBUGGING TO CHECK IF THE ANSWER IS RIGHT

                    valid_input = False
                    while not valid_input: #CHECK IF THE USER PUT A VALID NUMBER
                        try:
                            userAnswer = float(input("What is the answer? "))
                            valid_input = True
                        except ValueError:
                            print("Invalid input. Please enter whole numbers.")
                            valid_input = False

                    if compAnswer == userAnswer:
                        score += 1
                        attempts += 1
                        minor_clear()
                        print("Well done that is correct")
                    else:
                        minor_clear()
                        print(f"Nice try that was incorrect, the correct answer was {compAnswer}")
                        attempts += 1

                    print("Do you want to continue?")
                    print("1. Yes\n2. No")

                    valid_cont = False
                    while not valid_cont:
                        cont = input(" ").strip()
                        if cont == "1" or cont == "2":
                            valid_cont = True
                        else:
                            print("Please enter 1 or 2.")

                    if cont == "2":
                        quiz = False
                        end_quiz = True

                else:
                    minor_clear()
                    print("Please enter 1 or 2.")

            if end_quiz:
                clear_terminal()
                score = float(score)
                attempts = float(attempts)
                if attempts > 0:
                    percentage = (score / attempts) * 100 #DISPLAYS THE USERS SCORE
                    print(f"Well done you got {score} out of {attempts} or {percentage:.2f}%")
                else:
                    print("No attempts made.")
    if exit_system == True:
        MAIN_SYSTEM_LOOP = False
print("Youve left the loop")
