from machine import Pin, PWM

class Servo:
    # Defaults for the TowerPro SG90
    __servo_pwm_freq = 50
    __min_u16_duty = 1638  # Fine-tuned for SG90
    __max_u16_duty = 7864  # Fine-tuned for SG90
    min_angle = 0
    max_angle = 180
    current_angle = None  # Updated to None to force initial movement
    __pin_number = 16  # Predefined pin number

    def __init__(self):
        self.__initialise()

    def update_settings(self, servo_pwm_freq, min_u16_duty, max_u16_duty, min_angle, max_angle):
        self.__servo_pwm_freq = servo_pwm_freq
        self.__min_u16_duty = min_u16_duty
        self.__max_u16_duty = max_u16_duty
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.__initialise()

    def move(self, angle):
        angle = max(min(angle, self.max_angle), self.min_angle)  # Constrain angle to valid range
        angle = round(angle, 2)  # Round to reduce jitter

        if angle == self.current_angle:
            return  # No movement needed if the angle is unchanged

        self.current_angle = angle
        duty_u16 = self.__angle_to_u16_duty(angle)
        self.__motor.duty_u16(duty_u16)

    def __angle_to_u16_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u16_duty

    def __initialise(self):
        self.__angle_conversion_factor = (self.__max_u16_duty - self.__min_u16_duty) / (self.max_angle - self.min_angle)
        self.__motor = PWM(Pin(self.__pin_number))  # Use the predefined pin
        self.__motor.freq(self.__servo_pwm_freq)
        self.move(0)  # Ensures servo starts at 0 degrees
