from motor import MotorController
from servo import Servo
from ultrasonic import UltrasonicSensor
import time

#Initialize the components
motor = MotorController()
servo = Servo()
ultrasonic = UltrasonicSensor()

def scan_directions():
    # Look straight
    servo.move(90)
    time.sleep(1)
    straight_distance = ultrasonic.measure_distance()
    print(f"Straight distance: {straight_distance} cm")

    # Look left
    servo.move(180)
    time.sleep(1)
    left_distance = ultrasonic.measure_distance()
    print(f"Left distance: {left_distance} cm")

    # Look right
    servo.move(0)
    time.sleep(1)
    servo.move(90)  # move back to the original position to simulate looking "right" correctly
    time.sleep(1)
    right_distance = ultrasonic.measure_distance()
    print(f"Right distance: {right_distance} cm")

    # Decide the direction based on the maximum distance measured
    #always go straight if possible. Otherwise pick one w more
    #if L and R are =, then go L.
    
    if straight_distance > 20:
        return 'forward'
    elif left_distance >= right_distance:
        return 'left'
    elif right_distance > left_distance:
        return 'right'

def navigate():
    while True:
        servo.move(90)
        distance = ultrasonic.measure_distance()
        print(f"Detected distance: {distance} cm")
        
        if distance < 20:
            motor.stop()#no delay on stopping.
            direction = scan_directions()
            
            if direction == 'left':
                motor.turn_left(0.4)#delay 0.7 to let motors turn a bit.
            elif direction == 'right':
                motor.turn_right(0.4)
            else:
                print("im in nested forward")
                motor.move_forward(0)
        else:
            motor.move_forward(0)

if __name__ == "__main__":
    navigate()
