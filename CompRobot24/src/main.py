/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       CYBER                                                     */
/*    Created:      5/7/2024, 3:00:28 PM                                      */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/
#include "vex.h"
#include <iostream>
#include <string>
#include <math.h>
using namespace vex;
vex::competition Competition;
// A global instance of vex::brain used for printing to the V5 brain screen
vex::brain       Brain;

// define your global instances of motors and other devices here


int main() {
    
    Brain.Screen.printAt( 10, 50, "Hello V5" );
   
    while(1) {
        
        // Allow other tasks to run
        this_thread::sleep_for(10);
    }

}

vex::controller con = vex::controller();
vex::motor Leftfront_Motor(vex::PORT2, vex::gearSetting::ratio18_1, true);
vex::motor Leftback_Motor(vex::PORT10, vex::gearSetting::ratio18_1, true);
vex::motor Rightfront_Motor(vex::PORT1, vex::gearSetting::ratio18_1, true);
vex::motor Rightback_Motor(vex::PORT9, vex::gearSetting::ratio18_1, true);
vex::motor Intake_Motor(vex::PORT8, vex::gearSetting::ratio18_1, true);
vex::motor Climbing_system1(vex::PORT3, vex::gearSetting::ratio36_1, true);
vex::motor Climbing_system2(vex::PORT12, vex::gearSetting::ratio36_1, true);
vex::motor_group Right_group(Rightfront_Motor, Rightback_Motor);
vex::motor_group Left_group(Leftfront_Motor, Leftback_Motor );
void D_c() {

}
void Su_c() {
while (true){
    if (con.ButtonR1.pressing() == true)
    {
        Intake_Motor.setVelocity(100.0, percent);
        Intake_Motor.spin(directionType::fwd);
    }
    else (con.ButtonL1.pressing() == true);
    {
        Intake_Motor.setVelocity(100.0, percent);
        Intake_Motor.spin(directionType::rev);
    }
}
}
int comp() {
Competition.autonomous(D_c);
Competition.drivercontrol(Su_c);
while(1) {
    vex::task::sleep(5);
}
}
