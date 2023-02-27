#!/Users/zhiyang/anaconda3/bin/python

#	#!/usr/local/bin/python3


"""
	This is written by Zhiyang Ong to simplify the validation of paths
		for target output files.
	It checks if the path for the output file is exists and is writeable.
	If it is, we can create the output file.
	Else, get the absolute path of the target output file.
		Get the path of the directory that would contain this target output file.
		Check if this directory exists.
		If this directory exists, we can create the output file.
		Else, inform the user to select a path for the output file
			that would be stored in a valid directory.



	Synopsis: command name and [argument(s)]
	./verify_output_file_path.py

	



	Notes/Assumptions:
	+ BLAH...


	References:
	+ [DrakeJr2023a]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Standard Library," Python Software Foundation, Beaverton, OR, February 26, 2023. Available online from *Welcome to Python.org: Docs: Python 3.11.2 documentation: Library Reference* at: https://docs.python.org/3/library/; February 26, 2023 was the last accessed date.



	



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
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	#	= Set up loading of BibTeX database
	# Type of current time measurement.
	mode_current_time_measurement = "perf_counter"
	# Set the initial timestamp.
	execution_time_measurement_no_ns.set_initial_timestamp()
	"""
		Filename/path of the output file that contains the extracted BibTeX entries.
	"""
	output_filename = "./output-files/extracted_bibtext_entries.bib"
	# --------------------------------------------------------
	"""
		Check if the output filename is valid [DrakeJr2023a, from Generic Operating System Services: os — Miscellaneous operating system interfaces: Files and Directories].

		https://docs.python.org/3/library/os.html#os.access
		https://docs.python.org/3/library/os.html#os.W_OK
	"""
	if os.access(output_filename, os.W_OK):
		print("	Filename/Path to target output filename is valid:",output_filename,"=")
	else:
		print(">>>	Filename/Path to target output filename is invalid:",output_filename,"=")
		"""
			Get the absolute path containing the target output file.

			https://docs.python.org/3/library/os.path.html#os.path.abspath
		"""
		absolute_path_of_target_output_file = os.path.abspath(output_filename)
		print("	Path of target output:",absolute_path_of_target_output_file,"=")
		"""
			This approach only grabs the filename.
		path_of_directory_for_target_output_file = os.path.basename(output_filename)
		print("	Path of the directory for target output:",path_of_directory_for_target_output_file,"=")
		"""
		"""
			Get the path of the directory that would contain the target output file.

			https://docs.python.org/3/library/os.path.html#os.path.dirname
		"""
		path_of_directory_for_target_output_file = os.path.dirname(absolute_path_of_target_output_file)
		print("	Path of the directory for target output:",path_of_directory_for_target_output_file,"=")
		"""
			Is directory that would contain output file a valid directory?

			https://docs.python.org/3/library/os.path.html#os.path.isdir
		"""
		if os.path.isdir(path_of_directory_for_target_output_file):
			print("	Path of the directory for target output is valid.")
			print("	Target output file can be created.")
		else:
			print("	Path of the directory for target output is INVALID!!!")
			print("	Target output file cannot be created!!!")
			print("	Please kindly select path for output file in an existing directory!!!")
	output_filename = "./non-existent-directory/random_bibtex_database_non_existent.bib"
	if os.access(output_filename, os.W_OK):
		print("	Filename/Path to target output filename is valid:",output_filename,"=")
	else:
		print(">>>	Filename/Path to target output filename is invalid:",output_filename,"=")
		absolute_path_of_target_output_file = os.path.abspath(output_filename)
		print("	Path of target output:",absolute_path_of_target_output_file,"=")
		path_of_directory_for_target_output_file = os.path.dirname(absolute_path_of_target_output_file)
		print("	Path of the directory for target output:",path_of_directory_for_target_output_file,"=")
		if os.path.isdir(path_of_directory_for_target_output_file):
			print("	Path of the directory for target output is valid.")
			print("	Target output file can be created.")
		else:
			print("	Path of the directory for target output is INVALID!!!")
			print("	Target output file cannot be created!!!")
			print("	Please kindly select path for output file in an existing directory!!!")
	output_filename = "./output-files/z-empty-file.md"
	if os.access(output_filename, os.W_OK):
		print(">>>	Filename/Path to target output filename is valid:",output_filename,"=")
	else:
		print(">>>	Filename/Path to target output filename is invalid:",output_filename,"=")
	# --------------------------------------------------------
	# Get the elapsed time.
	elapsed_time = execution_time_measurement_no_ns.get_elapsed_time(mode_current_time_measurement)
	#temp_text = "Elapsed time:::"+str(datetime.timedelta(seconds=elapsed_time))+"=\n"
	print("Elapsed time:::",datetime.timedelta(seconds=elapsed_time),"=")