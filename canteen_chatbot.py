import time
print("Hello, I am chatbot at PESITM canteen")
time.sleep(2)
print("Press 1 for menu")
print("Press 2 for cleaning")
print("Press 3 for warm or cold water")
print("Press 4 for bill")
time.sleep(2)
userinput = int(input("Enter your choice"))
if userinput == 1:
    print("Dosa,Idli,Vada,Pulao,Tea,Coffee,Juice")
elif userinput == 2:
    print("Table cleaner will arrive soon")
elif userinput == 3:
    print("What do you prefer, hot ot cold water")
elif userinput == 4:
    print("The bill will be sent thorough SMS ")
else:
    print("Your request could not processed, you can apply again ")
print("Thank you,visit again")