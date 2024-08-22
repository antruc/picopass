import storage
import board, digitalio

btn1 = digitalio.DigitalInOut(board.GP15)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

# Disable devices only if button is not pressed.
if btn1.value:
   storage.disable_usb_drive()
