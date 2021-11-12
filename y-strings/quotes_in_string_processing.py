#!/usr/local/bin/python3

###	#!/Users/zhiyang/anaconda3/bin/python3





"""
	This Python script is written by Zhiyang Ong to experiment with
		extracting substrings surrounded by quotation marks, or
		embedded within quotation marks.

	These quotation marks can be single quotes or double marks.


	Synopsis:
	Extract substrings within quotation marks.

	This script can be executed as follows:
	./quotes_in_string_processing.py



	References from my BibTeX database.
	+ For running UNIX/Linux commands:
		- [Loreto2019]
	+ For string processing for the output of running UNIX/Linux commands:
		- [Roman2010]
	+ [KiteStaff20XY] Kite staff, "How to get the substring between two markers in Python", from Kite: The Python Language: Kite Docs, Kite, San Francisco, CA. Available online from Kite: The Python Language: Kite Docs at: https://www.kite.com/python/answers/how-to-get-the-substring-between-two-markers-in-python; November 9, 2021 was the last accessed date.



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

#print("===========================================================")
print("============================================================")
print("Obtain substring(s) within quotation marks.")
print("")


"""
	Obtain substring(s) within single quotes.

	Test with different strings.
"""
print("Obtain substring(s) within single quotes.")

print("= Method 1: Test with output from UNIX/Linux command.")
"""
	Reference:
	+ [DrakeJr2016b]
"""
#with Popen(["/usr/local/bin/python3", "-V"], stdout=subprocess.PIPE) as proc:
with Popen(["/usr/local/bin/python3", "-V"], stdout=PIPE) as proc:
	#print(proc.stdout.read())
	#	b'Python 3.10.0\n'
	python_version = proc.stdout.read()
	python_version_copy_1 = str(python_version)
	"""
		Method 1a: Extract substring within quotation marks (single quotes),
			using string.split().

		Reference:
		+ [Roman2010]
			- Roman, Answer to ``Extract string from between quotations,'' Stack Exchange Inc., New York, NY, January 16, 2010. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/2076399/1531728 and https://stackoverflow.com/questions/2076343/extract-string-from-between-quotations/2076399#2076399; November 5, 2021 was the last accessed date.
		+ [Koledoye2016]
			- Moses Koledoye, Answer to ``Stripping string in python between quotes'', Stack Exchange, Inc., New York, NY, July 2, 2016. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/38160543/1531728 and https://stackoverflow.com/questions/38160518/stripping-string-in-python-between-quotes/38160543#38160543; November 6, 2021 was the last accessed date.
	"""
	#print("	> Method 1a: get substring between quotes via string.split().")
	print("	> Method 1a: get substring between quotes...")
	print("		via string.split().")
	print("		Assign result to a variable.")
	python_version = str(python_version).split("'")
	#print("		python_version is:",python_version,"=")
	"""
		Remove the last two characters of the second of three tokens obtained
			from delimiting the string with a single quote
	"""
	python_version = python_version[1][:-2]
	#python_version = python_version[1][:-1]
	print("		python_version is:",python_version,"=")
	#print("	Stored Python version as a string.")
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	# Try another method to extract substring within quotation marks (single quotes).
	python_version = python_version_copy_1
	#print("	python_version is:",python_version,"=")
	"""
		Method 1b: Extract substring within quotation marks (single quotes),
			using re.findall("\'(.*?)\'",string).

		Reference:
		+ [akhilmd2016]
			- akhilmd, Answer to "Stripping string in python between quotes", Stack Exchange Inc., New York, NY, July 2, 2016. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/38161072/1531728 and ; November 5, 2021 was the last accessed date.
	"""
	#print("	> Method 1b: get substring between quotes via re.findall(\"\'(.*?)\'\", my_string).")
	print("	> Method 1b: get substring between quotes...")
	print("		via re.findall(\"\'(.*?)\'\", my_string).")
	python_version = re.findall("\'(.*?)\'",str(python_version))
	#python_version = re.findall('"\'([^"]*)\'"',str(python_version))
	python_version = python_version[0][:-2]
	#python_version = python_version[1]
	print("		python_version is:",python_version,"=")



my_strings = ["SetVariables 'a' 'b' 'c' ", "d2efw  	f 'first' +&%#$%'second',vwrfhir, d2e	u'third' dwedew", "'uno'?>P>MNUIHUH~!@#$%^&*()_+=0trewq'due'		'tre'fef	fre f", "		'uno''dos'		'tres'", "'unu''doua''trei'", " 	 'um' 		    		 'dois'  		  'tres'   			 	  "]
my_substrings = []
"""
	Test with the loop/enumeration approach [Booboo2020], and modified
		regular expression from [Avinash2021] and [user17405772021]
		for substrings embedded within single quotes.

	Swap the positions of the double quotes and the single quotes
		for the modification.

	References:
	+ [Booboo2020]
	+ [Avinash2021]
	+ [user17405772021]
"""
print("= Method 1c: Get substring with ...")
print("	re.findall(\"'(.+?)'\", string) method.")
# Enumerate all the test strings.
for current_test_string in my_strings:
	"""
		For each test string, extract substrings embedded within
			single quotes.
	"""
	for values in re.findall("'(.+?)'", current_test_string):
		# Append found embedded substring into the list of substrings.
		my_substrings.append(values)
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
"""
	Test with the loop/enumeration approach [Booboo2020], and modified
		regular expression from [Lundberg2012] and [Avinash2021]
		for substrings embedded within single quotes.

	Swap the positions of the double quotes and the single quotes
		for the modification.

	References:
	+ [Booboo2020]
	+ [Lundberg2012]
	+ [Avinash2021]
"""
print("= Method 1d: Get substring with ...")
print("	re.findall(r\"\\\'(.+?)\\\'\", string) method.")
# Enumerate all the test strings.
for current_test_string in my_strings:
	"""
		For each test string, extract substrings embedded within
			single quotes.
	"""
	for values in re.findall(r"\'(.+?)\'", current_test_string):
		# Append found embedded substring into the list of substrings.
		my_substrings.append(values)
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
"""
	Test with the loop/enumeration approach [Booboo2020], and modified
		regular expression from [Lundberg2012] and [Avinash2021]
		for substrings embedded within single quotes.

	Swap the positions of the double quotes and the single quotes
		for the modification.

	References:
	+ [Booboo2020]
	+ [Lundberg2012]
	+ [Avinash2021]
"""
print("= Method 1e: Get substring with ...")
print("	re.findall(r\"\\\'(.*?)\\\'\", string) method.")
# Enumerate all the test strings.
for current_test_string in my_strings:
	"""
		For each test string, extract substrings embedded within
			single quotes.
	"""
	for values in re.findall(r"\'(.*?)\'", current_test_string):
		# Append found embedded substring into the list of substrings.
		my_substrings.append(values)
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
"""
	Test with the loop/enumeration approach [Booboo2020], and modified
		regular expression from [Pieters2014] for substrings embedded
		within single quotes.

	Swap the positions of the double quotes and the single quotes
		for the modification.

	References:
	+ [Booboo2020]
	+ [Pieters2014]
"""
print("= Method 1f: Get substring with ...")
print("	re.findall(r\"'([^\']*)'\", string) method.")
# Enumerate all the test strings.
for current_test_string in my_strings:
	"""
		For each test string, extract substrings embedded within
			single quotes.
	"""
	for values in re.findall(r"'([^']*)'", current_test_string):
		# Append found embedded substring into the list of substrings.
		my_substrings.append(values)
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
"""
	Test with the loop/enumeration approach [Booboo2020], and modified
		regular expression from [Shelvington2020] for substrings embedded
		within single quotes.

	Swap the positions of the double quotes and the single quotes
		for the modification.

	References:
	+ [Booboo2020]
	+ [Shelvington2020]
"""
print("= Method 1g: Get substring with ...")
print("	re.findall(\"'(.*?)'\", string) method.")
# Enumerate all the test strings.
for current_test_string in my_strings:
	"""
		For each test string, extract substrings embedded within
			single quotes.
	"""
	for values in re.findall("'(.*?)'", current_test_string):
		# Append found embedded substring into the list of substrings.
		my_substrings.append(values)
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
"""
	Test with the loop/enumeration approach [Booboo2020], and modified
		regular expression from [jspcal2014] for substrings embedded
		within single quotes.

	Swap the positions of the double quotes and the single quotes
		for the modification.

	References:
	+ [Booboo2020]
	+ [jspcal2014]
"""
print("= Method 1h: Get substring with ...")
print("	re.findall(\"'([^']*)'\", string) method.")
# Enumerate all the test strings.
for current_test_string in my_strings:
	"""
		For each test string, extract substrings embedded within
			single quotes.
	"""
	for values in re.findall("'([^']*)'", current_test_string):
		# Append found embedded substring into the list of substrings.
		my_substrings.append(values)
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
"""
	Test with the loop/enumeration approach [Booboo2020], and modified
		regular expression from [Martelli2013] for substrings embedded
		within single quotes.

	Swap the positions of the double quotes and the single quotes
		for the modification.

	References:
	+ [Booboo2020]
	+ [Martelli2013]
"""
print("= Method 1i: Get substring with ...")
print("	re.findall(\"'[^']*'\", string) method.")
# Enumerate all the test strings.
for current_test_string in my_strings:
	"""
		For each test string, extract substrings embedded within
			single quotes.
	"""
	for values in re.findall("'[^']*'", current_test_string):
		# Append found embedded substring into the list of substrings.
		my_substrings.append(values)
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	!!! Fails to extract the substrings without the")
print("		quotation marks (single quotes)!!!")
"""
	Test with the loop/enumeration approach [Booboo2020], and modified
		regular expression from [Muthupandi2019] for substrings embedded
		within single quotes.

	Swap the positions of the double quotes and the single quotes
		for the modification.

	References:
	+ [Booboo2020]
	+ [Muthupandi2019]
"""
print("= Method 1j: Get substring with ...")
print("	re.findall(r\"['](.*?)[']\", string) method.")
# Enumerate all the test strings.
for current_test_string in my_strings:
	"""
		For each test string, extract substrings embedded within
			single quotes.
	"""
	for values in re.findall(r"['](.*?)[']", current_test_string):
		# Append found embedded substring into the list of substrings.
		my_substrings.append(values)
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
"""
	Test with the loop/enumeration approach [Booboo2020], and modified
		regular expression from [Hassan2014] for substrings embedded
		within single quotes.

	Swap the positions of the double quotes and the single quotes
		for the modification.

	References:
	+ [Booboo2020]
	+ [Hassan2014]
"""
print("= Method 1k: Get substring with ...")
print("	re.findall(r\"'(.*?)(?<!\\\\)'\", string) method.")
# Enumerate all the test strings.
for current_test_string in my_strings:
	"""
		For each test string, extract substrings embedded within
			single quotes.
	"""
	for values in re.findall(r"'(.*?)(?<!\\)'", current_test_string):
		# Append found embedded substring into the list of substrings.
		my_substrings.append(values)
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
"""
	Test with the loop/enumeration approach [Booboo2020], and modified
		regular expression for substrings embedded within single
		quotes.

	Swap the positions of the double quotes and the single quotes
		for the modification.

	References:
	+ [Booboo2020]
"""
print("= Method 1l: Get substring with ...")
print("	re.findall(r\"'(?:(?:(?!(?<!\\\\)').)*)'\", string) method.")
# Enumerate all the test strings.
for current_test_string in my_strings:
	"""
		For each test string, extract substrings embedded within
			single quotes.
	"""
	for values in re.findall(r"'(?:(?:(?!(?<!\\)').)*)'", current_test_string):
		# Append found embedded substring into the list of substrings.
		my_substrings.append(values)
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	!!! Fails to extract the substrings without the")
print("		quotation marks (single quotes)!!!")















# ===================================================================


"""
	Obtain substring(s) within double quotes.

	Test with different strings.
"""
print("")
print("Obtain substring(s) within double quotes.")

"""
	Reference:
	+ [jspcal2014]
		- jspcal, Answer to "Extract string from between quotations", Stack Exchange Inc., New York, NY, March 14, 2014. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/2076356/1531728 and https://stackoverflow.com/questions/2076343/extract-string-from-between-quotations/2076356#2076356; November 6, 2021 was the last accessed date.
"""
#print("= Method 2a: Get substring with ... re.findall(\'\"([^\"]*)\"\', string).")
print("= Method 2a: Get substring with ...")
print("	re.findall(\'\"([^\"]*)\"\', string).")
my_string = 'SetVariables "a" "b" "c" '
my_substrings = re.findall('"([^"]*)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in English): one, two, three.
my_string = 'd2efw  	f "first" +&%#$%"second",vwrfhir, d2e	u"third" dwedew'
my_substrings = re.findall('"([^"]*)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Italian): one, two, three, and an empty string.
my_string = '"uno"?>P>MNUIHUH~!@#$%^&*()_+=0trewq"due"		"tre"fef	""fre f'
my_substrings = re.findall('"([^"]*)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Spanish): one, two, empty string, three.
my_string = '		"uno""dos"		"""tres"'
my_substrings = re.findall('"([^"]*)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Romanian): one, two, three.
my_string = '"unu""doua""trei"'
my_substrings = re.findall('"([^"]*)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Portuguese): empty string, one, two, three.
my_string = '"" 	 "um" 		    		 "dois"  		  "tres"   			 	  '
my_substrings = re.findall('"([^"]*)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in French): one, two, three, and an empty string.
my_string = ' 	 "une" 		    		 "deux"  		  "trois"   			 	  ""'
my_substrings = re.findall('"([^"]*)"', my_string)
print("	my_substrings are:",my_substrings,"=")
print("	> stores empty strings embedded within quotation marks.")
print("	> Method works.")






"""
	Reference:
	+ [Martelli2013]
		- Alex Martelli and Sumit Singh, Answer to "Extract string from between quotations", Stack Exchange Inc., New York, NY, March 14, 2014. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/2076357/1531728 and https://stackoverflow.com/questions/2076343/extract-string-from-between-quotations/2076357#2076357; November 6, 2021 was the last accessed date.
"""
print("= Method 2b: Get substring with ...")
print("	re.findall(\'\"[^\"]*\"\', string).")
my_string = 'SetVariables "a" "b" "c" '
my_substrings = re.findall('"[^"]*"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in English): one, two, three.
my_string = 'd2efw  	f "first" +&%#$%"second",vwrfhir, d2e	u"third" dwedew'
my_substrings = re.findall('"[^"]*"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Italian): one, two, three.
my_string = '"uno"?>P>MNUIHUH~!@#$%^&*()_+=0trewq"due"		"tre"fef	""fre f'
my_substrings = re.findall('"[^"]*"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Spanish): one, two, three.
my_string = '		"uno""dos"		"""tres"'
my_substrings = re.findall('"[^"]*"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Romanian): one, two, three.
my_string = '"unu""doua""trei"'
my_substrings = re.findall('"[^"]*"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Portuguese): one, two, three.
my_string = '"" 	 "um" 		    		 "dois"  		  "tres"   			 	  '
my_substrings = re.findall('"[^"]*"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in French): one, two, three, and an empty string.
my_string = ' 	 "une" 		    		 "deux"  		  "trois"   			 	  ""'
my_substrings = re.findall('"[^"]*"', my_string)
print("	my_substrings are:",my_substrings,"=")
print("	!!! Fails to extract the substrings without the")
print("		quotation marks (double quotes)!!!")
print("	> stores empty strings embedded within quotation marks.")
print("	> Method works.")









"""
	Reference:
	+ [Hassan2014]
		- Sabuj Hassan, Answer to ``Extract a string between double quotes'', Stack Exchange, Inc., New York, NY, March 29, 2014. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/22735480/1531728 and https://stackoverflow.com/questions/22735440/extract-a-string-between-double-quotes/22735480#22735480; November 6, 2021 was the last accessed date.
"""
print("= Method 2c: Get substring with ...")
print("	re.findall(r\'\"(.*?)(?<!\\)\"\', string).")
my_string = 'SetVariables "a" "b" "c" '
my_substrings = re.findall(r'"(.*?)(?<!\\)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in English): one, two, three.
my_string = 'd2efw  	f "first" +&%#$%"second",vwrfhir, d2e	u"third" dwedew'
my_substrings = re.findall(r'"(.*?)(?<!\\)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Italian): one, two, three.
my_string = '"uno"?>P>MNUIHUH~!@#$%^&*()_+=0trewq"due"		"tre"fef	""fre f'
my_substrings = re.findall(r'"(.*?)(?<!\\)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Spanish): one, two, three.
my_string = '		"uno""dos"		"""tres"'
my_substrings = re.findall(r'"(.*?)(?<!\\)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Romanian): one, two, three.
my_string = '"unu""doua""trei"'
my_substrings = re.findall(r'"(.*?)(?<!\\)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Portuguese): one, two, three.
my_string = '"" 	 "um" 		    		 "dois"  		  "tres"   			 	  '
my_substrings = re.findall(r'"(.*?)(?<!\\)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in French): one, two, three, and an empty string.
my_string = ' 	 "une" 		    		 "deux"  		  "trois"   			 	  ""'
my_substrings = re.findall(r'"(.*?)(?<!\\)"', my_string)
print("	my_substrings are:",my_substrings,"=")
print("	> stores empty strings embedded within quotation marks.")
print("	> Method works.")








"""
	Reference:
	+ [Pieters2014]
		- Martijn Pieters, Answer to ``Extract a string between double quotes'', Stack Exchange, Inc., New York, NY, March 29, 2014. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/22735466/1531728 and https://stackoverflow.com/questions/22735440/extract-a-string-between-double-quotes/22735466#22735466; November 6, 2021 was the last accessed date.
"""
print("= Method 2d: Get substring with ...")
print("	re.findall(r\'\"([^\"]*)\"\', string).")
my_string = 'SetVariables "a" "b" "c" '
my_substrings = re.findall(r'"([^"]*)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in English): one, two, three.
my_string = 'd2efw  	f "first" +&%#$%"second",vwrfhir, d2e	u"third" dwedew'
my_substrings = re.findall(r'"([^"]*)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Italian): one, two, three.
my_string = '"uno"?>P>MNUIHUH~!@#$%^&*()_+=0trewq"due"		"tre"fef	""fre f'
my_substrings = re.findall(r'"([^"]*)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Spanish): one, two, three.
my_string = '		"uno""dos"		"""tres"'
my_substrings = re.findall(r'"([^"]*)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Romanian): one, two, three.
my_string = '"unu""doua""trei"'
my_substrings = re.findall(r'"([^"]*)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in Portuguese): one, two, three.
my_string = '"" 	 "um" 		    		 "dois"  		  "tres"   			 	  '
my_substrings = re.findall(r'"([^"]*)"', my_string)
print("	my_substrings are:",my_substrings,"=")
# Use the substrings (in French): one, two, three, and an empty string.
my_string = ' 	 "une" 		    		 "deux"  		  "trois"   			 	  ""'
my_substrings = re.findall(r'"([^"]*)"', my_string)
print("	my_substrings are:",my_substrings,"=")
print("	> stores empty strings embedded within quotation marks.")
print("	> Method works.")








"""
	Reference:
	+ [Booboo2020]
		- Booboo, Answer to ``Python Regex to find a string in double quotes within a string'', Stack Exchange, Inc., New York, NY, March 29, 2014. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/63707053/1531728 and https://stackoverflow.com/questions/9519734/python-regex-to-find-a-string-in-double-quotes-within-a-string/63707053#63707053; November 6, 2021 was the last accessed date.
"""
print("= Method 2e: Get substring with ...")
print("	re.findall(r'\"(?:(?:(?!(?<!\\)\").)*)\"\', string).")
"""
	Test strings with substrings embedded within quotation marks,
		which are double quotes in this case.
	After the first test string of single character substrings,
		we use strings containing one, two, three in the
		following languages.
	+ English
	+ Italian
	+ Spanish
	+ Romanian
	+ Portuguese
"""
my_strings = ['SetVariables "a" "b" "c" ', 'd2efw  	f "first" +&%#$%"second",vwrfhir, d2e	u"third" dwedew', '"uno"?>P>MNUIHUH~!@#$%^&*()_+=0trewq"due"		"tre"fef	""fre f', '		"uno""dos"		"""tres"', '"unu""doua""trei"', '"" 	 "um" 		    		 "dois"  		  "tres"   			 	  ', ' 	 "une" 		    		 "deux"  		  "trois"   			 	  ""']
my_substrings = []
# Enumerate all the test strings.
for current_test_string in my_strings:
	for values in re.findall(r'"(?:(?:(?!(?<!\\)").)*)"', current_test_string):
		my_substrings.append(values)
		#print("values are:",values,"=")
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	!!! Fails to extract the substrings without the")
print("		quotation marks (double quotes)!!!")
print("	> stores empty strings embedded within quotation marks.")
print("	> Method works.")










"""
	Combine the approaches from [Booboo2020] and [Pieters2014] to
		extract the substrings without the double quotes.

	[Booboo2020] uses the loop/enumeration approach to test the
		method, while [Pieters2014] has a good regular expression
		that is more understandable than others.

	References:
	+ [Booboo2020]
	+ [Pieters2014]
"""
print("= Method 2f: Get substring with ...")
print("	re.findall(r\'\"([^\"]*)\"\', string).")
# Enumerate all the test strings.
for current_test_string in my_strings:
	for values in re.findall(r'"([^"]*)"', current_test_string):
		my_substrings.append(values)
		#print("values are:",values,"=")
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	> stores empty strings embedded within quotation marks.")
print("	> Method works.")








"""
	References:
	+ [Muthupandi2019]
		- Daniel Muthupandi and trotta, Answer to ``Python Regex to find a string in double quotes within a string'', Stack Exchange, Inc., New York, NY, August 3, 2019. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/57337020/1531728 and https://stackoverflow.com/questions/9519734/python-regex-to-find-a-string-in-double-quotes-within-a-string/63707053#63707053; November 6, 2021 was the last accessed date.
"""
print("= Method 2g: Get substring with ...")
print("	re.findall(r'[\"](.*?)[\"]', string).")
# Enumerate all the test strings.
for current_test_string in my_strings:
	for values in re.findall(r'["](.*?)["]', current_test_string):
		my_substrings.append(values)
		#print("values are:",values,"=")
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	> stores empty strings embedded within quotation marks.")
print("	> Method works.")









"""
	References:
	+ [Lundberg2012]
		- Johan Lundberg, Answer to ``Python Regex to find a string in double quotes within a string'', Stack Exchange, Inc., New York, NY, March 1, 2012. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/9519934/1531728 and https://stackoverflow.com/questions/9519734/python-regex-to-find-a-string-in-double-quotes-within-a-string/9519934#9519934; November 6, 2021 was the last accessed date.
	+ [Avinash2021]
		- Arvind Kumar Avinash, Answer to ``Extract text between quotation using regex python'', Stack Exchange, Inc., New York, NY, October 12, 2021. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/69543129/1531728 and https://stackoverflow.com/questions/69542978/extract-text-between-quotation-using-regex-python/69543129#69543129; November 8, 2021 was the last accessed date.
"""
print("= Method 2h(i): Get substring with ...")
print("	re.findall(r'\\\"(.+?)\\\"', string).")
# Enumerate all the test strings.
for current_test_string in my_strings:
	for values in re.findall(r'\"(.+?)\"', current_test_string):
		my_substrings.append(values)
		#print("values are:",values,"=")
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	> Fails with empty strings embedded within quotation marks.")
print("	> Method FAILS!!!")
# Replace ".+" (one or more empty strings) wit ".*" (zero or more empty strings)
print("= Method 2h(ii): Get substring with ...")
print("	re.findall(r'\\\"(.*?)\\\"', string).")
# Enumerate all the test strings.
for current_test_string in my_strings:
	for values in re.findall(r'\"(.*?)\"', current_test_string):
		my_substrings.append(values)
		#print("values are:",values,"=")
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	> stores empty strings embedded within quotation marks.")
print("	> Method works.")











"""
	References:
	+ [Shelvington2020]
		- Iain Shelvington, Answer to ``Extracting only words out of a mixed string in Python [duplicate]'', Stack Exchange, Inc., New York, NY, January 5, 2020. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/59598630/1531728 and https://stackoverflow.com/questions/59598565/extracting-only-words-out-of-a-mixed-string-in-python/59598630#59598630; November 6, 2021 was the last accessed date.
	+ [w3resourceContributors2021] w3resource contributors, "Python: Extract values between quotation marks of a string", from w3resource: Backend tutorials: Python Tutorial: Python Exercises, Practice, Solution: Python Regular Expression - Exercises, Practice, Solution, or from w3resource: Exercises with online editor: Python Tutorial: Python Exercises, Practice, Solution: Python Regular Expression - Exercises, Practice, Solution, DataSoft, Khosbagan, Bardhaman, Purba Bardhaman, West Bengal, India, October 25, 2021. Available from w3resource: Backend tutorials: Python Tutorial: Python Exercises, Practice, Solution: Python Regular Expression - Exercises, Practice, Solution, or from w3resource: Exercises with online editor: Python Tutorial: Python Exercises, Practice, Solution: Python Regular Expression - Exercises, Practice, Solution at: https://www.w3resource.com/python-exercises/re/python-re-exercise-38.php; last accessed on November 10, 2021.
"""
print("= Method 2i: Get substring with ...")
print("	re.findall('\"(.*?)\"', string).")
# Enumerate all the test strings.
for current_test_string in my_strings:
	for values in re.findall('"(.*?)"', current_test_string):
		my_substrings.append(values)
		#print("values are:",values,"=")
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	> stores empty strings embedded within quotation marks.")
print("	> Method works.")










"""
	Use the regular expression from [Avinash2021], without the suggested
		re.search() method.

	References:
	+ [Avinash2021]
		- Arvind Kumar Avinash, Answer to ``Extract text between quotation using regex python'', Stack Exchange, Inc., New York, NY, October 12, 2021. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/69543129/1531728 and https://stackoverflow.com/questions/69542978/extract-text-between-quotation-using-regex-python/69543129#69543129; November 8, 2021 was the last accessed date.
	+ [user17405772021]
		- user1740577, Answer to ``Extract text between quotation using regex python'', Stack Exchange, Inc., New York, NY, October 12, 2021. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/69543030/1531728 and https://stackoverflow.com/questions/69542978/extract-text-between-quotation-using-regex-python/69543030#69543030; November 8, 2021 was the last accessed date.
"""
print("= Method 2j: Get substring with ...")
print("	re.findall('\"(.+?)\"', string).")
# Enumerate all the test strings.
for current_test_string in my_strings:
	for values in re.findall('"(.+?)"', current_test_string):
		my_substrings.append(values)
		#print("values are:",values,"=")
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	> stores empty strings embedded within quotation marks.")
print("	> Method FAILS!!!")






#print("= Method 2k: Get substring with ...")
#print("	re.search('\"(.+?)\"', string).")
"""
	Enumerate all the test strings.

	Use the method in [Avinash2021] based on regular expression objects,
		specifically 're.Match' object.

	However, it only finds the first/only substring embedded within
		quotation marks, double quotes in this case.

	[KiteStaff20XY] uses the re.search().group(1) method that
		returns only the first substring embedded within the
		specified markers.
"""
#	for current_test_string in my_strings:
		#values = re.search('"(.+?)"', current_test_string)
#		values = re.findall('"(.+?)"', current_test_string)
		#values = re.compile('"(.+?)"', current_test_string)
		#values = re.match('"(.+?)"', current_test_string)
		#values = re.fullmatch('"(.+?)"', current_test_string)
#		"""
#		if values:
#			print("values are:",values,"=")
#			#print("	my_substrings are:",my_substrings,"=")
#		my_substrings = []
#		"""
		#for v in values:
			#print("values are:",values.group(1),"=")
			#print("	my_substrings are:",my_substrings,"=")
#		print("values are:",values,"=")
		#print("values are:",values.span(),"=")
		#print("values are:",values.string,"=")
#			print("values are:",values.group(),"=")
		#print("values are:",values.group(0),"=")
		#print("values are:",values.group(1),"=")
		#print("values are:",values.group(2),"=")
		#my_substrings = []







"""
	Combining the my_string.split() method [Roman2010][Koledoye2016]
		with the loop/enumeration approach [Booboo2020].

	References:
	+ [Roman2010]
	+ [Koledoye2016]
"""
print("= Method 2k: Get substring with ...")
print("	my_string.split() method.")
# Enumerate all the test strings.
for current_test_string in my_strings:
	#values = current_test_string.split("'")
	#for x in values:
	for x in current_test_string.split("\""):
		if x.strip():
			my_substrings.append(x)
			#print("x is:",x,"=")
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	!!!Approach works for strings with targeted")
print("		substrings embedded in patterns!!!")
print("	> Method FAILS!!!")













"""
	References:
	+ [devnull2013]
		- devnull, Answer to `Extracting strings in Python in either single or double quotes', Stack Exchange, Inc., New York, NY, October 30, 2013. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/19675957/1531728 and https://stackoverflow.com/questions/19675760/extracting-strings-in-python-in-either-single-or-double-quotes/19675957#19675957; November 11, 2021 was the last accessed date.
"""
print("= Method 2l: Get substring with ...")
print("	re.findall(r\"['\\\"](.*?)['\\\"]\", string).")
# Enumerate all the test strings.
for current_test_string in my_strings:
	for values in re.findall(r"['\"](.*?)['\"]", current_test_string):
		my_substrings.append(values)
		#print("values are:",values,"=")
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	> stores empty strings embedded within quotation marks.")
print("	> Method works.")







"""
	References:
	+ [devnull2013]
		- devnull, Answer to `Extracting strings in Python in either single or double quotes', Stack Exchange, Inc., New York, NY, October 30, 2013. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/19675957/1531728 and https://stackoverflow.com/questions/19675760/extracting-strings-in-python-in-either-single-or-double-quotes/19675957#19675957; November 11, 2021 was the last accessed date.
	+ [devnull2013a]
		- tripleee, Comment about an answer to `Extracting strings in Python in either single or double quotes', Stack Exchange, Inc., New York, NY, October 30, 2013. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/questions/19675760/extracting-strings-in-python-in-either-single-or-double-quotes#comment29222674_19675957; November 11, 2021 was the last accessed date.
	+ [WikipediaContributors2019i]
		- Wikipedia contributors, "CAR and CDR", Wikimedia Foundation, San Francisco, CA, August 28, 2019. Available online from Wikipedia, The Free Encyclopedia: Lisp (programming language) at: https://en.wikipedia.org/wiki/CAR_and_CDR; February 19, 2020 was the last accessed date.
"""
print("= Method 2m: Get substring with ...")
print("	re.findall(r\"(['\\\"])(.*?)['\\\"]\", string).")
# Enumerate all the test strings.
for current_test_string in my_strings:
	for values in re.findall(r"(['\"])(.*?)['\"]", current_test_string):
		my_substrings.append(values)
		#print("values are:",values,"=")
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	> stores empty strings embedded within quotation marks.")
print("	> Store result in tuples, as cdr for the cons (car, cdr).")
#print("	> Method FAILS!!!")
print("	> Method works.")






"""
	References:
	+ [devnull2013]
		- devnull, Answer to `Extracting strings in Python in either single or double quotes', Stack Exchange, Inc., New York, NY, October 30, 2013. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/19675957/1531728 and https://stackoverflow.com/questions/19675760/extracting-strings-in-python-in-either-single-or-double-quotes/19675957#19675957; November 11, 2021 was the last accessed date.
	+ [tripleee2013]
		- tripleee, Comment about an answer to `Extracting strings in Python in either single or double quotes', Stack Exchange, Inc., New York, NY, October 30, 2013. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/questions/19675760/extracting-strings-in-python-in-either-single-or-double-quotes#comment29224831_19675957; November 11, 2021 was the last accessed date.
	+ [WikipediaContributors2019i]
		- Wikipedia contributors, "CAR and CDR", Wikimedia Foundation, San Francisco, CA, August 28, 2019. Available online from Wikipedia, The Free Encyclopedia: Lisp (programming language) at: https://en.wikipedia.org/wiki/CAR_and_CDR; February 19, 2020 was the last accessed date.
"""
print("= Method 2n: Get substring with ...")
print("	re.findall(r\"(['\\\"])(.*?)\\1\", string).")
# Enumerate all the test strings.
for current_test_string in my_strings:
	for values in re.findall(r"(['\"])(.*?)\1", current_test_string):
		my_substrings.append(values)
		#print("values are:",values,"=")
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	> stores empty strings embedded within quotation marks.")
print("	> Store result in tuples, as cdr for the cons (car, cdr).")
#print("	> Method FAILS!!!")
print("	> Method works.")










"""
	References:
	+ [Feldman2021]
		- Alex 'af3ld' Feldman and Shaido, Answer to `How do I find quotes in strings - Python', Stack Exchange, Inc., New York, NY, February 26, 2021. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/38444540/1531728 and https://stackoverflow.com/questions/38444389/how-do-i-find-quotes-in-strings-python/38444540#38444540; November 11, 2021 was the last accessed date.
	+ [Paluter2016]
		- Paluter, Answer to "How do I find quotes in strings - Python", Stack Exchange, Inc., New York, NY, July 18, 2016. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/38444653/1531728 and https://stackoverflow.com/questions/38444389/how-do-i-find-quotes-in-strings-python/38444653#38444653; November 11, 2021 was the last accessed date.
"""
print("= Method 2o: Get substring with ...")
print("	my_string.find(pattern, string_positional_index).")
my_substrings = []
# Enumerate all the test strings.
for current_test_string in my_strings:
	"""
	for values in re.findall(r"(['\"])(.*?)\1", current_test_string):
		my_substrings.append(values)
		#print("values are:",values,"=")
	print("	my_substrings are:",my_substrings,"=")
	"""
	start = current_test_string.find('"')
	while -1 != start:
		end = current_test_string.find('"', start+1)
		if -1 != end:
			substring = current_test_string[start+1:end]
			#print("	> substring of current_test_string is:",substring,"=")
			my_substrings.append(substring)
		start = current_test_string.find('"', end+1)
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	> stores empty strings embedded within quotation marks.")
#print("	> Method FAILS!!!")
print("	> Method works.")












"""
	Testing methods for non-capturing groups and non-consuming groups.

	References:
	+ [Tisnek2015]
		- Dima Tisnek and Kenly, Answer to `How do I find quotes in strings - Python', Stack Exchange, Inc., New York, NY, December 17, 2015. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/34155315/1531728 and https://stackoverflow.com/questions/34155110/python-find-text-in-file-between-quotation-marks/34155315#34155315; November 11, 2021 was the last accessed date.
"""
print("= Method 2p: Get substring with ...")
print("	re.findall('(?:\")([^\"]*)(?:\")', current_test_string).")
my_substrings = []
"""
	Enumerate all the test strings.

	Test methods for non-capturing groups.
"""
for current_test_string in my_strings:
	for values in re.findall('(?:")([^"]*)(?:")', current_test_string):
		my_substrings.append(values)
		#print("values are:",values,"=")
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	> stores empty strings embedded within quotation marks.")
#print("	> Method FAILS!!!")
print("	> Method works.")
"""
	Try alternate method in [Tisnek2015].

	Test methods for non-consuming groups.
"""
print("= Method 2q: Get substring with ...")
print("	re.findall('(?<=\")[^\"]*(?=\")', current_test_string).")
my_substrings = []
# Enumerate all the test strings.
for current_test_string in my_strings:
	for values in re.findall('(?<=")[^"]*(?=")', current_test_string):
		my_substrings.append(values)
		#print("values are:",values,"=")
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	> stores empty strings embedded within quotation marks.")
#print("	> Method FAILS!!!")
print("	> Method partially works, with erroneous extracted substrings.")






















"""
	Set of failed approaches:
	+ for values in re.findall('(?:[^"]*.)*[^"]*', current_test_string):
"""



"""
	References: FIX THIS!!!
	+ [devnull2013]
		- devnull, Answer to `Extracting strings in Python in either single or double quotes', Stack Exchange, Inc., New York, NY, October 30, 2013. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/19675957/1531728 and https://stackoverflow.com/questions/19675760/extracting-strings-in-python-in-either-single-or-double-quotes/19675957#19675957; November 11, 2021 was the last accessed date.
	+ [WikipediaContributors2019i]
		- Wikipedia contributors, "CAR and CDR", Wikimedia Foundation, San Francisco, CA, August 28, 2019. Available online from Wikipedia, The Free Encyclopedia: Lisp (programming language) at: https://en.wikipedia.org/wiki/CAR_and_CDR; February 19, 2020 was the last accessed date.
"""
print("= Method 2z: Get substring with ...")
print("	re.findall(r'[\"](.*?)[\"]', string).")
# Enumerate all the test strings.
for current_test_string in my_strings:
	for values in re.findall(r"(['\"])(.*?)\1", current_test_string):
		my_substrings.append(values)
		#print("values are:",values,"=")
	print("	my_substrings are:",my_substrings,"=")
	my_substrings = []
print("	> stores empty strings embedded within quotation marks.")
print("	> Store result in tuples, as cdr for the cons (car, cdr).")
#print("	> Method FAILS!!!")
print("	> Method works.")









"""
	The follow are failed implementations of suggested solutions.
	The suggestions are either incorrect or poor implementations.



	Try the techniques suggested in answers to the question [WEshruth2013] in Stack Overflow.

	Reference:
	+ [WEshruth2013]
		- WEshruth, ``how to extract string inside single quotes using python script,'' Stack Exchange Inc., New York, NY, October 18, 2013. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/q/19449709/1531728 and https://stackoverflow.com/questions/19449709/how-to-extract-string-inside-single-quotes-using-python-script; November 6, 2021 was the last accessed date.
	


	my_reg_ex = re.compile("(?<=')[^']+(?=')")
	for current_test_string in my_strings:
		for value in my_reg_ex.findall(current_test_string):
			my_substrings.append(value)


	for current_test_string in my_strings:
		#for values in re.findall(r"'(.*?)'", current_test_string, re.DOTALL):
		for values in re.findall(r"'(.*?)'", current_test_string):
			my_substrings.append(values)
			print("values are:",values,"=")
	print("my_substrings are:",my_substrings,"=")
"""


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =