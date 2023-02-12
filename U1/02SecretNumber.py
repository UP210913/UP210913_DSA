s = int(input("Enter the secret number: "))
c=0
n=0
while n != s:
    n = int(input("Enter a number: "))
    if n > s:
        print("You are up")
    elif n < s:
        print("You are down")
    c+=1

print("You got it right in", c, "attempt(s)")