#!/usr/bin/python2
#coding=utf-8

import RPi.GPIO as gpio
import time

class Wheel(object):
    def __init__(self, in_pin1, in_pin2, enable_pin1, enable_pin2):
        '''
        :param in_pin1 in_pin1: IN1 IN2 or IN3 IN4
        :param enable_pin1 enable_pin2: ENA or ENB
        '''
        self.pin1 = in_pin1
        self.pin2 = in_pin2

        # setup I/O OUT
        gpio.setup(in_pin1, gpio.OUT)
        gpio.setup(in_pin2, gpio.OUT)
        gpio.setup(enable_pin1, gpio.OUT)
        gpio.setup(enable_pin2, gpio.OUT)

        gpio.output(enable_pin1, True)
        gpio.output(enable_pin2, True)
        # enable
        self.pwm = gpio.PWM(enable_pin1, 50)
        self.pwm.start(0)
        #gpio.output(enable_pin1, True)
        #gpio.output(enable_pin2, True)

    def forward(self):
        gpio.output(self.pin1, True)
        gpio.output(self.pin2, False)

    def backward(self):
        gpio.output(self.pin1, False)
        gpio.output(self.pin2, True)
    
    def stop(self):
        gpio.output(self.pin1, False)
        gpio.output(self.pin2, False)

    def set_speed(self, dc):
	self.pwm.ChangeDutyCycle(dc)

class Car(object):
    def __init__(self):
        gpio.setmode(gpio.BOARD)

        self.left_wheel = Wheel(13, 15, 7, 11)
        self.right_wheel = Wheel(16, 18, 22, 29)

    def forward(self):
        self.left_wheel.forward()
        self.right_wheel.forward()

    def backward(self):
        self.left_wheel.backward()
        self.right_wheel.backward()

    def left(self):
        self.left_wheel.stop()
        self.right_wheel.forward()

    def right(self):
        self.left_wheel.forward()
        self.right_wheel.stop()

    def stop(self):
        self.left_wheel.stop()
        self.right_wheel.stop()        

    def set_speed(self, dc):
	self.left_wheel.set_speed(dc)
	self.right_wheel.set_speed(dc)

    def shutdown(self):
        self.stop()
        gpio.cleanup()

if __name__ == "__main__":
    smart_car = Car()
    smart_car.set_speed(50)
    smart_car.forward()
    time.sleep(2)
    smart_car.backward()
    time.sleep(2)
    smart_car.left()
    time.sleep(0.5)
    smart_car.set_speed(100)
    #time.sleep(2)
    smart_car.forward()
    time.sleep(2)
    smart_car.backward()
    time.sleep(2)
    smart_car.right()
    time.sleep(0.5)
    smart_car.shutdown()
