from vpython import *
import numpy as np

scene = canvas()

WallR = box(pos=vector(0.5,0.5,0), size=vector(0.01, 1, 1), color = color.cyan)
WallBo = box(pos=vector(0,0,0), size=vector(1, 0.01, 1), color = color.purple)
cube1 = box(pos=vector(-0.5,0.1,0), size=vector(0.2, 0.2, 0.2), color = color.green)
cube2 = box(pos=vector(0,0.1,0), size=vector(0.2, 0.2, 0.2), color = color.red)
contactsText = label(pos=vector(-0.5,1,0), space = 1, text = "0", height=10, color=color.green)

contacts  = 0
k = 5

m1 = 100**k
m2 = 1

cube1.velocity = vector(1,0,0)
cube2.velocity = vector(0,0,0)

dt = 0.000001

while 1:
    cube1.pos = cube1.pos + cube1.velocity * dt
    cube2.pos = cube2.pos + cube2.velocity * dt

    if cube1.pos.x + 0.2 >= cube2.pos.x:
        contacts+=1
        
        oldcube1vel = cube1.velocity
        oldcube2vel = cube2.velocity

        cube1.velocity = (oldcube1vel * (m1 - m2)/(m1 + m2) ) + (oldcube2vel * (2 * m2)/(m1 + m2))
        cube2.velocity = (oldcube1vel * (2 * m1)/(m1 + m2)) + (oldcube2vel * (m2 - m1)/(m1 + m2))

        cube1.pos = cube1.pos + cube1.velocity * dt
        cube2.pos = cube2.pos + cube2.velocity * dt

        contactsText.text = contacts

    if (cube2.pos.x + 0.1 >= 0.5):
        contacts += 1
        cube2.velocity = cube2.velocity * -1

        contactsText.text = contacts