from scroll import scroll
from time import sleep
from random import randint
messages = (
'your file was so big.      it might be very useful.      but now it is gone.',
'the web site you seek      cannot be located, but      countless more exist.',
'chaos reigns within.      reflect, repent, and reboot.      order shall return.',
'program aborting:      close all that you have worked on.      you ask far too much.',
'first snow, then silence.      this thousand-dollar screen dies      so beautifully.',
'the tao that is seen      is not the true tao-until      you bring fresh toner.',
'stay the patient course.      of little worth is your ire.      the network is down.',
'a crash reduces      your expensive computer      to a simple stone.',
'three things are certain:      death, taxes and lost data.      guess which has occurred.',
'you step in the stream,      but the water has moved on.      this page is not here.',
'out of memory.      we wish to hold the whole sky,      but we never will.',
'having been erased,      the document you’re seeking      must now be retyped.',
'serious error.      all shortcuts have disappeared.      screen. mind. both are blank.'
)
colors = [
    [10, 0, 0], [0, 10, 0], [0, 0, 10],
    [10, 10, 0], [10, 0, 10], [0, 10, 10]
]
bgcolors = [
    [5, 0, 0], [0, 5, 0], [0, 0, 5],
    [5, 5, 0], [5, 0, 5], [0, 5, 5]
]
while True:
    c = randint(0, len(colors)-1)
    b = (c + randint(1, len(colors))) % len(colors)
    msg = messages[randint(0, len(messages)-1)]
    scroll(msg, color=colors[c], background=bgcolors[b])
    sleep(10)
