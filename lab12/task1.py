from vpython import *
import math


class System:
    def __init__(self, L, g, phi, theta, clr=color.red):
        self.clr = clr
        self.L = L
        self.g = g
        self.oneBall = sphere(pos=vec(L*math.sin(phi), -L*math.cos(phi), 0), radius=0.1, color=self.clr)
        self.oneBall.angle = phi
        self.oneBall.angle_vel = 0
        self.oneBall.angle_acc = 0

        self.oneLine = cylinder(pos=vec(0, 0, 0), axis=self.oneBall.pos, color=self.clr, radius=0.01)

        self.secondBall = sphere(pos=vec(L*(math.sin(phi)+math.sin(theta)), -L*(math.cos(phi) + math.cos(theta)), 0), radius=0.1, color=self.clr)
        self.secondBall.angle = theta
        self.secondBall.angle_vel = 0
        self.secondBall.angle_acc = 0

        self.secondLine = cylinder(pos=self.oneBall.pos, axis=self.secondBall.pos- self.oneBall.pos, color=self.clr, radius=0.01)


    def update_position(self):
        self.oneBall.pos = vec(self.L*math.sin(self.oneBall.angle), -self.L*math.cos(self.oneBall.angle), 0)
        self.secondBall.pos = vec(self.L * (math.sin(self.oneBall.angle) + math.sin(self.secondBall.angle)),
                                  -self.L * (math.cos(self.oneBall.angle) + math.cos(self.secondBall.angle)), 0)

    def update_parameters(self, dt):
        phi = self.oneBall.angle
        theta = self.secondBall.angle
        self.oneBall.angle_acc = (-self.g/self.L)*(2*math.sin(phi) - math.sin(theta)*cos(phi - theta)) - (0.5*self.oneBall.angle_vel**2)*math.sin(2*phi - 2*theta) - (self.secondBall.angle_vel**2)*math.sin(phi-theta)
        self.oneBall.angle_acc /= (1 + math.sin(phi - theta)**2)

        self.secondBall.angle_acc = (-self.g/self.L)*(2*math.sin(theta) - 2*math.sin(phi)*math.cos(phi-theta)) + (0.5*self.secondBall.angle_vel**2)*math.sin(2*phi-2*theta) + (2*self.oneBall.angle_vel**2)*math.sin(phi-theta)
        self.secondBall.angle_acc /= (1+math.sin(phi-theta)**2)

        self.oneBall.angle_vel += self.oneBall.angle_acc*dt
        self.secondBall.angle_vel += self.secondBall.angle_acc*dt

        self.oneBall.angle += self.oneBall.angle_vel * dt
        self.secondBall.angle += self.secondBall.angle_vel * dt


    def update_lines(self):
        self.oneLine.axis = self.oneBall.pos
        self.secondLine.pos = self.oneBall.pos
        self.secondLine.axis = self.secondBall.pos - self.oneBall.pos

    def update(self, dt):
        self.update_parameters(dt)
        self.update_position()
        self.update_lines()



dt = 0.001

scene = canvas(width=1200, height=1000)
sys1 = System(1, 9.8, math.pi, math.pi - 0.1, color.white)
sys2 = System(1, 9.8000000001, math.pi, math.pi - 0.1, color.blue)

while True:
    rate(1000)
    sys1.update(dt)
    sys2.update(dt)
