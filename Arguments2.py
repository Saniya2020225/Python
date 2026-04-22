# SUM
def add(*numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total


print(add(1, 2, 3, 4, 5))

# MULTIPLY

def mul(*numbers):
    pro = 1
    for i in numbers:
        pro = pro * i
    return pro

print(mul(1,2,3,4,5))