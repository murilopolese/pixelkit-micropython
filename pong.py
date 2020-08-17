import PixelKit as kit
from random import randint as random
t = 0
ballPosition = [7, 4]
ballDirection = [1, 1]
padPosition = 2
padSize = 2
gameOver = False
level = 12
score = 0
def reset(button=False):
    global t
    global ballPosition
    global ballDirection
    global padPosition
    global gameOver
    global level
    global score
    t = 0
    ballPosition = [7, 4]
    ballDirection = [1, 1]
    padPosition = 2
    gameOver = False
    level = 12
    score = 0
def renderBall():
    kit.set_pixel(ballPosition[0], ballPosition[1], [20, 20, 20])
def renderLeftPad():
    for i in range(0, padSize):
        kit.set_pixel(0, int(padPosition + i), [0, 0, 10])
def renderRightPad():
    for i in range(0, padSize):
        kit.set_pixel(15, int(padPosition + i), [0, 10, 0])
def renderFrame():
    renderBall()
    renderLeftPad()
    renderRightPad()
def hitPad():
    return ballPosition[1] >= int(padPosition) and ballPosition[1] <= int(padPosition)+(padSize-1)
def updateBall():
    global gameOver
    global level
    global score
    newPosition = [
        ballPosition[0] + ballDirection[0],
        ballPosition[1] + ballDirection[1]
    ];
    if newPosition[1] > 7 or newPosition[1] < 0:
        ballDirection[1] = ballDirection[1] * -1
    if newPosition[0] == 15 or newPosition[0] == 0:
        if hitPad():
            ballDirection[0] = ballDirection[0] * -1
            level = level - 0.5
            if level < 3:
                level = 3
            score = score + 1
        else:
            gameOver = True
    ballPosition[0] = ballPosition[0] + ballDirection[0]
    ballPosition[1] = ballPosition[1] + ballDirection[1]
def onJoystickUp():
    global padPosition
    if padPosition > 0:
        padPosition = padPosition - 0.2
def onJoystickDown():
    global padPosition
    if padPosition < 5:
        padPosition = padPosition + 0.2
def onDial(value):
    global padPosition
    dialPosition = int((value/4095)*7)
    if dialPosition >= 0 and dialPosition <= 7-(padSize-1):
        padPosition = dialPosition
def nothing():
    return None
kit.on_joystick_up = nothing
kit.on_joystick_down = nothing
kit.on_joystick_left = nothing
kit.on_joystick_right = nothing
kit.on_button = reset
kit.on_button_a = reset
kit.on_button_b = reset
kit.on_dial = onDial
def loop():
    global t
    t = t + 1
    kit.check_controls()
    if not gameOver:
        if t % int(level) == 0:
            updateBall()
        kit.clear()
        renderFrame()
        kit.render()
    else:
        kit.set_background([10, 10, 0])
        for i in range(0, score):
            kit.set_pixel(i%16, int(i/16), [10, 0, 0])
        kit.render();
def start():
    reset()
    while True:
        loop()


start()
