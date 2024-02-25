import numpy as np
import matplotlib.pyplot as plt


def second_equation(x, y):
    x = 0.85 * x + 0.04 * y
    y = -0.04 * x + 0.85 * y + 1.6 

    def equation1(x, y):
        new_x = 0.85 * x + 0.04 * y
        new_y = -0.04 * x + 0.85 * y + 1.6
        return new_x, new_y

    def equation2(x, y):
        new_x = 0.2 * x - 0.26 * y
        new_y = 0.23 * x + 0.22 * y + 1.6
        return new_x, new_y

    def equation3(x, y):
        new_x = -0.15 * x + 0.28 * y
        new_y = 0.26 * x + 0.24 * y + 0.44
        return new_x, new_y

    def equation4(x, y):
        new_x = 0
        new_y = 0.16 * y
        return new_x, new_y

    x_values = []
    y_values = []

    x = 0
    y = 0

    square_x_values = []
    square_y_values = []
    count = 0
    for _ in range(1000000000):
        random_num = np.random.random()
        if random_num <= 0.85:
            new_x, new_y = equation1(x, y)
        elif 0.85 < random_num <= 0.92:
            new_x, new_y = equation2(x, y)
        elif 0.92 < random_num <= 0.99:
            new_x, new_y = equation3(x, y)
        else:
            new_x, new_y = equation4(x, y)

        if ((new_x >= 1 and new_x <= 1.5 ) and (new_y >= 4 and new_y <= 5)):
            square_x_values.append(new_x)
            square_y_values.append(new_y)
            count += 1
            print(count)
        if count == 1000000:
            break

        x = new_x
        y = new_y
        x_values.append(x)
        y_values.append(y)


    plt.plot(square_x_values, square_y_values, '.', c='red', markersize=1)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig('plot.png', dpi=400)
    plt.show()

second_equation(0, 0)