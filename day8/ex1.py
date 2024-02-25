from vpython import *
import numpy as np

scene = canvas()
scene.range = 300

sun = sphere(pos=vector(0, 0, 0), radius = 10, color = color.yellow)
mercure = sphere(pos=vector(70, 0, 0), radius = 10, color = color.red, make_trail = True)
venus = sphere(pos=vector(110, 0, 0), radius = 10, color = color.red, make_trail = True)
terre = sphere(pos=vector(150, 0, 0), radius = 10, color = color.red, make_trail = True)
mars = sphere(pos=vector(250, 0, 0), radius = 10, color = color.red, make_trail = True)

mercure.velocity = vector(0,39/(10**9),0)
venus.velocity = vector(0,35/(10**9),0)
terre.velocity = vector(0,30/(10**9),0)
mars.velocity = vector(0,22/(10**9),0)

macceleration = vector(0,0,0)
vacceleration = vector(0,0,0)
tacceleration = vector(0,0,0)
maacceleration = vector(0,0,0)

dt = 100000

while 1:
    # rate(200)
    old_mpos = mercure.pos
    old_vpos = venus.pos
    old_tpos = terre.pos
    old_mapos = mars.pos
    old_mvel = mercure.velocity
    old_vvel = venus.velocity
    old_tvel = terre.velocity
    old_mavel = mars.velocity

    macceleration_s = -(6.67e-11) * (2e30) / ((mag(mercure.pos*1e11))**3)
    macceleration_vector = vector(mercure.pos.x, mercure.pos.y, mercure.pos.z)

    vacceleration_s = -(6.67e-11) * (2e30) / ((mag(venus.pos*1e11))**3)
    vacceleration_vector = vector(venus.pos.x, venus.pos.y, venus.pos.z)

    tacceleration_s = -(6.67e-11) * (2e30) / ((mag(terre.pos*1e11))**3)
    tacceleration_vector = vector(terre.pos.x, terre.pos.y, terre.pos.z)

    maacceleration_s = -(6.67e-11) * (2e30) / ((mag(mars.pos*1e11))**3)
    maacceleration_vector = vector(mars.pos.x, mars.pos.y, mars.pos.z)


    macceleration.x = macceleration_s * (macceleration_vector.x*1e11)
    macceleration.y = macceleration_s * (macceleration_vector.y*1e11)
    macceleration.z = macceleration_s * (macceleration_vector.z*1e11)

    vacceleration.x = vacceleration_s * (vacceleration_vector.x*1e11)
    vacceleration.y = vacceleration_s * (vacceleration_vector.y*1e11)
    vacceleration.z = vacceleration_s * (vacceleration_vector.z*1e11)

    tacceleration.x = tacceleration_s * (tacceleration_vector.x*1e11)
    tacceleration.y = tacceleration_s * (tacceleration_vector.y*1e11)
    tacceleration.z = tacceleration_s * (tacceleration_vector.z*1e11)

    maacceleration.x = maacceleration_s * (maacceleration_vector.x*1e11)
    maacceleration.y = maacceleration_s * (maacceleration_vector.y*1e11)
    maacceleration.z = maacceleration_s * (maacceleration_vector.z*1e11)

    # macceleration = macceleration_s * macceleration_vector

    # macceleration = -((6.67e-11) * (2e30) / (mag(mercure.pos) * 1e11)**3) * vector(mercure.pos.x, mercure.pos.y, mercure.pos.z)


    mercure.velocity = old_mvel + macceleration/1e11 * dt
    mercure.pos = old_mpos + mercure.velocity * dt

    venus.velocity = old_vvel + vacceleration/1e11 * dt
    venus.pos = old_vpos + venus.velocity * dt

    terre.velocity = old_tvel + tacceleration/1e11 * dt
    terre.pos = old_tpos + terre.velocity * dt

    mars.velocity = old_mavel + maacceleration/1e11 * dt
    mars.pos = old_mapos + mars.velocity * dt