import RPi.GPIO as GPIO
import time

# Pin setup
ENA = 18   # PWM pin
IN1 = 23
IN2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Setup PWM on ENA at 1000Hz
pwm = GPIO.PWM(ENA, 1000)
pwm.start(0)  # Start with 0% speed

def motor_forward(speed):
    GPIO.output(IN1, True) # you can also use GPIO.HIGH
    GPIO.output(IN2, False) # you can also use GPIO.LOW
    pwm.ChangeDutyCycle(speed)

def motor_backward(speed):
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    pwm.ChangeDutyCycle(speed)

def stop():
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)

# In list form
a = [25, 50, 75, 100]
try:
    for i in a:
        print(i,"Speed")
        motor_forward(i)
        time.sleep(3)
        motor_backward(i)
        time.sleep(3)
        stop()
        time.sleep(1)   

finally:
    pwm.stop()
    GPIO.cleanup()
