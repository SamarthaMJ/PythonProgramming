n = int(input("Enter first term"))
m = int(input("Enter last term"))
choice = int(input("Even(1) or odd(2)"))
if choice == 1:
    if n%2 != 0:
        n = n+1
    if m%2 != 0:
        m = m-1
    for i in range(n,m+1,2):
        print(i)
elif choice == 2:
    if n%2 == 0:
        n = n-1
    if m%2 == 0:
        m = m+1
    for i in range(n,m,2):
        print(i)