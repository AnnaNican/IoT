###write to sqlite database python

import sqlite3 as lite
import sys
import time
import datetime

import serial

# ---------------------------------------------------------------------
#                                                           Utilities
# ---------------------------------------------------------------------
def tableExists( cursor, tableName ):
	'''Returns true if `tableName` exists in `cursor`'''
	cursor.execute( '''SELECT name FROM sqlite_master WHERE
		type='table' AND
		name=(?)
	''', (tableName,) )
	return cursor.fetchone() != None

# ---------------------------------------------------------------------
#                                               Connections: Database
# ---------------------------------------------------------------------

con = None
try:
    con = lite.connect('test')
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print "SQLite version: %s" % data
except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)

# ---------------------------------------------------------------------
#                                               Connections: Arduino
# TODO: Better device name handling
# ---------------------------------------------------------------------

try:
	ser = serial.Serial('/dev/ttyACM0', 9600)
except:
	# probably should handle this better
	print 'Could not connect to arduino'
	sys.exit(1)

# ---------------------------------------------------------------------
#                                                     Setup: Database
# ---------------------------------------------------------------------
# Creates a 'light' and 'temperature' table for storing data

if not tableExists( cur, 'light' ):
	cur.execute('''create table light (
		time text,
		date text,
		value int
	)''')

if not tableExists( cur, 'temperature' ):
	cur.execute('''create table temperature (
		time text,
		date text,
		value int
	)''')

# ---------------------------------------------------------------------
#                                                                Main
# ---------------------------------------------------------------------
# Does the actual work
# TODO: limit data saving to once per minute or similar
# WARNING: serial connection does not work reliably when sending 1 
# message per minute

while True:
	line = ser.readline()
	line.strip( '\n' )
	currentTime = time.strftime("%H:%M:%S")
	currentDate = datetime.date.today().strftime("%m_%d_%Y")
	print '%s @ %s %s' % (line, currentDate, currentTime)
	(light,temperature) = line.split( ',' )
	cur.execute( 'insert into light values (?,?,?)', (
		currentTime,
		currentDate,
		light
	) )
	cur.execute( 'insert into light values (?,?,?)', (
		currentTime,
		currentDate,
		temperature
	) )

# ---------------------------------------------------------------------
#                                                               Extra
# ---------------------------------------------------------------------
# Notes and stuff, not currently used

#get and parse values
#value_light = #whatever you are getting from arduiono
#value_temp

###check if the database exists else create it 
# with con:
#     cur.execute("CREATE TABLE LIGHT( CUR_TIME TEXT, CUR_DATE TEXT, CUR_VALUE Int)")

with con:
	# cur.execute ("SELECT * FROM LIGHT;")
	# print cur.fetchall()
    cur.execute("INSERT INTO LIGHT VALUES (?,?,?)", (str(time), str(datestamp), int(value_light)))

with con:
	cur.execute ("SELECT * FROM LIGHT;")
	print cur.fetchall()


#print tha

# finally:
    
#     if con:
#         con.close()
