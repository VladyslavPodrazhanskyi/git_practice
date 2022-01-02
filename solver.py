import math


class Solver:
    def quadratic_equ_solution(self, a, b, c):
        d = b ** 2 - 4 * a * c
        if d > 0:
            disc = math.sqrt(d)
            x1 = (-b - disc) / (2 * a)
            x2 = (-b + disc) / (2 * a)
            return x1, x2
        elif d == 0:
            return -b / (2 * a)
        else:
            return "There is no equation root"


if __name__ == '__main__':
    solver = Solver()
    while True:
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        result = solver.quadratic_equ_solution(a, b, c)
        print(result)