#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################
import front_wheels
import rear_wheels
import time
from SEN040134 import SEN040134_Tracking as line

from car import Car



class myCar(object):

    def __init__(self, car_name):
        self.car = Car("car_name")

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
         
        direction_controller = front_wheels.Front_Wheels(db='config')
        driving_controller = rear_wheels.Rear_Wheels(db='config')
        direction_controller.turn_straight()
        time.sleep(1)
        line_detector = line.SEN040134_Tracking([16, 18, 22, 40, 32])
        #line_detector = self.car.line_detector([16,18,22,40,32])
        
        
        checkAngle=-1
        driving_controller.forward_with_speed(30)
        while (1):
            
            
            if (checkAngle != 90 and line_detector.is_equal_status([1,1,0,1,1])):
                checkAngle = 90
                direction_controller.turn(90)
                
                
            elif (checkAngle != 85 and line_detector.is_equal_status([0,1,1,0,0])):
                checkAngle = 85
                direction_controller.turn(85)
           
                
            elif (checkAngle != 100 and line_detector.is_equal_status([0,0,1,1,0])):
                checkAngle = 100
                direction_controller.turn(100)
            elif (checkAngle != 50 and line_detector.is_equal_status([1,0,0,0,0])):
                checkAngle = 50
                direction_controller.turn(50)     
                
            elif (checkAngle != 80 and line_detector.is_equal_status([0,1,0,0,0])):
                checkAngle = 80
                direction_controller.turn(80)   
            elif (checkAngle != 105 and line_detector.is_equal_status([0,0,0,1,0])):
                checkAngle = 105
                direction_controller.turn(105)    
            
            elif (checkAngle != 55 and line_detector.is_equal_status([1,1,0,0,0])):
                checkAngle = 55
                direction_controller.turn(55)
            elif (checkAngle != 125 and line_detector.is_equal_status([0,0,0,1,1])):
                checkAngle = 125
                direction_controller.turn(125)
            
            
            
            elif (checkAngle != 130 and line_detector.is_equal_status([0,0,0,0,1])):
                checkAngle = 130
                direction_controller.turn(130)    
                    
                        
                #just one 0 exist
if __name__ == "__main__":
    try:
        myCar = myCar("car_name")
        myCar.__init__("car_name")
        li = line.SEN040134_Tracking([16, 18, 22, 40, 32])
        
        myCar.car_startup()
            
    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()