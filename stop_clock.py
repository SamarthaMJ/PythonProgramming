import time
print("Enter 1 to start stop clock")
print("Enter 2 to start count down timer")
choice = int(input(""))
if choice == 1:
    for i in range(61):
        time.sleep(1)
        print(i)
elif choice == 2:
    num = int(input("Enter count down"))
    for i in range(num, 0, -1):
        time.sleep(1)
        print(i)
else:
    print("Invalid choice")