import pixelkit as kit
from time import sleep, time
from random import randint
log = print
playing = True
def toggle():
    global playing
    playing = not playing
kit.on_button_b = toggle
colors = [
    (0,   0,  5),
    (10, 10, 10),
    (10, 10,  5),
    (10,  5, 10),
    ( 5, 10, 10),
    (10,  5,  5),
    ( 5,  5, 10),
    (10, 10,  0),
    (10,  0, 10),
    ( 0, 10, 10),
    (10,  0, 10),
    ( 0,  0, 10),
    (10,  5,  0),
    (10,  0,  0)
]
ship = [0, 3] # Ship position
bullet = None
invaders = [
[14, 1], [14, 3], [14, 5],
[12, 1], [12, 3], [12, 5],
[10, 1], [10, 3], [10, 5]
]
direction = 1
ship_sprite = [
[1, 1, 0],
[0, 1, 1],
[1, 1, 0]
]
t = 0
level = 20
invader_color = 0
def draw_sprite(x, y, sprite, color=None):
    for j, line in enumerate(sprite):
        for i, value in enumerate(line):
            if value > -1:
                if color is None:
                    kit.set_pixel(x+i, y+j, colors[value])
                else:
                    kit.set_pixel(x+i, y+j, colors[color])
def spawn_invaders():
    global invaders
    invaders = invaders = [
[14, 1], [14, 3], [14, 5],
[12, 1], [12, 3], [12, 5],
[10, 1], [10, 3], [10, 5]
]
def update_invaders():
    global playing
    global direction
    global invaders
    will_bounce = False
    for invader in invaders:
        kit.set_pixel(invader[0], invader[1], colors[0])
        if invader[1]+direction > 7 or invader[1]+direction < 0:
            will_bounce = True
    if will_bounce:
        direction *= -1
    for i, invader in enumerate(invaders):
        invaders[i][1] += direction
        if will_bounce:
            if invaders[i][0] - 1 > 2:
                invaders[i][0] -= 1
            else:
                log('game over boy')
                kit.set_background(colors[2+invader_color])
                kit.render()
                playing = False
def draw_invaders():
    for invader in invaders:
        kit.set_pixel(invader[0], invader[1], colors[2+invader_color])
def get_ship_position():
    y = (kit.dial_value / 4095) * 5
    return (0, int(y))
def get_pixel(p):
    index = kit.get_index_from_coordinate(p[0], p[1])
    value = kit.np[index]
    return colors.index(value)
def shoot():
    global bullet
    if bullet is None:
        bullet = [ ship[0]+2, ship[1]+1 ]
kit.on_joystick_click = shoot
kit.set_background(colors[0])
while playing:
    try:
        t += 1
        kit.check_controls()
        draw_sprite(ship[0], ship[1], ship_sprite, 0)
        ship = get_ship_position()
        draw_sprite(ship[0], ship[1], ship_sprite)
        if t % level == 0:
            update_invaders()
        draw_invaders()
        if not (bullet is None):
            next_bullet = [int(bullet[0]+1), int(bullet[1])]
            if get_pixel(next_bullet) > 1:
                log('BANG', next_bullet, get_pixel(next_bullet), invaders)
                kit.set_pixel(bullet[0], bullet[1], colors[0])
                kit.set_pixel(next_bullet[0], next_bullet[1], colors[0])
                invaders.remove(next_bullet)
                if len(invaders) == 0:
                    level = max(0, level-1)
                    invader_color = (invader_color+1) % (len(colors)-2)
                    spawn_invaders()
                bullet = None
            elif bullet[0] <= 14:
                kit.set_pixel(bullet[0], bullet[1], colors[0])
                bullet[0] += 1
                kit.set_pixel(bullet[0], bullet[1], colors[1])
            else:
                kit.set_pixel(bullet[0], bullet[1], colors[0])
                bullet = None
        kit.render()
        sleep(0.01)
    except Exception as e:
        log(e)
        playing = False
