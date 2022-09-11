#!/usr/bin/env python3
import time
from subprocess import run
from gpiozero import MotionSensor
s1=MotionSensor(15)
while True: 
	print(s1.motion_detected)
	if s1.motion_detected:
		run('vcgencmd display_power 1',shell=True)
		time.sleep(60)
	else:
		run('vcgencmd display_power 0',shell=True)
