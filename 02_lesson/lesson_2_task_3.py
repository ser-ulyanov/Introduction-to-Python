import math

def square(side):
    area = side * side
    if not isinstance(side, int):
        area = math.ceil(area)
    return area

# Примеры использования
print(square(5))    # 25
print(square(7))  # 49
print(square(9))  # 81