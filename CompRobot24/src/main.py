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

con = Controller()

def yuzhen_driver():
    if controller.axis3.pressing() == True:
        Left_Motor.spin(FORWARD) 
        Left_Motor.set.velocity(75, PERCENT)
    elif controller.axis3.pressing() == True: 
        Left_Motor.spin(REVERSE)
        Left_Motor.set.velocity(75, PERCENT)
    else:
        Left_Motor.stop()
    
    if controller.axis2.pressing() == True: 
        Right_Motor.spin(FORWARD)
        Right_Motor.set.velocity(75, PERCENT)
    elif controller.axis2.pressing() == True: 
        Right_Motor.spin(REVERSE)
        Right_Motor.set.velocity(75, PERCENT)
    else: 
        Right_Motor.stop()
    pass

def jaine_drive():
    if controller.axis2.pressing() == True:
        Left_Motor.spin(FORWARD)
        Left_Motor.set.velocity(75, PERCENT)
        Right_Motor.spin(FORWARD)
        Right_Motor.set.velocity(75, PERCENT)
    elif controller.axis2.pressing() == True:
        Left_Motor.spin(REVERSE)
        Left_Motor.set.velocity(75, PERCENT)
        Right_Motor.spin(REVERSE)
        Right_Motor.set.velocity(75, PERCENT)
    else:
        Right_Motor.stop
        Left_Motor.stop()

    if controller.axis1.pressing() == True:
        Left_Motor.spin(FORWARD)
    elif controller.axis1.pressing() == True:
        Right_Motor.spin(FORWARD)
    else

    pass
        
        
