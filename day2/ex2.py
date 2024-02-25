import random
import math

def circleSquare():
    file = open('ex2.txt', 'w')
    additional_terms = [1000, 10000, 100000, 1000000]
    inside_circle = 0

    for i in range(1, 101):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x ** 2 + y ** 2

        if distance <= 1:
            inside_circle += 1
        pi_estimate = 4 * inside_circle / i
        file.write(f"{i}) {pi_estimate}, {pi_estimate / math.pi}\n")

    for a in additional_terms:
        inside_circle = 0
        for useless in range(a):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            distance = x ** 2 + y ** 2

            if distance <= 1:
                inside_circle += 1

        pi_estimate = 4 * inside_circle / a
        file.write(f"{a}) {pi_estimate}, {pi_estimate / math.pi}\n")

circleSquare()
