from vpython import *

nb = 21
scene = canvas()
scene.range = 10

left_wall = box(pos=vector(0, 0, 0), size=vector(1, 7, 7), color=color.green)
right_wall = box(pos=vector((nb*2)+2, 0, 0), size=vector(1, 7, 7), color=color.cyan)

balls = []
coils = []

i = 1
while i < (nb + 1):
    if i == 1:
        ball = sphere(pos=vector(i*2, 2, 0), radius=0.5, color=color.red)
        ball.velocity = vector(0,0,0)
        balls.append(ball)
        spring = helix(pos=left_wall.pos, axis=balls[i-1].pos - left_wall.pos, radius=0.2, thickness=0.1)
        coils.append(spring)
    else:
        ball = sphere(pos=vector(i*2, 0, 0), radius=0.5, color=color.red)
        ball.velocity = vector(0,0,0)
        balls.append(ball)
        if i > 1:
            spring = helix(pos=balls[i-2].pos, axis=balls[i-1].pos - balls[i-2].pos, radius=0.2, thickness=0.1)
            coils.append(spring)
    i += 1
spring = helix(pos=balls[i-2].pos, axis=right_wall.pos - balls[i-2].pos, radius=0.2, thickness=0.1)
coils.append(spring)
scene.camera.pos = vector(nb, 0, 30)

dt = 0.0001

while True:
    rate(100)
    force_first = (balls[1].pos + left_wall.pos - (balls[0].pos + balls[0].pos))
    balls[0].velocity += force_first
    for i in range(1, nb-2):
        force = (balls[i+1].pos + balls[i-1].pos - ( balls[i].pos + balls[i].pos))
        balls[i].velocity += force
    force_last = (right_wall.pos + balls[nb-2].pos - (balls[nb-1].pos + balls[nb-1].pos))
    balls[nb-1].velocity += force_last

    balls[0].pos += balls[0].velocity * 0.0001
    for i in range(1, nb-1):
        balls[i].pos += balls[i].velocity * 0.0001
    balls[nb-1].pos += balls[nb-1].velocity * 0.0001

    coils[0].pos = left_wall.pos
    coils[0].axis = balls[0].pos - left_wall.pos
    for i in range(1, nb):
        coils[i].pos = balls[i-1].pos
        coils[i].axis = balls[i].pos - balls[i-1].pos
    coils[len(coils)-1].pos = right_wall.pos
    coils[len(coils)-1].axis = balls[nb-1].pos -right_wall.pos