# Getting started
## Installing MicroPython for Esp3ESP32 (firmware)
Read this quiet easy and straightforward [instructions](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html).
Basically you need a Python-package "esptool" and a corresponding ESP32-MicroPython-Firmware to flash on.  


## Deploy your own program without the whole toolchain
You can run single commands via serial-console. But how do you get your program working which was developed on your PC?

Small note to serial port: This was developed on my Windows-PC. The ESP was connected on `COM8`. Change it to your corresponding serial port (or on unix to your `/dev/ttyXYZ`).

### Create your project
#### Virtual environment
TODO venv

#### Main-file
File `main_file.py` in this repository:
``` python
import time

for i in range(5):
    print("Hello World", i)
    time.sleep(0.5)
```
 
### Deployment
#### ampy
Adafruit MicroPython Tool (ampy) is a tool to interact with CircuitPython or MicroPython boards over serial connections.

``pip install adafruit-ampy``

#### Test if it's working

``ampy --port COM8 ls``

If this is your initial call there should be at least one item called `/boot.py`


#### Get it working

It is quiet simple:

``ampy --port COM8 run main_file.py``

Attention: ampy's `run` waits for the code to finish and THEN return its output. So if you're writing code which runs forever, this script will never return (or put something in stdio).

# Autostart of project

If you want your script to be started automatically on boot of the ESP. Upload a file called ``main.py``. If this file exists, it will be executed after `boot.py` is called.
E.g. in this project:


``ampy --port COM8 put main_file.py main.py``
Note: If you want to keep its original name, just leave out the last parameter.

If you run ``ampy --port COM8 ls`` again you should see you ``main.py``.

Note: You can NOT directly run internal files with ampy's `run`!