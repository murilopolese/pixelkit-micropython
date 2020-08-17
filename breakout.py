import PixelKit as kit
from time import sleep
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
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
t = 0
gameOver = False
t = 0
colors = [
    [4, 3, 1],      #0 - background
    [10, 0, 0],     #1 - red
    [10, 10, 0],    #2 - yellow
    [0, 10, 0],     #3 - green
    [0, 10, 10],    #4 - cyan
    [0, 0, 10],     #5 - blue
    [10, 0, 10],    #6 - purple
    [10, 10, 10]    #7 - white
]
padPosition = 4
padSize = 3
ballPosition = [4, 4]
ballDirection = [1, 1]
level = 3
def reset():
    global gameOver
    global t
    global padPosition
    global padSize
    global ballPosition
    global ballDirection
    global level
    global stage
    gameOver = False
    t = 0
    padPosition = 4
    padSize = 3
    ballPosition = [4, 4]
    ballDirection = [1, 1]
    level = 1
    stage = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
def updatePad():
    global padPosition
    value = kit.dial.read()
    padPosition = int( (value/4095) * (16-padSize) )
def updateBall():
    global ballPosition
    ballPosition[0] += ballDirection[0]
    ballPosition[1] += ballDirection[1]
    # Constrain the ball position to the stage
    ballPosition[0] = max(ballPosition[0], 0)
    ballPosition[0] = min(ballPosition[0], 15)
    ballPosition[1] = max(ballPosition[1], 0)
    ballPosition[1] = min(ballPosition[1], 7)
def renderPad():
    for x in range(padPosition, padPosition+padSize):
        kit.set_pixel(x, 7, colors[7])
def renderBall():
    kit.set_pixel(ballPosition[0], ballPosition[1], colors[4])
def renderStage():
    for y, line in enumerate(stage):
        for x, pixel in enumerate(line):
            kit.set_pixel(x, y, colors[pixel])
def checkCollision():
    global gameOver
    global ballDirection
    global stage
    # bounce on pad
    if ballPosition[1] == 6 and (ballPosition[0] >= padPosition-1 and ballPosition[0] <= padPosition+padSize):
        # If bounce on the corners, get some extra speed
        if ballPosition[0] == padPosition-1 or ballPosition[0] == padPosition+padSize:
            if ballDirection[0] == 1 or ballDirection[0] == -1:
                ballDirection[0] *= -2
        else:
            # If bounce anywhere else, constrain the speed between -1 and 1
            ballDirection[0] = max(-1, ballDirection[0])
            ballDirection[0] = min(1, ballDirection[0])
        # vertical bounce
        ballDirection[1] *= -1
    # bounce on stage pixels
    if stage[ballPosition[1]][ballPosition[0]] != 0:
        stage[ballPosition[1]][ballPosition[0]] = 0
        ballDirection[0] *= -1
        ballDirection[1] *= -1
    else:
        # bounce on side walls
        if ballPosition[0] == 15 or ballPosition[0] == 0:
            ballDirection[0] *= -1
        # bounce on ceiling
        if ballPosition[1] == 0:
            ballDirection[1] *= -1
        # game over
        if ballPosition[1] == 7:
            gameOver = True
            ballDirection = [0, 0]
def loop():
    updatePad()
    if t % 4 == 0 and not gameOver:
        checkCollision()
        updateBall()
    renderStage()
    renderPad()
    renderBall()
def start():
    global t
    reset()
    while True:
        t += 1
        kit.set_background(colors[0])
        if gameOver and kit.button_a.value() == 0:
            reset()
        loop()
        kit.render()
        sleep(0.01)
start()
