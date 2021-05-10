import RPi.GPIO as GPIO
import time
control = [10,5, 10]
servo = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)

p = GPIO.PWM(servo, 50)
p.start(2.5)

try:
       while True:
           for x in range(3):
             p.ChangeDutyCycle(control[x])
             time.sleep(1)
             print(x)
except KeyboardInterrupt:
    GPIO.cleanup()
