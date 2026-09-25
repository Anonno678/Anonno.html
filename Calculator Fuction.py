def add(a,b):

sum=a+b

return sum

def multi(a,b):

prod=a*b

return prod

print("1. add")

print("2. multiply")

ch = int(input("enter choice"))
a1=int(input("enter 1st no"))
b1=int(input("enter 2nd no"))
if ch==1:
print(add(a1,b1))
elif ch==2:
print(multi(a1,b1))
else:
print("wrong choice")