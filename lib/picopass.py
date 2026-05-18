import board
import digitalio
import time
import usb_hid

# English keyboard
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Spanish keyboard
# https://github.com/Neradoc/Circuitpython_Keyboard_Layouts
# from keyboard_layout_win_es import KeyboardLayout
# from keycode_win_es import Keycode

import adafruit_displayio_sh1107
import adafruit_imageload
import busio
import displayio
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label

# Set Keyboard
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# Set buttons for Pico-OLED-1.3
btn1 = digitalio.DigitalInOut(board.GP15)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(board.GP17)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

# Set password and pin
password = "password"
pin = "pin"


def press_enter():
    kbd.send(Keycode.ENTER)
    time.sleep(0.1)


def write_text(text):
    layout.write(text)
    time.sleep(0.1)


# Release any currently configured displays
displayio.release_displays()

# Configure SPI
oled_clk = board.GP10
oled_din = board.GP11
oled_cs = board.GP9
oled_dc = board.GP8
oled_res = board.GP12

spi = busio.SPI(oled_clk, oled_din)
display_bus = displayio.FourWire(
    spi, command=oled_dc, chip_select=oled_cs, reset=oled_res
)

# Set Resolution
WIDTH = 128
HEIGHT = 64

display = adafruit_displayio_sh1107.SH1107(display_bus, width=WIDTH, height=HEIGHT)

# Make display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Load icon
bitmap, palette = adafruit_imageload.load(
    "/icon.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette
)

# Make the color at index 0 show as transparent
palette.make_transparent(0)

# Create a TileGrid to hold the bitmap icon
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette, x=32, y=0)

splash.append(tile_grid)

# Set font and color
font = bitmap_font.load_font("/spleen-32x64.bdf")
text_color = 0xFFFFFF


def display_code(code, location_x, location_y):
    splash = displayio.Group()
    display.root_group = splash

    # Create text label
    text_area = label.Label(font, text=code, color=text_color)

    # Set location
    text_area.x = location_x
    text_area.y = location_y
    splash.append(text_area)


def init():
    while True:
        if not btn1.value:
            write_text(password)
            press_enter()
            display_code("***", 20, 25)
        if not btn2.value:
            write_text(pin)
            press_enter()
            display_code("123", 20, 27)
