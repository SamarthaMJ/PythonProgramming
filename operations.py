import math

print("Select 1 to find factorial of a number")
print("Select 2 to find average of numbers")
print("Select 3 to find sum of numbers")
print("Select 4 to find the even numbers given in the range")
print("Select 5 to find the odd numbers given in the range")
userInput = int(input("Enter your choice"))

# 1 Factorial of a number
if userInput == 1:
    f = int(input("Enter the number to find factorial"))
    print("Factorial of ", f, "=", math.factorial(f))

# 2 Average of number
elif userInput == 2:
    n = int(input("Enter number"))
    sum = 0
# loop
    for num in range(1, n + 1, 1):
        sum = sum + num
        average = sum / n
    print("Average of ", n, "numbers is: ", average)

# 3 Sum of a number
elif userInput == 3:
    num = int(input("Enter number"))
    sum = 0
# loop from 1 to n
    for num in range(1, num + 1, 1):
        sum = sum + num
    print("Sum of first ",num, "numbers is: ", sum)

elif userInput == 4:
    n = int(input("Enter first term"))
    m = int(input("Enter last term"))
    if n % 2 != 0:
        n = n + 1
    if m % 2 != 0:
        m = m - 1
    for i in range(n, m + 1, 2):
        print(i)
elif userInput == 5:
    n = int(input("Enter first term"))
    m = int(input("Enter last term"))
    if n % 2 == 0:
        n = n - 1
    if m % 2 == 0:
        m = m + 1
    for i in range(n, m, 2):
        print(i)

else:
    print("Invalid choice")