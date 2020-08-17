import pixelkit as kit
from time import sleep
from random import randint as random
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
gameOver = False
score = 0
def restart():
    global t
    global shooterPosition
    global gameOver
    global score
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
    for x in range(0, 3):
        for y in range(0, 8):
            if random(0, 100) > 50:
                stage[y][12+x] = 1
def cleanLines():
    global stage
    for x in range(0, 16):
        i = 15-x
        sum = 0
        for y in range(0, 8):
            sum = sum + stage[y][i]
        if sum == 8:
            for y in range(0, 8):
                stage[y][i] = 0
def shift():
    global stage
    for x in range(1, 16):
        for y in range(0, 8):
            stage[y][x-1] = stage[y][x]
    for y in range(0, 8):
        stage[y][15] = 1 * random(0, 1)
def move(value):
    global shooterPosition
    shooterPosition = int((value/4095)*7)
def shoot():
    global stage
    global gameOver
    last = 15
    for i, value in enumerate(stage[shooterPosition][::-1]):
        if value == 1:
            last = max(15 - (i+1), 0)
    if last == 0:
        gameOver = True
    else:
        stage[shooterPosition][last] = 1
    cleanLines()
def nothing():
    return None
kit.on_joystick_up = shoot
kit.on_joystick_down = shoot
kit.on_joystick_right = shoot
kit.on_joystick_left = shoot
kit.on_joystick_click = shoot
kit.on_dial = move
kit.on_button_a = nothing
kit.on_button_b = nothing
def renderStage():
    global stage
    global score
    sum = 0
    for i, row in enumerate(stage):
        for j, value in enumerate(row):
            sum = sum + value
            color = [10*value] * 3
            kit.set_pixel(j, i, color)
    if sum == 0:
        score = score + 1
        restart()
def cover():
    kit.clear()
    renderStage()
    kit.render()
def update():
    global gameOver
    if stage[shooterPosition][0] == 1:
        gameOver = True
    if (t % 240 - score) == 0:
        shift()
    kit.clear()
    renderStage()
    kit.set_pixel(0, shooterPosition, [8, 8, 8])
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
        sleep(0.001)
start()
