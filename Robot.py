import Adafruit_BBIO.PWM as PWM


class Robot:
	def __init__(self):
		self.steerServoPin='P8_13'
		self.motorServoPin='P8_19'
		PWM.start(self.steerServoPin, 1.0/20.0, 50)	
		PWM.start(self.motorServoPin, 1.0/20.0, 50)	

	def turing(self,angle):
		self.turningDuty=angle/90.0/20.0
		PWM.set_duty_cycle(self.steerServoPin,self.turningDuty)

	def speed(self,motorSpeed):
		self.speedDuty=motorSpeed/90.0/20.0
		PWM.set_duty_cycle(self.motorServoPin,self.speedDuty)
	def __del__(self)
		PWM.stop(self.steerServoPin)
		PWM.stop(self.motorServoPin)
		PWM.cleanup()
