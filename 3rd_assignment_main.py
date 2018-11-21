
#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from SR02 import SR02_Ultrasonic as Ultrasonic_Sensor
import front_wheels
import rear_wheels
import time
from SEN040134 import SEN040134_Tracking as line
from car import Car

class myCar(object):

	def __init__(self, car_name):
		self.car = Car(car_name)

	def drive_parking(self):
		self.car.drive_parking()
	def no_line_left(self):
		direction_controller = front_wheels.Front_Wheels(db='config')
		driving_controller = rear_wheels.Rear_Wheels(db='config')
		line_detector = line.SEN040134_Tracking([16, 18, 22, 40, 32])
		direction_controller.turn(120)
		driving_controller.backward_with_speed(30)
		if line_detector.is_in_line:
			return 0

	def no_line_right(self):
		direction_controller = front_wheels.Front_Wheels(db='config')
		driving_controller = rear_wheels.Rear_Wheels(db='config')
		line_detector = line.SEN040134_Tracking([16, 18, 22, 40, 32])
		direction_controller.turn(60)
		driving_controller.backward_with_speed(30)
		if line_detector.is_in_line:
			return 0

	def obstacles(self):
		distance_detector = Ultrasonic_Sensor.Ultrasonic_Avoidance(35)
		line_detector = line.SEN040134_Tracking([16, 18, 22, 40, 32])
		direction_controller = front_wheels.Front_Wheels(db='config')
		driving_controller = rear_wheels.Rear_Wheels(db='config')
		direction_controller.turn_straight()
		time.sleep(1)
		o_count=0


		while(1):

			distance = distance_detector.get_distance()
			print(distance)
			time.sleep(0.1)
			if distance<30:
				direction_controller.turn(60)
				time.sleep(0.5)
				driving_controller.forward_with_speed(30)
				time.sleep(0.5)
				direction_controller.turn(90)
				time.sleep(0.5)
				o_count = o_count + 1
				if line_detector.is_in_line():

					while(1):
						if line_detector.is_inline():
							driving_controller.forward_with_speed(30)

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
						else:
							o_count=o_count+1
							break

				elif o_count==2 :
					driving_controller.forward_with_speed(30)
					direction_controller.turn(60)
					time.sleep(0.5)
					driving_controller.forward_with_speed(30)
					time.sleep(0.5)
					direction_controller.turn(90)
					time.sleep(0.5)
					if line_detector.is_in_line():
						return 0
#
			
		# Example Of Real Motor Control




	# =======================================================================
	# 3RD_ASSIGNMENT_CODE
	# Complete the code to perform Third Assignment
	# =======================================================================
	def car_startup(self):
		direction_controller = front_wheels.Front_Wheels(db='config')
		driving_controller = rear_wheels.Rear_Wheels(db='config')
		direction_controller.turn_straight()
		time.sleep(1)
		line_detector = line.SEN040134_Tracking([16, 18, 22, 40, 32])
		checkAngle=-1
		check_round=0
		count=0
		while (1):
			driving_controller.forward_with_speed(30)
			self.obstacles()
			if(line_detector.is_equal_status([0,0,0,0,0])):
				count=count+1
				if count==3:
					break


			if (checkAngle != 90 and line_detector.is_equal_status([1,1,0,1,1])):
				checkAngle = 90
				direction_controller.turn(90)


			elif (checkAngle != 85 and line_detector.is_equal_status([0,1,1,0,0])):
				checkAngle = 85
				direction_controller.turn(85)
				if not line_detector.is_in_line:
					self.no_line_left()

			elif (checkAngle != 100 and line_detector.is_equal_status([0,0,1,1,0])):
				checkAngle = 100
				direction_controller.turn(100)
				if not line_detector.is_in_line:
					self.no_line_right()

			elif (checkAngle != 50 and line_detector.is_equal_status([1,0,0,0,0])):
				checkAngle = 50
				direction_controller.turn(50)
				if not line_detector.is_in_line:
					self.no_line_left()
			elif (checkAngle != 80 and line_detector.is_equal_status([0,1,0,0,0])):
				checkAngle = 80
				direction_controller.turn(80)
				if notline_detector.is_in_line:
					self.no_line_left()
			elif (checkAngle != 105 and line_detector.is_equal_status([0,0,0,1,0])):
				checkAngle = 105
				direction_controller.turn(105)
				if not line_detector.is_in_line:
					self.no_line_right()
			elif (checkAngle != 55 and line_detector.is_equal_status([1,1,0,0,0])):
				checkAngle = 55
				direction_controller.turn(55)
				if not line_detector.is_in_line:
					self.no_line_left()
			elif (checkAngle != 125 and line_detector.is_equal_status([0,0,0,1,1])):
				checkAngle = 125
				direction_controller.turn(125)
				if not line_detector.is_in_line:
					self.no_line_right()

			elif (checkAngle != 130 and line_detector.is_equal_status([0,0,0,0,1])):
				checkAngle = 130
				direction_controller.turn(130)
				if not line_detector.is_in_line:
					self.no_line_right()

if __name__ == "__main__":
	try:
		myCar = myCar("CarName")
		
		myCar.car_startup()

	except KeyboardInterrupt:
		# when the Ctrl+C key has been pressed,
		# the moving object will be stopped
		myCar.drive_parking()

