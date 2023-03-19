#!/usr/local/bin/python3

###!/Users/zhiyang/anaconda3/bin/python3


"""
	This Python script is written by Zhiyang Ong to experiment with
		concurrent input and output file streams.


	Synopsis:
	Automatically test file read and write operations for concurrent
		input and output file streams.

	This script can be executed as follows:
	./w_concurrent_ip_op_file_streams.py



	Notes:
	+ The default mode for the open() method to open file input/output
		streams is the "read" mode [Brandl2017a, in Section 7 Input and Output: Section 7.2. Reading and Writing Files].



	References:
	+ [DrakeJr2023b]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Tutorial," Python Software Foundation, Beaverton, OR, February 26, 2023. Available online from *Welcome to Python.org: Docs: Python 3.11.2 documentation: Tutorial* at: https://docs.python.org/3/tutorial/; February 26, 2023 was the last accessed date.
	+ [Brandl2017a, in Section7 Input and Output: Section 7.2. Reading and Writing Files]
		- Georg Brandl, Benjamin Peterson, Senthil Kumaran, Guido van Rossum, Chris Jerdonek, and Andrew Kuchling, "The Python Tutorial," Python Software Foundation, Beaverton, OR, March 26, 2017. Available online from *Welcome to Python.org: Python 3.6.1 documentation* at: https://docs.python.org/3/tutorial/; April 4, 2017 was the last accessed date.
	+ [DrakeJr2023a]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Standard Library," Python Software Foundation, Beaverton, OR, February 26, 2023. Available online from *Welcome to Python.org: Docs: Python 3.11.2 documentation: Library Reference* at: https://docs.python.org/3/library/; February 26, 2023 was the last accessed date.
	+ [DrakeJr2016b]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Standard Library," Python Software Foundation, Beaverton, OR, March 23, 2016. Available online from *Welcome to Python.org: Python 3.5.1 documentation* at: https://docs.python.org/3/library/; April 1, 2016 was the last accessed date.



	Revision History:
	September 6, 2019			Version 0.1	Script.
	March 16, 2023				Version 1.0 Script
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'March 16, 2023'

#	The MIT License (MIT)

#	Copyright (c) <2023> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?


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
	time	To obtain information about the current time.
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
import time
# For method #2 from [Marnach2019].
from contextlib import ExitStack
# From [DrakeJr2016b, File and Directory Access: fileinput — Iterate over lines from multiple input streams]
import fileinput
# From [DrakeJr2023a, from File and Directory Access: filecmp -- File and Directory Comparisons]
import filecmp



# ===================================================================


"""
	Create multiple input file streams concurrently.

	We can also modify this for creating multiple output file streams
		concurrently.

	Reference:
	+ [Marnach2019]
		- Sven Marnach, Answer to `How can I open multiple files using ``with open'' in {Python}?', Stack Exchange, Inc., New York, NY, February 10, 2019. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/4617069/1531728 and https://stackoverflow.com/questions/4617034/how-can-i-open-multiple-files-using-with-open-in-python/4617069#4617069; November 13, 2021 was the last accessed date.
	+ [DrakeJr2023b]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Tutorial," Python Software Foundation, Beaverton, OR, February 26, 2023. Available online from *Welcome to Python.org: Docs: Python 3.11.2 documentation: Tutorial* at: https://docs.python.org/3/tutorial/; February 26, 2023 was the last accessed date.
"""
print("= Try method #1 from [Marnach2019].")
input_file_path = "./input-files/ip-file-1.md"
output_file_path = "./output-files/op-file-1.md"
#with open("./test-cases/input-files/ip-file-1.md", "r") as ip_file_1, open("./test-cases/output-files/op-file-1.md", "w") as op_file_1:
with open(input_file_path, "r") as ip_file_1, open(output_file_path, "w") as op_file_1:
	"""
		Use file_object.readline() method to read the next line from a file
			[Brandl2017a, in Section 7 Input and Output: Section 7.2. Reading and Writing Files: Section 7.2.1 Methods of File Objects].

		Read line #1 from input file, and copy this line to the output file by writing to it [DrakeJr2023b, from Section 7. Input and Output: 7.2. Reading and Writing Files].

		#### IMPORTANT NOTES:
		"Warning Calling f.write() without using the with keyword or calling f.close() might result in the arguments of f.write() not being completely written to the disk, even if the program exits successfully."
		+ Hence, all file input/output operations must use the "with"
			statement or ensure that the input/output file streams
			are closed.
	"""
	current_line_ip_file = ip_file_1.readline()
	print(current_line_ip_file)
	op_file_1.write(current_line_ip_file)
	# Read line #2.
	current_line_ip_file = ip_file_1.readline()
	print(current_line_ip_file)
	op_file_1.write(current_line_ip_file)
	# Read line #3.
	current_line_ip_file = ip_file_1.readline()
	print(current_line_ip_file)
	op_file_1.write(current_line_ip_file)


# Check if input and output file streams are closed properly.
if ip_file_1.closed and op_file_1.closed:
	print("= File streams are closed properly: ip_file_1 and op_file_1.")
if filecmp.cmp(input_file_path, output_file_path, shallow=False):
	print("= ip_file_1 and op_file_1 are equivalent.")
else:
	print("= ip_file_1 and op_file_1 are DIFFERENT!!!")




print("====================================")
print("	End of script.")
print("====================================")
