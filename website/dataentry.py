import MySQLdb
import random
import re
from django.db import connection
from soc.config import *
conn = MySQLdb.connect(host= "127.0.0.1",
		user=DB_USER_DEFAULT,
		passwd=DB_PASS_DEFAULT,
		db=DB_NAME_DEFAULT)
x = conn.cursor()

def entry(code, example_id, dependency_exists):
	foo="exec"
	 
   

	b= 0
	c= 1303985023
	d= example_id

	print dependency_exists
	if foo in code:
		aa = code.find('exec(\'',1)	
		
		if aa > 0: 
			bb = code.find('\'',aa+7)	
			value = code[(aa+6):bb]
		
		else:
			aa = code.index('exec (\"')	
			if aa > 0:
				bb = code.find('\"',aa+7)
				value = code[(aa+7):bb]

			else :
				{
				}
		x.execute("""SELECT id FROM textbook_companion_dependency_files WHERE filename = %s""", [value]) #get the dependency id
		conn.commit()
		data = x.fetchone()  # extract the id 
		print data
		if data is not None:
			role = int(data[0])
			print role
			if not dependency_exists:
				print role
				x.execute(""" INSERT into textbook_companion_example_dependency (example_id, dependency_id, approval_status,timestamp) values (%s, %s, %s, %s)""", (d, role, b, c))   #insert new dependency file entry 
				conn.commit()
				
			
				dependency_exists= True
		conn.close()
	else:
		dependency_exists= False
	return dependency_exists 
		






