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

brain=Brain()

brain.screen.print("Hello V5")
con = Controller(PRIMARY)
con2 = Controller(PARTNER)
Leftfront_Motor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
Leftback_Motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True) 
Rightfront_Motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
Rightback_Motor = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True) 
Intake = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
Climbing_system = Motor(Ports.PORT3, GearSetting.RATIO_36_1, True)
Left_group = MotorGroup(Leftback_Motor, Leftfront_Motor)
Right_group = MotorGroup(Rightback_Motor, Rightfront_Motor)

def main():

    pass


def preauto():
    pass

def automonus():



    pass


def primary_joysticks():
    axis3 = con.axis3.position()
    axis4 = con.axis4.position()
    total = axis3 + axis4
    more_total = axis3 + axis4
    if abs(total) > 5: 
        Left_group.set_velocity(total, PERCENT)
        Left_group.spin(FORWARD)
        Right_group.set_velocity(more_total, PERCENT)
        Right_group.spin(FORWARD)
        

def primary_driver():
    while True:
        primary_joysticks()
        if controller.axis3.position() == -100: 
            Left_Motor.spin(REVERSE)
            Left_Motor.set_velocity(75, PERCENT)
        else:
            Left_Motor.stop()
        
        if controller.axis2.position() == True: 
            Right_Motor.spin(FORWARD)
            Right_Motor.set_velocity(75, PERCENT)
        elif controller.axis2.position() >= 50: 
            Right_Motor.spin(REVERSE)
            Right_Motor.set_velocity(75, PERCENT)
        else: 
            Right_Motor.stop()

def Partner_joystick():
    axis2 = con2.axis2.position()
    axis1 = con2.axis1.position()
    leftsped = axis2 - axis1
    rightsped = axis2 + axis1

    Left_group.set_velocity(leftsped, PERCENT)
    Right_group.set_velocity(rightsped, PERCENT)
    Left_group.spin(FORWARD); Right_group.spin(REVERSE)


def Partner_control():
    while True:
        if con.buttonR1.pressing() == True:
            Intake.set_velocity(75, PERCENT)
            Intake.spin(FORWARD)
        elif con.buttonL1.pressing() == True:
            Intake.set_velocity(75, PERCENT)
            Intake.spin(REVERSE)
        else():
            Intake.stop
        if con.buttonR2.pressing() == True:
            Climbing_system.set_velocity(100, PERCENT)
            Climbing_system.spin(FORWARD)
        elif con.buttonL2.pressing() == True:

    pass
    
       


        

        
