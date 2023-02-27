#!/usr/local/bin/python3


"""
	This is written by Zhiyang Ong to test input argument processing.



	Synopsis: command name and [argument(s)]
	./z_sys_arg_for_loop.py
	./z_sys_arg_for_loop.py [-h]
	./z_sys_arg_for_loop.py [-h] [-k] [set of BibTeX keys stored as a CSV file]
	./z_sys_arg_for_loop.py [-h] [-m] [set of keyphrases stored as a CSV file]
	./z_sys_arg_for_loop.py [-h] [-k] [set of BibTeX keys stored as a CSV file] [-m] [set of keyphrases stored as a CSV file]
	./z_sys_arg_for_loop.py [-k] [set of BibTeX keys stored as a CSV file] [-m] [set of keyphrases stored as a CSV file] [-h]
	./z_sys_arg_for_loop.py [-k] [set of BibTeX keys stored as a CSV file] [-h] [-m] [set of keyphrases stored as a CSV file]


	Parameters:
	[input BibTeX file]:	A BibTeX database.

	[-h]:					If an optional "-h" flag is used as an
								input argument, print the help manual.

	[-k]:					If an optional "-k" flag is used as an
								input argument, check if the next input
								argument exists and if it refers to an
								existing input file.
								If these conditions are not satisfied,
									print the help manual.
								Subsequently, check that the input file
								is a valid CSV file.
									This subsequent check allows the
										use of the "with" statement for
										input/output file processing,
										which is recommended as opposed
										to error processing with the
										traditional pair of open and
										close statements for input/output
										file objects.

	[-m]:					If an optional "-m" flag is used as an
								input argument, check if the next input
								argument exists and if it refers to an
								existing input file.
								If these conditions are not satisfied,
									print the help manual.
								Subsequently, check that the input file
								is a valid CSV file.
									This subsequent check allows the
										use of the "with" statement for
										input/output file processing,
										which is recommended as opposed
										to error processing with the
										traditional pair of open and
										close statements for input/output
										file objects.

	[-a]:					If an optional "-a" flag is used as an
							input argument, check if the next input
								argument exists.
								If this condition is not satisfied,
									print the help manual.
								Since this condition is a string by
									default, no further checks are
									required.

	[-z]:					If an optional "-z" flag is used as an
							input argument, check if the next input
								argument exists.
								If this condition is not satisfied,
									print the help manual.
								Since this condition is a string by
									default, no further checks are
									required.


	[-b]:					If an optional "-y" flag is used as an
							input argument, check if the next input
								argument exists.
								If this condition is not satisfied,
									print the help manual.
								Since this condition is a string by
									default, no further checks are
									required.

	[-j]:					If an optional "-j" flag is used as an
							input argument, check if the next input
								argument exists.
								If this condition is not satisfied,
									print the help manual.
								Since this condition is a string by
									default, no further checks are
									required.

	[-s]:					If an optional "-s" flag is used as an
							input argument, check if the next input
								argument exists.
								If this condition is not satisfied,
									print the help manual.
								Since this condition is a string by
									default, no further checks are
									required.

	[-u]:					If an optional "-u" flag is used as an
							input argument, check if the next input
								argument exists.
								If this condition is not satisfied,
									print the help manual.
								Since this condition is a string by
									default, no further checks are
									required.




	Its procedure is described as follows:
	
	Process input arguments.
	If the [-h] input argument/option is selected,
		print the help manual with the synopsis of the command name
		and argument(s).
	Enumerate each input system argument for this Python script.
		If the [-k] input argument/option is selected,
			check if the next input argument exists and if it refers
			to an existing input file.
			If these conditions are not satisfied,
				print the help manual.
			Subsequently, check that the input file is a valid CSV file.
				This subsequent check allows the use of the "with"
					statement for input/output file processing,
					which is recommended as opposed to error processing
					with the traditional pair of open and close
					statements for input/output file objects.
			If the [-m] input argument/option is also selected,
				find the subset of these records that have keyphrases
				found in the set of keyphrases, and print out information about these records into an output file.
			Similarly, if multiple options are selected, process them here.
		If the [-m] input argument/option is selected,
			check if the next input argument exists and if it refers
			to an existing input file.
			If these conditions are not satisfied,
				print the help manual.
			Subsequently, check that the input file is a valid CSV file.
				This subsequent check allows the use of the "with"
					statement for input/output file processing,
					which is recommended as opposed to error processing
					with the traditional pair of open and close
					statements for input/output file objects.
		If the [-a] input argument/option is selected,
			check if the next input argument exists.
			If this condition is not satisfied,
				print the help manual.
			Since this condition is a string by default,
				no further checks are required.
		If the [-z] input argument/option is selected,
			check if the next input argument exists.
			If this condition is not satisfied,
				print the help manual.
			Since this condition is a string by default,
				no further checks are required.
		If the [-b] input argument/option is selected,
			check if the next input argument exists.
			If this condition is not satisfied,
				print the help manual.
			Since this condition is a string by default,
				no further checks are required.
		If the [-j] input argument/option is selected,
			check if the next input argument exists.
			If this condition is not satisfied,
				print the help manual.
			Since this condition is a string by default,
				no further checks are required.
		If the [-s] input argument/option is selected,
			check if the next input argument exists.
			If this condition is not satisfied,
				print the help manual.
			Since this condition is a string by default,
				no further checks are required.
		If the [-u] input argument/option is selected,
			check if the next input argument exists.
			If this condition is not satisfied,
				print the help manual.
			Since this condition is a string by default,
				no further checks are required.
		If no input argument/option is selected, print the help manual.
		



	Notes/Assumptions:
	CSV refers to comma-separated values, and is a delimited text file
		that uses commas (or ",") to separate/delimit values.

	Since the installation of packages via PyPI are placed in the Anaconda
		"Conda" environment, and my Python environment is dependent on the
		"Conda" package and environment management system, I have to use
		the Python interpreter from Conda to use the PyPI package installations.
	Else, I can use other Python interpreters, one of which is commented out
		to enable the usage of the Python interpreter from Conda.





	References:
	+ [DrakeJr2023a]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Standard Library," Python Software Foundation, Beaverton, OR, February 26, 2023. Available online from *Welcome to Python.org: Docs: Python 3.11.2 documentation: Library Reference* at: https://docs.python.org/3/library/; February 26, 2023 was the last accessed date.
	+ [DrakeJr2023b]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Tutorial," Python Software Foundation, Beaverton, OR, February 26, 2023. Available online from *Welcome to Python.org: Docs: Python 3.11.2 documentation: Tutorial* at: https://docs.python.org/3/tutorial/; February 26, 2023 was the last accessed date.







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


###############################################################

#	Import Python Modules from installed Python packages, via PyPI


# Requires the following installation.
#pip install bibtexparser
# Import [Boulogne2022] [Boulogne2023a]
#import bibtexparser




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


# Options for the script.
# [-h] option for the script.
h_option = "-h"
# [-k] option for the script.
k_option = "-k"
# [-m] option for the script.
m_option = "-m"
# [-a] option for the script.
a_option = "-a"
# [-z] option for the script.
z_option = "-z"
# [-b] option for the script.
b_option = "-b"
# [-j] option for the script.
j_option = "-j"
# [-s] option for the script.
s_option = "-s"
# [-u] option for the script.
u_option = "-u"




# --------------------------------------------------------

"""
	Method to print the "help" manual for this script, and a synopsis
		of how to use it, using the name of this script and set of
		acceptable input arguments.
	@param None - No input arguments.
	@return Nothing.
"""
def print_help_manual():
	print("--------------------------------------------------------")
	print("")
	print("Synopsis of using: z_sys_arg_for_loop.py")
	print("")
	print("./z_sys_arg_for_loop.py [-h] [-k] [input CSV file] [-m] [input CSV file] [-a] [string] [-z] [string] [-b] [string] [-j] [string] [-s] [string] [-u] [string]")
	print("")
	print("The only unary input argument is: [-h]")
	print("")
	print("Other input arguments come in pairs, 2-tuples: [flag] [filename or string]")
	print("")
	print("Acceptable flags for 2-tuples input arguments are: [-k] [-m] [-a] [-z] [-b] [-j] [-s] [-u]")
	print("")


"""
	Flag to indicate it the next input argument in the command for
		this script is a filename, rather than a string.

	Boolean true value indicates that the next argument is a filename.
	Else, it indicates a string.
"""
#filename_not_string = False


# --------------------------------------------------------

"""
	Process the input arguments [DrakeJr2023a, from Python Runtime Services: sys — System-specific parameters and functions: sys.argv].

	https://docs.python.org/3/library/sys.html
"""

# Are there any input arguments?
if 1 < len(sys.argv):
	# Yes. Is the [-h] option/flag is used?
	if h_option in sys.argv:
		# Yes, print the help manual. Skip subsequent processing of [-h].
		print_help_manual()
		# Is the number of 
	"""
		Enumerate the options of the program.

		If the [-h] option is encountered, skip its processing.
	"""
	# List of input arguments.
	#list_of_input_arguments = sys.argv[1:]
	iterator_for_list_of_input_arguments = enumerate(sys.argv[1:])
	#for index, option in enumerate(sys.argv[1:]):
	#for index, option in enumerate(list_of_input_arguments):
	for index, option in iterator_for_list_of_input_arguments:
		# Is this input argument the [-h] option?
		if h_option == option:
			"""
				Yes, skip its processing [DrakeJr2023b, from Section 4. More Control Flow Tools: Subsection 4.4. break and continue Statements, and else Clauses on Loops]

				https://docs.python.org/3/tutorial/controlflow.html
			"""
			continue
		elif k_option == option:
			print("= Processing the [-k] option.")
			print("index is:",index,"=")
			print("option is:",option,"=")
			#index = index + 1
			print("= Filename of input CSV file for the [-k] option.")
			print("index is:",index+1,"=")
			bibtex_key_csv_filename = next(iterator_for_list_of_input_arguments)[1]
			print("option is:",bibtex_key_csv_filename,"=")
			"""
				Is the filename/path for the CSV file containing BibTeX keys valid?

				Or, does that file or path exist?
			"""
			if not os.path.isfile(bibtex_key_csv_filename):
				# No, it does not exist.
				print(">>>	filename is invalid:", bibtex_key_csv_filename,"=")
			# Else, proceed.
			#print("option is:",next(iterator_for_list_of_input_arguments),"=")
			# The next input argument should be a filename.
			#filename_not_string = True
		else:
			# Else, process the next input argument.
			print("index is:",index,"=")
			print("option is:",option,"=")
else:
	# No, print the help manual.
	print_help_manual()









# --------------------------------------------------------
# Get the elapsed time.
elapsed_time = execution_time_measurement_no_ns.get_elapsed_time(mode_current_time_measurement)
#temp_text = "Elapsed time:::"+str(datetime.timedelta(seconds=elapsed_time))+"=\n"
print("Elapsed time:::",datetime.timedelta(seconds=elapsed_time),"=")