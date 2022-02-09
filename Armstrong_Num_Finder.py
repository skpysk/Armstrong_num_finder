
x = int(input("Enter Your Number For Finding :  "))   
sum = 0
x2 = x
order = len(str(x))
while (x>0):
    digit = x%10
    sum += digit**order
    x = x//10
if ( sum == x2  ):
    print(f"{x2} is an Armstrong Number")
else:
    print(f"{x2} is not an Armstrong Number")