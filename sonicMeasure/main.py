from machine import Pin
from time import sleep
import utime

ledGreenOne = Pin(10,Pin.OUT)
ledGreenTwo = Pin(8,Pin.OUT)
ledYellowThree = Pin(7,Pin.OUT)
ledYellowFour = Pin(6,Pin.OUT)
ledYellowFive = Pin(5,Pin.OUT)
ledRedSix = Pin(4,Pin.OUT)
ledRedSeven = Pin(3,Pin.OUT)
ledRedEight = Pin(2,Pin.OUT)
ledRedNine = Pin(1,Pin.OUT)
ledRedTen = Pin(0,Pin.OUT)

trigger = Pin(15, Pin.OUT)
echo = Pin(14, Pin.IN)

def clearLights():
    ledGreenOne.value(0)
    ledGreenTwo.value(0)
    ledYellowThree.value(0)
    ledYellowFour.value(0)
    ledYellowFive.value(0)
    ledRedSix.value(0)
    ledRedSeven.value(0)
    ledRedEight.value(0)
    ledRedNine.value(0)
    ledRedTen.value(0)
def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
       signaloff = utime.ticks_us()
    while echo.value() == 1:
       signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print("The distance from object is ",distance,"cm")
    return distance

while True:
    clearLights()
    if ultra() >= 100:
        ledGreenOne.value(1)
    if ultra() < 100:
        ledGreenTwo.value(1)
    if ultra() < 90:
         ledYellowThree.value(1)
    if ultra() < 80:
         ledYellowFour.value(1)
    if ultra() < 70:
         ledYellowFive.value(1)
    if ultra() < 60:
         ledRedSix.value(1)
    if ultra() < 50:
         ledRedSeven.value(1)
    if ultra() < 40:
         ledRedEight.value(1)
    if ultra() < 30:
         ledRedNine.value(1)
    if ultra() < 20:
         ledRedTen.value(1)
    sleep(1)
    
