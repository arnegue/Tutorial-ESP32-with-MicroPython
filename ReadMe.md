# Getting started
## Installing MicroPython for ESP32 (firmware)
Read this quiet easy and straightforward [instructions](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html).
Basically you need a Python-package "esptool" and a corresponding ESP32-MicroPython-Firmware to flash on.  


## Deploy your own program without the whole toolchain
You can run single commands via serial-console. But how do you get your program working which was developed on your PC?

Small note to serial port: This was developed on my Windows-PC. The ESP was connected on `COM8`. Change it to your corresponding serial port (or on unix to your `/dev/ttyXYZ`).

## Create your project
### Main-file
File `test_main.py` in this repository. Every 0.5 second it will print "Hello world" with it's current iteration and toggle a LED on ESP32:
``` python
import time
from machine import Pin

led = Pin(2, Pin.OUT)  # On-Board LED

for i in range(5):
    print("Hello World", i)
    time.sleep(0.5)
    led.on() if i % 2 else led.off()  # Toggle LED
```
 
## Deployment
### ampy
Adafruit MicroPython Tool (ampy) is a tool to interact with CircuitPython or MicroPython boards over serial connections.

``pip install adafruit-ampy``

### Test if ampy is working
``ampy --port COM8 ls``

If this is your initial call there should be at least one item called `/boot.py`


### Get it your script working
It is quiet simple:

``ampy --port COM8 run test_main.py``

Attention: ampy's `run` waits for the code to finish and THEN return its output. So if you're writing code which runs forever, this script will never return (or put something in stdio).

## Autostart of project, uploading files
If you want your script to be started automatically on boot of the ESP, you need to upload your files. The entry script must be called `main.py`. If this file exists, it will be executed after `boot.py` is called.
E.g. in this project:

``ampy --port COM8 put test_main.py main.py``

Note: If you want to keep its original name, just leave out the last parameter.

If you run ``ampy --port COM8 ls`` again you should see you `main.py`.

Note: You can NOT directly run internal files with ampy's `run`!
`run` only uploads given script. So if you have further scripts to import, you have to upload them with:

``ampy --port COM8 put another_file.py``

## Pre-Compile
### Install mpy-cross
You may want to cross-compile your code for optimization reasons: This can be done with the library `mpy-cross`:

``pip install mpy_cross`` (note the underscore instead of dash).

### Compile your test_main
``python -m mpy_cross test_main.py``

Now a further file called `test_main.mpy` was created. 

### Upload your test_main
Upload it using:
 
 ``ampy --port COM8 put test_main.mpy``

### But how do you call it?
Simply by importing it via a Standard-Script
```python
import test_main
```

This will directly execute given code. So if you just run or upload the python file mentioned content. It will be executed.
