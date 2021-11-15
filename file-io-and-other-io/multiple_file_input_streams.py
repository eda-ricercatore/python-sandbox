#!/usr/local/bin/python3

###!/Users/zhiyang/anaconda3/bin/python3


"""
	This Python script is written by Zhiyang Ong to experiment with
		file read operations.


	Synopsis:
	Automatically test file read operations for multiple file streams.

	This script can be executed as follows:
	./multiple_file_input_streams.py





	Notes:
	+ The default mode for the open() method to open file input/output
		streams is the "read" mode [Brandl2017a, in \S7 Input and Output: \S 7.2. Reading and Writing Files].





	References:
	+ [Brandl2017a, in \S7 Input and Output: \S 7.2. Reading and Writing Files]



	Revision History:
	September 6, 2019			Version 0.1	Script.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'September 6, 2018'

#	The MIT License (MIT)

#	Copyright (c) <2019> <Zhiyang Ong>

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












# ===================================================================


"""
	Create multiple input file streams concurrently.

	We can also modify this for creating multiple output file streams
		concurrently.

	Reference:
	+ [Marnach2019]
		- Sven Marnach, Answer to `How can I open multiple files using ``with open'' in {Python}?', Stack Exchange, Inc., New York, NY, February 10, 2019. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/4617069/1531728 and https://stackoverflow.com/questions/4617034/how-can-i-open-multiple-files-using-with-open-in-python/4617069#4617069; November 13, 2021 was the last accessed date.
"""
print("= Try method #1 from [Marnach2019].")
with open("./test-cases/input-files/ip-file-1.md", "r") as ip_file_1, open("./test-cases/input-files/ip-file-2.md", "r") as ip_file_2, open("./test-cases/input-files/ip-file-3.md", "r") as ip_file_3:
	"""
		Use file_object.readline() method to read the next line from a file
			[Brandl2017a, in \S7 Input and Output: \S 7.2. Reading and Writing Files: \S7.2.1 Methods of File Objects].

		Read line #1.
	"""
	print(ip_file_1.readline())
	print(ip_file_2.readline())
	print(ip_file_3.readline())
	# Read line #2.
	ip_file_1.readline()
	ip_file_2.readline()
	ip_file_3.readline()
	# Read line #3.
	print(ip_file_1.readline())
	print(ip_file_2.readline())
	print(ip_file_3.readline())
	# Read line #3.
	ip_file_1.readline()
	ip_file_2.readline()
	ip_file_3.readline()
	# Read line #3.
	print(ip_file_1.readline())
	print(ip_file_2.readline())
	print(ip_file_3.readline())
"""
# Read nonexistent line from closed file object.
ip_file_1.readline()
ip_file_2.readline()
ip_file_3.readline()
"""





"""
	Reference:
	+ [Salgado2021]
		- Pablo Galindo Salgado, "What's New In Python 3.10: New Features: Parenthesized context managers", Python Software Foundation, Beaverton, OR, November 14, 2021. Available online from Python: Python 3.10.0 documentation: What's New In Python as Release 3.10.0 at: https://docs.python.org/3.10/whatsnew/3.10.html#parenthesized-context-managers; November 14, 2021 was the last accessed date.
"""
print("= Try method from [Salgado2021].")
#with (open("./test-cases/input-files/ip-file-1.md", "r") as ip_file_1, open("./test-cases/input-files/ip-file-2.md", "r") as ip_file_2, open("./test-cases/input-files/ip-file-3.md", "r") as ip_file_3):
with (
	open("./test-cases/input-files/ip-file-1.md", "r") as ip_file_1,
	open("./test-cases/input-files/ip-file-2.md", "r") as ip_file_2,
	open("./test-cases/input-files/ip-file-3.md", "r") as ip_file_3
	):
	"""
		Use file_object.readline() method to read the next line from a file
			[Brandl2017a, in \S7 Input and Output: \S 7.2. Reading and Writing Files: \S7.2.1 Methods of File Objects].

		Read line #1.
	"""
	print(ip_file_1.readline())
	print(ip_file_2.readline())
	print(ip_file_3.readline())
	# Read line #2.
	ip_file_1.readline()
	ip_file_2.readline()
	ip_file_3.readline()
	# Read line #3.
	print(ip_file_1.readline())
	print(ip_file_2.readline())
	print(ip_file_3.readline())
	# Read line #3.
	ip_file_1.readline()
	ip_file_2.readline()
	ip_file_3.readline()
	# Read line #3.
	print(ip_file_1.readline())
	print(ip_file_2.readline())
	print(ip_file_3.readline())











"""
	Reference:
	+ [Marnach2019]
		- Sven Marnach, Answer to `How can I open multiple files using ``with open'' in {Python}?', Stack Exchange, Inc., New York, NY, February 10, 2019. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/4617069/1531728 and https://stackoverflow.com/questions/4617034/how-can-i-open-multiple-files-using-with-open-in-python/4617069#4617069; November 13, 2021 was the last accessed date.
	+ [timgeb2020]
		- timgeb and Community Bot, Answer to `How can I open multiple files using ``with open'' in {Python}?', Stack Exchange, Inc., New York, NY, June 20, 2020. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/53363923/1531728 and https://stackoverflow.com/questions/4617034/how-can-i-open-multiple-files-using-with-open-in-python/53363923#53363923; November 13, 2021 was the last accessed date.
	+ [DrakeJr2016b, Python 3.10.0 Documentation: The Python Standard Library: Python Runtime Services: contextlib — Utilities for with-statement contexts: Utilities]
		- https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack
		- For version Python 3.10.0 Documentation.
		- Last accessed on November 14, 2021.
		- Last Modified on November 14, 2021.
"""
print("= Try method #2 from [Marnach2019].")
filenames = ["./test-cases/input-files/ip-file-1.md", "./test-cases/input-files/ip-file-2.md", "./test-cases/input-files/ip-file-3.md"]
with ExitStack() as stack:
	files = [stack.enter_context(open(fname)) for fname in filenames]
	"""
		Use file_object.readline() method to read the next line from a file
			[Brandl2017a, in \S7 Input and Output: \S 7.2. Reading and Writing Files: \S7.2.1 Methods of File Objects].

		Read line #1.
	"""
	print(files[0].readline())
	print(files[1].readline())
	print(files[2].readline())
	# Read line #2.
	files[0].readline()
	files[1].readline()
	files[2].readline()
	# Read line #3.
	print(files[0].readline())
	print(files[1].readline())
	print(files[2].readline())
	# Read line #3.
	files[0].readline()
	files[1].readline()
	files[2].readline()
	# Read line #3.
	print(files[0].readline())
	print(files[1].readline())
	print(files[2].readline())

























"""
	Attempted solutions that do not work.


	References:
	+ [Rands2021]
		- Chris Rands, Answer to `How can I open multiple files using ``with open'' in {Python}?', Stack Exchange, Inc., New York, NY, February 26, 2021. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/66388647/1531728 and https://stackoverflow.com/questions/4617034/how-can-i-open-multiple-files-using-with-open-in-python/66388647#66388647; November 13, 2021 was the last accessed date.
"""