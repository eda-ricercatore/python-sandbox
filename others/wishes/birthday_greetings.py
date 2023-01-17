"""
	Python script to wish people, "Happy Birthday," repeatedly
		whenever it is their birthday.
	If they run the program indefinitely on their birthday
		(in 2025, 2030, or 2100), it will keep wishing them,
		"Happy Birthday!"
	
	This Python code snippet can be run at:
		https://replit.com/languages/python3
"""
#	Import Python module from Python Standard Library for operations about dates.
import datetime
#	Call function of the aforementioned module to determine the current date.
now = datetime.datetime.now()
#	While it is your birthday, ...
while "08-30" == now.strftime('%m-%d'):
	# Keep wishing you, "Happy Birthday!"
	print('Happy Birthday, Dr. BLAH!')
