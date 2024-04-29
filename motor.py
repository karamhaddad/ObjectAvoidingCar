from machine import Pin
import time

class MotorController:
    def __init__(self):
        # Motor A
        self.In1 = Pin(7, Pin.OUT)
        self.In2 = Pin(6, Pin.OUT)
        self.EN_A = Pin(8, Pin.OUT)
        
        # Motor B
        self.In3 = Pin(4, Pin.OUT)
        self.In4 = Pin(3, Pin.OUT)
        self.EN_B = Pin(2, Pin.OUT)

        # Enable motors
        self.EN_A.high()
        self.EN_B.high()

    def move_forward(self,delay):
        self.In1.high()
        self.In2.low()
        self.In3.high()
        self.In4.low()
        print("Moving Forward")

    def move_backward(self,delay):
        self.In1.low()
        self.In2.high()
        self.In3.low()
        self.In4.high()
        print("Moving Backward")

    def turn_right(self,delay):
        self.In1.low()
        self.In2.low()
        self.In3.low()
        self.In4.high()
        print("Turning Right")
        time.sleep(delay) #I added the delay to keep it exclusive to left and right in main

    def turn_left(self,delay):
        self.In1.low()
        self.In2.high()
        self.In3.low()
        self.In4.low()
        print("Turning Left")
        time.sleep(delay) #delay only for left and right

    def stop(self):
        self.In1.low()
        self.In2.low()
        self.In3.low()
        self.In4.low()
        print("Stopping")
