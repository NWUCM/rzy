import math 
h=0.1
yn=1.0
tn=2.0
def f(t,y):
    return (t**3*y) 
for i in range(10):
    yn1=yn+h*f(tn,yn)
    tn=tn+h
    print(yn1)
