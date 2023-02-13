import math as ma

x1 = 1
x2 = 2
xm = None
es = 0.001
er = abs(x2-x1) 
i = 1
it = round((ma.log(x2 - x1) - ma.log(es)) / ma.log(2))
print(it)

print("i         |    x1     |    x2     |    er    |    xm    |    f(x1)    |    f(xm)     |    f(x1) * f(xm)   |")

def pot(num):
    return pow(num,2)-2

while (er >= es): 
        xm = (x1 + x2) / 2
        print(i,round(x1,4), round(x2,4), round(er,4), round(xm,4), round(pot(x1),4), round(pot(xm),4), round((pot(x1)*pot(xm)),4), sep= "\t|")
        if(pot(x1)* pot(xm) < 0):
            x2 = xm
        else:
            x1 = xm                                                  
        er = abs(x2 - x1)
        i += 1

print("The result is: ", xm)