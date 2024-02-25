def triplets_square():
    triplets = []
    for c in range(1, 151):
        for a in range(1, c + 1):
            for b in range(a, c + 1):
                if a**2 + b**2 == c**2:
                    triplets.append((a, b, c))
    return triplets

def triplets_p3():
    triplets = []
    for c in range(1, 151):
        for a in range(1, c + 1):
            for b in range(a, c + 1):
                if a**3 + b**3 == c**3:
                    triplets.append((a, b, c))
    return triplets

def triplets_p4():
    triplets = []
    for c in range(1, 151):
        for a in range(1, c + 1):
            for b in range(a, c + 1):
                if a**4 + b**4 == c**4:
                    triplets.append((a, b, c))
    return triplets

def wtf(a, b, c):
    file = open('ex1.txt', 'w')
    for triplet in a:
        file.write(f"{triplet[0]} {triplet[1]} {triplet[2]}\n")
    for triplet in b:
        file.write(f"{triplet[0]} {triplet[1]} {triplet[2]}\n")
    for triplet in c:
        file.write(f"{triplet[0]} {triplet[1]} {triplet[2]}\n")


a = triplets_square()
b = triplets_p3()
c = triplets_p4()
wtf(a, b, c)
