# increase speed when driver presses pushbutton. 

import wiringpi

# initialize
wiringpi.wiringPiSetup()

# define GPIO mode
GPIO23 = 4
GPIO24 = 5
LOW = 0
HIGH = 1
OUTPUT = 1
INPUT = 0
PULL_DOWN = 1
wiringpi.pinMode(GPIO23, OUTPUT)  # LED, row 2 col 8
wiringpi.pinMode(GPIO24, INPUT)  # push button, row 2 col 9 
wiringpi.pullUpDnControl(GPIO24, PULL_DOWN)  # pull down


# make all LEDs off
def clear_all():
    wiringpi.digitalWrite(GPIO23, LOW)

try:
    clear_all()
    while 1:
        button_state = wiringpi.digitalRead(GPIO24)
        print(button_state)
        if button_state == 1:
            wiringpi.digitalWrite(GPIO23, HIGH)
            print("Speed increased!")
            increaseSpeed = 1
        else:
            wiringpi.digitalWrite(GPIO23, LOW)

        wiringpi.delay(20)

except KeyboardInterrupt:
    clear_all()

print("done")