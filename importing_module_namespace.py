
import math

def sin(x):                 # function sin defined in user namespace
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14                   # Varible pi defined in userspace!

print(sin(pi/2))            
print(math.sin(math.pi/2)   # Functions math/sin and variable pi are imported from math 
