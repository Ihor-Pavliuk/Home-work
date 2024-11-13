#Fraction

#Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною 
# перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій та операції порівняння між 
# об'єктами класу Fraction
import math
 

class Fraction:
    def __init__(self, a, b):
        if a ==0 or b == 0:
            raise ZeroDivisionError("Numbers can`t be zero")
        gcd = math.gcd(a, b)
        self.a = a // gcd
        self.b = b // gcd
        #print(self.a, self.b)
    
    def __add__(self, other):
        new_a = (self.a * other.b) + (other.a * self.b)
        new_b = self.b * other.b
        return Fraction(new_a, new_b)
    def __sub__(self, other):
        new_a = (self.a * other.b) - (other.a * self.b)
        new_b = self.b * other.b
        return Fraction(new_a, new_b)
    def __mul__(self, other):
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)
    def __truediv__(self, other):
        new_a = self.a * other.b
        new_b = self.b * other.a
        return Fraction(new_a, new_b)
    def __eq__(self, other):
        return self.a * other.b == other.a * self.b
    def __str__(self):
        return f"{self.a}/{self.b}"
    
if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)
assert x + y == Fraction(3, 4)
result_sub = x - y
print(result_sub) 

result_mul = x * y
print(result_mul)  

result_div = x / y
print(result_div)