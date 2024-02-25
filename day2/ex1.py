import math

def generateFile():
    f = open('ex1.txt', 'w')
    pi_approximation = 0
    additional_terms = [1000, 10000, 100000, 1000000, 10000000]

    for i in range(1, 101):
        brackets = 0
        for j in range(i):
            if j % 2 == 0:
                brackets += 1 / (2 * j + 1)
            else:
                brackets -= 1 / (2 * j + 1)
        
        pi_approximation = 4 * brackets
        f.write(f"{i}) {pi_approximation}, {pi_approximation / math.pi}\n")

    for x in additional_terms:
        brackets = 0
        for j in range(x):
            if j % 2 == 0:
                brackets += 1 / (2 * j + 1)
            else:
                brackets -= 1 / (2 * j + 1)
        
        pi_approximation = 4 * brackets
        f.write(f"{x}) {pi_approximation}, {pi_approximation / math.pi}\n")
    f.close()

generateFile()
