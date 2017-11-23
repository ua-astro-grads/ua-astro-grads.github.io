---
author: "Craig Kulesa"
title: "Real Programmers Debug with Fire Extinguishers"
---

Talk slides [are available here](/downloads/2017-18/kulesa-hardware-slides.pdf).   A hands-on session with example hardware is offered on 11/29; email Craig if you're interested.  

## Resources

For your amusement, the Antarctic observatory used as an example in the talk is [HEAT](http://soral.as.arizona.edu/heat/)

Go build something and control it with software.  [Sparkfun](https://www.sparkfun.com/) and [Adafruit](https://www.adafruit.com/) have a lot of good resources and some nifty development boards to get you started.

### Talking to hardware:  SPI and I2C

Wikipedia links for [I2C](https://en.wikipedia.org/wiki/I%C2%B2C) and [SPI](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus).

A very low-level example of performing SPI communication via a microcontroller in C is [here](https://www.maximintegrated.com/en/app-notes/index.mvp/id/4184).

For the python-centric, look at [spidev](https://pypi.python.org/pypi/spidev) and [I2C](https://pypi.python.org/pypi/smbus-cffi/0.5.1), also [this](https://pypi.python.org/pypi/smbus2/0.1.0).

### Talking to hardware:  Serial (RS232, RS485, RS422)

If you get a USB-to-serial converter, ones with a Prolific PL2303 chipset will work generically under just about any operating system without fuss.  They can be purchased with flying leads for about $5 and with a DB9 connector for $10-20.

The bible:  [Serial Programming Guide for POSIX Operating Systems](https://www.cmrr.umn.edu/~strupp/serial.html). 

The [pySerial](http://pyserial.readthedocs.io/en/latest/shortintro.html) API is excellent and will get you to a working device quickly.  

### Talking to hardware:  CAN bus

The [SocketCAN or can-utils package](https://github.com/linux-can/can-utils) will let you display, record, generate, or replay CAN traffic.

The [python-can](http://python-can.readthedocs.io/en/latest/) library is excellent.

### Wrappers for astronomical hardware

Abstract your system onto the network using [network sockets](https://en.wikipedia.org/wiki/Network_socket).  Examples for basic client and server operations can be found in most languages [like C](http://www.thegeekstuff.com/2011/12/c-socket-programming/?utm_source=feedburner) and [python](https://docs.python.org/3.7/howto/sockets.html).  This lets you control your instrument using scripts or a GUI without impacting the hardware or low-level control software itself.

INDI, the [Instrument Neutral Distributed Interface](http://indilib.org/about/discover-indi.html) is a nifty way to wrap up multiple elements of an astronomical system into a clean, self-describing system.  

