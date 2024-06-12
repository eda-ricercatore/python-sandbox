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


	This script requires files with Python modules from the custom
		"utilities" Python package to generate a filename affix, using
		the timestamp or date-timestamp.
	


	Notes:
	[Welch2022] provides a summary of solutions in text, and in tables
		[jezrael2021],
		that summarize the similarities and differences between methods
		from the shutil module.
	[Welch2022] provides additional methods to copy files, particularly
		those base on creating file objects for file input processing
		and file output processing.
	+ [Sun2022] provides an interesting method via creating file objects
		for file input processing and file output processing.




	References:
	+ [DrakeJr2023i, The Python Standard Library: File and Directory Access: shutil -- High-level file operations: Directory and files operations]
		https://docs.python.org/3/library/shutil.html
	+ [DrakeJr2023i, The Python Standard Library: Text Processing Services: string -- Common string operations: Helper functions]
		https://docs.python.org/3/library/string.html#helper-functions
	+ [DrakeJr2023i, The Python Standard Library: Built-in Types: Text Sequence Type -- str: String Methods]
		https://docs.python.org/3/library/stdtypes.html#str.split



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

#	Import modules and functions from the Python Standard Library.
# Module to support file copying and file deletion [DrakeJr2023i, The Python Standard Library: File and Directory Access: shutil -- High-level file operations: Directory and files operations].
import shutil

# OS module to enumerate the specified directory.
from os import walk
# Glob module to use regular expressions to filter out files.
import glob
# Pathlib module for recursive enumeration of a specified directory.
from pathlib import Path


#####################################################################

#	Import Custom Python Modules

# Package and module to generate filename affix with timestamp.
from utilities.generate_results_filename import generate_filename


#####################################################################


# ===================================================================

# Global variables.

source_file_path				= "./source-files/makefile"
destination_directory			= "./destination-files/"
"""
	Use the str.split(sep=None, maxsplit=-1) function to tokenize the destination file path.
	[DrakeJr2023i, The Python Standard Library: Built-in Types: Text Sequence Type -- str: String Methods]
	[DrakeJr2023i, The Python Standard Library: Text Processing Services: string -- Common string operations: Helper functions]

	Use negative list indexing to access the last element of the list
		of string tokens obtained from the tokenization of strings.
	[DrakeJr2023m, The Python Tutorial: 3. An Informal Introduction to Python: 3.1. Using Python as a Calculator: 3.1.2. Text and 3.1.3. Lists]
"""
destination_filename			= source_file_path.split("/")[-1]
print("	Destination filename is:", destination_filename,"=")
destination_file_path			= destination_directory + destination_filename
print("	Destination file path is:", destination_file_path,"=")
filename_extension				= ".md"


# ===================================================================

"""
	Method to generate a filename affix and update the destination
		file path with the filename affix.
	@param None, since no paramaters or input arguments are needed.
	@return updated destination file path with filename suffix.
	O(1) method.
"""
def updated_destination_file_path_with_filename_suffix(destn_fpath, fname_extn):
	print("	Generate a filename affix with the current date and time stamp.")
	filename_affix = generate_filename.create_filename("")
	# Add the filename affix and filename extension as a suffix to the filename.
	filename_suffix = "-" + filename_affix + fname_extn
	print("	Filename suffix is:",filename_suffix,"=")
	destn_fpath		= destn_fpath + filename_suffix
	print("	Updated destination file path with suffix is:", destn_fpath,"=")
	return destn_fpath


# ===================================================================

print("Testing Solution #1.")
# Create a destination file path with current time stamp.
destination_file_path = updated_destination_file_path_with_filename_suffix(destination_file_path, filename_extension)
"""
	Solution #1.
	Copy the source file to the destination location with the appended filename suffix.
	Method does not require the use of creating file objects for file copying.
	Methid also does not copy metadata associated with the source file.
"""
shutil.copyfile(source_file_path,destination_file_path)
print("Testing Solution #2.")
# Reset destination file path.
destination_file_path			= destination_directory + destination_filename
"""
	Create another destination file path with current time stamp,
		so that we can distinguish the effects of trying the previous
		method, Solution #1, and this current method, Solution #2.
"""
destination_file_path = updated_destination_file_path_with_filename_suffix(destination_file_path, filename_extension)
"""
	Solution #2.
	Method does not require the use of creating file objects for file copying.
	Methid copies partial metadata associated with the source file for file's permission mode.

"""
shutil.copy(source_file_path,destination_file_path)
print("Testing Solution #3.")
# Reset destination file path.
destination_file_path			= destination_directory + destination_filename
"""
	Create another destination file path with current time stamp,
		so that we can distinguish the effects of trying the previous
		methods, Solution #1 and Solution #2, and this current method,
		Solution #3.
"""
destination_file_path = updated_destination_file_path_with_filename_suffix(destination_file_path, filename_extension)
"""
	Solution #3.
	Method does not require the use of creating file objects for file copying.
	Methid copies metadata associated with the source file for file's permission mode.
"""
shutil.copy2(source_file_path,destination_file_path)


print("Testing Solution #4.")
# Reset destination file path.
destination_file_path			= destination_directory + destination_filename
"""
	Create another destination file path with current time stamp,
		so that we can distinguish the effects of trying the previous
		methods, Solution #1, Solution #2, and Solution #3, and this
		current method, Solution #4.
"""
destination_file_path = updated_destination_file_path_with_filename_suffix(destination_file_path, filename_extension)
"""
	Solution #4.
	Method does not require the use of creating file objects for file copying.
	Methid copies metadata associated with the source file for file's permission mode.
"""
open(destination_file_path, 'wb').write(open(source_file_path, 'rb').read())









