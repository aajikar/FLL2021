from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class RobotFLL2021(DriveBase):
    
    def __init__(self, left_motor=Motor(Port.B), right_motor=Motor(Port.C),
                 wheel_diameter=0, axle_track=0, module1=None, module2=None,
                 module3=None, touch_sensor=None, infrared=None, ultrasound=None):
        super().__init__(left_motor, right_motor, wheel_diameter, axle_track)
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.module1 = module1
        self.module2 = module2
        self.module3 = module3
        self.touch_sensor = touch_sensor
        self.infrared = infrared
        self.ultrasound = ultrasound
        
    def drive_square(self, length):
        for _ in range(4):
            self.straight(length)
            self.turn(90)
        self.turn(90)
        return None
    
    # Drive forward until touch sensors gets pressed
    def drive_until_touch(self):
        while  not self.touch_sensor.pressed():
            # Drive forward forever
            self.drive(drive_speed=30, turn_rate=30)
        return None
    
    def drive_until_object_detected(self, stopping_distance=30, drive_speed=30, turn_rate=30):
        while self.ultrasound.distance() >= stopping_distance:
            self.drive(drive_speed=drive_speed, turn_rate=turn_rate)
        return None

    def mission1(self):
        # Drive forward until you see and object then turn right, drive 15cm the drive in square
        # Drive forward until 15cm away from obstacle
        self.drive_until_object_detected(stopping_distance=150)
        # Turn RIGHT (-90) deg
        self.turn(-90)
        # Drive straight for 15cm
        self.straight(150)
        # Drive in square of length 30cm
        self.drive_square(300)
        self.beep()
        return None


robot1 = RobotFLL2021(wheel_diameter=152, axle_track=52, touch_sensor=TouchSensor(Port.1), infrared=InfraredSensor(Port.2))

robot1.mission1()
