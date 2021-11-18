#!/Users/zhiyang/anaconda3/bin/python

"""
	This is written by Zhiyang Ong to recursively enumerate a
		given directory.

	Use a regular expression to select files of interest, and
		filter off other files.

	It does not process any input arguments from users, so that
		we can avoid input processing.
	
	It does not generate files.
	
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







# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Main method.
print("= Recursively enumerate the specified directory.")
# Enumerate the current directory.
#enumerate_specified_directory_walk(".")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
#enumerate_specified_directory_enumerate_walk(working_directory)
enumerate_specified_directory_pathlib_path_rglob()
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
#enumerate_specified_directory_glob()
#enumerate_specified_directory_pathlib_glob()
print("= Finished the recursive enumeration of the specified directory.")
