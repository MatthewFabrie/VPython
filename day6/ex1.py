from matplotlib import pyplot as plot 
import matplotlib.patches as patches
import numpy as np

x0 = 0
y0 = 0
x_arr = np.zeros(1000000)
y_arr = np.zeros(1000000)
counter = 0

plot.rcParams['agg.path.chunksize'] = 10000

def firstExercice():
    points = np.array(np.random.randint(1, 101, 1000000))
    
    for point in points:
        if (point <= 85):
            formula1()
        elif (point > 85 and point <= 92):
            formula2()
        elif (point > 92 and point <= 99):
            formula3()
        else:
            formula4()

    rect = plot.Rectangle((1, 2), 0.5, 2, linewidth=1, edgecolor='g', facecolor='none')

    plot.gca().add_patch(rect)
    plot.plot(x_arr, y_arr, '.r', markersize=0.1)
    plot.savefig('leaf.png', format='png', dpi=400)
    plot.show()

def formula1():
    global x0, y0
    global x_arr, y_arr
    global counter
    tmp_x0 = x0
    tmp_y0 = y0
    x0 = 0.85 * tmp_x0 + 0.04 * tmp_y0
    y0 = -0.04 * tmp_x0 + 0.85 * tmp_y0 + 1.6
    x_arr[counter] = x0
    y_arr[counter] = y0
    counter+=1

def formula2():
    global x_arr, y_arr
    global x0, y0
    global counter
    tmp_x0 = x0
    tmp_y0 = y0
    x0 = 0.2 * tmp_x0 - 0.26 * tmp_y0
    y0 = 0.23 * tmp_x0 + 0.22 * tmp_y0 + 1.6
    x_arr[counter] = x0
    y_arr[counter] = y0
    counter+=1

def formula3():
    global x0, y0
    global x_arr, y_arr
    global counter
    tmp_x0 = x0
    tmp_y0 = y0
    x0 = -0.15 * tmp_x0 + 0.28 * tmp_y0
    y0 = 0.26 * tmp_x0 + 0.24 * tmp_y0 + 0.44
    x_arr[counter] = x0
    y_arr[counter] = y0
    counter+=1

def formula4():
    global x0, y0
    global x_arr, y_arr
    global counter
    tmp_x0 = x0
    tmp_y0 = y0
    x0 = 0
    y0 = 0.16 * tmp_y0
    x_arr[counter] = x0
    y_arr[counter] = y0
    counter+=1

def secondExercice():
    points = np.array(np.random.randint(1, 101, 100000000))

    for point in points:
        if (counter == 1000000):
            break
        if (point <= 85):
            formula12()
        elif (point > 85 and point <= 92):
            formula22()
        elif (point > 92 and point <= 99):
            formula32()
        else:
            formula42()
    plot.plot(x_arr, y_arr, '.r', markersize=0.1)
    plot.show()

def formula12():
    global x0, y0
    global x_arr, y_arr
    global counter
    tmp_x0 = x0
    tmp_y0 = y0
    x0 = 0.85 * tmp_x0 + 0.04 * tmp_y0
    y0 = -0.04 * tmp_x0 + 0.85 * tmp_y0 + 1.6
    if ((x0 >= 1 and x0 <= 1.5) and (y0 >= 2 and y0 <= 4)):
        x_arr[counter] = x0
        y_arr[counter] = y0
        counter+=1

def formula22():
    global x_arr, y_arr
    global x0, y0
    global counter
    tmp_x0 = x0
    tmp_y0 = y0
    x0 = 0.2 * tmp_x0 - 0.26 * tmp_y0
    y0 = 0.23 * tmp_x0 + 0.22 * tmp_y0 + 1.6
    if ((x0 >= 1 and x0 <= 1.5) and (y0 >= 2 and y0 <= 4)):
        x_arr[counter] = x0
        y_arr[counter] = y0
        counter+=1

def formula32():
    global x0, y0
    global x_arr, y_arr
    global counter
    tmp_x0 = x0
    tmp_y0 = y0
    x0 = -0.15 * tmp_x0 + 0.28 * tmp_y0
    y0 = 0.26 * tmp_x0 + 0.24 * tmp_y0 + 0.44
    if ((x0 >= 1 and x0 <= 1.5) and (y0 >= 2 and y0 <= 4)):
        x_arr[counter] = x0
        y_arr[counter] = y0
        counter+=1

def formula42():
    global x0, y0
    global x_arr, y_arr
    global counter
    tmp_x0 = x0
    tmp_y0 = y0
    x0 = 0
    y0 = 0.16 * tmp_y0
    if ((x0 >= 1 and x0 <= 1.5) and (y0 >= 2 and y0 <= 4)):
        x_arr[counter] = x0
        y_arr[counter] = y0
        counter+=1

# firstExercice()
secondExercice()