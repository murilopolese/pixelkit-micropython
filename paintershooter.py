import PixelKit as kit
from time import sleep
from random import randint as random
colors = [
    [0, 0, 0],
    [10, 0, 0],
    [10, 10, 0],
    [0, 10, 0],
    [0, 10, 10],
    [0, 0, 10],
    [10, 0, 10],
    [10, 10, 10]
]
stage = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
t = 0
shooterPosition = 3
currentColor = 1
gameOver = False
def restart():
    global t
    global shooterPosition
    global gameOver
    global stage
    t = 0
    gameOver = False
    stage = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    randomizeStart()
def randomizeStart():
    global stage
    for x in range(0, 8):
        for y in range(0, 8):
            if random(0, 100) > 50:
                stage[y][8+x] = random(1, len(colors)-1)
def move(value):
    global shooterPosition
    shooterPosition = int((value/4095)*7)
def shoot():
    global stage
    global gameOver
    last = 15
    for i, value in enumerate(stage[shooterPosition][::-1]):
        if value != 0:
            last = max(15 - (i+1), 0)
    if last == 0:
        gameOver = True
    else:
        if currentColor == 0 and last < 15:
            stage[shooterPosition][last+1] = currentColor
        else:
            stage[shooterPosition][last] = currentColor
def previousColor():
    global currentColor
    currentColor = (currentColor - 1) % len(colors)
def nextColor():
    global currentColor
    currentColor = (currentColor + 1) % len(colors)
def nothing():
    return None
kit.on_joystick_up = shoot
kit.on_joystick_down = shoot
kit.on_joystick_right = shoot
kit.on_joystick_left = shoot
kit.on_joystick_click = shoot
kit.on_dial = move
kit.on_button_a = previousColor
kit.on_button_b = nextColor
def renderStage():
    for i, row in enumerate(stage):
        for j, value in enumerate(row):
            kit.set_pixel(j, i, colors[value])
def cover():
    kit.clear([0, 0, 0])
    renderStage()
    kit.render()
def update():
    global gameOver
    if stage[shooterPosition][0] != 0:
        gameOver = True
    kit.clear()
    renderStage()
    kit.set_pixel(0, shooterPosition, colors[currentColor])
    kit.render()
def clearScreen():
    for i in range(0, 16):
        for j in range(0, 8):
            kit.set_pixel(15-i, j, [10, 10, 10])
        kit.render()
        sleep(0.2)
def loop():
    global t
    kit.check_controls()
    t = t + 1
    if gameOver:
        clearScreen()
        restart()
    else:
        update()
def start():
    restart()
    while True:
        loop()
        sleep(0.1)

start()
