from time import sleep, time
from random import randint, random
import math
import pixelkit as kit
# Escape variable
playing = True
def toggle():
    global playing
    playing = not playing
kit.on_joystick_click = toggle
# Calculates the distance between two points/tuples
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
# Constrain two numbers
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)
# Convert HSV to RGB (all values from 0.0 to 1.0)
def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h*6.0) # XXX assume int() truncates!
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i%6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q
    # Cannot get here
def get_color(p):
    s = 0
    color_max = 20
    for ball in balls:
        s += 15*ball.radius / max(distance(p, ball.pos), 0.01)
    s = clamp(s / (color_max * len(balls)), 0, 0.9)
    s = (s+time()/100)%1
    normal_color = hsv_to_rgb(s, 1, 1)
    c = (
        int(normal_color[0]*color_max),
        int(normal_color[1]*color_max),
        int(normal_color[2]*color_max)
    )
    return c
class Ball():
    def __init__(self, pos=None, vel=None, radius=None):
        if pos is None:
            self.pos = [randint(0, 15), randint(0, 7)]
        else:
            self.pos = pos
        if vel is None:
            self.vel = [random(), random()]
        else:
            self.vel = vel
        if radius is None:
            self.radius = 4
        else:
            self.radius = radius
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if self.pos[0] <= 0 or self.pos[0] >= 15:
            self.vel[0] *= -1
        if self.pos[1] <= 0 or self.pos[1] >= 7:
            self.vel[1] *= -1
    def draw(self):
        kit.set_pixel(int(self.pos[0]), int(self.pos[1]), [20, 20, 20])
balls = [Ball(), Ball()]
for i in range(0, randint(1, 3)):
    balls.append(Ball())
kit.clear()
kit.render()
while playing:
    kit.check_controls()
    for x in range(0, 16):
        for y in range(0, 8):
            c = get_color((x, y))
            kit.set_pixel(x, y, c)
    for ball in balls:
        ball.update()
    kit.render()
    sleep(0.01)
