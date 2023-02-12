m = int(input("Enter the amount of money: "))
c=0
t=1
while m > t:
    m-=t
    c+=1
    t+=1

print("You can buy", c, "ticket(s)")
print("You stayed with $",m)