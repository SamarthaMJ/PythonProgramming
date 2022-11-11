""" This is a scientific calculator that can calculate
    trignometric values,exponential power of two numbers,logarithm,factorial,GCD of two numbers
    unit conversions like degree-radian,distance,temperature and speed conversions,"""

import math
print("Python scientific calculator")
print("Select your choice")                       # There are three main choices
print("Press 1 for trignometric calculations")
print("Press 2 for conversions")
print("Press 3 for other calculations")
userInput = int(input("Enter your choice"))

# main choice 1
if userInput == 1:
    print("Trigonometric Functions \n")
    val = float(input("Enter the value in degrees : "))
    print(" Enter your choice \n 1. Sine value \n 2. Cosine value \n 3. tangential value \n 4. Secent value \n 5. Cosecent value \n 6. Cotangential Value \n ")
    radval = (val*3.142)/180
    choice = int(input("Enter the number of your choice: "))    # There are 6 sub choices in 1st main choice
    if choice == 1:
        print("Sine value: ",math.sin(radval))
    elif choice == 2:
        print("Cos value: ",math.cos(radval))
    elif choice == 3:
        print("Tan value: ",math.tan(radval))
    elif choice == 4:
        sec = 1/ math.cos(radval)
        print("Sec value: ",sec)
    elif choice == 5:
        cosec = 1/math.sin(radval)
        print("Cosec value: ",cosec)
    elif choice == 6:
        cot = 1/math.tan(radval)
        print("Cot value: ",cot)
    else:
        print("Invalid Choice.")

# main choice 2
# distance
elif userInput == 2:
    print("Press 1 for distance conversion")
    print("Press 2 for temperature conversion")
    print("Press 3 for degree-radian conversion")
    choice = int(input("Enter the choice"))               # There are 3 sub choices in 2nd main choice
    if choice == 1:
        print("Press 1 to convert cm to m")
        print("Press 2 to convert m to cm")
        choice2 = int(input("enter your choice"))         # Nested if inside another nested if
        if choice2 == 1:
            cm = float(input("Enter centimeters"))
            meter = cm/100
            print(cm, "Centimeters is equal to",meter, "meters")
        elif choice2 == 2:
            meter = float(input("Enter meters"))
            cm = meter * 100
            print(meter, "Meters is equal to",cm, "centimeters")
        else:
            print("Invalid operator")

# temperature
    elif choice == 2:
        print("Press 1 to convert celsius to fahrenheit")
        print("Press 2 to convert fahrenheit to celsius")
        choice3 = int(input("Enter choice"))
        if choice3 == 1:
            celsius = int(input("Enter celsius"))
            fahrenheit = (celsius * (9/5))+32
            print(celsius,"C is equal to", fahrenheit ,"F")
        elif choice3==2:
            fahrenheit=int(input("Enter fahrenheit"))
            celsius= (fahrenheit-32)*(5/9)
            print(fahrenheit,"F is equal to",celsius,"C")
        else:
            print("Invalid operator")

# degree-radian
    elif choice == 3:
        print("Press 1 to convert radians to degrees")
        print("Press 2 to convert degrees to radians")
        choice4 = int(input("Enter choice"))
        if choice4 == 1:
            number = float(input('enter the number in radians'))
            degree = number * 180 / 3.14
            print('the number in degree is ', degree)
        elif choice4 == 2:
            number = float(input('Enter a number in degree: '))
            radians = number * math.pi / 180
            print('the number in radian is:', radians)
        else:
            print("Invalid operator")
    else:
        print("Invalid selection of choice")

# 3
# other calculations
elif userInput == 3:
    print("Press P/p to find exponential power of two numbers")
    print("Press F/f to find factorial of a number")
    print("Press L/l to find the logarithm of a number")
    print("Press G/g to find GCD of two numbers")
    in_choice = input("Enter your choice")
    if in_choice == 'F' or 'f':
        print("Enter base and power")
        x=int(input(""))
        y=int(input(""))
        print(pow(x,y))
    elif in_choice == 'L' or 'l':
        a=int(input("Enter the number"))
        m=int(input("Enter the base"))
        print("Log of",a,"=",math.log(a,m))
    elif in_choice == 'F' or 'f':
        n=int(input("Enter the number"))
        print("Factorial of ",n,"=",math.factorial(n))
    elif in_choice == 'G' or 'g':
        a=int(input("Enter one number"))
        b=int(input("Enter another number"))
        print("GCD of",a,",",b,"=",math.gcd(a,b))
    else:
        print("Invalid operator")

else:
    print("Invalid operator")

