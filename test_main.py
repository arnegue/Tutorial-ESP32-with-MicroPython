import time
from machine import Pin

led = Pin(2, Pin.OUT)  # On-Board LED

for i in range(5):
    print("Hello World", i)
    time.sleep(0.5)
    led.on() if i % 2 else led.off()  # Toggle LED
