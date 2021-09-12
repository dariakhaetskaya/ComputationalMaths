from __future__ import division
import math

epsilon = pow(10, -12)
right = 0
left = 1


def f(x, a, b, c):
    return x ** 3 + a * x ** 2 + b * x + c


def sign(x):
    return (1, -1)[x < 0]


def bisectional_root_search(a, b, c1, c2, c3):
    if sign(f(a, c1, c2, c3)) == sign(f(b, c1, c2, c3)):
        raise Exception("a and b do not bound a root")

    m = (a + b) / 2

    if abs(f(m, c1, c2, c3)) <= epsilon:
        return m
    elif abs(a - b) < epsilon:
        return a
    elif sign(f(m, c1, c2, c3)) != sign(f(b, c1, c2, c3)):
        return bisectional_root_search(m, b, c1, c2, c3)
    elif sign(f(m, c1, c2, c3)) != sign(f(a, c1, c2, c3)):
        return bisectional_root_search(a, m, c1, c2, c3)


def discriminant_derivative(a, b):
    return 4 * a ** 2 - 12 * b


def find_interval(left_bound, right_bound, direction, a, b, c):
    if direction == right:
        step = 1
    else:
        step = -1

    while sign(f(left_bound, a, b, c)) == sign(f(right_bound, a, b, c)):
        left_bound += step
        right_bound += step
    if f(left_bound, a, b, c) == 0:
        return left_bound
    elif f(right_bound, a, b, c) == 0:
        return right_bound
    else:
        return bisectional_root_search(left_bound, right_bound, a, b, c)


def solve_equation(a, b, c):
    if discriminant_derivative(a, b) <= 0:
        if f(0, a, b, c) < -epsilon:
            print("equation has one root: x = ", find_interval(0, 1, right, a, b, c))
        elif f(0, a, b, c) > epsilon:
            print("equation has one root: x = ", find_interval(-1, 0, left, a, b, c))
        else:
            print("equation has one root: x = 0")
    else:
        x_1 = (-2 * a - math.sqrt(discriminant_derivative(a, b))) / 6
        x_2 = (-2 * a + math.sqrt(discriminant_derivative(a, b))) / 6

        if f(x_1, a, b, c) < -epsilon:
            print("equation has one root: x_1 = ", find_interval(x_2, x_2 + 1, right, a, b, c))

        elif f(x_2, a, b, c) > epsilon and not f(x_2, a, b, c):
            print("equation has one root: x_1 = ", find_interval(x_1 - 1, x_1, left, a, b, c))

        elif f(x_1, a, b, c) > epsilon and f(x_2, a, b, c):
            print("equation has one root: x_1 = ", find_interval(x_1 - 1, x_1, left, a, b, c))
            print("x_2 = ", find_interval(x_2, x_2 + 1, right, a, b, c))
            print("x_3 = ", bisectional_root_search(x_1, x_2, a, b, c))

        elif abs(f(x_1, a, b, c)) < epsilon and f(x_2, a, b, c) < -epsilon:
            print("equation has two roots: x_1 = ", x_1)
            print("x_2 = ", find_interval(x_2, x_2 + 1, right, a, b, c))

        elif abs(f(x_2, a, b, c)) < epsilon < f(x_1, a, b, c):
            print("equation has two roots: x_1 = ", x_2)
            print("x_2 = ", find_interval(x_1 - 1, x_1, left, a, b, c))

        elif abs(f(x_1, a, b, c)) < epsilon and abs(f(x_2, a, b, c)) < epsilon:
            print("equation has three roots x_1 = x_2 = x_3 = ", x_1)
        exit()


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
solve_equation(a, b, c)
