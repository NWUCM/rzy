def f(t,u):
    return 4*t*u**0.5
h=0.1
t0=0
u0=1
step=10
def explicit_euler(f,h,t0,u0,step=10):
    us=[u0]
    for i in range (step):
        us.append(u0+h*f(t0,u0))
        t0=t0+h
    return us
us=explicit_euler(f,h,t0,u0,step)
print(us)