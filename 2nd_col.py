lineline_detector = self.car.line_detector
        self.car.accelerator.go_forward(50)
        checkAngle = -1
        while(line_detector.is_in_line() == True) :
            if (currentAngle != 90 and line_detector.is_equal_status([0,0,1,0,0])):
                checkAngle = 90
                self.car.steering.turn(90)
            elif (currentAngle != 85 and line_detector.is_equal_status([0,1,1,0,0])):
                currentAngle = 85
                self.car.steering.turn(85)
            elif (currentAngle != 95 and line_detector.is_equal_status([0,0,1,1,0])):
                currentAngle = 95
                self.car.steering.turn(95)
            elif (currentAngle != 80 and line_detector.is_equal_status([0,1,0,0,0])):
                currentAngle = 80
                self.car.steering.turn(80)
            elif (currentAngle != 100 and line_detector.is_equal_status([0,0,0,1,0])):
                currentAngle = 100
                self.car.steering.turn(100)
            elif (currentAngle != 60 and line_detector.is_equal_status([1,1,0,0,0])):
                currentAngle = 60
                self.car.steering.turn(60)
            elif (currentAngle != 120 and line_detector.is_equal_status([0,0,0,1,1])):
                currentAngle = 120
                self.car.steering.turn(120)
            elif (currentAngle != 55 and line_detector.is_equal_status([1,0,0,0,0])):
                currentAngle = 55
                self.car.steering.turn(55)
            elif (currentAngle != 125 and line_detector.is_equal_status([0,0,0,0,1])):
                currentAngle = 125
                self.car.steering.turn(125)
        # implement the assignment code here
        self.drive_parking()