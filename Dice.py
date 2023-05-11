import machine
import utime
import urandom

# Define the built-in LED
led = machine.Pin(25, machine.Pin.OUT)

# Function to blink the LED
def blink_led(times):
    for i in range(times):
        led.value(1)
        utime.sleep(1)
        led.value(0)
        utime.sleep(1)

# Function to roll the dice
def roll_dice():
    roll = urandom.randint(1, 6)
    print("Rolled: ", roll)
    blink_led(roll)

# Roll the dice every 5 seconds
while True:
    roll_dice()
    utime.sleep(5)
