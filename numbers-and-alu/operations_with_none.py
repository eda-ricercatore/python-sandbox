#!/usr/local/bin/python3

###!/Users/zhiyang/anaconda3/bin/python3


"""
	This Python script is written by Zhiyang Ong to experiment with
		operations involving 'None' objects.


	Synopsis:
	Automatically run operations for 'None' objects.

	This script can be executed as follows:
	./operations_with_none.py



	Notes:
	+ 



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


a = "Ciao tutti!"
if a is not None:
	print("= String value of a:",a,"=")
else:
	print("= String VALUE of a:",a,"=")
a = None
if a is not None:
	print("= VALUE of a:",a,"=")
else:
	print("= Value of a:",a,"=")
b = ""
if b is not None:
	print("= Value of b:",b,"=")
else:
	print("= VALUE of b:",b,"=")

