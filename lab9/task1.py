from vpython import *

scene = canvas(title='Solar system',
     width=600, height=600,
     center=vector(0, 0, 0))

G = 6.7 * 10**(-11)
SUN_MASS = 2*10**30


sun = sphere(pos=vec(0, 0, 0), radius=10**10, color=color.orange, make_trail=True)
mercury = sphere(pos=vec(70 * 10**9, 0, 0), radius=5*10**9, color=color.white, make_trail=True)
wenus = sphere(pos=vec(110 * 10**9, 0, 0), radius=5*10**9, color=color.green, make_trail=True)
earth = sphere(pos=vec(150 * 10**9, 0, 0), radius=5*10**9, color=color.blue, make_trail=True)
mars = sphere(pos=vec(250 * 10**9, 0, 0), radius=5*10**9, color=color.red, make_trail=True)

# in m/s
mercury.vel = vec(0, 4.7*10**4, 0)
wenus.vel = vec(0, 3.5*10**4, 0)
earth.vel = vec(0, 3*10**4, 0)
mars.vel = vec(0, 2.4*10**4, 0)

dt = 3600

while True:
    rate(1000)
    merc_acc = - (mercury.pos - sun.pos) * G * SUN_MASS / (mag(mercury.pos - sun.pos) ** 3)
    wenus_acc = - (wenus.pos - sun.pos) * G * SUN_MASS / (mag(wenus.pos - sun.pos) ** 3)
    earth_acc = - (earth.pos - sun.pos) * G * SUN_MASS / (mag(earth.pos - sun.pos) ** 3)
    mars_acc = - (mars.pos - sun.pos) * G * SUN_MASS / (mag(mars.pos - sun.pos) ** 3)

    mercury.vel += merc_acc*dt
    mercury.pos += mercury.vel*dt
    wenus.vel += wenus_acc * dt
    wenus.pos += wenus.vel * dt
    earth.vel += earth_acc * dt
    earth.pos += earth.vel * dt
    mars.vel += mars_acc * dt
    mars.pos += mars.vel * dt




