# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       ameer                                                        #
# 	Created:      1/30/2024, 4:15:02 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello V5")
controller = Controller(PRIMARY)
con2 = Controller(PARTNER)
Left_Motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True) 
Right_Motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True) 
Intake = Motor(Ports.PORT6, GearSetting.RATIO_6_1, True)
Catapult = Motor(Ports.PORT8, GearSetting.RATIO_36_1, True)

def main():

    pass


def preauto():
    pass

def automonus():



    pass




def primary_joysticks():
    axis3 = controller.axis3.position()
    axis4 = controller.axis4.position()
    total = axis3 + axis4
    more_total = axis3 - axis4
    if abs(total) > 5: 
        Left_Motor.set.velocity(total, PERCENT)
        Left_Motor.spin(FORWARD)
        Right_Motor.set.velocity(more_total, PERCENT)
        Right_Motor.spin(FORWARD)
        

def primary_driver():
    while True:
        primary_joysticks()
        if controller.axis3.position() == -100: 
            Left_Motor.spin(REVERSE)
            Left_Motor.set.velocity(75, PERCENT)
        else:
            Left_Motor.stop()
        
        if controller.axis2.position() == True: 
            Right_Motor.spin(FORWARD)
            Right_Motor.set.velocity(75, PERCENT)
        elif controller.axis2.position() == True: 
            Right_Motor.spin(REVERSE)
            Right_Motor.set.velocity(75, PERCENT)
        else: 
            Right_Motor.stop()
        pass

def Partner_joystick():
    axis2 = con2.axis2.position()
    axis1 = con2.axis1.position()
    leftsped = axis2 - axis1
    rightsped = axis2 + axis1

    Left_Motor.set_velocity(leftsped, PERCENT)
    Right_Motor.set_velocity(rightsped, PERCENT)
    Left_Motor.spin(FORWARD); Right_Motor.spin(FORWARD)

    pass


def Partner_control():
    

    pass
        


        

        
