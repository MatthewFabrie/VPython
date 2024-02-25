import math

x_values = []
y_values = []
nbp = []
nbm = []
f = open('graph.txt', 'w')

for i in range(51):
    x_values.append(i * (2 * math.pi / 50))
for x in x_values:
    y_values.append(50 * math.sin(x))
for i in range(51):
    print(int(y_values[i]))
    if int(y_values[i]) > 0:
        for i in range(int(y_values[i])):
            nbp.append('+')
        for x in nbp:
            f.write(x)
        f.write('\n')
    elif int(y_values[i]) < 0:
        for i in range(int(abs(y_values[i]))):
            nbm.append('-')
        for x in nbm:
            f.write(x)
        f.write('\n')
    else:
        f.write('0\n')
    
    nbp = []
    nbm = []