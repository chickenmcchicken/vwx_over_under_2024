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
#Identifying motors and motor groups
Leftfront_Motor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
Leftback_Motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True) 
Rightfront_Motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
Rightback_Motor = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True) 
Intake = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
Climbing_system = Motor(Ports.PORT3, GearSetting.RATIO_36_1, True)
Climbing_system2 = Motor(Ports.PORT12, GearSetting.RATIO_36_1, True)
Left_group = MotorGroup(Leftback_Motor, Leftfront_Motor)
Right_group = MotorGroup(Rightback_Motor, Rightfront_Motor)



def Primary_control():
    brain.screen.clear_screen()
    brain.screen.print("Driver control")
    #having an indicator for when a function is running 
    #so print is used
    while True:
        #intake controls
        if con.buttonR1.pressing() == True:
            Intake.set_velocity(100, PERCENT)
            Intake.spin(FORWARD)
        elif con.buttonL1.pressing() == True:
            Intake.set_velocity(100, PERCENT)
            Intake.spin(REVERSE)
        else:
            Intake.set_velocity(0, PERCENT)
            Intake.set_stopping(HOLD)
        #Climbing system controls
        if con.buttonR2.pressing() == True:
            Climbing_system.set_velocity(100, PERCENT)
            Climbing_system2.set_velocity(100, PERCENT)
            Climbing_system.spin(REVERSE)
            Climbing_system2.spin(FORWARD)
        elif con.buttonL2.pressing() == True:
            Climbing_system.set_velocity(100, PERCENT)
            Climbing_system2.set_velocity(100, PERCENT)
            Climbing_system.spin(FORWARD)
            Climbing_system2.spin(REVERSE)
        else:
            Climbing_system.set_velocity(0, PERCENT)
            Climbing_system.set_stopping(HOLD)
            Climbing_system2.set_velocity(0, PERCENT)
            Climbing_system2.set_stopping(HOLD)
        #movement control with joysticks
            pos3 = con.axis3.position()
            pos4 = con.axis1.position()
            Leftsped = pos4 + pos3
            Rightsped =  pos4 - pos3
            Left_group.set_velocity(Rightsped, PERCENT)
            Right_group.set_velocity(Leftsped, PERCENT)
            Left_group.spin(REVERSE)
            Right_group.spin(REVERSE)
        wait(20, MSEC)



def auton():
    brain.screen.clear_screen()
    brain.screen.print("auton")
    Right_group.set_velocity(100, PERCENT)
    Left_group.set_velocity(100, PERCENT)
    Left_group.spin(FORWARD)
    Right_group.spin(REVERSE)
    wait(0.8, SECONDS)
    Right_group.stop()
    Left_group.stop()
    wait(1, SECONDS)
    Right_group.set_velocity(100, PERCENT)
    Left_group.set_velocity(100, PERCENT)
    Left_group.spin(REVERSE)
    Right_group.spin(REVERSE)
    wait(0.25, SECONDS)
    Right_group.stop()
    Left_group.stop()
    
    
#     Intake.set_velocity(100, PERCENT)
#     Intake.spin(FORWARD)
#     wait(1, SECONDS)   
#     Intake.stop()
#     Right_group.set_velocity(100, PERCENT)
#     Left_group.set_velocity(100, PERCENT)
#     Left_group.spin(REVERSE)
#     Right_group.spin(REVERSE)
#     wait(0.5, SECONDS)
#     Right_group.stop()
#     Left_group.stop()
#     Right_group.set_velocity(100, PERCENT)
#     Left_group.set_velocity(100, PERCENT)
#     Left_group.spin(REVERSE)
#     Right_group.spin(FORWARD)
#     wait(0.15, SECONDS)
#     Left_group.stop()
#     Right_group.stop()
#     Left_group.set_velocity(100, PERCENT)
#     Right_group.set_veloctiy(100, PERCENT)
#     Left_group.spin(FORWARD)
#     Right_group.spin(REVERSE)
#     wait(0.15, SECONDS)
#     Right_group.stop()
#     Left_group.stop() 

#make the functions repeat
#they must be under functions 
#or else there will be a error where 
#autonomous will not work
def Driver_function():
    Thread(Primary_control)


def auton_function():
    Thread(auton)


comp = Competition(Driver_function, auton)
    
        
