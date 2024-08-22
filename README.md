# picopass

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

USB dongle for authentication using Circuitpython

# Requirements

- [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico)
- [Pico OLED 1.3 display module](https://www.waveshare.com/wiki/Pico-OLED-1.3)

# Getting Started

[Download](https://circuitpython.org/downloads) and [install](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython) CircuitPython on the board

Also install:

- [Adafruit_CircuitPython_HID](https://github.com/adafruit/Adafruit_CircuitPython_HID)
- [Adafruit_CircuitPython_DisplayIO_SH1107](https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SH1107)
- [Adafruit_CircuitPython_ImageLoad](https://github.com/adafruit/Adafruit_CircuitPython_ImageLoad)
- [Adafruit_CircuitPython_Bitmap_Font](https://github.com/adafruit/Adafruit_CircuitPython_Bitmap_Font)
- [Adafruit_CircuitPython_Display_Text](https://github.com/adafruit/Adafruit_CircuitPython_Display_Text)

Optional:

Install [Circuitpython_Keyboard_Layouts](https://github.com/Neradoc/Circuitpython_Keyboard_Layouts) for international keyboards

Change the variables inside picopass.py:
```
password = "password"
pin = "pin"
```

You can also use [mpy-cross](https://learn.adafruit.com/welcome-to-circuitpython/frequently-asked-questions#how-can-i-create-my-own-mpy-files-3020687-11) to turn picopass.py into a .mpy file

To make your own icon you can use this [tutorial.](https://learn.adafruit.com/creating-your-first-tilemap-game-with-circuitpython/indexed-bmp-graphics)

# Usage

Connect the USB and just press one of the buttons

# Credits

Thanks to fcambus for the awesome [font](https://github.com/fcambus/spleen)
