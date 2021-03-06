#!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to test concepts in string processing.

	Synopsis:
	Script to process strings.


	Revision History:
	1) November 13, 2014. Initial working version.




	References:
	+ References provided within square brackets are BibTeX keys of
		entries in my BibTeX database of references (set of BibTeX entries).



 	The MIT License (MIT)

 	Copyright (c) <2014> <Zhiyang Ong>

 	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

 	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

 	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"
"""


#	Import packages and functions from the Python Standard Library.
import string
import os
import sys


#	============================================================


my_str = "UC Berkeley's logic synthesis tool, ABC, is the best logic synthesis and verification tool in the world."
print(my_str)

my_str = my_str.replace("UC Berkeley", "MIT")
print(my_str)

filename, file_extension = os.path.splitext('daniela-stefanescu')
if None == file_extension:
	print("file_extension is equal to None.")
else:
	print("file_extension is equal to something else.")

if not file_extension:
	print("file_extension is empty.")
else:
	print("file_extension is not empty???")


base_directory = "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"
a_path = "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization/2020"
if a_path.startswith(base_directory):
	print("=	a_path starts with base_directory.")
else:
	print("=	a_path DOES NOT start with base_directory.")
if "tyriuoipo".startswith(base_directory):
	print("=	tyriuoipo STARTS WITH base_directory.")
else:
	print("=	a_path does not start with base_directory.")
if "tyriuoipo".startswith("dwedew"):
	print("=	tyriuoipo STARTS WITH base_directory.")
else:
	print("=	a_path does not start with base_directory.")








print("\n\n")
"""
	The Python method "os.path.splitext()" to split the path
		for a file into the root of the path (without the
		file extension suffix) and the file extension.


	Unfortunately, by default, it defines the file extension
		as the string starting from the last period (if it
		exists) till the end of the string.
	Hence, file extensions such as ".tar.gz" would not be
		recognized and detected correctly.
	If I want to define file extension otherwise, I have
		to provide an implementation of a Python method
		complying with the new definition.

	References:
	+ BibTeX key: DrakeJr2016b
		- From the section "File and Directory Access",
			subsection "os.path - Common pathname manipulations".
		- By definition of the "os.path.splitext ()" (Python)
			method returns the root of the file's path and
			the file extension.
"""
print ("25-3-2010-5-8-51-9407.txt is being partitioned into the filename without the file extension suffix and the file extension.")
filename_wo_extn, file_extn = os.path.splitext ("25-3-2010-5-8-51-9407.txt")
print ("filename_wo_extn is:", filename_wo_extn, "=")
print("file_extn is:",file_extn,"=")
print("/path/to/filename.pdf.tar.gz is being partioned into the filename without the file extension suffix and the file extension.")
filename_wo_extn, file_extn = os.path.splitext("/path/to/filename.pdf.tar.gz")
print("filename_wo_extn is:",filename_wo_extn,"=")
print("file_extn is:",file_extn,"=")
tokens = filename_wo_extn.split("-")
print("isinstance(tokens, list) is:",isinstance(tokens, list),"=")
print("isinstance(None, list) is:",isinstance(None, list),"=")
print("isinstance('dewd323 vrevnoi.123', str) is:",isinstance("dewd323 vrevnoi.123", str),"=")
print("isinstance(None, str) is:",isinstance(None, str),"=")
print("isinstance(32.234, str) is:",isinstance(32.234, str),"=")
print("\n\n")




months_of_the_year = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
print("months_of_the_year[2] is:",months_of_the_year[2-1],"=")
#print("months_of_the_year[02] is:",months_of_the_year[int(02)],"=")
print("months_of_the_year[10] is:",months_of_the_year[10-1],"=")



a_bin_str = "0b0010100110"
b_bin_str = a_bin_str[2:]
print("b_bin_str is:",b_bin_str,"=")


c_string = "I love fried plantains."
for char in c_string:
	print("current character is:", char, "=")
	if ('a' == char) or ('n' == char):
		print("=	Found 'a' or 'n'.")
print("======================================================")
empty_string = ""
# Is the string empty?
if not empty_string:
	print("+	The string is empty.")
else:
	print("+	The string is NOT empty!!!")
if 0 == len(empty_string):
	print("+	len(empty_string) is 0.")
else:
	print("+	len(empty_string) is NOT 0!!!")

"""
	Reference:
	+ vault, Answer to ``How to check if the string is empty?,'' Stack Exchange Inc., New York, NY, March 12, 2021. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/27982561/1531728 and https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty/27982561#27982561; November 6, 2021 was the last accessed date.
"""
if not bool(empty_string.strip()):
	print("+	bool(empty_string.strip()) returns false.")
else:
	print("+	bool(empty_string.strip()) returns TRUE!!!")
"""
	Reference:
	+ Dakkaron, Answer to ``How to check if the string is empty?,'' Stack Exchange Inc., New York, NY, April 18, 2019. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/55747410/1531728 and https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty/55747410#55747410; November 6, 2021 was the last accessed date.

"""
if "".__eq__(empty_string):
	print("+	\"\".__eq__(empty_string) indicates that the string is empty.")
else:
	print("+	\"\".__eq__(empty_string) indicates that the string is NOT empty!!!")



"""
	References:
	+ Wikipedia contributors, "Magic number (programming)," in Wikipedia, The Free Encyclopedia: Anti-patterns, Wikimedia Foundation, San Francisco, CA, November 8, 2021.
	Available online from Wikipedia, The Free Encyclopedia: Anti-patterns at: https://en.wikipedia.org/wiki/Magic_number_(programming); November 9, 2021 was the last accessed date.
	+ firelynx Community bot, Answer to ``How to check if the string is empty?,'' Stack Exchange Inc., New York, NY, April 18, 2019. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/55747410/1531728 and https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty/55747410#55747410; November 6, 2021 was the last accessed date.
"""
if "" == empty_string:
	print("+	\"\" == empty_string indicates that the string is empty.")
else:
	print("+	\"\" == empty_string indicates that the string is NOT empty!!!")



"""
	References:
	+ Thai Tran, Answer to ``How to check whether a str(variable) is empty or not?,'' Stack Exchange Inc., New York, NY, April 5, 2017. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/43222230/1531728 and https://stackoverflow.com/questions/9926446/how-to-check-whether-a-strvariable-is-empty-or-not/43222230#43222230; November 9, 2021 was the last accessed date.
"""
if not bool(empty_string):
	print("+	bool(empty_string) indicates that the string is empty.")
else:
	print("+	bool(empty_string) indicates that the string is NOT empty!!!")



not_empty_string = "String is not empty."
# Is the string empty?
if not_empty_string:
	print("+	The string is not empty.")
else:
	print("+	The string is EMPTY!!!")

print("======================================================")

my_string = "Hello World"

if my_string:
	print("my_string is not empty:",my_string,"=")
else:
	print("The string is EMPTY!!!:",my_string,"=")


if not my_string:
	print("my_string is empty!!!:",my_string,"=")
else:
	print("The non-empty string is:",my_string,"=")



if 0 < len(my_string):
	print("+	len(my_string) is > 0. Hence, the string is not empty.")
else:
	print("+	len(my_string) is 0!!! The string is empty.")

"""
	Reference:
	+ vault, Answer to ``How to check if the string is empty?,'' Stack Exchange Inc., New York, NY, March 12, 2021. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/27982561/1531728 and https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty/27982561#27982561; November 6, 2021 was the last accessed date.
"""
if bool(my_string.strip()):
	print("+	bool(my_string.strip()) returns true.")
else:
	print("+	bool(my_string.strip()) returns FALSE!!!")
"""
	Reference:
	+ Dakkaron, Answer to ``How to check if the string is empty?,'' Stack Exchange Inc., New York, NY, April 18, 2019. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/55747410/1531728 and https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty/55747410#55747410; November 6, 2021 was the last accessed date.

"""
if "".__eq__(my_string):
	print("+	\"\".__eq__(my_string) indicates that the string is empty.")
else:
	print("+	\"\".__eq__(my_string) indicates that the string is NOT empty!!!")
"""
	References:
	+ Wikipedia contributors, "Magic number (programming)," in Wikipedia, The Free Encyclopedia: Anti-patterns, Wikimedia Foundation, San Francisco, CA, November 8, 2021.
	Available online from Wikipedia, The Free Encyclopedia: Anti-patterns at: https://en.wikipedia.org/wiki/Magic_number_(programming); November 9, 2021 was the last accessed date.
	+ firelynx Community bot, Answer to ``How to check if the string is empty?,'' Stack Exchange Inc., New York, NY, April 18, 2019. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/55747410/1531728 and https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty/55747410#55747410; November 6, 2021 was the last accessed date.
"""
if "" != my_string:
	print("+	\"\" != my_string indicates that the string is not empty.")
else:
	print("+	\"\" != my_string indicates that the string is EMPTY!!!")
if "" == my_string:
	print("+	\"\" == my_string indicates that the string is EMPTY!!!")
else:
	print("+	\"\" == my_string indicates that the string is not empty.")




"""
	References:
	+ Thai Tran, Answer to ``How to check whether a str(variable) is empty or not?,'' Stack Exchange Inc., New York, NY, April 5, 2017. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/43222230/1531728 and https://stackoverflow.com/questions/9926446/how-to-check-whether-a-strvariable-is-empty-or-not/43222230#43222230; November 9, 2021 was the last accessed date.
"""
if bool(my_string):
	print("+	bool(my_string) indicates that the string is empty.")
else:
	print("+	bool(my_string) indicates that the string is NOT empty!!!")












print("= length of input arguments to the program:",len(sys.argv),"=")
if 1 < len(sys.argv):
	print("The first argument is:",sys.argv[1],"=")
else:
	print("The first argument does not exist.")

print("======================================================")

a = 45.5
b = 98
c = 0.23
d = 34
prompt = " a is:{}= and b is:{}= and c is:{}= and d is:{}="
print(prompt .format(a,b,c,d))


print("======================================================")

"""
	Methods to replace/delete a substring.

	References:
	+ [Garg2019]
		- https://www.geeksforgeeks.org/python-remove-the-given-substring-from-end-of-string/ 
		- Python | Remove the given substring from end of string
		- 07-06-2019   
		- garg_ak0109
		- Akshat Garg
"""



my_string = "This is an substring that I want to eliminate."
print("= my_string is:",my_string,"=")
my_substring = "substring that I "
print("= my_substring is:",my_substring,"=")

print("= Method 2 from [Garg2019].")
import re
result_1 = re.sub(my_substring, "", my_string)
print("= result_1 is:",result_1,"=")

print("= Method 3 from [Garg2019].")
result_2 = my_string.replace(my_substring, "")
print("= result_2 is:",result_2,"=")


my_substring = "4568798yu9cwever32r"
print("= Try deleting non-existent substring.")
result_3 = my_string.replace(my_substring, "")
print("= result_3 is:",result_3,"=")
if result_3 == my_string:
	print("= result_3 and my_string are the same.")
else:
	print("= result_3 and my_string are different.")

print("======================================================")

"""
	Methods to determine if a substring exists in a string.

	References:
	+ [Stopak20XY]
		- https://stackabuse.com/python-check-if-string-contains-substring/
		- Python: Check if String Contains Substring
		- Jacob Stopak
		- No date
	+ [Edpresso Editor 2020]
		- https://www.educative.io/edpresso/how-to-check-if-python-string-contains-another-string   
		- How to check if Python string contains another string
		- August 12, 2020.
		- Educative, Inc.: Bellevue, WA.
	+ [Striver2000]
		- https://www.geeksforgeeks.org/python-check-substring-present-given-string/
		- Python | Check if a Substring is Present in a Given String
		- Last Updated: 18-05-2020
	+ [Kumar20XY]
		- https://www.askpython.com/python/string/check-string-contains-substring-python 
		- How to Check if a String contains a Substring in Python?
		- Python String
		- Python Programming
		- AskPython.com
		- pankaj.0323@gmail.com
		- Pankaj Kumar, "How to Check if a String contains a Substring in Python?," from AskPython.com: Python Programming: Python String, JournalDev IT Services Private Limited, Bengaluru, Karnataka, India. Available online from JournalDev IT Services Private Limited: AskPython.com: Python Programming: Python String at: https://www.askpython.com/python/string/check-string-contains-substring-python; August 24, 2020 was the last accessed date.



   
August 12, 2020

	Notes:
	+ "Lists are iterables, and the in method acts on iterables, not just strings."
		- From: https://stackoverflow.com/a/43687082
		- firelynx (author of quote)
		- Apr 28 '17 at 18:52
		- Community at: Jun 20 at 9:12
		- firelynx and Community, Answer to "Does Python have a string 'contains' substring method?", Stack Exchange Inc., New York, NY, June 20, 2020. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/43687082 and https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method/43687082#43687082; March 7, 2020 was the last accessed date.
"""

print("= Method 1 from [Stopak20XY]. Method 2 from [Edpresso Editor 2020]")
if my_substring in my_string:
	print("my_string contains my_substring.")
else:
	print("my_string does NOT contain my_substring!!!")

print("= Modify my_string and my_substring.")
my_string = "drtifyougiphojp tofyguhci eiu ucvwek32 89r 	jfkr o"
print("= my_string is:",my_string,"=")
my_substring = "rtftyguihojk"
print("= my_substring is:",my_substring,"=")
if my_substring not in my_string:
	print("my_string does not contain my_substring.")
else:
	print("my_string CONTAINS my_substring!!!")
if my_substring in my_string:
	print("alt: my_string CONTAINS my_substring!!!")
else:
	print("alt: my_string does not contain my_substring.")


print("")
print("= Method 3 from [Stopak20XY]. Method 1 from [Edpresso Editor 2020].")
my_string = "This is an substring that I want to eliminate."
my_substring = "substring that I "
if -1 != my_string.find(my_substring):
	print("my_string contains my_substring.")
else:
	print("my_string does NOT contain my_substring!!!")
print("= Modify my_string and my_substring.")
my_string = "drtifyougiphojp tofyguhci eiu ucvwek32 89r 	jfkr o"
print("= my_string is:",my_string,"=")
my_substring = "rtftyguihojk"
print("= my_substring is:",my_substring,"=")
if -1 != my_string.find(my_substring):
	print("alt: my_string CONTAINS my_substring!!!")
else:
	print("alt: my_string does not contain my_substring.")



print("")
print("= Method 4 from [Stopak20XY].")
from re import search
my_string = "This is an substring that I want to eliminate."
my_substring = "substring that I "
if search(my_substring, my_string):
	print("my_string contains my_substring.")
else:
	print("my_string does NOT contain my_substring!!!")
print("= Modify my_string and my_substring.")
my_string = "drtifyougiphojp tofyguhci eiu ucvwek32 89r 	jfkr o"
print("= my_string is:",my_string,"=")
my_substring = "rtftyguihojk"
print("= my_substring is:",my_substring,"=")
if search(my_substring, my_string):
	print("alt: my_string CONTAINS my_substring!!!")
else:
	print("alt: my_string does not contain my_substring.")


 
print("")
print("= Method 3 from [Edpresso Editor 2020].")
my_string = "This is an substring that I want to eliminate."
my_substring = "substring that I "
if 0 != my_string.count(my_substring):
	print("my_string contains my_substring.")
else:
	print("my_string does NOT contain my_substring!!!")
print("= Modify my_string and my_substring.")
my_string = "drtifyougiphojp tofyguhci eiu ucvwek32 89r 	jfkr o"
print("= my_string is:",my_string,"=")
my_substring = "rtftyguihojk"
print("= my_substring is:",my_substring,"=")
if 0 != my_string.count(my_substring):
	print("alt: my_string CONTAINS my_substring!!!")
else:
	print("alt: my_string does not contain my_substring.")



print("")
print("= Method 5 from [Kumar20XY].")
import operator
my_string = "This is an substring that I want to eliminate."
my_substring = "substring that I "
if operator.contains(my_string,my_substring):
	print("my_string contains my_substring.")
else:
	print("my_string does NOT contain my_substring!!!")
print("= Modify my_string and my_substring.")
my_string = "drtifyougiphojp tofyguhci eiu ucvwek32 89r 	jfkr o"
print("= my_string is:",my_string,"=")
my_substring = "rtftyguihojk"
print("= my_substring is:",my_substring,"=")
if operator.contains(my_string,my_substring):
	print("alt: my_string CONTAINS my_substring!!!")
else:
	print("alt: my_string does not contain my_substring.")

print("======================================================")
my_string = "This is an substring that I want to eliminate from my sentence."
set_of_substrings = {"substring that I ", "to eliminate from", "non-existent"}
"""
	Note that the order of elements in the set that selected for
		processing varies between execution of this Python script.
"""
for x in set_of_substrings:
	print("=	substring:",x,"=")
	if x in my_string:
		print("substring exists in my_string.")
	else:
		print("substring is not found in my_string.")




print("======================================================")
"""
	Exploring ways to measure the size of (empty) strings.

	References:
	+ Nicholas Humphrey and Solomon Ucko, ``Why does an empty string in Python sometimes take up 49 bytes and sometimes 51?,'' Stack Exchange Inc., New York, NY, December 22, 2018. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/q/53899931/1531728 and https://stackoverflow.com/questions/53899931/why-does-an-empty-string-in-python-sometimes-take-up-49-bytes-and-sometimes-51; November 9, 2021 was the last accessed date.
"""
print("Size of empty string:",sys.getsizeof(""),"=")
print("Size of string 'dui hiewlf ifywei7f wfuywf o2o4':",sys.getsizeof("dui hiewlf ifywei7f wfuywf o2o4"),"=")
print("Size of empty string:",sys.getsizeof(""),"=")





print("======================================================")

"""
	Test methods to extract substrings embedded within quotation marks.

	Reference:
	+ [KiteStaff20XY]
"""

print("= Extract a substring within a pair of markers,")
print("	left marker 'AUG\|' and right marker '\|UGA'.")
s = "abc123AUG|GAC|UGAasdfg789"
pattern = "AUG\|(.*?)\|UGA"
substring = re.search(pattern, s).group(1)
print("s is:",s,"=")
print("substring of s is:",substring,"=")
s = 'd2efw  	f "first" +&%#$%"second",vwrfhir, d2e	u"third" dwedew'
pattern = '"(.*?)"'
substring = re.search(pattern, s).group(1)
#substring = re.search(pattern, s).group(3)
print("s is:",s,"=")
print("substring of s is:",substring,"=")
print("	> This method returns only the first substring that")
print("		is embedded within the specified markers.")
s = "abc123AUG|GAC|UGAasdfg789"
start = s.find("AUG|") + len("AUG|")
end = s.find("|UGA")
substring = s[start:end]
print("s is:",s,"=")
print("substring of s is:",substring,"=")
s = 'd2efw  	f "first" +&%#$%"second",vwrfhir, d2e	u"third" dwedew'
start = s.find('"') + len('"')
end = s.find('"')
substring = s[start:end]
print("s is:",s,"=")
print("substring of s is:",substring,"=")
print("	> This method FAILS to return substrings embedded within")
print("		the specified equivalent begin & end markers.")
s = 'd2efw  	f ?first" +&%#$%?second",vwrfhir, d2e	u?third" dwedew'
start = s.find('?') + len('?')
end = s.find('"')
substring = s[start:end]
print("s is:",s,"=")
print("substring of s is:",substring,"=")
print("	> This method returns only the first substring that")
print("		is embedded within the specified markers,")
print("		if these markers are different;")
print("		i.e., the begin & end markers are different.")
"""
	Method only returns the first substring embedded within quotation
		marks.

	Hence, for strings with multiple substrings embedded within
		quotation marks, this method only returns the first embedded
		substring.

	Reference:
	+ [Feldman2021]
		- Alex 'af3ld' Feldman and Shaido, Answer to `How do I find quotes in strings - Python', Stack Exchange, Inc., New York, NY, February 26, 2021. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/38444540/1531728 and https://stackoverflow.com/questions/38444389/how-do-i-find-quotes-in-strings-python/38444540#38444540; November 11, 2021 was the last accessed date.
	+ [Paluter2016]
		- Paluter, Answer to "How do I find quotes in strings - Python", Stack Exchange, Inc., New York, NY, July 18, 2016. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/38444653/1531728 and https://stackoverflow.com/questions/38444389/how-do-i-find-quotes-in-strings-python/38444653#38444653; November 11, 2021 was the last accessed date.
"""
s = 'd2efw  	f "first" +&%#$%"second",vwrfhir, d2e	u"third" dwedew'
#s = 'd2efw  	f ?first" +&%#$%?second",vwrfhir, d2e	u?third" dwedew'
start = s.find('"')
if -1 != start:
	end = s.find('"', start+1)
	if -1 != end:
		substring = s[start+1:end]
		print("s is:",s,"=")
		print("substring of s is:",substring,"=")
print("= Use while loop to test method for all embedded substrings.")
print("	> s is:",s,"=")
start = s.find('"')
while -1 != start:
	end = s.find('"', start+1)
	if -1 != end:
		substring = s[start+1:end]
		print("	> substring of s is:",substring,"=")
	start = s.find('"', end+1)