import numpy as np
import sys

def karatsuba(x,y):
    if len(x) != 1 and len(y) != 1:
        l = (len(x)+len(y))//4
        a = x[:-l]
        b = x[-l:]
        c = y[:-l]
        d = y[-l:]
        add1 = str(int(a)+int(b))
        add2 = str(int(c)+int(d))
        term1 = karatsuba(a,c)
        term2 = karatsuba(b,d)
        term3 = karatsuba(add1,add2) - term1 - term2
        return 10**(2*l)*term1 + term2 + 10**(l)*term3
    else:
        return int(x)*int(y)


x,y = sys.argv[1:3]


print(karatsuba(x,y))