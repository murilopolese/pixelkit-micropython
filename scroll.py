from time import sleep
import pixelkit as kit
from scroll_letters import letters
from scroll_numbers import numbers
from scroll_symbols import symbols
charset = {}
charset.update(letters)
charset.update(numbers)
charset.update(symbols)
en = enumerate
white = [10, 10, 10]
def draw_letter(x, y, l, c=white):
  if not str(l) in charset.keys():
    pass
  for ly, line in en(charset[l]):
    for lx, value in en(line):
      if value != 0:
        kit.set_pixel(x+lx, y+ly, c)
def buff_phrase(phrase='', offset=0, c=white):
  buff = [[0]*16, [0]*16, [0]*16,
          [0]*16, [0]*16]
  for l in phrase:
    if str(l) in charset.keys():
      for ly, line in en(charset[l]):
        for value in line:
          buff[ly].append(value)
        buff[ly].append(0)
  return buff
def draw_buff(buff, o=0, c=white):
  for x in range(0, 16):
    for y in range(0, 5):
      try:
        if buff[y][o+x] != 0:
          kit.set_pixel(x, 1+y, c)
      except Exception as e:
        pass
def scroll(p, color=white, background=[0,0,0], interval=0.1):
  buff = buff_phrase(p)
  for i in range(0, len(buff[0])):
    kit.set_background(background)
    draw_buff(buff, i, color)
    kit.render()
    sleep(interval)
