import pixelkit as kit
from time import sleep
from random import randint
from scroll import draw_letter
for i in range(0, 20):
    kit.set_background([i, i, i])
    kit.render()
for i in range(0, 20):
    kit.set_background([20-i, 20-i, 20-i])
    kit.render()
    sleep(0.005)

bgcolor = (
    randint(5, 15),
    randint(5, 15),
    randint(5, 15)
)
def invd():
    import invaders
def brko():
    import breakout
def advt():
    import adventure

def tetr():
    import tetris

def jump():
    import jumper

def meta():
    import metaballs

def shot():
    import paintershooter

def revt():
    import revertris

def pong():
    import pong

def haik():
    import haiku

def hilb():
    import hilbert

games = (
    ('invd', invd),
    ('brko', brko),
    ('advt', advt),
    ('tetr', tetr),
    ('jump', jump),
    ('meta', meta),
    ('shot', shot),
    ('revt', revt),
    ('pong', pong),
    ('haik', haik),
    ('hilb', hilb)
)

index = 0
while True:
    kit.check_controls()
    if kit.is_pressing_click:
        games[index][1]()
    if kit.is_pressing_a or kit.is_pressing_left:
        index = (index+1) % len(games)
        sleep(0.1)
    if kit.is_pressing_b or kit.is_pressing_right:
        index = (index-1) % len(games)
        sleep(0.1)
    kit.set_background(bgcolor)
    for i, c in enumerate(games[index][0]):
        draw_letter(i*4, 1, c, c=[0,0,0])
    kit.render()
    sleep(0.05)
