import math

def quadratic(a, b, c):
    x1=(-b+math.sqrt(pow(b,2)-4*a*c))/2*a
    x2=(-b-math.sqrt(pow(b,2)-4*a*c))/2*a
    return x1,x2
print('qudratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('fail')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('fail')
else:
    print('success')
