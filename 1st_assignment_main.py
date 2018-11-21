#########################################################################
# Date: 2018/10/02
# file name: 1st_assignment_main.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
# this code is used for the student only
#########################################################################
from SR02 import SR02_Ultrasonic as Ultrasonic_Sensor
import front_wheels
import rear_wheels
import time
from car import Car

class myCar(object):
    def __init__(self, car_name):
        
         self.car = Car("car_name")

    def drive_parking(self):
         
         self.car.drive_parking()

    # =======================================================================
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def car_startup(self):
        # Implement the assignment code here.
        
        direction_controller = front_wheels.Front_Wheels(db='config')
        driving_controller = rear_wheels.Rear_Wheels(db='config')
        direction_controller.turn_straight()
        time.sleep(1)
        i=0
        distance_detector = Ultrasonic_Sensor.Ultrasonic_Avoidance(35)
                    
        while(i<=2):
            
            distance = distance_detector.get_distance()    
            print(distance)
            time.sleep(0.1)
                        
            if i==0:
                while(1):
                    driving_controller.forward_with_speed(30)
                    time.sleep(0.1)
                    distance = distance_detector.get_distance()    
                    print(distance)
                    time.sleep(0.1)
            
                    if distance<=15:
                         driving_controller.stop()
                         time.sleep(0.1)
                         driving_controller.backward_with_speed(50)
                         time.sleep(4)
                     
                         driving_controller.stop()
                         time.sleep(0.1)
                         i=i+1
                         break
            elif i==1:                      
                while(1):
                    driving_controller.forward_with_speed(50)
                    time.sleep(0.1)
                    distance = distance_detector.get_distance()    
                    print(distance)
                    time.sleep(0.1)
            
                    if distance<=20:
                        driving_controller.forward_with_speed(50)
                        time.sleep(0.1)
                        driving_controller.stop()
                        time.sleep(0.1)
                        driving_controller.backward_with_speed(50)
                        time.sleep(4)
                        driving_controller.stop()
                        time.sleep(0.1)
                        i=i+1
                        break
            elif i==2:
                while(1):
                    driving_controller.forward_with_speed(70)
                    time.sleep(0.1)
                    distance = distance_detector.get_distance()    
                    print(distance)
                    time.sleep(0.1)
            
                    if distance<=25:
                        driving_controller.stop()
                        time.sleep(0.1)
                        driving_controller.backward_with_speed(50)
                        time.sleep(4)
                        driving_controller.stop()
                        time.sleep(0.1)
                        i=i+1
                        break
        # Example Of Real Motor Control

        

        driving_controller.stop()
        driving_controller.power_down()

if __name__ == "__main__":
    cnt =0
    try:
        myCar = myCar("car_name" )
        myCar.car_startup()
        
    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
