from vpython import *
import numpy as np

scene = canvas()
scene.range = 10

WallR = box(pos=vector(4,0,0), size=vector(1, 7, 7), color = color.cyan)
WallL = box(pos=vector(-4,0,0), size=vector(1, 7, 7), color = color.green)
Ball1 = sphere(pos=vector(-2, 0, 0), radius = 0.5, color = color.magenta)
Ball2 = sphere(pos=vector(0, 2, 0), radius = 0.5,color = color.magenta)
Ball3 = sphere(pos=vector(2, 0, 0), radius = 0.5,color = color.magenta)
coil1 = helix(pos=WallL.pos, axis = Ball1.pos - WallL.pos, radius = 0.5, coils = 10, thickness = 0.05, color = color.green)
coil2 = helix(pos=Ball1.pos, axis = Ball2.pos - Ball1.pos, radius = 0.5, coils = 10, thickness = 0.05, color = color.green)
coil3 = helix(pos=Ball2.pos, axis = Ball3.pos - Ball2.pos, radius = 0.5, coils = 10, thickness = 0.05, color = color.green)
coil4 = helix(pos=Ball3.pos, axis = WallR.pos - Ball3.pos, radius = 0.5, coils = 10, thickness = 0.05, color = color.green)

dt = 0.0001

Ball1.velocity = vector(0, 0, 0)
Ball2.velocity = vector(0, 0, 0)
Ball3.velocity = vector(0, 0, 0)

while 1:

    Ball1OldVel = Ball1.velocity
    Ball2OldVel = Ball2.velocity
    Ball3OldVel = Ball3.velocity
    Ball1Oldpos = Ball1.pos
    Ball2Oldpos = Ball2.pos
    Ball3Oldpos = Ball3.pos

    Ball1Force = Ball2.pos + WallL.pos - (Ball1.pos + Ball1.pos)
    Ball2Force = Ball3.pos + Ball1.pos - (Ball2.pos + Ball2.pos)
    Ball3Force = WallR.pos + Ball2.pos - (Ball3.pos + Ball3.pos)

    Ball1.velocity = Ball1OldVel + Ball1Force * dt
    Ball2.velocity = Ball2OldVel + Ball2Force * dt
    Ball3.velocity = Ball3OldVel + Ball3Force * dt

    Ball1.pos = Ball1Oldpos + Ball1.velocity * dt
    Ball2.pos = Ball2Oldpos + Ball2.velocity * dt
    Ball3.pos = Ball3Oldpos + Ball3.velocity * dt

    coil1.axis = Ball1.pos - WallL.pos
    coil2.axis = Ball2.pos - Ball1.pos
    coil3.axis = Ball3.pos - Ball2.pos
    coil4.axis = WallR.pos - Ball3.pos
    coil1.pos = WallL.pos
    coil2.pos = Ball1.pos
    coil3.pos = Ball2.pos
    coil4.pos = Ball3.pos