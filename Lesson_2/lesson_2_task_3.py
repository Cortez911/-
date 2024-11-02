import math


def square(side):
    area = side * side
    return math.ceil(area)


side = 11.9  # Заменить на любое число для проверки
area = square(side)
print(f"Площадь квадрата со стороной {side}: {area}")
