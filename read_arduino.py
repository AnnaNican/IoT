###read from arduino

import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
	line = ser.readline()
	print line
	(light,temp) = line.split( ',' )
	print int(light)
	print int(temp)
	#print ser.read()