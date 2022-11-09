""" This is a chatbot that can used as a basic receptionist in health care centres or hospitals """

import time
print("Hello, I'm a chatbot for health services.")
time.sleep(2)
print("Press 1 for you're suffering from any disease")
time.sleep(2)
print("Press 2 for vaccines")
time.sleep(2)
print("Press 3 for ambulance services")

# main choice 1
userinput = int(input("Enter your choice"))
if userinput == 1:
    print("Press 1 for common cold or fever")
    print("Press 2 for infectious diseases")
    time.sleep(2)
    userinput = int(input("Enter your choice"))
    if userinput == 1:
        print("Please take paracetamol if it isn't allergic to you")
    else:
        print("Please visit your nearest hospital")

# main choice 2
elif userinput == 2:
    print("Press F for 1st dose")
    print("Press S for 2nd dose")
    time.sleep(2)
    userinput = input("Enter your choice")
    if userinput == "F":
        print("Please come to the nearest vaccine centre with your aadhar")
    elif userinput == "S":
        print("Please come to the vaccine centre with records of the previous dose")
    else:
        print("Invalid choice")

# main choice 3
elif userinput == 3:
    print("Press 1 if you live in the centre of the City")
    print("Press 2 if you live on the outskirts of City")
    time.sleep(2)
    userinput = int(input("Enter your choice"))
    if userinput == 1:
        print("The ambulance will arrive shortly")
    else:
        print("The ambulance might take a little time to arrive")
else:
    print("Invalid choice")
print("Thank you for using the chatbot, do take care of your health")