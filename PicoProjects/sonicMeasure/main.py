from machine import Pin
from time import sleep
import utime

ledGreenOne = Pin(9,Pin.OUT);
ledGreenTwo = Pin(8,Pin.OUT);
ledYellowThree = Pin(7,Pin.OUT);
ledYellowFour = Pin(6,Pin.OUT);
ledYellowFive = Pin(5,Pin.OUT);
ledRedSix = Pin(4,Pin.OUT);
ledRedSeven = Pin(3,Pin.OUT);
ledRedEight = Pin(2,Pin.OUT);
ledRedNine = Pin(1,Pin.OUT);
ledRedTen = Pin(0,Pin.OUT);

trigger = Pin(15, Pin.OUT)
echo = Pin(14, Pin.IN)

def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    print(echo.value())
    while echo.value() == 0:
       signaloff = utime.ticks_us()
    while echo.value() == 1:
       signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print("The distance from object is ",distance,"cm")

while True:
    ultra()
    ledGreenOne.value(1);
    sleep(0.25);
    ledGreenTwo.value(1);
    sleep(0.25);
    ledYellowThree.value(1);
    sleep(0.25);
    ledYellowFour.value(1);
    sleep(0.25);
    ledYellowFive.value(1);
    sleep(0.25);
    ledRedSix.value(1);
    sleep(0.25);
    ledRedSeven.value(1);
    sleep(0.25);
    ledRedEight.value(1);
    sleep(0.25);
    ledRedNine.value(1);
    sleep(0.25);
    ledRedTen.value(1);
    sleep(0.25);
    