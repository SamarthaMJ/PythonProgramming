"""This is a basic calculator which can perform addition,subtraction,multiplication,division,square,cube and also
square root"""

import math
a = float(input("Enter first number"))                    # take 1st number input
choice = input("Enter operator (+,-,*,/,**,***,sqrt)")        # take character  input
if choice == '**':
    result = a*a
elif choice == "sqrt":
    result = math.sqrt(a)
elif choice == '***':
    result = a*a*a
elif choice == '+':
    b = float(input("Enter second number"))               # take 2nd number input only when +,-,*,/ operation is used
    result = a+b
elif choice == '-':
    b = float(input("Enter second number"))
    result = a-b
elif choice == '*':
    b = float(input("Enter second number"))
    result = a*b
elif choice == '/':
    b = float(input("Enter second number"))
    result = a/b
else:                                                     # exit when invalid character input is given
    print("Invalid operator")
    exit(0)
print(result)