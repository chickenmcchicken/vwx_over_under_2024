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
AWD = MotorGroup(Rightback_Motor, Rightfront_Motor, Leftback_Motor, Leftfront_Motor)





def Primary_control():
    while True:
        if con.buttonR1.pressing() == True:
            Intake.set_velocity(100, PERCENT)
            Intake.spin(FORWARD)
        elif con.buttonL1.pressing() == True:
            Intake.set_velocity(100, PERCENT)
            Intake.spin(REVERSE)
        else:
            Intake.set_velocity(0, PERCENT)
            Intake.set_stopping(HOLD)
            wait(20, MSEC)
        #
        if con.buttonR2.pressing() == True:
            Climbing_system.set_velocity(100, PERCENT)
            Climbing_system.spin(REVERSE)
        elif con.buttonL2.pressing() == True:
            Climbing_system.set_velocity(100, PERCENT)
            Climbing_system.spin(FORWARD)
        else:
            Climbing_system.set_velocity(0, PERCENT)
            Climbing_system.set_stopping(HOLD)
            pos3 = con.axis3.position()
            pos4 = con.axis1.position()
            Leftsped = pos4 + pos3
            Rightsped = pos4 - pos3
            Left_group.set_velocity(Rightsped, PERCENT)
            Right_group.set_velocity(Leftsped, PERCENT)
            Left_group.spin(REVERSE)
            Right_group.spin(REVERSE)
        wait(20, MSEC)
        



# def autonomous():
#     AWD.set_velocity(100, PERCENT)
#     AWD.spin(FORWARD)
#     wait(4, SECONDS)
#     #Right_group.stop()
#     #Left_group.stop()
#     #Right_group.set_velocity(100, PERCENT)
#     #Right_group.spin(REVERSE)
#     #wait(2, SECONDS)
#     #Right_group.stop()
#     #Intake.set_velocity(100, PERCENT)
#     #Intake.spin(FORWARD)
#     #Intake.stop()
    

# def main():
#     Competition(Primary_control, autonomous)
    
        
# main()
