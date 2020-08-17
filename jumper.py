import PixelKit as kit
from time import sleep
t = 0
colors = [
    [1, 2, 3], #0 - background
    [10, 0, 0], #1 - red
    [10, 10, 0], #2 - yellow
    [0, 10, 0], #3 - green
    [0, 10, 10], #4 - cyan
    [0, 0, 10], #5 - blue
    [10, 0, 10], #6 - purple
    [10, 10, 10] #7 - white
]
charSprite = [
    [
        [0, 2, 3, 3],
        [3, 3, 1, 1],
        [3, 3, 3, 3],
        [3, 0, 0, 3]
    ],
    [
        [0, 2, 3, 3],
        [3, 3, 1, 1],
        [3, 3, 3, 3],
        [0, 0, 0, 3]
    ],[
        [0, 2, 3, 3],
        [3, 3, 1, 1],
        [3, 3, 3, 3],
        [3, 0, 0, 3]
    ],
    [
        [0, 2, 3, 3],
        [3, 3, 1, 1],
        [3, 3, 3, 3],
        [3, 0, 0, 0]
    ]
]
charPosition = 3
obstaclePosition = 14
level = 1
gameOver = False
sky = [
    [0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 7, 7],
    [0, 7, 7, 0, 0, 0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0],
    [7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 0, 0]
]
def reset():
    global charPosition
    global obstaclePosition
    global level
    global gameOver
    charPosition = 3
    obstaclePosition = 14
    level = 1
    gameOver = False
def renderFloor():
    for x in range(0, 16):
        kit.set_pixel(x, 7, colors[5])
def renderSky():
    i = int(t/2)
    for y, line in enumerate(sky):
        for x, pixel in enumerate(line):
            kit.set_pixel(x, y, colors[sky[y][(x+i)%16]])
def renderObstacle():
    n = int(obstaclePosition)
    kit.set_pixel(n, 6, colors[6])
    kit.set_pixel(n, 5, colors[6])
    kit.set_pixel(n+1, 6, colors[6])
    kit.set_pixel(n+1, 5, colors[6])
def moveObstacle():
    global obstaclePosition
    global level
    obstaclePosition -= (level/4)
    if obstaclePosition < 0:
        obstaclePosition = 14
        level += 0.1
def renderCharacter():
    i = int(t/4)%len(charSprite)
    for y, line in enumerate(charSprite):
        for x, pixel in enumerate(line):
            ny = int(charPosition) + y
            kit.set_pixel(x, ny, colors[charSprite[i][y][x]])
def jump():
    global charPosition
    if int(charPosition) >= 3 and kit.is_pressing_a:
        charPosition = 0
    elif int(charPosition) < 3:
        charPosition += level/6
        if charPosition > 3:
            charPosition = 3
def checkCollision():
    global gameOver
    no = int(obstaclePosition)
    if no <= 3 and no >= 2 and int(charPosition) >= 3:
        gameOver = True
def loop():
    if not gameOver:
        moveObstacle()
        renderObstacle()
        jump()
        checkCollision()
    renderFloor()
    renderSky()
    renderCharacter()
    if gameOver:
        for i in range(0, int(level*2)):
            kit.set_pixel(i%16, int(i/16), colors[4])
        if kit.is_pressing_b:
            reset()
def start():
    global t
    global level
    while True:
        t = t + level
        kit.check_controls()
        kit.set_background(colors[0])
        loop()
        kit.render()
    sleep(0.01)
start()
