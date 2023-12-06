import math
a=int(input())
x=int(input())
y=math.log(math.fabs(x**7),math.e)+math.atan(x**2)+math.pi/(math.sqrt((math.fabs(a+x))))
print(y)