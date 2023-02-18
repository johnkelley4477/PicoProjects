from machine import Pin

ledOne = Pin(0,Pin.OUT)
ledTwo = Pin(1,Pin.OUT)
ledThree = Pin(2,Pin.OUT)
ledFour = Pin(3,Pin.OUT)

swOne = Pin(4,Pin.IN,Pin.PULL_DOWN)
swTwo = Pin(5,Pin.IN,Pin.PULL_DOWN)
swThree = Pin(6,Pin.IN,Pin.PULL_DOWN)
swFour = Pin(7,Pin.IN,Pin.PULL_DOWN)
swReset = Pin(8,Pin.IN,Pin.PULL_DOWN)

While seReset.value():
  if(swOne.value() || swTwo.value() || swThree.value() || swFour.value() ):
    ledOne.value(swOne.value())
    ledTwo.value(swTwo.value())
    ledThree.value(swThree.value())
    ledFour.value(swFour.value())
  else:
    seReset.value(1)
