"""OOP problems: operator overloading.

Special methods used:
    +   __add__      -   __sub__      *   __mul__
    <   __lt__       >   __gt__       ==  __eq__
    !=  __ne__       >=  __ge__       <=  __le__
Each method receives self (left operand) and other (right operand).
Returning NotImplemented tells Python "I do not know this type".
"""

import math


# ------------------------------------------------------------ Problem 1
class Complex:
    """Complex number with + and - overloaded."""

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        return Complex(self.real - other.real, self.imag - other.imag)

    def __eq__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        return self.real == other.real and self.imag == other.imag

    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"


# ------------------------------------------------------------ Problem 2
class Person:
    """p1 > p2 is True if p1 is older than p2."""

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __gt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age > other.age

    def __str__(self):
        return f"{self.name} ({self.age}, {self.gender})"


# ------------------------------------------------------------ Problem 4
class Vector:
    """3D vector. vector1 * vector2 returns the dot product (a number)."""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


# ------------------------------------------------------------ Problem 5
class Circle:
    """All six comparison operators, based on the radius."""

    def __init__(self, radius):
        self.radius = radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __ne__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius != other.radius

    def __ge__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius >= other.radius

    def __le__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius <= other.radius

    # Defining __eq__ removes the default __hash__, so we add one back.
    def __hash__(self):
        return hash(self.radius)

    def __str__(self):
        return f"Circle(radius={self.radius})"


# ------------------------------------------------------------ Problem 6
class Point2D:
    """Points are compared by their Euclidean distance from the origin."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        if not isinstance(other, Point2D):
            return NotImplemented
        return self.distance() < other.distance()

    def __gt__(self, other):
        if not isinstance(other, Point2D):
            return NotImplemented
        return self.distance() > other.distance()

    def __eq__(self, other):
        if not isinstance(other, Point2D):
            return NotImplemented
        # isclose avoids float rounding problems
        return math.isclose(self.distance(), other.distance())

    def __ne__(self, other):
        if not isinstance(other, Point2D):
            return NotImplemented
        return not math.isclose(self.distance(), other.distance())

    def __ge__(self, other):
        if not isinstance(other, Point2D):
            return NotImplemented
        return self > other or self == other

    def __le__(self, other):
        if not isinstance(other, Point2D):
            return NotImplemented
        return self < other or self == other

    def __hash__(self):
        return hash(round(self.distance(), 9))

    def __str__(self):
        return f"Point2D({self.x}, {self.y})"


# ------------------------------------------------------------ Problem 7
class Matrix:
    """Matrix stored as a list of rows. * is the matrix product."""

    def __init__(self, rows):
        self.rows = rows

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        n_rows = len(self.rows)
        n_inner = len(self.rows[0])
        n_cols = len(other.rows[0])
        # A (n x m) times B (m x p) needs: columns of A == rows of B
        if n_inner != len(other.rows):
            raise ValueError("Dimensions do not match for multiplication")
        result = []
        for i in range(n_rows):
            row = []
            for j in range(n_cols):
                total = 0
                for k in range(n_inner):
                    total += self.rows[i][k] * other.rows[k][j]
                row.append(total)
            result.append(row)
        return Matrix(result)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        return self.rows == other.rows

    def __str__(self):
        return "\n".join(" ".join(str(v) for v in row) for row in self.rows)


# ------------------------------------------------------------ tests
if __name__ == "__main__":
    # Problem 1
    a, b = Complex(3, 2), Complex(1, -4)
    print("P1:", a, "+", b, "=", a + b)
    print("P1:", a, "-", b, "=", a - b)

    # Problem 2
    p1, p2 = Person("Aya", 22, "F"), Person("Tom", 30, "M")
    print("P2:", p1 > p2, p2 > p1)

    # Problem 4
    v1, v2 = Vector(1, 2, 3), Vector(4, 5, 6)
    print("P4: dot product =", v1 * v2)   # 1*4 + 2*5 + 3*6 = 32

    # Problem 5
    c1, c2, c3 = Circle(2), Circle(5), Circle(2)
    print("P5:", c1 < c2, c1 > c2, c1 == c3, c1 != c2, c1 >= c3, c2 <= c1)

    # Problem 6
    pa, pb, pc = Point2D(3, 4), Point2D(0, 6), Point2D(4, 3)
    print("P6:", pa < pb, pa > pb, pa == pc, pa != pb, pa >= pc, pb <= pa)

    # Problem 7
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    print("P7:\n" + str(m1 * m2))          # [[19, 22], [43, 50]]
    m3 = Matrix([[1, 2, 3]])               # 1x3
    m4 = Matrix([[1], [2], [3]])           # 3x1
    print("P7 (1x3 * 3x1):\n" + str(m3 * m4))
