#!/usr/bin/env python3
import time
from subprocess import run
from gpiozero import MotionSensor
npm start
while True:
	run('vcgencmd display_power 0',shell=True) 
	if MotionSensor(15).motion_detected:
		print('On')
		run('vcgencmd display_power 1',shell=True)
		time.sleep(30)
	else:
		print('Off')
		run('vcgencmd display_power 0',shell=True)
		time.sleep(1)
