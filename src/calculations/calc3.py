from math import pi


def get_pi(precision=5):
    return round(pi, precision)


def calculate_func_area(radius):
    return get_pi() * radius * radius
