#!/Users/zhiyang/anaconda3/bin/python

"""
	This is written by Zhiyang Ong to modify the UNIX shebang of
		scripts or computer programs.

	It does not process any input arguments from users, so that
		we can avoid input processing.
	
	It requires the user to specify the current/original UNIX shebang
		and the preferred/target UNIX shebang.
	
	It only modifies files to change the UNIX shebang from the
		current/original UNIX shebang to the preferred/target
		shebang.
	
	It does not generate additional files.
	
	IMPORTANT NOTES:
	Assume that since I am checking if the first line of a text file
		file has the original UNIX shebang, I am also checking
		if the file is of a given file type.
	
	Regarding UNIX file types, see the following:
	+ https://en.wikipedia.org/wiki/Unix_file_types
	+ https://en.wikipedia.org/wiki/Text_file
	+ https://en.wikipedia.org/wiki/Binary_file
	
	
	
	References:
	+ Chaurasia2020
		- Vikram 'sid779' `Nihari Nalli' Chaurasia, "How to use Glob() function to find files recursively in Python?", from GeekstoGeeks: Tutorials: Languages: Python Programming Language, GeekstoGeeks, Noida, Uttar Pradesh, India, April 25, 2020.
			Available online at: https://www.geeksforgeeks.org/how-to-use-glob-function-to-find-files-recursively-in-python/;
				last accessed on October 17, 2021.
	
	
"""

#	Import packages and functions from the Python Standard Library.
# OS module to enumerate the specified directory.
from os import walk
# Glob module to use regular expressions to filter out files.
import glob
# Pathlib module for recursive enumeration of a specified directory.
from pathlib import Path
# Datetime module for processing elapsed time.
import datetime


###############################################################

#	Import Custom Python Modules

# Module to process input arguments to the script/program.
#from utilities.queue_ip_arguments import queue_ip_args
# Module to perform file I/O (input/output) operations.
#from utilities.file_io import file_io_operations

"""
	Unless this script is hosted in the parent Git directory
"""

#from timing_measurements.performance_measurement_no_ns import execution_time_measurement_no_ns
from timing_measurements.performance_measurement import execution_time_measurement
#from utilities.timing_measurements.performance_measurement_no_ns import execution_time_measurement_no_ns

# ===================================================================

# Global variables.

# Old and new UNIX shebangs.
original_unix_shebang = "#!/opt/local/bin/octave"
new_unix_shebang = "#!/usr/local/bin/octave"
# File extension for text files to process.
#file_extension = "./**/*.m"
file_extension = "/Users/zhiyang/Documents/progetti/interview-preparation/octave-sandbox/**/*.m"
#file_extension = "/Users/zhiyang/Documents/progetti/interview-preparation/octave-sandbox/*.m"
#####file_extension = "/Users/zhiyang/Documents/progetti/interview-preparation/octave-sandbox/**/*.m"
#file_extension = "?.m"
# Working directory to enumerate
working_directory = "."


# ===================================================================


print("= Modifying the UNIX shebang for scripts...")


"""
	Method to enumerate the specified directory, using the
		"os.walk" method.
	
	####TO BE FIXED
	Bug:
	+ Does not recursively enumerate subdirectorie to list
		their files.
		- This is a critical specification for the script.
	+ Currently, this method FAILS!!!

	This
	Reference:
	+ [Karnivaurus2016]
		- Karnivaurus, "Python: os.walk() with enumeration",
			Stack Exchange Inc.: Stack Overflow: Questions,
			Stack Exchange, Inc., New York, NY, March 24, 2016.
			Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/q/36211707/1531728 and https://stackoverflow.com/questions/36211707/python-os-walk-with-enumeration; last accessed on October 18, 2021.
"""
def enumerate_specified_directory_walk(specified_dir_path):
	print("Enumerating the directory:",specified_dir_path,"=")
	for (directory_path, directory_names, filenames) in walk(specified_dir_path):
		print("List of files are:",filenames,"=")
		print("List of directories are:",directory_names,"=")
		print("List of directory paths are:",directory_path,"=")


"""
	Method to enumerate the specified directory, using the
		"enumerate()" and "os.walk()" methods.
	
	+ This method works.
	+ It would take a significant amount of work to make use of the results.
	+ Proposed approach.
		- Combine the filename with the directory path to get the
			relative/absolute path of the file.


	Reference:
	+ [Embree2016]
		- Ralph `zondo' Embree, "Python: os.walk() with enumeration",
			Stack Exchange Inc.: Stack Overflow: Questions,
			Stack Exchange, Inc., New York, NY, March 24, 2016.
			Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/36211735/1531728 and https://stackoverflow.com/questions/36211707/python-os-walk-with-enumeration/36211735#36211735; last accessed on October 18, 2021.
"""
def enumerate_specified_directory_enumerate_walk(specified_dir_path):
	print("Enumerating the directory:",specified_dir_path,"=")
	for directory_number, (directory_path, directory_names, filenames) in enumerate(walk(specified_dir_path)):
		print("List of files are:",filenames,"=")
		print("List of directories are:",directory_names,"=")
		#if ".git" == directory_names[len(directory_names)-1]:
		if (0 < len(directory_names)) and (".git" == directory_names[-1]):
			directory_names.remove(".git")
		print("Updated list of directories are:",directory_names,"=")
		print("List of directory paths are:",directory_path,"=")
		print("Directory number:",directory_number,"=")


# Enumerate the current directory
#enumerate_specified_directory("./")
#enumerate_specified_directory(".")
#enumerate_specified_directory()

"""
	Method to enumerate the specified directory, using the
		"glob.glob" method.
	
	This method fails to work.
	
	Reference:
	[Chaurasia2020]
"""
def enumerate_specified_directory_glob():
	#for path_to_file in glob.glob(file_extension,recursive=True):
	for path_to_file in glob.glob("*",recursive=True):
		print("path_to_file is:",path_to_file,"=")





"""
	Method to enumerate the specified directory, using the
		Path().glob() method from pathlib.
	
	The chosen regular expression selects files with the
		file extension ".m" and filters off other files.

	Reference:
	+ 
"""
def enumerate_specified_directory_pathlib_path_rglob():
	#for path_to_file in Path(file_extension).glob("**/*"):
	for path_to_file in Path(working_directory).rglob("*.m"):
		print("path_to_file is:",path_to_file,"=")








"""
	Method to enumerate the specified directory, using the
		Path().glob() method from pathlib.
	
	####TO BE FIXED
	Bug:
	+ Does not recursively enumerate subdirectorie to list
		their files.
		- This is a critical specification for the script.
	+ Currently, this method FAILS!!!


	Reference:
	+ 
"""
def enumerate_specified_directory_pathlib_glob():
	for path_to_file in Path(working_directory).glob("*.m"):
		print("path_to_file is:",path_to_file,"=")
		# Create a file object for reading.
		print("=	Create a file object for reading.")
		ip_file_obj = open(ip_filename, 'r')
		print("=	Close the file object for reading.")
		ip_file_obj.close()






# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Main method.
# Enumerate the current directory.
# Type of current time measurement.
#mode_current_time_measurement = "perf_counter"
mode_current_time_measurement = "perf_counter_ns"
# Set the initial timestamp.
execution_time_measurement.set_initial_timestamp(mode_current_time_measurement)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
# Methods that work.
#enumerate_specified_directory_enumerate_walk(working_directory)
enumerate_specified_directory_pathlib_path_rglob()
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
"""
	Failed methods.
	#enumerate_specified_directory_walk(".")
	#enumerate_specified_directory_glob()
	#enumerate_specified_directory_pathlib_glob()
"""
print("= Fixed UNIX shebang for scripts.")
elapsed_time = execution_time_measurement.get_elapsed_time(mode_current_time_measurement)
#print("Elapsed time:::",datetime.timedelta(seconds=elapsed_time),"=")
one_billion = 1000000000
one_thousand = 1000
print("Elapsed time:::",datetime.timedelta(seconds=elapsed_time/one_billion),"=")
print("Elapsed time:::",datetime.timedelta(microseconds=elapsed_time/one_thousand),"=")
print("Elapsed time in nanoseconds:::",elapsed_time,"=")