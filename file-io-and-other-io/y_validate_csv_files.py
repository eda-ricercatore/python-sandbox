#!/Users/zhiyang/anaconda3/bin/python
#	#!/usr/local/bin/python3


"""
	This is written by Zhiyang Ong to validate comma-separated values
		(CSV) files.

	That is, it checks if CSV files abide by the CSV format.


	Synopsis: command name and [argument(s)]
	./y_validate_csv_files.py




	Notes/Assumptions:
	+ BLAH...




	References:
	+ [DrakeJr2023a]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Standard Library," Python Software Foundation, Beaverton, OR, February 26, 2023. Available online from *Welcome to Python.org: Docs: Python 3.11.2 documentation: Library Reference* at: https://docs.python.org/3/library/; February 26, 2023 was the last accessed date.
	+ [DrakeJr2023b]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Tutorial," Python Software Foundation, Beaverton, OR, February 26, 2023. Available online from *Welcome to Python.org: Docs: Python 3.11.2 documentation: Tutorial* at: https://docs.python.org/3/tutorial/; February 26, 2023 was the last accessed date.
	+ [Miles2013]
		- Alistair Miles, "csvvalidator 1.2," Python Software Foundation, Beaverton, OR, May 16, 2013. Available online from *PyPI -- The Python Package Index: csvvalidator 1.2* as Version 1.2 at: https://pypi.org/project/csvvalidator/; February 25, 2023 was the last accessed date.







	Revision History:
	February 25, 2023			Version 0.1, initial build.
"""

#	The MIT License (MIT)

#	Copyright (c) <2023> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?

#	==========================================================

__author__ = 'Zhiyang Ong'
__version__ = '0.1'
__date__ = 'February 25, 2025'

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
	datetime	For operations regarding date and time.
"""

import sys
import os
import os.path
from subprocess import call
import time
import warnings
import re
import filecmp
import datetime
#import datetime.timedelta
from datetime import timedelta
"""
	Import the CSV [Miles2013] [DrakeJr2023a, from File Formats: csv — CSV File Reading and Writing].

	https://docs.python.org/3/library/csv.html
"""
import csv

###############################################################

#	Import Python Modules from installed Python packages, via PyPI


# Requires the following installations.
#pip install bibtexparser
#pip install csvvalidator
# Import [Boulogne2022] [Boulogne2023a]
#import bibtexparser



"""
	Import [Miles2013].
	This Python package from PyPI causes problems with finding
		the method: datetime.timedelta()
	
	A workaround is described as follows.

	Import the following in addition to: "import datetime"
	from datetime import timedelta

	Subsequently, use the following method call instead.

	timedelta()
"""
#import csvvalidator
from csvvalidator import *





###############################################################

#	Import Custom Python Modules

# Module to process input arguments to the script/program.
#from utilities.queue_ip_arguments import queue_ip_args
# Module to perform file I/O (input/output) operations.
#from utilities.file_io import file_io_operations


# Module for timing measurements.
from timing_measurements.performance_measurement_no_ns import execution_time_measurement_no_ns

###############################################################



#	= Set up loading of BibTeX database
# Type of current time measurement.
mode_current_time_measurement = "perf_counter"
# Set the initial timestamp.
execution_time_measurement_no_ns.set_initial_timestamp()

# --------------------------------------------------------


"""
	Method to validate a comma-separated values (CSV) file.
	@param csv_filename - Filename of the CSV file to be validated.
	@return boolean True, if csv_filename is a valid CSV file;
		else, return False.
"""
def validate_csv_file(csv_filename=None):
	#print("	csv_filename is:",csv_filename,"=")
	if None != csv_filename:
		validator = CSVValidator("Generic CSV file")
		csv_data = csv.reader(csv_filename)
		problems_with_csv_file = validator.validate(csv_data)
		#print("	problems_with_csv_file is:",problems_with_csv_file,"=")
		if not problems_with_csv_file:
			#print("	There are no problems with the CSV file.")
			return True
		else:
			#print("	There are problems with the CSV file!!!")
			#print("	problems_with_csv_file is:",problems_with_csv_file,"=")
			return False
	else:
		#print("	The csv_filename is:",csv_filename,"=")
		#print("	csv_filename is NOT 'None'.")
		return False



# --------------------------------------------------------


input_filename = "./input-files/bibtex_keys.csv"
print("Processing file:",input_filename,"=")
#validator = CSVValidator(field_names)
validator = CSVValidator("BibTeX keys")
csv_data = csv.reader(input_filename)
problems_with_csv_file = validator.validate(csv_data)
"""
	The following line of code raises the following: AttributeError.

	Since "problems_with_csv_file" is an empty list, by checking if
		it is an empty list, I can check if there are no problems in
		validating the CSV file.
"""
#write_problems(problems_with_csv_file, sys.stdout)
print("problems_with_csv_file is:",problems_with_csv_file,"=")
if not problems_with_csv_file:
	print("	There are no problems with the CSV file.")
else:
	print("	There are problems with the CSV file!!!")
#csv_data = csv.reader("./input-files/keyphrases_as_metadata.csv")
input_filename = "./input-files/keyphrases_as_metadata.csv"
print("Processing file:",input_filename,"=")
if True == validate_csv_file(csv_filename=input_filename):
	print("	No problems with the CSV file for keyphrases.")
else:
	print("	There are problems with the CSV file for keyphrases!!!")
input_filename = "./input-files/keyphrases_as_metadata_with_quotes.csv"
print("Processing file:",input_filename,"=")
if validate_csv_file(csv_filename=input_filename):
	print("	No problems with the CSV file for keyphrases.")
else:
	print("	There are problems with the CSV file for keyphrases!!!")










# --------------------------------------------------------
# Get the elapsed time.
elapsed_time = execution_time_measurement_no_ns.get_elapsed_time(mode_current_time_measurement)
#temp_text = "Elapsed time:::"+str(datetime.timedelta(seconds=elapsed_time))+"=\n"
#print("Elapsed time:::",datetime.timedelta(seconds=elapsed_time),"=")
print("Elapsed time:::",timedelta(seconds=elapsed_time),"=")
print("")
print("")