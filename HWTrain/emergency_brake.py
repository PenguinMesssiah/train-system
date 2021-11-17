# decrease speed when driver presses push button.

import wiringpi

# initialize
wiringpi.wiringPiSetup()

# define GPIO mode
GPIO5 = 4
GPIO6 = 5
LOW = 0
HIGH = 1
OUTPUT = 1
INPUT = 0
PULL_DOWN = 1
wiringpi.pinMode(GPIO5, OUTPUT)  # LED, row 1 col 6
wiringpi.pinMode(GPIO6, INPUT)  # push button, row 1 col7
wiringpi.pullUpDnControl(GPIO6, PULL_DOWN)  # pull down


# make all LEDs off
def clear_all():
    wiringpi.digitalWrite(GPIO5, LOW)

try:
    clear_all()
    while 1:
        button_state = wiringpi.digitalRead(GPIO6)
        print(button_state)
        if button_state == 1:
            wiringpi.digitalWrite(GPIO5, HIGH)
            print("Emergency brake pulled!")
            decreaseSpeed = 1
            emergBrake = 1
        else:
            wiringpi.digitalWrite(GPIO5, LOW)

        wiringpi.delay(20)

except KeyboardInterrupt:
    clear_all()

print("done")