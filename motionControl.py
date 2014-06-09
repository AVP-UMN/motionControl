import Adafruit_BBIO.PWM as PWM
import time

class Robot:
        def __init__(self):
		PWM.cleanup()
                self.steerServoPin='P8_13'
                self.motorServoPin='P9_14'
                PWM.start(self.motorServoPin, 1.5/20.0*100, 50)
                PWM.start(self.steerServoPin, 1.5/20.0*100, 50)

        def turn(self,angle):
                self.turningDuty=angle/90.0/20.0
                PWM.set_duty_cycle(self.steerServoPin,(1.5/20+self.turningDuty)*100)

        def speed(self,motorSpeed):
                self.speedDuty=motorSpeed/90.0/20.0
                PWM.set_duty_cycle(self.motorServoPin,(1.5/20+self.speedDuty)*100)
        def __del__(self):
                PWM.set_duty_cycle(self.motorServoPin,(1.5/20)*100)
                PWM.set_duty_cycle(self.steerServoPin,(1.5/20)*100)

if __name__=='__main__':
	c=Robot();
	i=0;
	while True:
		c.turn(-40+i)
		c.speed(-40+i)
		i=i+10
		time.sleep(0.5)
		if i>90: i=0
		                                   
