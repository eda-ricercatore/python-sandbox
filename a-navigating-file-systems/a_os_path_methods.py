#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3


"""
	This Python script is written by Zhiyang Ong to test methods that
		perform operations with relative and absolute paths.


	

	This script can be executed as follows:
		./a_os_path_methods.py



	Revision History:
	September 6, 2019			Version 0.1	Script.
"""


__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'September 6, 2019'

#	The MIT License (MIT)

#	Copyright (c) <2019> <Zhiyang Ong>

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






"""
	References for handling the "__file__" attribute.
	+ depling and Octavia Togami and tornikeo, ``what does the __file__ variable mean/do?,'' Stack Exchange Inc., New York, NY, October 21, 2022. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/q/9271464/1531728 and https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do; November 9, 2021 was the last accessed date.
"""


import os

print("= Perform split() operation.")
path_prefix, last_pathname_component = os.path.split('/my/path/to/whatever/somefile.ext')
print(path_prefix)
print(last_pathname_component)

print("= Perform splitext() operation.")
filename, file_extension = os.path.splitext('/some/path/to/somefile.ext')
print(filename)
print(file_extension)

print("= Perform splitext() operation again.")
filename, file_extension = os.path.splitext('fosca.battati')
print(filename)
print(file_extension)


print("= Perform splitext() operation yet another time.")
filename, file_extension = os.path.splitext('daniela-stefanescu')
print(filename)
print(file_extension)



print("= Perform splitext() operation on multiple file extensions.")
filename, file_extension = os.path.splitext('ansu_mani.tar.gz')
print(filename)
print(file_extension)
f_name, f_extension = os.path.splitext(file_extension)
print(f_name)
print(f_extension)
f_name1, f_extension1 = os.path.splitext(filename)
print(f_name1)
print(f_extension1)



"""
	References and notes:
	+ \cite[From section "File and Directory Access", subsection "os.path — Common pathname manipulations"]{DrakeJr2016b}
		Available online from "The Python Standard Library: File and Directory Access: os.path — Common pathname manipulations" at: https://docs.python.org/3/library/os.path.html#os.path.expanduser;
			February 12, 2020 was the last accessed date.
		- Information about the "os.path.expanduser(path)" command
			replaces relative paths starting from the current
			user's home directory (starting with "~" or "~user").
			* Hence, if the path does not start with "~" nor
				"~user", or if the path cannot be expanded,
				the 'path' remains unchanged.
	+ \cite[From section "Generic Operating System Services", subsection "os — Miscellaneous operating system interfaces"]{DrakeJr2016b}
		Available online from "The Python Standard Library: Generic Operating System Services: os — Miscellaneous operating system interfaces" at: https://docs.python.org/3/library/os.html#os.getcwd;
		February 12, 2020 was the last accessed date.
	+ [Dias2016] Russell Dias and Mark Amery, Answer to "Find current
		directory and file's directory [duplicate]", from
		Stack Exchange Inc.: Stack Overflow: Questions,
		Stack Exchange, Inc., New York, NY, July 31, 2016.
		Available online from Stack Exchange Inc.: Stack
			Overflow: Questions at: https://stackoverflow.com/a/5137509/1531728 and https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory/5137509#5137509;
			February 12, 2020 was the last accessed date.
	+ John Howard and Mark Amery, "Find current
		directory and file's directory [duplicate]", from
		Stack Exchange Inc.: Stack Overflow: Questions,
		Stack Exchange, Inc., New York, NY, July 31, 2016.
		Available online from Stack Exchange Inc.: Stack
			Overflow: Questions at: https://stackoverflow.com/q/5137497/1531728 and https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
			February 12, 2020 was the last accessed date.
"""
valid_path = os.path.expanduser("./")
print("valid_path is:",valid_path,"=")
"""
	See \cite[From section "File and Directory Access", subsection "os.path — Common pathname manipulations"]{DrakeJr2016b}
		for reasons why the "os.path.expanduser(path)" command
		does not work with the paths "./" nor ".".
"""
valid_path = os.path.expanduser(".")
print("New valid_path is:",valid_path,"=")
"""
	See \cite[From section "Generic Operating System Services", subsection "os — Miscellaneous operating system interfaces"]{DrakeJr2016b}.
"""
current_wking_dir = os.getcwd()
print("New current_wking_dir is:",current_wking_dir,"=")

# \cite{Dias2016}
full_path = os.path.realpath("./")
print("full_path is:",full_path,"=")
full_path = os.path.realpath(".")
print("Now full_path is:",full_path,"=")

absolute_path = os.path.abspath("./")
print("absolute_path is:",absolute_path,"=")
absolute_path = os.path.abspath(".")
print("Now absolute_path is:",absolute_path,"=")


"""
	Get the name of the current directory, and the path
		to the current directory.
	Reference:
	+ StormShadow, Answer to "Find current directory and file's directory [duplicate]," Stack Exchange Inc., New York, NY, October 9, 2013.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/19269546/1531728 and https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory/19269546#19269546
			February 13, 2020 was the last accessed date.
"""
current_folder_path, current_folder_name = os.path.split(os.getcwd())
print("current_folder_path is:",current_folder_path,"=")
print("current_folder_name is:",current_folder_name,"=")





absolute_path_to_store_results = "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"

print("=	Valid path, existent file.")
path_to_file = "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization/2020/february/7-2-2020-9-56-54-334414.txt"
if path_to_file is not None:
	print("	path_to_file is not None")
if os.path.exists(path_to_file):
	print("	os.path.exists(path_to_file)")
if os.path.isfile(path_to_file):
	print("	os.path.isfile(path_to_file)")
if path_to_file.startswith(absolute_path_to_store_results):
	print("	path_to_file.startswith(absolute_path_to_store_results)")


print("=	Valid path, non-existent file.")
path_to_file = "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization/2020/random.rnd"
if path_to_file is not None:
	print("	path_to_file is not None")
if os.path.exists(path_to_file):
	print("	os.path.exists(path_to_file)")
if os.path.isfile(path_to_file):
	print("	os.path.isfile(path_to_file)")
if path_to_file.startswith(absolute_path_to_store_results):
	print("	path_to_file.startswith(absolute_path_to_store_results)")