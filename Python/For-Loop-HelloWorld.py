n = int(input('Please enter a number: '))
for _ in range(1, n+1):
    if(n%4 == 0):
        if(n%6 == 0):
            print("Hello World!")
        else:
            print("Hello")
    elif(n%6 == 0):
        if(n%4 == 0):
            print("Hello World!")
        else:
            print("World")
    else:
        print("Invalid. Please try again.")
