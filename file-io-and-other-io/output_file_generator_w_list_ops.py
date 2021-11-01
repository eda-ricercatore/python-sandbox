#!/Users/zhiyang/anaconda3/bin/python3

###	#!/usr/local/bin/python3



"""
	This Python script is written by Zhiyang Ong to experiment with writing
		to output files.


	Synopsis:
	Automatically test file write operations.

	This script can be executed as follows:
	./output_file_generator.py




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






# ===================================================================

# Generate the test data set.

# Generate the data.
#list_1 = [range(35,50)]

list_1 = range(10,20)
list_2 = [x+1 if x >= 15 else x+2 for x in list_1]
# Turn a 
list_3 = [x for x in list_1]
print("list 1 is:",list_1,"=")
print("list 2 is:",list_2,"=")
print("list 3 is:",list_3,"=")


list_1 = range(35,50)
list_2 = [x+1 if x >= 45 else x+5 for x in list_1]
list_3 = [x^2 if x >= 45 else x+2 for x in list_1]
list_4 = [x for x in list_1]
print("list 1 is:",list_1,"=")
print("list 2 is:",list_2,"=")
print("list 3 is:",list_3,"=")
print("list 4 is:",list_4,"=")






with open("test-cases/output-files/op-file-1.md", "w") as op_file_1:
	op_file_1.write("")



