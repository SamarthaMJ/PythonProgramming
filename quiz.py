import time

correct = 0              # initialize scoreboard to 0
print("Hello, welcome to quiz and true or false game.")
print("Totally there will be 2 rounds")
print("Total of 15 questions")
print("1st Round - Questions with clue")
print("2nd Round - True or False")
time.sleep(5)
name = input("What is your name?")
time.sleep(2)
print(name, "nice name")
time.sleep(2)
print("Lets begin!!")
print("1st Round:")

# first round
# question 1
time.sleep(2)
print("1.How many seconds are there in an hour?")
print("and 60 minutes in an hour")
ans1 = int(input(">>>"))
if ans1 == 3600:
    correct += 1
else:
    correct += 0           # adds one to scoreboard whenever correct answer is given

# 2
time.sleep(2)
print("2.How many days are there in leap year")
ans2 = int(input(">>>"))
if ans2 == 366:
    correct += 1
else:
    correct += 0

# 3
time.sleep(2)
print("3.Who is the president of America?")
ans3 = input(">>> ")
three = "Joe Biden,joe biden,Joe biden,joe Biden"       """ user may give input with or without caps , 
                                                        three variable is used to store all the possible inputs """
if ans3 in three:
    correct += 1
else:
    correct += 0

# 4
time.sleep(2)
print("4.Which is the largest ocean?")
ans4 = input(">>>")
four = "Pacific Ocean,pacific ocean,pacific,Pacific"
if ans4 in four:
    correct += 1
else:
    correct += 0

# 5
time.sleep(2)
print("5.What is the name of Bengaluru International Airport?")
ans5 = input("(type the name only) >>>")
five = "Kempegowda,kempegowda"
if ans5 in five:
    correct += 1
else:
    correct += 0

# 6
time.sleep(2)
print("6.Which is the capital of India.")
ans6 = input(">>>")
six = "New Delhi,new delhi ,newdelhi,New delhi"
if ans6 in six:
    correct += 1
else:
    correct += 0

# 7
time.sleep(2)
print("7.The capital of China is?")
ans7 = input(">>>")
seven = "Beijing,beijing"
if ans7 in seven:
    correct += 1
else:
    correct += 0

# 8
time.sleep(2)
print("8.Which city is known as the silicon city of India.")
ans8 = input(">>>")
eight = "Bengaluru,bengaluru,banglore,Banglore,bangalore"
if ans8 in eight:
    correct += 1
else:
    correct += 0

# 9
time.sleep(2)
print(" 9.Which is the biggest planet.")
ans9 = input("Your answer >>>")
nine = "Jupiter,jupiter"
if ans9 in nine:
    correct += 1
else:
    correct += 0

# 10
time.sleep(2)
print("10.What is the full form of CD")
ans10 = input(">>>")
ten = "Compact Disk,compact disk,Compact disk,compact disc,Compact disc,Compact Disc"
if ans10 in ten:
    correct += 1
else:
    correct += 0
time.sleep(3)

# True or False round based on boolean
print("Ok", name, "lets move on to 2nd round.")
true = ["True", "true", "t"]                        # user can give t,true or True as input
false = ["False", "false", "f"]                     # user can give f,false or False as input

# 11
time.sleep(2)
print("Type T/t or F/f for true or false")
print("11.Blue whale is a mammal.")
choice = input(">>>")
if choice in true:
    correct += 1
else:
    correct += 0

# 12
time.sleep(2)
print("12.New Delhi is an union territory")
choice = input(">>>")
if choice in true:
    correct += 1
else:
    correct += 0

# 13
time.sleep(2)
print("13.There are 22 spokes in Ashoka Chakra.")
choice = input(">>>")
if choice in false:
    correct += 1
else:
    correct += 0

# 14
time.sleep(2)
print("14.Bill gates is the founder of Microsoft.")
choice = input(">>>")
if choice in true:
    correct += 1
else:
    correct += 0

# 15
time.sleep(2)
print("15.Mango is the National fruit of India.")
choice = input(">>>")
if choice in true:
    correct += 1
else:
    correct += 0
time.sleep(2)

# display score that is stored in correct variable
if correct == 15:
    print("Wow Congrats", name, "You got", correct, "/15")
elif (correct <= 15 , correct >= 10):
    print("Not bad", name, "You got", correct, "/15")
else:
    print("Good luck next time,You got", correct, "/15")