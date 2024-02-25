def even_odd_prime():
    number = input()
    x = 2
    nb_dividands = 0

    if (int(number) % 2 == 0):
        print("even")
    else:
        print("odd")
    while x < int(number):
        if (int(number) % x == 0):
            nb_dividands += 1
        x += 1
    if (nb_dividands == 0):
        print("prime")

even_odd_prime()