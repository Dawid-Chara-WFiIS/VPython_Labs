from vpython import *
import random
N = 15
S = 5

scene = canvas(width=1000, height=1000)
wallR = box(pos=vec(S, 0, 0), size=vec(0.1, 2*S, 2*S), color=color.red)
wallL = box(pos=vec(-S, 0, 0), size=vec(0.1, 2*S, 2*S), color=color.green)
wallT = box(pos=vec(0, S, 0), size=vec(2*S, 0.1, 2*S), color=color.blue)
wallD = box(pos=vec(0, -S, 0), size=vec(2*S, 0.1, 2*S), color=color.orange)
wallB = box(pos=vec(0, 0, -S), size=vec(2*S, 2*S, 0.1), color=color.magenta)

balls = []
i = 4
j = -4
counter = 0
dt = 0.005

while counter < N:
    ball = sphere(pos=vec(i, j, 0), radius=0.5, color=color.black)
    ball.vel = vec(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
    balls.append(ball)
    j += 1
    if j == 4:
        i -= 1
        j = -4
    counter += 1

while True:
    rate(1000)
    for i in range(N):
        ball = balls[i]
        ball.pos += ball.vel * dt
        if ball.pos.x + ball.radius >= S:
            ball.vel.x = -ball.vel.x
            ball.color = color.red
        if ball.pos.x - ball.radius <= -S:
            ball.vel.x = -ball.vel.x
            ball.color = color.green
        if ball.pos.y + ball.radius >= S:
            ball.vel.y = -ball.vel.y
            ball.color = color.blue
        if ball.pos.y - ball.radius <= -S:
            ball.vel.y = -ball.vel.y
            ball.color = color.orange
        if ball.pos.z + ball.radius >= S:
            ball.vel.z = -ball.vel.z
            ball.color = color.black
        if ball.pos.z - ball.radius <= -S:
            ball.vel.z = -ball.vel.z
            ball.color = color.magenta
        for j in range(0, i):
            other_ball = balls[j]
            if mag(ball.pos - other_ball.pos) <= 2*ball.radius:
                ball.vel, other_ball.vel = other_ball.vel, ball.vel
        for j in range(i+1, N):
            other_ball = balls[j]
            if mag(ball.pos - other_ball.pos) <= 2*ball.radius:
                ball.vel, other_ball.vel = other_ball.vel, ball.vel
