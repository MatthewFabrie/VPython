from ex1 import sum_list

def four_perfect_numbers():
    current_nb = 1
    counter = 1
    counter_list = []
    perfect_numbers = []

    while len(perfect_numbers) < 4:
        while counter < current_nb:
            if (current_nb % counter == 0) :
                counter_list.append(counter)
            counter += 1
        if (sum_list(counter_list) == current_nb):
            perfect_numbers.append(current_nb)
        counter_list = []
        current_nb += 1
        counter = 1
    print(perfect_numbers)

four_perfect_numbers()