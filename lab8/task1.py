from vpython import *
import random

scene = canvas(width=1000, height=1000)
wallR = box(pos=vec(4, 0, 0), size=vec(0.1, 8, 8), color=color.red)
wallL = box(pos=vec(-4, 0, 0), size=vec(0.1, 8, 8), color=color.green)
wallT = box(pos=vec(0, 4, 0), size=vec(8, 0.1, 8), color=color.blue)
wallD = box(pos=vec(0, -4, 0), size=vec(8, 0.1, 8), color=color.orange)
wallB = box(pos=vec(0, 0, -4), size=vec(8, 8, 0.1), color=color.magenta)

ball = sphere(pos=vec(0, 0, 0), radius=0.2, color=color.black, make_trail=True)
ball.vel = 4*vec(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
dt = 0.005

while True:
    rate(1000)
    ball.pos += ball.vel*dt
    if ball.pos.x + ball.radius >= 4:
        ball.vel.x = -ball.vel.x
        ball.color = color.red
    if ball.pos.x - ball.radius <= -4:
        ball.vel.x = -ball.vel.x
        ball.color = color.green
    if ball.pos.y + ball.radius >= 4:
        ball.vel.y = -ball.vel.y
        ball.color = color.blue
    if ball.pos.y - ball.radius <= -4:
        ball.vel.y = -ball.vel.y
        ball.color = color.orange
    if ball.pos.z + ball.radius >= 4:
        ball.vel.z = -ball.vel.z
        ball.color = color.black
    if ball.pos.z - ball.radius <= -4:
        ball.vel.z = -ball.vel.z
        ball.color = color.magenta
