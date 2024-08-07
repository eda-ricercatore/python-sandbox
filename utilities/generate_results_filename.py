#!/opt/local/bin/python3.12

###	#!/opt/homebrew/bin/python3
###	#!/usr/local/bin/python3


###	#!/opt/anaconda3/bin/python

###!/Users/zhiyang/anaconda3/bin/python3

"""
	This is written by Zhiyang Ong to generate a filename to store
		experimental data/results from running experiments, and/or
		automated software regression testing and hardware regression
		verification.



	Synopsis: command name and [argument(s)]
	./generate_results_filename.py [-h]

	Parameters:
	[input BibTeX file]:	A BibTeX database.

	[-h]				:	If an optional "-h" flag is used as an
							input argument, show the brief user manual
							and exit (terminate the program).


	Its procedure is described as follows:
	If the optional "-h" flag is specified,
		display the brief user manual.
	Get the current date and time in the DD-MM-YY-HH-MM-SS-uS format,
		and create an empty file named after the current date and time.


	Notes/Assumptions:
	Since I would be categorizing and storing the experimental results
		based on the year and month, the filename containg experimental
		results would be named in the DD-MM-YY-HH-MM-SS-uS format so that
		I can quickly find the file of a given build (or experimental
		run) as I read the filename from left to right.



	References:
	[SaltyCrane2014]
		Eliot "Salty Crane", "How to get the current date and time in Python," from Salty Crane Blog, June 26, 2008. Available online from Salty Crane Blog at: https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/; modified on October 22, 2014; self-published; August 31, 2018 was the last accessed date

	[DrakeJr2016b, datetime module, Section 8.1.4 datetime Objects, now() function]

	[DrakeJr2023i, The Python Standard Library: Generic Operating System Services: time -- Time access and conversions: Functions]
		https://docs.python.org/3/library/time.html#time.strptime
		https://docs.python.org/3/library/time.html#time.strftime


	Revision History:
	April 17, 2017			Version 0.1, initial build.
"""


#	The MIT License (MIT)

#	Copyright (c) <2014-2017> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; print " "; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d "\n" | tr -d 'ir' | tr y "\n"
#	Che cosa significa?

#	==========================================================

__author__ = 'Zhiyang Ong'
__version__ = '0.2'
__date__ = 'Apr 17, 2017'

###############################################################

"""
	Import modules from The Python Standard Library.
	sys			Get access to any command-line arguments.
	os			Use any operating system dependent functionality.
	os.path		For pathname manipulations.

	subprocess -> call
				To make system calls.
	time		To measure elapsed time.
	warnings	Raise warnings.
	re			Use regular expressions.
	filecmp		For file comparison.
"""

import sys
import os
import os.path
from subprocess import call
import time
import warnings
import re
import filecmp
from datetime import date
import datetime

###############################################################

#	Import Custom Python Modules

# Module to process input arguments to the script/program.
#from utilities.queue_ip_arguments import queue_ip_args


###############################################################
class generate_filename:
	##	Method to generate a filename affix for the results of
	#		the experimental/simulation run, or execution of
	#		the automated regression testing (for software) or
	#		automated regression verification.
	#	@return - Affix/Suffix for the filename based on the
	#		date-timestamp.
	#	O(1) method.
	@staticmethod
	def create_filename_affix_strptime(file_extension = ".txt"):
		"""
			From [DrakeJr2023i, The Python Standard Library: Generic Operating System Services: time -- Time access and conversions: Functions]:
			The format for the date-timestamp is provided for the
				following fields:
			+ month
			+ date
			+ year
			+ hour
			+ minute
			+ second
			+ microsecond

			Additional Notes:
			time.strptime() does not work with the "%f" directive
				to obtain the current time with microsecond precision.
		"""
		current_time = time.strptime("%B-%d-%Y-%H-%M-%S-%f")
		current_time = current_time + file_extension
		return current_time
	##	Method to generate a filename affix for the results of
	#		the experimental/simulation run, or execution of
	#		the automated regression testing (for software) or
	#		automated regression verification.
	#	@return - Affix/Suffix for the filename based on the
	#		date-timestamp.
	#	O(1) method.
	@staticmethod
	def create_filename_affix_strftime(file_extension = ".txt"):
		"""
			From [DrakeJr2023i, The Python Standard Library: Generic Operating System Services: time -- Time access and conversions: Functions]:
			The format for the date-timestamp is provided for the
				following fields:
			+ month
			+ date
			+ year
			+ hour
			+ minute
			+ second
			+ microsecond
		"""
		current_time = time.strftime("%B-%d-%Y-%H-%M-%S-%f")
		current_time = current_time + file_extension
		return current_time
	##	Method to generate a filename for the results of the
	#		experimental/simulation run, or execution of the
	#		automated regression testing (for software) or
	#		automated regression verification.
	#	@return - Affix/Suffix for the filename based on the
	#		date-timestamp.
	#	O(1) method.
	@staticmethod
	def create_filename(file_extension = ".txt"):
		"""
			Generate filename to store experimental/simulation
				results [SaltyCrane2014]
				[DrakeJr2016b, datetime module, Section 8.1.4 datetime Objects, now() function].
		"""
		now = datetime.datetime.now()
		"""
		print("Current date and time using instance attributes:")
		print("Current year: %d" % now.year)
		print("Current month: %d" % now.month)
		print("Current day: %d" % now.day)
		print("Current hour: %d" % now.hour)
		print("Current minute: %d" % now.minute)
		print("Current second: %d" % now.second)
		print("Current microsecond: %d" % now.microsecond)
		print("")
		print("Current date and time using strftime:")
		print(now.strftime("%Y-%m-%d %H:%M"))
		print("")
		print("Current date and time using isoformat:")
		print(now.isoformat())
		print("")
		"""
		current_time = str(now.day) + "-" + str(now.month) + "-" + str(now.year) + "-" + str(now.hour) + "-"  + str(now.minute) + "-"  + str(now.second) + "-"  + str(now.microsecond) + file_extension
		#print(current_time)
		return current_time
	# ============================================================
	##	Method to determine if the user wants help, and conequently
	#		display the user manual.
	#	O(n) method, with respect to the number of input arguments.
	@staticmethod
	def check_if_help_wanted():
		# If user wants to read the brief user manual,
		if "-h" in sys.argv:
			# Display the user manual and exit.
			print("-------------------------------------------------")
			print("==>	This script generates a filename based on.")
			print("	the date and time.")
			print("")
			print("This script can be executed as follows:")
			print("./generate_results_filename.py [-h]")
			print("")
			print("An optional '-h' flag can be used as any input argument")
			print("	to show the brief user manual and exit.")
			print("")
			print("-------------------------------------------------")













###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	generate_filename.check_if_help_wanted()
	print("===================================================")
	print("Generate filename to store experimental/simulation results.")
	print("")
	print("Create filename: datetime.datetime.now()")
	filename = generate_filename.create_filename()
	print("filename is:",filename,"=")
	print("")
	print("Create filename: time.strptime()")
	filename = generate_filename.create_filename_affix_strptime()
	print("filename is:",filename,"=")
	print("")
	print("Create filename: time.strftime()")
	filename = generate_filename.create_filename_affix_strftime()
	print("filename is:",filename,"=")
	print("	= end =")


#	Python database management
#	Python: date, time, now, string
#	Add references.
#	[Hetland2005] [Lutz2010] [Lutz2011] [Sileika2010] [Younker2008].
#	[Beazley2009, Chp. 17,25]
