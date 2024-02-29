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

def Primary_joystick():
    pos1 = con.axis1.position()
    pos2 = con.axis2.position()
    Leftspeed = abs(pos1)
    Rightspeed = abs(pos2)
    Left_group.set_velocity(speed, PERCENT)
    Right_group.set_velocity(speed, PERCENT)
    Left_group.spin(FORWARD)
    Right_group.spin(REVERSE)


def Primary_control():
    while True:
        if con.buttonR1.pressing() == True:
            Intake.set_velocity(75, PERCENT)
            Intake.spin(FORWARD)
        elif con.buttonL1.pressing() == True:
            Intake.set_velocity(75, PERCENT)
            Intake.spin(REVERSE)
        else:
            Intake.stop
        if con.buttonR2.pressing() == True:
            Climbing_system.set_velocity(100, PERCENT)
            Climbing_system.spin(FORWARD)
        elif con.buttonL2.pressing() == True:
            Climbing_system.set_velocity(100, PERCENT)
            Climbing_system.spin(REVERSE)
        else:
            Climbing_system.stop
        if con.axis1.position() >= 5:
            Right_group.spin(FORWARD)
        elif con.axis1.position() <= -5:
            Left_group.spin(FORWARD)
        else:
            Left_group.stop
            Right_group.stop
        if con.axis3.position() >= 5:
            Right_group.spin(FORWARD)
            Left_group.spin(FORWARD)
        elif con.axis3.position() <= -5:
            Right_group.spin(REVERSE)
            Left_group.spin(REVERSE)
        else:
            Left_group.stop
            Right_group.stop

    pass
    
       
        
