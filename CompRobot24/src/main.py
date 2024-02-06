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



def driver():
    if con_buttonL1.pressing() == True:
        Left_Motor.spin(FORWARD) 
        Left_Motor.set.velocity(75, PERCENT)
    elif con.buttonL2.pressing() == True: 
        Left_Motor.spin(REVERSE)
        Left_Motor.set.velocity(75, PERCENT)
    else:
        Left_Motor.stop()
    pass
        
