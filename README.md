# Raspberry-Pi-Motor-Driver-Control-with-PWM
This project demonstrates how to control the speed and direction of a DC motor using PWM (Pulse Width Modulation) with a Raspberry Pi.

🔌 Hardware Required

Raspberry Pi

Motor Driver Module (L298N / L293D)

DC Motor

External Power Supply for Motor

Jumper Wires

🔧 GPIO Pin Configuration
GPIO Pin	Connected To	Purpose
GPIO 18	ENA	PWM Speed Control
GPIO 23	IN1	Motor Direction
GPIO 24	IN2	Motor Direction
💻 Software Requirement

RPi.GPIO library (usually preinstalled)

If not:

pip install RPi.GPIO

▶ How to Run the Code
1️⃣ Save the file

Save as:

main.py

2️⃣ Connect Hardware

- ENA → GPIO 18
- IN1 → GPIO 23
- IN2 → GPIO 24

Motor connected to motor driver

Motor driver powered properly

⚠️ Do NOT power motor directly from Raspberry Pi.

3️⃣ Run on Raspberry Pi
python3 main.py

⚙️ How the Code Works
🔹 PWM Setup
pwm = GPIO.PWM(ENA, 1000)
pwm.start(0)


Creates PWM signal at 1000 Hz to control motor speed.

🔹 Motor Forward
motor_forward(speed)


IN1 = HIGH, IN2 = LOW → Motor rotates forward
Speed controlled by PWM duty cycle.

🔹 Motor Backward
motor_backward(speed)


IN1 = LOW, IN2 = HIGH → Motor rotates in reverse.

🔹 Speed Levels
a = [25, 50, 75, 100]


Motor runs at:

25% speed

50% speed

75% speed

100% speed

Each speed runs forward for 3 seconds, then backward for 3 seconds.

🛑 Stop Motor
stop()


Both direction pins LOW → Motor stops.

🔁 Automatic Cleanup

After program ends:

pwm.stop()
GPIO.cleanup()


Ensures GPIO pins reset safely.
