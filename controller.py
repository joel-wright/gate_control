#!/usr/bin/python  
import RPi.GPIO as GPIO  
import time  


def init_gpio():
    # Set pin 4 to low
    GPIO.setmode(GPIO.BCM)  
    GPIO.setup(4, GPIO.OUT)   
    GPIO.output(4, GPIO.HIGH)  

def gate_toggle():
    # time to sleep between operations in the main loop  
    GPIO.output(4, GPIO.LOW)  
    time.sleep(1);   
    GPIO.output(4, GPIO.HIGH)  

def cleanup_gpio():
    GPIO.cleanup()

