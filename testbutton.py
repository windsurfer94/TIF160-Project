#!/usr/bin/env python3
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        print("high")
    else:
        print("low")