print("Enter 1 to calculate average of 10 squared numbers ")
print("Enter 2 to calculate average of 10 cube numbers")
print("Enter which operation u need: ")
choice = int(input(""))
if choice == 1:
    total_sum = 0
    for n in range(10):
        numbers = float(input('Enter number : '))
        # iterates and adds squares of given numbers
        total_sum = total_sum + (numbers * numbers)
    avg = total_sum/10
    print('Average of 10 numbers is :',avg)
elif choice == 2:
    total_sum = 0
    for n in range(10):
        numbers = float(input('Enter number : '))
        # iterates and adds cubes of given numbers
        total_sum = total_sum + (numbers * numbers * numbers)
    avg = total_sum/10
    print('Average of 10 numbers is s:',avg)
else:
    print("Invalid Choice")