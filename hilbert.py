import pixelkit as kit
from time import sleep
h = []
def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h*6.0) # XXX assume int() truncates!
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i%6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q
    # Cannot get here
def hilbert(x0, y0, xi, xj, yi, yj, n):
    if n <= 0:
        X = (x0 + (xi + yi) / 2)
        Y = (y0 + (xj + yj) / 2)
        h.append((int(X), int(Y)))
    else:
        hilbert(x0, y0, yi / 2, yj / 2, xi / 2, xj / 2, n - 1)
        hilbert(x0 + xi / 2, y0 + xj / 2, xi / 2, xj / 2, yi / 2, yj / 2, n - 1)
        hilbert(x0 + xi / 2 + yi / 2, y0 + xj / 2 + yj / 2, xi / 2, xj / 2, yi / 2, yj / 2, n - 1)
        hilbert(x0 + xi / 2 + yi, y0 + xj / 2 + yj, -yi / 2, -yj / 2, -xi / 2, -xj / 2, n - 1)
hilbert(0.0, 0.0, 8, 0, 0, 8, 3)
kit.clear()
kit.render()
def get_color(i):
    return [
        int(hsv_to_rgb(i, 1, 1)[0]*20),
        int(hsv_to_rgb(i, 1, 1)[1]*20),
        int(hsv_to_rgb(i, 1, 1)[2]*20)
    ]
counter = 0
interval = 0.05
while True:
    for p in h:
        counter += 0.95
        c = get_color( (counter%len(h)) / len(h) )
        kit.set_pixel(7-p[0], 7-p[1], c)
        kit.render()
        sleep(interval)
    for p in h:
        counter += 1
        c = get_color( (counter%len(h)) / len(h) )
        kit.set_pixel(8+p[0], p[1], c)
        kit.render()
        sleep(interval)
