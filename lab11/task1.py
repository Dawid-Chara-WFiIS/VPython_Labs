from vpython import *
import random
import math
N = 50
scene = canvas(width=1200, height=1000)
big_mass = 30
small_mass = 1
balls = []
basic_vel = 2
rad = 3
angle = 0
dt = 0.005

# generate ring
r = ring(pos=vec(0, 0, 0), radius=10, thickness=0.2, axis=vec(0, 0, 1), color=color.blue)

# generate balls
big_one = sphere(pos=vec(0, 0, 0), radius=2, color=color.red, make_trail=True)
big_one.vel = vec(0, 0, 0)
big_one.m = big_mass
balls.append(big_one)

for i in range(N):
    if angle > 2*math.pi:
        rad += 1
        angle = 0
    ball = sphere(pos=vec(rad*math.cos(angle), rad*math.sin(angle), 0),  radius=0.4, color=color.green)
    ball.vel = vec(basic_vel*random.uniform(-1, 1), basic_vel*random.uniform(-1, 1), 0)
    ball.m = small_mass
    balls.append(ball)
    angle += 36*math.pi/180


while True:
    rate(1000)
    for i in range(N+1):
        if mag(balls[i].pos) > 10 - balls[i].radius:
            # collisions with circle
            vel_r = (balls[i].pos / mag(balls[i].pos)) * dot(balls[i].vel, balls[i].pos / mag(balls[i].pos))
            balls[i].vel -= 2 * vel_r

        for j in range(i, N + 1):
            r1 = balls[i].radius
            r2 = balls[j].radius
            m1 = balls[i].m
            m2 = balls[j].m
            v1 = balls[i].vel
            v2 = balls[j].vel
            pos1 = balls[i].pos
            pos2 = balls[j].pos
            if mag(pos1 - pos2) <= r1 + r2:
                # collisions of balls
                a = mag(v1 - v2) ** 2
                b = -2 * dot(pos1 - pos2, v1 - v2)
                c = mag(pos1 - pos2) ** 2 - (r1 + r2) ** 2
                delta = b ** 2 - 4 * a * c
                if a == 0 or delta < 0:
                    continue
                else:
                    dt_prim = (-b + sqrt(delta)) / 2 * a
                    balls[i].pos -= dt_prim * v1
                    balls[i].vel -= 2 * m2 / (m1 + m2) * dot(v1 - v2,
                                                             (pos1 - pos2) / mag((pos1 - pos2))) * (pos1 - pos2) / mag(
                        (pos1 - pos2))
                    balls[j].vel += 2 * m1 / (m1 + m2) * dot(v1 - v2,
                                                             (pos1 - pos2) / mag((pos1 - pos2))) * (pos1 - pos2) / mag(
                        (pos1 - pos2))
                    balls[i].pos += dt_prim * v1

        balls[i].pos += dt * balls[i].vel
