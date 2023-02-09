def computepay(h,r):
    return p

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h <= 40:
    p = (h*r)
elif h>40:
    p = (40*r + (h-40)*1.5*r)

print("Pay",p)
