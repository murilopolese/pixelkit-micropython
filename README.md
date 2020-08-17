# MicroPython + PixelKit = <3

Kano has killed the PixelKit but the dream still lives in my heart!

Here is a growing collection of MicroPython games, demos and other fun programs I wrote for PixelKit.

I made them using my very own experimental code editor: [Fabulous Flying Machine](https://github.com/murilopolese/fabulous-flying-machine). I don't blame you if you don't want to use Fabulous Flying Circus. You can always rely on the much better [MuEditor](https://codewith.mu/). By the time I write this, you might install Mu via `pip` to get the ESP8266/ESP32 mode (PixelKit runs on an ESP32!).

For this collection of games I chose to turn wifi and `webrepl` off but go ahead and connect to your wifi for maximum fun. You can follow [this tutorial](https://learn.adafruit.com/micropython-basics-esp8266-webrepl/access-webrepl) or install the prototype I made for Kano: [Pixel32](https://github.com/murilopolese/kano-pixel-kit-pixel32). If you go for Pixel32, pay attention that the `pixelkit.py` library in one project is different than the other. This will give you some headache.

The `main.py` file contains a very simple menu system for you to browse the installed games. It does not detect anything automatically, you have to add or edit the game array with the games, you can do it!

If you make a new game, I'd love to play it :)
