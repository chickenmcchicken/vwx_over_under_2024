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
            Left_group.set_velocity(Leftsped, PERCENT)
            Right_group.set_velocity(Rightsped, PERCENT)
            Left_group.spin(REVERSE)
            Right_group.spin(REVERSE)
        wait(20, MSEC)


#for this auton is when the goal is on the right
def auton():

    #
    #For this autonomous to work the robot must be
    #6 inches left and 2.75 inches left on the
    #starting tile
    #

    brain.screen.clear_screen()
    brain.screen.print("auton")
    #print auton
    Right_group.set_velocity(100, PERCENT)
    Left_group.set_velocity(100, PERCENT)
    Left_group.spin(FORWARD)
    Right_group.spin(REVERSE)
    wait(0.3, SECONDS)
    #Robot moves forward
    Right_group.stop()
    Left_group.stop()
    Right_group.set_velocity(50, PERCENT)
    Left_group.set_velocity(50, PERCENT)
    Left_group.spin(FORWARD)
    Right_group.spin(REVERSE)
    wait(0.3, SECONDS)
    wait(20, MSEC)
    Left_group.set_velocity(100, PERCENT)
    Left_group.spin(FORWARD)
    wait(1.09, SECONDS)
    #Robot turns left and aligns for goal
    Left_group.stop()
    Right_group.set_velocity(100, PERCENT)
    Left_group.set_velocity(100, PERCENT)
    Left_group.spin(REVERSE)
    Right_group.spin(FORWARD)
    wait(0.1, SECONDS)
    Right_group.stop()
    Left_group.stop()
    Intake.set_velocity(100, PERCENT)
    Intake.spin(REVERSE)
    wait(0.4, SECONDS)
    #Intake spins
    Intake.set_velocity(60, PERCENT)
    Intake.spin(REVERSE)
    wait(0.3, SECONDS)
    Intake.set_velocity(30, PERCENT)
    Intake.spin(REVERSE)
    wait(0.3, SECONDS)
    Intake.stop()
    Right_group.stop()
    Left_group.stop()
    Right_group.spin(REVERSE)
    Left_group.spin(FORWARD)
    wait(0.1, SECONDS)
    Left_group.stop()
    Right_group.stop()
    Right_group.set_velocity(100, PERCENT)
    Left_group.set_velocity(100, PERCENT)
    Left_group.spin(REVERSE)
    Right_group.spin(REVERSE)
    #Robot does 180
    wait(0.7, SECONDS)
    Right_group.stop()
    Left_group.stop() 
    Right_group.set_velocity(100, PERCENT)
    Left_group.set_velocity(100, PERCENT)
    Left_group.spin(FORWARD)
    Right_group.spin(REVERSE)
    wait(0.8, SECONDS)
    #Robot rams acorn in
    Right_group.stop()
    Left_group.stop()
    Left_group.set_velocity(100, PERCENT)
    Right_group.set_velocity(100, PERCENT)
    Left_group.spin(REVERSE)
    Right_group.spin(FORWARD)
    #Robot backs up
    wait(0.7, SECONDS)
    Right_group.stop()
    Left_group.stop()
    wait(20, MSEC)
    Left_group.set_velocity(100, PERCENT)
    Right_group.set_velocity(100, PERCENT)
    Right_group.spin(FORWARD)
    Left_group.spin(FORWARD)
    wait(0.68, SECONDS)
    #robot aligns for 2nd acorn
    Right_group.stop()
    Left_group.stop()
    wait(20, MSEC)    
    Left_group.set_velocity(100, PERCENT)
    Right_group.set_velocity(100, PERCENT)
    Right_group.spin(FORWARD)
    Left_group.spin(REVERSE)
    wait(0.82, SECONDS)
    #Robot goes for 2nd acorn
    Right_group.stop()
    Left_group.stop()
    wait(20, MSEC)
    Right_group.set_velocity(100, PERCENT)
    Left_group.set_velocity(100, PERCENT)
    Left_group.spin(FORWARD)
    Right_group.spin(REVERSE)
    # Left_group.set_velocity(100, PERCENT)
    # Right_group.set_velocity(100, PERCENT)
    # Left_group.spin(FORWARD)
    # Right_group.spin(FORWARD)
    wait(20, MSEC)
    Left_group.set_velocity(100, PERCENT)
    Right_group.set_velocity(100, PERCENT)
    Intake.set_velocity(100)
    Right_group.spin(FORWARD)
    Left_group.spin(REVERSE)
    Intake.spin(FORWARD)
    wait(2, SECONDS)
    Left_group.stop()
    Right_group.stop()
    Left_group.spin(FORWARD)
    Right_group.spin(REVERSE)
    wait(1.2, SECONDS)
    Left_group.stop()
    Right_group.stop()
    Left_group.set_velocity(100, PERCENT)
    Right_group.set_velocity(100, PERCENT)
    Left_group.spin(FORWARD)
    Right_group.spin(FORWARD)
    wait(0.18, SECONDS)
    Intake.stop()
    Left_group.stop()
    Right_group.stop()
    Right_group.set_velocity(100, PERCENT)
    Left_group.set_velocity(100, PERCENT)
    Left_group.spin(FORWARD)
    Right_group.spin(REVERSE)
    wait(0.3, SECONDS)
    Left_group.stop()
    Right_group.stop()
    # wait(0.5, SECONDS)
    # Left_group.spin(REVERSE)
    # Right_group.spin(FORWARD)
    # wait(1.55, SECONDS)
    # Left_group.stop()
    # Right_group.stop()
    # wait(0.4, SECONDS)
#make the functions repeat
#they must be under functions 
#or else there will be a error where 
#autonomous will not work
def Driver_function():
    Thread(Primary_control)


def auton_function():
    Thread(auton)


comp = Competition(Driver_function, auton)
    
        

        
