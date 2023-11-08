

class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd2(a, b)
        self.a /= x
        self.b /= x


    def gcd2(self, a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a
    
    def __str__(self):
        return '%d/%d' % (self.a, self.b)
    
    def zgs(self, a, b):
        x = self.gcd2(a, b)
        return (a * b / x)

    def __add__(self, other):
        a = self.a
        b = self.b
        c= other.a
        d = other.b
        fenmu = self.zgs(b, d)
        fenzi = a * (fenmu / b) + c * (fenmu / d)
        return Fraction(fenzi, fenmu)

# f = Fraction(30, 15)
# print(f)
a = Fraction(1,6)
b = Fraction(1,4)
print(a+b)