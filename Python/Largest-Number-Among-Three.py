a = float(input("Enter Your First Number: "))
b = float(input("Enter Your Second Number: "))
c = float(input("Enter Your Third Number: "))

if (a>b) and (a>c):
	largest = a
elif (b>a) and (b>c):
	largest = b
else: 
	largest = c

print("The largest number is:", largest)
