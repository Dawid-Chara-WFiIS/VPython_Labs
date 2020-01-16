from vpython import *

scene = canvas(width=1800, height=1000)

N = int(input("Please enter number of balls: "))
# balls list
balls = []
# initial conditions
r = 5
startX = -r * N / 2
dt = 0.001
k = 1
m = 1


# generate most left ball
balls.append(sphere(pos=vector(startX + r, 0, 0), radius=0.5, vel=vector(0, 0, 0)))

# generate balls rest of the balls
for i in range(2, N):
    balls.append(sphere(pos=vector(startX + i * r, 0, 0), radius=0.5, vel=vector(0, 0, 0)))
    
balls.append(sphere(pos=vector(startX + r * N, 0, 0), radius=0.5, vel=vector(0, 0, 0)))

# generate walls
wallL = box(pos=vector(startX, 0, 0), size=vector(1, 5, 0.1), color=color.red)
wallR = box(pos=vector(startX + r * N + r, 0, 0), size=vector(1, 5, 0.1), color=color.red)
# generate left and right helixes
heL = helix(pos=vector(startX, 0, 0), axis=balls[0].pos - vector(startX, 0, 0), radius=0.5,
            coils=10)
heR = helix(pos=vector(startX + r * N + r, 0, 0), axis=(vector(startX + r * N + r, 0, 0) - balls[N - 1].pos) * (-1),
            radius=0.5, coils=10)

# helixes list
helixes = []

for i in range(0, N - 1):
    helixes.append(helix(pos=balls[i].pos, axis=balls[i + 1].pos - balls[i].pos, vel=vector(0, 0, 0),
        radius=0.5, coils=10))

lab = label(pos=vector(0, -3, 0), text='', height=20, color=color.cyan, linecolor=color.red)

balls[0].pos += vector(0, 20, 0)
balls[N-1].pos += vector(0, -20, 0)

while True:
    rate(1000)
    # forces list
    F = []
    F.append(k * (vector(startX, 0, 0) + balls[1].pos - 2 * balls[0].pos))
    for i in range(1, N - 1):
        F.append(k * (balls[i - 1].pos + balls[i + 1].pos - 2 * balls[i].pos))
    F.append(k * (balls[N - 2].pos + vector(startX + r * N + r, 0, 0) - 2 * balls[N - 1].pos))
    for i in range(N):
        balls[i].vel += dt * F[i] / m
        balls[i].pos += balls[i].vel * dt
    heL.axis = balls[0].pos - vector(startX, 0, 0)
    for i in range(N - 1):
        helixes[i].pos = balls[i].pos
        helixes[i].axis = balls[i + 1].pos - balls[i].pos
    heR.axis = balls[N - 1].pos - vector(startX + r * N + r, 0, 0)
    EnergyK = 0.0
    for ball in balls:
        EnergyK += m * ((mag(ball.vel)) ** 2) / 2
    EnergyP = 0.0
    for hel in helixes:
        EnergyP += k * ((mag(hel.axis)) ** 2) / 2
    EnergyP += k * ((mag(heL.axis)) ** 2) / 2
    EnergyP += k * ((mag(heR.axis)) ** 2) / 2
    lab.text = 'Kinetic Energy = ' + str(EnergyK) + '\n' + 'Potential Energy = ' + str(EnergyP) + '\n' + 'Energy = ' + str(EnergyK + EnergyP)

