from random import randrange

p = int(input("Enter the size for the matrix: "))
M = [[0 for j in range(p)] for i in range(p)]
F = 0
C = 0
while F < p:
    Rep = False
    num = randrange(1, ((p**2) + 1))
    for F1 in range(p):
        for C1 in range(p):
            if (M[F1][C1] == num):
                Rep = True
    if Rep == False:
        M[F][C] = num
        C += 1
        if C == p:
            C = 0
            F += 1
print("All numbers are different")
print(M)