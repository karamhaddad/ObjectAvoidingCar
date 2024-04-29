from machine import Pin
import utime

class UltrasonicSensor:
    def __init__(self):
        self.trigger = Pin(10, Pin.OUT)  # Update to GP10 for trigger
        self.echo = Pin(11, Pin.IN)      # Update to GP11 for echo

    def measure_distance(self):
        self.trigger.low()
        utime.sleep_us(2)
        self.trigger.high()
        utime.sleep_us(5)
        self.trigger.low()

        while self.echo.value() == 0:
            signaloff = utime.ticks_us()

        while self.echo.value() == 1:
            signalon = utime.ticks_us()

        timepassed = utime.ticks_diff(signalon, signaloff)
        distance = (timepassed * 0.0343) / 2  # Calculate distance in cm
        return distance
