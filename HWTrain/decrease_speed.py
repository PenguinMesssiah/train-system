# decrease speed when driver presses push button.

import wiringpi

# initialize
wiringpi.wiringPiSetup()

# define GPIO mode
GPIO17 = 4
GPIO27 = 5
LOW = 0
HIGH = 1
OUTPUT = 1
INPUT = 0
PULL_DOWN = 1
wiringpi.pinMode(GPIO17, OUTPUT)  # LED, row 1 col 6
wiringpi.pinMode(GPIO27, INPUT)  # push button, row 1 col7
wiringpi.pullUpDnControl(GPIO27, PULL_DOWN)  # pull down


# make all LEDs off
def clear_all():
    wiringpi.digitalWrite(GPIO17, LOW)

try:
    clear_all()
    while 1:
        button_state = wiringpi.digitalRead(GPIO27)
        print(button_state)
        if button_state == 1:
            wiringpi.digitalWrite(GPIO17, HIGH)
            print("Speed decreased!")
            decreaseSpeed = 1
        else:
            wiringpi.digitalWrite(GPIO17, LOW)

        wiringpi.delay(20)

except KeyboardInterrupt:
    clear_all()

print("done")