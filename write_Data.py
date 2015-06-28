###write to sqlite database python

import sqlite3 as lite
import sys
import time, datetime



###########
#connect

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
    


time = time.strftime("%H:%M:%S")
datestamp = datetime.date.today().strftime("%m_%d_%Y")

#get and parse values
#value_light = #whatever you are getting from arduiono
#value_temp


###check if the database exists else create it 
# with con:
#     cur.execute("CREATE TABLE LIGHT( CUR_TIME TEXT, CUR_DATE TEXT, CUR_VALUE Int)")

with con:
	# cur.execute ("SELECT * FROM LIGHT;")
	# print cur.fetchall()
    cur .execute("INSERT INTO LIGHT VALUES (?,?,?)", (str(time), str(datestamp), int(value_light)))


with con:
	cur.execute ("SELECT * FROM LIGHT;")
	print cur.fetchall()


#print tha

# finally:
    
#     if con:
#         con.close()
