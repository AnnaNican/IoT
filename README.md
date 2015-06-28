# IoT

## Installation

This works really well for a RPi connected to an Arduino.

On your RPi, you need to run these as root (ie run `sudo -i` first):

	apt-get update
	apt-get install python-pip
	pip install pyserial

TODO: check that this works on fresh RPi.

## Notes

You can program an Arduino from your laptop then plug it into the PI
when you are ready to run. The Arduino always runs the last program 
that was flashed onto it.
