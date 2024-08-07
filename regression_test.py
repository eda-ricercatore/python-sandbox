#!/usr/local/bin/python3

###	#!/Users/zhiyang/anaconda3/bin/python3
###	#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3


"""
	This Python script is written by Zhiyang Ong to perform automated
		regression testing.


	Synopsis:
	Perform automated regression testing of the common packages and
		their Python modules.

	This script can be executed as follows:
		./regression_test.py



	Commented out IPython magic to ensure Python compatibility.



	Revision History:
	September 6, 2019			Version 0.1	Script.
	June 7, 2024				Version 0.2	Script.
"""

__author__ = 'Zhiyang Ong'
__version__ = '0.2'
__date__ = 'September 6, 2019'

#	The MIT License (MIT)

#	Copyright (c) <2019> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person
#		obtaining a copy of this software and associated
#		documentation files (the "Software"), to deal in the
#		Software without restriction, including without
#		dlimitation the rights to use, copy, modify, merge, publish
#		distribute, sublicense, and/or sell copies of the Software,
#		and to permit persons to whom the Software is furnished
#		to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be
#		included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#		EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
#		WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
#		PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
#		OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#		OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
#		OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
#		THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; print " "; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d "\n" | tr -d 'ir' | tr y "\n"
#	Che cosa significa?



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

	pathlib->Path
				For mapping a string to a path.
	datetime	To obtain information about the current date and time.
	time		To obtain information about the current time.
				time_ns version provides information about the
					current time with nanosecond accuracy.
	warnings	Provide warnings to users without terminating the
					program abruptly.
	process_time (& process_time_ns)
				To determine the time stamp using the process
					time method, which is platform independent in
					Python 3.x, and its alternative providing
					nanosecond accuracy.
	perf_counter (& perf_counter_ns)
				To determine the time stamp using the process
					time method, which is platform independent in
					Python 3.x, and its alternative providing
					nanosecond accuracy.
	monotonic (& pm_monotonic_ns)
				To monotonically obtain time stamps, for performance
					measurement, and its alternative providing
					nanosecond accuracy.
"""

import sys
import os
import os.path
#from pathlib import Path
from subprocess import call
import time
import warnings
import re
import datetime
# ImportError: cannot import name 'perf_counter_ns'
from time import perf_counter as pc_timestamp
#from time import perf_counter_ns as pc_timestamp_ns
from time import process_time as pt_timestamp
#from time import process_time_ns as pt_timestamp_ns
#from time import time_ns as t_ns
from time import monotonic as pm_monotonic
#from time import monotonic_ns as pm_monotonic_ns

###############################################################
#	Import Custom Python Packages and Modules




# From the statistics_pkg package.
"""
	Package and module to print statistics of software testing
		results.
"""
from statistics_pkg.test_statistics import statistical_analysis
"""
	Package and module to test method(s) to print statistics of
		software testing results.
"""
from statistics_pkg.test_statistics_tester import statistical_analysis_tester
"""
	Package and module to perform miscellaneous tasks in data
		analysis.
"""
from statistics_pkg.data_analysis_tool import data_analysis
"""
	Package and module to test methods that perform miscellaneous
		tasks in data analysis.
"""
from statistics_pkg.data_analysis_tool_tester import data_analysis_tester




# From the utilities package.
# Package and module to process input arguments to the script/program.
from utilities.queue_ip_arguments import queue_ip_args
"""
	Package and module to test processing of input arguments to the
		script/program.
"""
from utilities.queue_ip_arguments_tester import queue_ip_args_tester
# Package and module to perform file I/O operations.
from utilities.file_io import file_io_operations
# Package and module to test methods that perform file I/O operations.
from utilities.file_io_tester import file_io_operations_tester
"""
	Package and module to configure the software application's
		parameters.
"""
from utilities.configuration_manager import config_manager
"""
	Package and module to test methods that configure the software
		application's parameters.
"""
from utilities.configuration_manager_tester import config_manager_tester
# Package and module to generate filename with time stamp.
from utilities.generate_results_filename import generate_filename
"""
	Package and module to test methods that generate filename with
		time stamp.
"""
from utilities.generate_results_filename_tester import generate_filename_tester
"""
	Package and module to perform methods in the miscellaneous
		class.
"""
from utilities.miscellaneous import misc
"""
	Package and module to test methods that perform methods in the
		miscellaneous class.
"""
from utilities.miscellaneous_tester import misc_tester
# Package and module to perform date and time operations.
from utilities.date_time_processing import date_time_operations
# Package and module that tests methods to perform date and time operations.
from utilities.date_time_processing_tester import date_time_operations_tester
#	Packages and modules to throw/raise custom exceptions.
"""
	Package and module to throw/raise the custom exception
		graph_exception.
"""
from utilities.custom_exceptions.graph_error import graph_error
"""
	Package and module to test methods that throw/raise the custom
		exception graph_exception.
"""
#from utilities.custom_exceptions.graph_error_tester import graph_error_tester
#import utilities.custom_exceptions.graph_error_tester
from utilities.custom_exceptions.graph_error_tester import graph_error_test
# From the utilities.timing_measurements subpackage of Python modules.
# Package and module that compute the factorial of a number.
from utilities.timing_measurements.get_factorial import calculate_factorial
# Package and module that test methods to compute the factorial of a number.
from utilities.timing_measurements.get_factorial_tester import calculate_factorial_tester
#	Package and subpackage to measure the current time.
# Package and module with methods to measure the current time.
from utilities.timing_measurements.performance_measurement_no_ns import execution_time_measurement_no_ns
# Package and module that test methods to measure the current time.
from utilities.timing_measurements.performance_measurement_no_ns_tester import execution_time_measurement_no_ns_tester
# Package and module with methods to measure the current time.
from utilities.timing_measurements.performance_measurement import execution_time_measurement
# Package and module that test methods to measure the current time.
from utilities.timing_measurements.performance_measurement_tester import execution_time_measurement_tester






# Main method for the program.
                                                                                                                                                    
#	If this is executed as a Python script,
if __name__ == "__main__":
	print("==================================================")
	print("Testing package: statistics_pkg.")
	print("Testing module: statistics_pkg.test_statistics.")
	statistical_analysis_tester.test_statistical_analysis()
	print("")
	print("Testing module: statistics_pkg.data_analysis_tool.")
	data_analysis_tester.test_data_analysis()
	print("==================================================")
	print("==================================================")
	print("Testing package: utilities.")
	print("Testing module: utilities.queue_ip_arguments.")
	queue_ip_args_tester.test_queue_ip_args()
	print("")
	print("Testing module: utilities.file_io.")
	file_io_operations_tester.test_file_io_operations()
	print("")
	print("Testing module: utilities.configuration_manager.")
	config_manager_tester.test_configure_sw_application_parameters()
	print("")
	print("Testing module: utilities.generate_results_filename.")
	generate_filename_tester.test_filename_generation_methods()
	print("")
	print("Testing module: utilities.miscellaneous.")
	misc_tester.test_miscellaneous_methods()
	print("")
	print("Testing module: utilities.date_time_processing.")
	date_time_operations_tester.test_date_time_operations()
	print("")
	print("Testing module: utilities.custom_exceptions.graph_error.")
	graph_error_test.test_raising_graph_error()
	print("")
	print("Testing module: utilities.timing_measurements.get_factorial.")
	calculate_factorial_tester.test_get_factorial_methods()
	print("")
	print("Testing module: utilities.timing_measurements.performance_measurement_no_ns.")
	execution_time_measurement_no_ns_tester.test_current_time_measurement_methods()
	print("")
	print("Testing module: utilities.timing_measurements.performance_measurement.")
	execution_time_measurement_tester.test_current_time_measurement_methods()
	print("==================================================")
	print("==================================================")
	statistical_analysis.print_statistics_of_software_testing()
