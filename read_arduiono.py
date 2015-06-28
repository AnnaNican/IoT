###read from arduino

import serial
ser = serial.Serial('/dev/tty.usbserial', 9600)
while True: