import time
import board
import digitalio
import usb_hid

# For English keyboard
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# For Spanish keyboard
# https://github.com/Neradoc/Circuitpython_Keyboard_Layouts
# from keycode_win_es import Keycode
# from keyboard_layout_win_es import KeyboardLayout

import busio
import displayio
import adafruit_displayio_sh1107
import adafruit_imageload
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

# Use for SPI
oled_clk = board.GP10
oled_din = board.GP11
oled_cs = board.GP9
oled_dc = board.GP8
oled_res = board.GP12

spi = busio.SPI(oled_clk, oled_din)
display_bus = displayio.FourWire(
    spi, command=oled_dc, chip_select=oled_cs, reset=oled_res
)

# Resolution
WIDTH = 128
HEIGHT = 64

display = adafruit_displayio_sh1107.SH1107(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Create icon
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
color = 0xFFFFFF


def display_password():
    splash = displayio.Group()
    display.root_group = splash
    # Create the tet label
    text_area = label.Label(font, text="***", color=color)
    # Set the location
    text_area.x = 20
    text_area.y = 25
    splash.append(text_area)


def display_pin():
    splash = displayio.Group()
    display.root_group = splash
    # Create the tet label
    text_area = label.Label(font, text="123", color=color)
    # Set the location
    text_area.x = 20
    text_area.y = 27
    splash.append(text_area)


def init():
    while True:
        if not btn1.value:
            write_text(password)
            press_enter()
            display_password()
        if not btn2.value:
            write_text(pin)
            press_enter()
            display_pin()
