blockI = [
[
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
],
[
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
]

blockS = [
[
    [0, 1, 1],
    [1, 1, 0],
    [0, 0, 0]
],
[
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0]
]
]


blockZ = [
[
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 0]
],
[
    [0, 0, 1],
    [0, 1, 1],
    [0, 1, 0]
]
]

blockL = [
[
    [1, 0, 0],
    [1, 0, 0],
    [1, 1, 0]
],
[
    [0, 0, 0],
    [0, 0, 1],
    [1, 1, 1]
],
[
    [0, 1, 1],
    [0, 0, 1],
    [0, 0, 1]
],
[
    [1, 1, 1],
    [1, 0, 0],
    [0, 0, 0]
]
]

blockJ = [
[
    [0, 0, 1],
    [0, 0, 1],
    [0, 1, 1]
],
[
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 0]
],
[
    [1, 1, 0],
    [1, 0, 0],
    [1, 0, 0]
],
[
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 1]
],
]

blockT = [
[
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
],
[
    [0, 1, 0],
    [1, 1, 0],
    [0, 1, 0]
],
[
    [0, 0, 0],
    [1, 1, 1],
    [0, 1, 0]
],
[
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0]
],
]

blockO = [
[
    [1, 1],
    [1, 1]
]
]

blocks = [blockI, blockS, blockZ, blockL, blockJ, blockT, blockO]
import pixelKit as kit
from random import randint
from time import sleep
res = 50
w = 8
h = 16
colors = [
    (0, 0, 0),
    (255, 0, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 255, 255),
    (0, 0, 255),
    (255, 0, 255)
]
# [0]*8 is a shortcut to [0, 0, 0, 0, 0, 0, 0, 0]
stage = [
    [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8,
    [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8
]
def setPixel(x, y, c):
    _c = (int(c[0]/10), int(c[1]/10), int(c[2]/10))
    kit.set_pixel(15-y, x, _c)
def drawStage():
    for y, sLine in enumerate(stage):
        for x, value in enumerate(sLine):
            if value != 0:
                setPixel(x, y, colors[value])
def drawBlock(px, py, block):
    for y, bLine in enumerate(block):
        for x, value in enumerate(bLine):
            if value == 1:
                setPixel(px+x, py+y, colors[currentColor])
def checkWallCollision(px, py, block):
    for y, bLine in enumerate(block):
        for x, value in enumerate(bLine):
            if value == 1:
                nx = px+x
                if nx < 0:
                    raise Exception('Hit left wall')
                if nx >= w:
                    raise Exception('Hit right wall')
def checkFloorCollision(px, py, block):
    for y, bLine in enumerate(block):
        for x, value in enumerate(bLine):
            if value == 1:
                ny = py+y
                if ny >= h:
                    raise Exception('Hit floor')
def checkStageCollision(px, py, block):
    for y, bLine in enumerate(block):
        for x, value in enumerate(bLine):
            if value == 1:
                nx = px+x
                ny = py+y
                if stage[ny][nx] != 0:
                    raise Exception('Hit stage')
def clearLines():
    for y, sLine in enumerate(stage):
        count = 0
        # count how many blocks in the line
        for value in sLine:
            if value != 0:
                count += 1
        # if line is filled
        if count == 8:
            # remove the line
            del stage[y]
            # prepend an emtpy line
            stage.insert(0, [0]*8)
def newBlock():
    global currentBlock
    global currentRotation
    global currentColor
    global posX
    global posY
    global gameOver
    posX = 3
    posY = 0
    currentBlock = randint(0, len(blocks)-1)
    currentRotation = randint(0, len(blocks[currentBlock])-1)
    currentColor = randint(1, len(colors)-1)
    try:
        checkStageCollision(posX, posY, blocks[currentBlock][currentRotation])
    except Exception as e:
        print(e)
        stamp(posX, posY, blocks[currentBlock][currentRotation])
        gameOver = True
def stamp(px, py, block):
    global stage
    for y, bLine in enumerate(block):
        for x, value in enumerate(bLine):
            if value:
                stage[py+y][px+x] = currentColor
def moveDown(b):
    global posY
    try:
        nY = posY + 1
        checkFloorCollision(posX, nY, b)
        checkStageCollision(posX, nY, b)
        posY = nY
        return True
    except Exception as e:
        print(e)
        stamp(posX, posY, b)
        sleep(0.2)
        clearLines()
        newBlock()
        return False

gameOver = False
t = 0
posX = 3
posY = -1
debounceButton = False
currentBlock = 0
currentRotation = 0
currentColor = 0
key_up = False
key_down = False
key_left = False
key_right = False
key_pressed = key_up or key_down or key_left or key_right
def setup():
    global stage
    global gameOver
    stage = [
        [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8,
        [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8
    ]
    gameOver = False
    newBlock()

def draw():
    global posY
    global posX
    global debounceButton
    global key_up
    global key_down
    global key_left
    global key_right

    kit.check_controls()
    key_up = kit.joystick_right.value() == 0
    key_down = kit.joystick_left.value() == 0
    key_left = kit.joystick_up.value() == 0
    key_right = kit.joystick_down.value() == 0
    key_pressed = key_up or key_down or key_left or key_right

    if not gameOver:
        global t
        t += 1
        kit.set_background(colors[0])

        if key_pressed and not debounceButton:
            debounceButton = True
            controls()
        if not key_pressed:
            debounceButton = False

        b = blocks[currentBlock][currentRotation]
        drawStage()
        drawBlock(posX, posY, b)

        if t % 10 == 0:
            moveDown(b)
    else:
        drawStage()
        if kit.joystick_click.value() == 0:
            setup()

    kit.render()
    sleep(0.1)
def controls():
    global posX
    global posY
    global currentRotation

    if key_left:
        try:
            b = blocks[currentBlock][currentRotation]
            checkWallCollision(posX-1, posY, b)
            checkStageCollision(posX-1, posY, b)
            posX -= 1
        except Exception as e:
            print(e)
    if key_right:
        try:
            b = blocks[currentBlock][currentRotation]
            checkWallCollision(posX+1, posY, b)
            checkStageCollision(posX+1, posY, b)
            posX += 1
        except Exception as e:
            print(e)
    if key_up:
        try:
            r = (currentRotation + 1) % len(blocks[currentBlock])
            b = blocks[currentBlock][r]
            checkWallCollision(posX, posY, b)
            checkStageCollision(posX, posY, b)
            currentRotation = r
        except Exception as e:
            print(e)
    if key_down:
        b = blocks[currentBlock][currentRotation]
        while moveDown(b):
            sleep(0.01)
# Start runtime
setup()
while True:
    draw()
