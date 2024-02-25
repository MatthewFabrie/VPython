from vpython import *

g = 9.8
L1 = 1.0
L2 = 1.0000000001

phi = pi
theta = pi - 0.1
a = 0
b = 0

phi2 = pi
theta2 = pi - 0.1
a2 = 0
b2 = 0

scene = canvas()
pen1_line = cylinder(pos=vector(0, 0, 0), axis=vector(L1 * sin(phi), -L1 * cos(phi), 0), radius=0.01, color=color.blue)
pen1_ball = sphere(pos=pen1_line.axis, radius=0.05, color=color.blue)
pen2_line = cylinder(pos=vector(pen1_ball.pos), axis=vector(L1 * sin(theta), -L1 * cos(theta), 0), radius=0.01, color=color.red)
pen2_ball = sphere(pos=pen2_line.pos + pen2_line.axis, radius=0.05, color=color.red)

pen3_line = cylinder(pos=vector(0, 0, 0), axis=vector(L2 * sin(phi2), -L2 * cos(phi2), 0), radius=0.01, color=color.magenta)
pen3_ball = sphere(pos=pen3_line.axis, radius=0.05, color=color.magenta)
pen4_line = cylinder(pos=vector(pen3_ball.pos), axis=vector(L2 * sin(theta2), -L2 * cos(theta2), 0), radius=0.01, color=color.green)
pen4_ball = sphere(pos=pen3_line.pos + pen3_line.axis, radius=0.05, color=color.green)

txt1 = label(pos=vector(2,1,0), space = 1, text = 'Energy = 0', height=10, color=color.red)
txt2 = label(pos=vector(2,1.8,0), space = 1, text = 'Energy = 0', height=10, color=color.green)

dt = 0.00001

while 1:
    rate(100000)

    pen1_acc = (-g/L1) * (2 * sin(phi) - sin(theta) * cos(phi - theta)) - 0.5 * a**2 * sin(2 * phi - 2 * theta) - b**2 * sin(phi - theta)
    pen2_acc = (-g/L1) * (2 * sin(theta) -2 * sin(phi) * cos(phi - theta)) + 0.5 * b**2 * sin(2 * phi - 2 * theta) + 2 * a**2 * sin(phi - theta)


    pen3_acc = (-g / L2) * (2 * sin(phi2) - sin(theta2) * cos(phi2 - theta2)) - 0.5 * a2**2 * sin(2 * phi2 - 2 * theta2) - b2**2 * sin(phi2 - theta2)
    pen4_acc = (-g / L2) * (2 * sin(theta2) -2 * sin(phi2) * cos(phi2 - theta2)) + 0.5 * b2**2 * sin(2 * phi2 - 2 * theta2) + 2 * a2**2 * sin(phi2 - theta2)

    t1 = pen1_acc / (1 + (sin(phi - theta))**2)
    t2 = pen2_acc / (1 + (sin(phi - theta))**2)
    t3 = pen3_acc / (1 + (sin(phi2 - theta2))**2)
    t4 = pen4_acc / (1 + (sin(phi2 - theta2))**2)

    old_a = a
    old_b = b
    old_a2 = a2
    old_b2 = b2

    a = old_a + t1 * dt
    b = old_b + t2 * dt
    a2 = old_a2 + t3 * dt
    b2 = old_b2 + t4 * dt

    old_phi = phi
    old_theta = theta
    old_phi2 = phi2
    old_theta2 = theta2

    phi = old_phi + a * dt
    theta = old_theta + b * dt
    phi2 = old_phi2 + a2 * dt
    theta2 = old_theta2 + b2 * dt

    pen1_line.axis = vector(L1 * sin(phi), -L1 * cos(phi), 0)
    pen1_ball.pos = vector(L1 * sin(phi), -L1 * cos(phi), 0)
    pen2_ball.pos = vector(L1 * sin(phi) + L1 * sin(theta), -L1 * cos(phi) - L1 * cos(theta), 0)

    pen3_line.axis = vector(L2 * sin(phi2), -L2 * cos(phi2), 0)
    pen3_ball.pos = vector(L2 * sin(phi2), -L2 * cos(phi2), 0)
    pen4_ball.pos = vector(L2 * sin(phi2) + L2 * sin(theta2), -L2 * cos(phi2) - L2 * cos(theta2), 0)

    pen2_line.pos = pen1_ball.pos
    pen2_line.axis = vector(L1 * sin(theta), -L1 * cos(theta), 0)
    pen4_line.pos = pen3_ball.pos
    pen4_line.axis = vector(L2 * sin(theta2), -L2 * cos(theta2), 0)

    energy1 = 1 * g * pen1_ball.pos.y + 1 * g * pen2_ball.pos.y + 0.5 * 1 * L1**2 * (2 * a**2 + b**2 + 2 * a * b * cos(phi - theta))
    energy2 = 1 * g * pen3_ball.pos.y + 1 * g * pen4_ball.pos.y + 0.5 * 1 * L2**2 * (2 * a2**2 + b2**2 + 2 * a2 * b2 * cos(phi2 - theta2))
    txt1.text = energy1
    txt2.text = energy2