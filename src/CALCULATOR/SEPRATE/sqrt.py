import math

def sqrt2(a):



    if a < 0 :
        a = a * -1
        c = math.sqrt(a)
    else:
        c = math.sqrt(a)



    return c

class sqrt:
    res2 = 0
    def sqrt(self, a):
        self.res2 = sqrt2(a)
        return self.res2