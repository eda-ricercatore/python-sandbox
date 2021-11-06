#!/usr/local/bin/python3

###	#!/Users/zhiyang/anaconda3/bin/python3





"""
	This Python script is written by Zhiyang Ong to experiment with
		calling Linux/UNIX commands.


	Synopsis:
	Call Linux/UNIX commands from this Python script.

	This script can be executed as follows:
	./run_unix_linux_commands.py



	References from my BibTeX database.
	+ For running UNIX/Linux commands:
		- [Loreto2019]
	+ For string processing for the output of running UNIX/Linux commands:
		- [Roman2010]




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
# [Loreto2019]
import os
import os.path
#from pathlib import Path
from subprocess import call
import time
import warnings
import re
import datetime
import time
# For random number generation.
import random
# [Loreto2019]
from subprocess import call
# [DrakeJr2016b]
from subprocess import run
# [DrakeJr2016b]
from subprocess import Popen
# [DrakeJr2016b]
from subprocess import PIPE





# ===================================================================

"""
	Run Linux/UNIX commands from the command line, via the
		Terminal application.
"""
print("===================================================================")
print("Run UNIX/Linux commands from the command line, via the Terminal application.")
print("")


print("= Method 1: os.system()")
"""
	Reference:
	+ [Loreto2019]
		- Bruno `Kira' Loreto, Answer to "Execute shell commands in Python," Stack Exchange Inc., New York, NY, February 27, 2019. Available online from Stack Exchange Inc.: Unix & Linux Stack Exchange: Questions at: https://unix.stackexchange.com/a/238185/395331 and https://unix.stackexchange.com/questions/238180/execute-shell-commands-in-python/238185#238185; March 7, 2020 was the last accessed date.
"""
os.system("/usr/local/bin/python3 -V")
#os.system("/Frameworks/Python.framework/Versions/3.10/bin/python3 -V")




# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


print("= Method 2: subprocess.call()")
"""
	Method 2 subprocess.call() is "safer, more powerful and likely faster"
		than Method 1 os.system() [Loreto2019].

	Reference:
	+ [Loreto2019]
		- Bruno `Kira' Loreto, Answer to "Execute shell commands in Python," Stack Exchange Inc., New York, NY, February 27, 2019. Available online from Stack Exchange Inc.: Unix & Linux Stack Exchange: Questions at: https://unix.stackexchange.com/a/238185/395331 and https://unix.stackexchange.com/questions/238180/execute-shell-commands-in-python/238185#238185; March 7, 2020 was the last accessed date.
"""
#call("/Frameworks/Python.framework/Versions/3.10/bin/python3 -V")
#call("/Frameworks/Python.framework/Versions/3.10/bin/python3 -V", shell=True, check=True, capture_output=True)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


print("= Method 3: subprocess.run()")
"""
	Reference:
	+ [DrakeJr2016b]
"""
#run(["/Frameworks/Python.framework/Versions/3.10/bin/python3", "-V"], shell=True, check=True, capture_output=True)
#std_output = run(["/usr/local/bin/python3", "-V"], shell=True, check=True, capture_output=True)
#std_output = run(["/usr/local/bin/python3", "-V"], shell=True, check=True)
#run(["/usr/local/bin/python3", "-V"], shell=True, check=True)
run(["/usr/local/bin/python3", "-V"])
#run("exit()", shell=True, check=True)
run("exit", shell=True, check=True)
#run(["/usr/local/bin/python3", "-V"], capture_output=True)
#print("std_output:",std_output,"=")


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


print("= Method 4: subprocess.Popen()")
"""
	Reference:
	+ [DrakeJr2016b]
"""
Popen(["/usr/local/bin/python3", "-V"])
proc_obj = Popen(["/usr/local/bin/python3", "-V"])
#print("Popen.stdout",Popen.stdout,"=")
#print("Popen.stdout",proc_obj.stdout.read(),"=")
#####print("Popen.stdout",proc_obj.stdout,"=")

#run("exit", shell=True, check=True)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


print("= Method 5: subprocess.Popen() with stdout=PIPE")
"""
	Reference:
	+ [DrakeJr2016b]
"""
with Popen(["/usr/local/bin/python3", "-V"], stdout=PIPE) as proc:
#with Popen(["/usr/local/bin/python3", "-V"], stdout=subprocess.PIPE) as proc:
	#print(proc.stdout.read())
	#	b'Python 3.10.0\n'
	python_version = proc.stdout.read()
	python_version_copy_1 = str(python_version)
	"""
		Reference:
		+ [Roman2010]
			- Roman, Answer to ``Extract string from between quotations,'' Stack Exchange Inc., New York, NY, January 16, 2010. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/2076399/1531728 and https://stackoverflow.com/questions/2076343/extract-string-from-between-quotations/2076399#2076399; November 5, 2021 was the last accessed date.

	"""
	print("	> Method 5a: get Python version between quotes via string.split().")
	python_version = str(python_version).split("'")
	python_version = python_version[1][:-2]
	print("	python_version is:",python_version,"=")
	print("	Stored Python version as a string.")
	python_version = python_version_copy_1
	#print("	python_version is:",python_version,"=")
	"""
		Reference:
		+ 
			- akhilmd, Answer to "Stripping string in python between quotes", Stack Exchange Inc., New York, NY, July 2, 2016. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/38161072/1531728 and ; November 5, 2021 was the last accessed date.
	"""
	print("	> Method 5b: get Python version between quotes via re.findall().")
	python_version = re.findall("\'(.*?)\'",str(python_version))
	#python_version = re.findall('"\'([^"]*)\'"',str(python_version))
	#python_version = re.findall('"([^"]*)"',str(python_version))
	python_version = python_version[0][:-2]
	#python_version = python_version[1]
	print("	python_version is:",python_version,"=")





# ===================================================================