#!/usr/local/bin/python3

###	#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
###	#!/Users/zhiyang/anaconda3/bin/python3
###	#!/Users/zhiyang/anaconda3/bin/python




"""
	This is written by Zhiyang Ong to copy and delete files.

	Assume that the current working directory can allow the following:
	+ file creation
	+ file deletion
	Essentially, it assumes that the current directory allows for
		file modification.


	
	This script can be executed as follows:
		./copy_n_delete_files.py
	


	Revision History:
	September 6, 2019			Version 0.1	Script.
	June 9, 2024				Version 0.2	Script.
"""





__author__ = 'Zhiyang Ong'
__version__ = '0.2'
__date__ = 'June 9, 2024'

#	The MIT License (MIT)

#	Copyright (c) <2024> <Zhiyang Ong>

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

#	Import packages and functions from the Python Standard Library.
# Module to support file copying and file deletion [DrakeJr2023i, The Python Standard Library: File and Directory Access: shutil -- High-level file operations: Directory and file operations].
#	https://docs.python.org/3/library/shutil.html
import shutil

# OS module to enumerate the specified directory.
from os import walk
# Glob module to use regular expressions to filter out files.
import glob
# Pathlib module for recursive enumeration of a specified directory.
from pathlib import Path


#####################################################################

#	Import Custom Python Modules

# Package and module to generate filename with time stamp.
from utilities.generate_results_filename import generate_filename


#####################################################################


# ===================================================================

# Global variables.

source_file_path				= "./source-files/makefile"
destination_directory			= "./destination-files/"
destination_filename			= source_file_path.split("/")[-1]
print("	Destination filename is:", destination_filename,"=")
destination_file_path			= destination_directory + destination_filename
print("	Destination file path is:", destination_file_path,"=")
filename_extension				= ".md"


# ===================================================================


print("	Generate a filename affix with the current date and time stamp.")
filename_affix = generate_filename.create_filename("")
# Add the filename affix and filename extension as a suffix to the filename.
filename_suffix = filename_affix + filename_extension
print("	Filename suffix is:",filename_suffix,"=")
destination_file_path			= destination_file_path + filename_suffix
print("	Updated destination file path with suffix is:", destination_file_path,"=")
shutil.copyfile(source_file_path,destination_file_path)

