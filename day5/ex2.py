import numpy as np
import sys

#[n=2[[2][2][2][2][2][2][2][2]]]

#arr[0] = arr[0][:, np.newaxis]
#if (arr[0] == arr[0])

# a = np.array([1,2,3,4])
# b = np.array([10,20,30])
# b = b [:,np.newaxis]
# print(a+b)
# print(a>b)
# print(a==b)

def get_probability():
    probabilities = np.zeros((1000, 366)) # init my list
    for i in range(1000):
        for n in range(2, 366):
            birthdays = np.random.randint(1, 364, size=n) # make my list (do this 1000 times for every number 2 - 365)

            if duplicates(birthdays): # if there are duplicates set this index's value to 1
                probabilities[i, n - 2] = 1
    avg_probabilities = np.sum(probabilities, axis=0) / 1000 # add all 1's in probabilities

    return avg_probabilities

def duplicates(birthdays):
    sorted = np.sort(birthdays)
    return np.any(sorted[:-1] == sorted[1:]) # compare sorted[n] to sorted[n + 1]

probabilities = get_probability()

for n in range (2, 366):
    print(f"Room size: {n}, Average Probability: {probabilities[n - 2]:.4f}")