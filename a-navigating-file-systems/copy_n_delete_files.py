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
	[Welch2022] provides a set of solutions in text and source code,
		and in tables [jezrael2021] [Sauthoff2018], that summarize
		the similarities and differences between methods from the
		shutil module.
	+ [jezrael2021] provides a comparison of the methods for the
		following attributes/characteristics:
		- copies metadata
		- copies permissions
		- uses file object
		- destination may be directory
	+ [Sauthoff2018] provides a comparison of the methods for the
		following attributes/characteristics:
		- preserves permissions
		- supports directory destination
		- accepts file objects
		- copies other metadata


	[Welch2022] provides additional methods to copy files, particularly
		those base on creating file objects for file input processing
		and file output processing.
	+ [Sun2022] provides an interesting method via creating file objects
		for file input processing and file output processing.
	+ [Kalimuthu2020] uses commands for UNIX-like operating systems to
		copy the files via the following options:
		- os.popen()
		- os.system()
		- subprocess.call()




	References:
	+ [DrakeJr2023i, The Python Standard Library: File and Directory Access: shutil -- High-level file operations: Directory and files operations]
		https://docs.python.org/3/library/shutil.html
	+ [DrakeJr2023i, The Python Standard Library: Text Processing Services: string -- Common string operations: Helper functions]
		https://docs.python.org/3/library/string.html#helper-functions
	+ [DrakeJr2023i, The Python Standard Library: Built-in Types: Text Sequence Type -- str: String Methods]
		https://docs.python.org/3/library/stdtypes.html#str.split
	+ [DrakeJr2023i, The Python Standard Library: File and Directory Access: os.path -- Common pathname manipulations]
		https://docs.python.org/3/library/os.path.html#os.path.basename
		https://docs.python.org/3/library/os.path.html#os.path.split
	+ [DrakeJr2023i, The Python Standard Library: File and Directory Access: filecmp -- File and Directory Comparisons]
		https://docs.python.org/3/library/filecmp.html
	+ [DrakeJr2023i, The Python Standard Library: Text Processing Services: difflib -- Helpers for computing deltas]
		https://docs.python.org/3/library/difflib.html


	Revision History:
	September 6, 2019			Version 0.1	Script.
	June 9, 2024				Version 0.2	Script.
	June 27, 2024				Version 0.3	Script. Add file comparison
									feature to check if copied file is
									the same as the source file, in its
									content.
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

# Module to compare files [DrakeJr2023i, The Python Standard Library: File and Directory Access: filecmp -- File and Directory Comparisons].
import filecmp


# OS module for functions to process the file path.
import os
# OS module to enumerate the specified directory.
#from os import walk
# Glob module to use regular expressions to filter out files.
#import glob
# Pathlib module for recursive enumeration of a specified directory.
#from pathlib import Path




# Module to process delta differences in sequence or file comparison.
import difflib





"""
	Import modules from the Python Standard Library concurrently
		in a line.
"""
#import shutil, filecmp, os, difflib



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
print("	Methd 1: Destination filename is:", destination_filename,"=")
destination_file_path			= destination_directory + destination_filename
print("	Methd 1: Destination file path is:", destination_file_path,"=")
"""
	Another approach to get the filename.
	[DrakeJr2023i, The Python Standard Library: File and Directory Access: os.path -- Common pathname manipulations]
	https://docs.python.org/3/library/os.path.html#os.path.basename

	IMPORTANT NOTE:
	This is the preferred approach.
	It is simple and does not require negative indexing of lists.
"""
destination_filename			= os.path.basename(source_file_path)
print("	Methd 2: Destination filename is:", destination_filename,"=")
destination_file_path			= destination_directory + destination_filename
print("	Methd 2: Destination file path is:", destination_file_path,"=")
"""
	Yet another approach to get the filename.
	[DrakeJr2023i, The Python Standard Library: File and Directory Access: os.path -- Common pathname manipulations]
	https://docs.python.org/3/library/os.path.html#os.path.split
"""
destination_filename			= os.path.split(source_file_path)[-1]
print("	Methd 3: Destination filename is:", destination_filename,"=")
destination_file_path			= destination_directory + destination_filename
print("	Methd 3: Destination file path is:", destination_file_path,"=")
# File extension.
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
if filecmp.cmp(source_file_path, destination_file_path, shallow=False):
	print("	Solution #1 works. Copied file and source file are the same.")
else:
	print("	Solution #1 fails. Copied file and source file differ.")
#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
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
if filecmp.cmp(source_file_path, destination_file_path, shallow=False):
	print("	Solution #2 works. Copied file and source file are the same.")
else:
	print("	Solution #2 fails. Copied file and source file differ.")
#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
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
if filecmp.cmp(source_file_path, destination_file_path, shallow=False):
	print("	Solution #3 works. Copied file and source file are the same.")
else:
	print("	Solution #3 fails. Copied file and source file differ.")
#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
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
	Solution #4 [Sun2022].
	Method does not require the use of creating file objects for file copying.
	Methid copies metadata associated with the source file for file's permission mode.
"""
open(destination_file_path, 'wb').write(open(source_file_path, 'rb').read())
if filecmp.cmp(source_file_path, destination_file_path, shallow=False):
	print("	Solution #4 works. Copied file and source file are the same.")
else:
	print("	Solution #4 fails. Copied file and source file differ.")
print("============================================================")
if filecmp.cmp("recursively-enumerate-dir.py", "a_os_path_methods.py", shallow=False):
	print("	'recursively-enumerate-dir.py' and 'a_os_path_methods.py' are the same.")
else:
	print("	'recursively-enumerate-dir.py' and 'a_os_path_methods.py' differ.")


print("============================================================")

print("=Implement file comparison approaches not yet explored.")

a_file = "/Applications/apps/comune/scripts/bibtex-analytics/notes/LICENSE"
another_file = "/Applications/apps/comune/scripts/bibtex-analytics/notes/mit-license.text"

with open(a_file, 'r') as ip_file_obj:
	ip_file_info = ip_file_obj.readlines()

with open(another_file, 'r') as op_file_obj:
	op_file_info = op_file_obj.readlines()

#set_of_differences = difflib.unified_diff(ip_file_info, op_file_info, ip_file_obj, op_file_obj, lineterm="")
set_of_differences = difflib.unified_diff(ip_file_info, op_file_info, a_file, another_file, lineterm="")
# Generator object cannot be printed.
#print("1) set_of_differences:",set_of_differences,"=")

#print("	=set_of_differences:",set_of_differences,"=")
#print(set_of_differences)
# Print each line in the generator object from the file comparison.
for current_line in set_of_differences:
	print("	=line is:",current_line,"=")
	#print(current_line)


print("============================================================")

with open(source_file_path, 'r') as ip_file_obj:
	ip_file_info = ip_file_obj.readlines()

with open(destination_file_path, 'r') as op_file_obj:
	op_file_info = op_file_obj.readlines()

#set_of_differences = difflib.unified_diff(ip_file_info, op_file_info, ip_file_obj, op_file_obj, lineterm="")
set_of_differences = difflib.unified_diff(ip_file_info, op_file_info, source_file_path, destination_file_path, lineterm="")
# Generator object cannot be printed.
#print("1) set_of_differences:",set_of_differences,"=")
#print(set_of_differences)

# Print each line in the generator object from the file comparison.
for current_line in set_of_differences:
	print("	=line is:",current_line,"=")

print("=Size of 'set_of_differences' is:",set_of_differences,"=")