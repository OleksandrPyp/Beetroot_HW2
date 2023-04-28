#Task 3 Fraction
from math import lcm
from dataclasses import dataclass
@dataclass
class Fraction:
    nominator: int
    denominator: int
    #condition = isinstance(other, Fraction)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("Input is not valid")
        new_denom = lcm(self.denominator, other.denominator)
        left_nom = int(new_denom*self.nominator/self.denominator)
        right_nom = int(new_denom*other.nominator/other.denominator)
        return Fraction(nominator=left_nom+right_nom, denominator=new_denom)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("Input is not valid")
        new_denom = lcm(self.denominator, other.denominator)
        left_nom = int(new_denom*self.nominator/self.denominator)
        right_nom = int(new_denom*other.nominator/other.denominator)
        return Fraction(nominator=left_nom-right_nom, denominator=new_denom)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("Input is not valid")
        new_denom = int(self.denominator * other.denominator)
        new_nom = int(self.nominator * other.nominator)
        return Fraction(nominator=new_nom, denominator=new_denom)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("Input is not valid")
        new_nom = int(self.nominator * other.denominator)
        new_denom = int(self.denominator * other.nominator)
        return Fraction(nominator=new_nom, denominator=new_denom)

    def __lt__(self, other):
        new_denom = lcm(self.denominator, other.denominator)
        left_nom = int(new_denom * self.nominator / self.denominator)
        right_nom = int(new_denom * other.nominator / other.denominator)
        return left_nom < right_nom

    def __eq__(self, other):
        new_denom = lcm(self.denominator, other.denominator)
        left_nom = int(new_denom * self.nominator / self.denominator)
        right_nom = int(new_denom * other.nominator / other.denominator)
        return left_nom == right_nom

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return not self.__lt__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __str__(self) -> str:
        return f"{self.nominator}/{self.denominator}"


print(Fraction(1,8) + Fraction(3,7))
print(Fraction(1,8) - Fraction(3,7))
print(Fraction(1,8) * Fraction(3,7))
print(Fraction(1,8) / Fraction(3,7))
print(Fraction(1,8) <= Fraction(3,7))