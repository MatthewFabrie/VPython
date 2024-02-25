from vpython import *
import numpy as np

scene = canvas()

WallL = box(pos=vector(-4,0,0), size=vector(1, 7, 7), color = color.green)
WallTo = box(pos=vector(0,4,0), size=vector(7, 1, 7), color = color.blue)
WallR = box(pos=vector(4,0,0), size=vector(1, 7, 7), color = color.cyan)
WallBo = box(pos=vector(0,-4,0), size=vector(7, 1, 7), color = color.purple)
WallBa = box(pos=vector(0,0,-4), size=vector(7, 7, 1), color = color.yellow)
WallF = box(pos=vector(0,0,4), size=vector(7, 7, 1), color = color.white, opacity=0)

dt = 0.005

spheres = []

for i in range(100):
    spheres.append(sphere(pos=vector(0, 0, 0), radius = 0.25, color = color.red))
    random_vector = np.random.uniform(-3, 3, 3)
    spheres[i].velocity = vector(random_vector[0], random_vector[1], random_vector[2])

while 1:
    rate(100)
    for ball in spheres:
        ball.pos = ball.pos + ball.velocity * dt
        if abs(ball.pos.x) >= (3.25):
            if (ball.pos.x < 0):
                ball.color = color.green
            else:
                ball.color = color.cyan
            ball.velocity.x = -ball.velocity.x
        if abs(ball.pos.y) >= (3.25):
            if (ball.pos.y < 0):
                ball.color = color.purple
            else:
                ball.color = color.blue
            ball.velocity.y = -ball.velocity.y
        if abs(ball.pos.z) >= (3.25):
            if (ball.pos.z < 0):
                ball.color = color.yellow
            else:
                ball.color = color.white
            ball.velocity.z = -ball.velocity.z