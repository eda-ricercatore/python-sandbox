#!/usr/local/bin/python3



"""
	This is written by Zhiyang Ong to demonstrate how to:
	+ Delimit and tokenize each full name in a string of full names
		into an element of a list.
	+ Find the number of characters in a string.
	+ Determine if an object is in a list.
	+ Filtering a collection with an if statement in a list comprehension.




	References:
	+ See references cited in text.
	+ pawan_asipu, "Python String | split()," GeekstoGeeks,
		Noida, Uttar Pradesh, India, June 1, 2200.
		Available online from GeekstoGeeks at: https://www.geeksforgeeks.org/python-string-split/;
			October 7, 2020 was the last accessed date.
	+ Wikipedia contributors, ``Regular expression,'' in Wikipedia, The Free Encyclopedia: Pattern matching, Wikimedia Foundation, San Francisco, CA, Pattern matching 7, 2020. Available online at: https://en.wikipedia.org/wiki/Regular_expression; last accessed on October 9, 2020.
		- Regular expressions cannot process text that requires
			context-free grammar (CFG).
			* That is, it is based on regular grammar, rather than
				context-sensitive grammar (CSG).
	+ Wikipedia contributors, ``Parsing expression grammar,'' in Wikipedia, The Free Encyclopedia: Formal languages, Wikimedia Foundation, San Francisco, CA, September 21, 2020. Available online at: https://en.wikipedia.org/wiki/Parsing_expression_grammar; last accessed on October 9, 2020.
		- parsing expression grammar (PEG) is similar to
			context-free grammar (CFG), and cannot be ambiguous.
	+ [DrakeJr2023b]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Tutorial," Python Software Foundation, Beaverton, OR, February 26, 2023. Available online from *Welcome to Python.org: Docs: Python 3.11.2 documentation: Tutorial* at: https://docs.python.org/3/tutorial/; February 26, 2023 was the last accessed date.
	+ [manjeet042023]
		- manjeet\_04, "Python: Check if one list is subset of other," Sanchhaya Education Pvt. Ltd., Noida, Gautam Buddha Nagar, Meerut, Uttar Pradesh, India, February 21, 2023. Available online from *GeeksforGeeks: Python: Python Programming Language* at: https://www.geeksforgeeks.org/python-check-if-one-list-is-subset-of-other/; February 28, 2023 was the last accessed date.
	+ [DrakeJr2023a]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Standard Library," Python Software Foundation, Beaverton, OR, February 26, 2023. Available online from *Welcome to Python.org: Docs: Python 3.11.2 documentation: Library Reference* at: https://docs.python.org/3/library/; February 26, 2023 was the last accessed date.
	+ [Karefylakis2013]
		- James "jamylak" Karefylakis, Answer to "How can I verify if one list is a subset of another?", Stack Exchange Inc., New York, NY, May 16, 2013. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/16579133/1531728 and https://stackoverflow.com/questions/16579085/how-can-i-verify-if-one-list-is-a-subset-of-another/16579133#16579133; March 26, 2023 was the last accessed date.
	+ [WikipediaContributors2023]
		- Wikipedia contributors, "Complement (set theory)," Wikimedia Foundation, San Francisco, CA, January 11, 2023. Available online from *Wikipedia, The Free Encyclopedia: Operations on sets* at: https://en.wikipedia.org/wiki/Complement_(set_theory) and https://en.wikipedia.org/wiki/Complement_(set_theory)#Relative_complement; March 3, 2023 was the last accessed date.
	+ [WikipediaContributors2023a]
		- Wikipedia contributors, "Set theory," Wikimedia Foundation, San Francisco, CA, February 14, 2023. Available online from *Wikipedia, The Free Encyclopedia: Set theory* at: https://en.wikipedia.org/wiki/Set_theory; March 3, 2023 was the last accessed date.
	+ [WikipediaContributors2023b]
		- Wikipedia contributors, "Set (mathematics)," Wikimedia Foundation, San Francisco, CA, January 22, 2023. Available online from *Wikipedia, The Free Encyclopedia: Set theory* and *Wikipedia, The Free Encyclopedia: Mathematical objects* at: https://en.wikipedia.org/wiki/Set_(mathematics) and https://en.wikipedia.org/wiki/Set_(mathematics)#Basic_operations; March 3, 2023 was the last accessed date.
	+ [Kenny2017]
		- Eamonn Kenny, Answer to "How can I verify if one list is a subset of another?", Stack Exchange Inc., New York, NY, November 14, 2017. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/47282975/1531728; March 2, 2023 was the last accessed date.






	Additional resources:
	+ https://runestone.academy/runestone/books/published/fopp/Sequences/SplitandJoin.html
	+ https://www.pitt.edu/~naraehan/python3/split_join.html
	+ https://www.w3resource.com/python-exercises/re/python-re-exercise-47.php
	+ https://docs.python.org/3/reference/lexical_analysis.html#delimiters
	+ https://note.nkmk.me/en/python-split-rsplit-splitlines-re/
"""

###############################################################
#	Import modules from The Python Standard Library.

# Import regular expressions package.
import re


# For the is_list_a_subset_of_another_functools_and_operator_method() method.
"""
	Import the functools module for "higher-order functions and
		operations on callable objects".
"""
from functools import reduce
# Import the operator module for "standard operators as functions".
from operator import __and__
# To enable testing the Python "multiset" approach.
from collections import Counter


###############################################################

print("=========================================================")

"""
	Delimit and tokenize each full name in a string of full names
		into an element of a list.

	A string that I want to delimit and tokenize each full name into
		an element of a list.
"""
string_of_names = "Min Chen and Sergio Gonzalez and Athanasios Vasilakos and Huasong Cao and Victor C. M. Leung"


"""
	The following method works.

	Earlier problems in trying to get it to work resulted from treating
		the delimiter " = " as equivalent to " and ".
	I made this mistake when I was writing the program while being sleepy.




	
	References:
	+ pawan_asipu, "Python String | split()," GeekstoGeeks,
		Noida, Uttar Pradesh, India, June 1, 2200.
		Available online from GeekstoGeeks at: https://www.geeksforgeeks.org/python-string-split/;
			October 7, 2020 was the last accessed date.
"""
#list_of_names = string_of_names.split(' and ')
list_of_names = string_of_names.split(" and ")
print("list_of_names is:",list_of_names,"=")
print("string_of_names.split(' and ') is:",string_of_names.split(" and "),"=")

print("=========================================================")


list_of_names = ["Alberto L. Sangiovanni-Vincentelli", "Eric {von Hippel}", "Donata {von der Leyen}", "Wolff {van Sintern}", "Adolfo Rodriguez Tsourouksdissian", "Evan Driscoll", "Lit-Min Sam", "Albert-L{\'{a}}szl{\'{o}} Barab{\'{a}}si"]

"""
	My solution.

	Reference:
	+ https://docs.python.org/3/library/re.html
		Subsection: re — Regular expression operations
		Section: Text Processing Services
		Document: The Python Standard Library
		From: Python 3.9.0 documentation
"""
for current_name in list_of_names:
	print("Full name is:",current_name,"=")
	tokens = current_name.split(" ")
	tokens = re.split("\{??\}| ",current_name)
	for current_token in tokens:
		print("	current token is:",current_token,"=")


"""
	
	Reference:
	+ https://stackoverflow.com/a/58656637/1531728
		https://stackoverflow.com/questions/38999344/extract-string-within-parentheses-python/58656637#58656637
	+ https://stackoverflow.com/a/38999682/1531728
		https://stackoverflow.com/questions/38999344/extract-string-within-parentheses-python/38999682#38999682

"""
s = "name(something)"
na, so = re.match(r"(.*)\((.*)\)" ,s).groups()
print("na is:",na,"=")
print("so is:",so,"=")


"""
	From above:
	list_of_names = ["Alberto L. Sangiovanni-Vincentelli", "Eric {von Hippel}", "Donata {von der Leyen}", "Wolff {van Sintern}", "Adolfo Rodriguez Tsourouksdissian", "Evan Driscoll", "Lit-Min Sam"]
"""
for i in list_of_names:
	print("	current name is:",i,"=")
	list_of_tokens = re.match(r"(.*)\{(.*)\}| " ,s)
	#list_of_tokens = re.match(r"(.*){(.*)}| " ,s)
	print("	list_of_tokens is:",list_of_tokens,"=")

print("===	Test code on \{\}, instead of \(\) or ().")
list_of_names = ["Alberto L. Sangiovanni-Vincentelli", "Eric (von Hippel)", "Donata (von der Leyen)", "Wolff (van Sintern)", "Adolfo Rodriguez Tsourouksdissian", "Evan Driscoll", "Lit-Min Sam"]
for nn in list_of_names:
	print("	current name is:",nn,"=")
	"""
		The function re.match() will return a match object
			if the regular expression has matches in the given string. 
		+ https://docs.python.org/3/library/re.html
		+ https://docs.python.org/3/library/re.html#match-objects

		Match objects are different from regular expression objects
			(regex objects).
		+ https://docs.python.org/3/library/re.html#regular-expression-objects
		+ egular Expression HOWTO: https://docs.python.org/3/howto/regex.html#regex-howto
		+ https://docs.python.org/3/library/re.html#match-objects


		Reference:
		+ Python contributors, "re — Regular expression operations," from Python: Python 3.9.0 documentation: The Python Standard Library (or, Library Reference): Text Processing Services, Python Software Foundation, October 10, 2020. Available online at: https://docs.python.org/3/library/re.html; last accessed on October 10, 2020.
	"""
	list_of_tokens = re.match(r"(.*)\((.*)\)| " ,nn)
	print("	list_of_tokens is:",list_of_tokens,"=")
	"""
	if list_of_tokens is not None:
		for tt in list_of_tokens:
			print("	Its tokens are:",list_of_tokens,"=")
	"""
"""
	Implement this in the check_names() function for my
		BibTeX management software.


for current_name in list_of_names:
	print("Full name is:",current_name,"=")
	#tokens = current_name.split(" ")
	#tokens = re.match(r'\((.*)\)',current_name).group(1)
	#tokens = re.match(r'\((.*)\)',current_name)
	#tokens = re.match(r"(.*)\((.*)\)",current_name).groups()
	#tokens_1,tokens_2,tokens_3,tokens_4,tokens_5,tokens_6 = re.match(r"(.*)\((.*)\)",current_name).groups()
	#tokens_1,tokens_2,tokens_3 = re.match(r"(.*)\((.*)\)",current_name).groups()
	#tokens_1,tokens_2 = re.match(r"(.*)\((.*)\)",current_name).groups()
	#tokens = re.match(r"(.*)\((.*)\)",current_name).groups()
	tokens = re.match(r"(.*)\((.*)\)",current_name)
	for current_token in tokens:
		print("	current token is:",current_token,"=")
"""

print("=========================================================")


s = "<alpha.Customer[cus_Y4o9qMEZAugtnW] active_card=<alpha.AlphaObject[card]\
 ...>, created=1324336085, description='Customer for My Test App',\
 livemode=False>"

"""
	Reference:
	+ David Alber, https://stackoverflow.com/a/8569256/1531728
		December 20, 2011.
"""
val = s.split('[', 1)[1].split(']')[0]
print("David Alber val is:",val,"=")
tokens = s.split('[')[1].split(']')[0]
"""
	The following does not work since it requires selecting the
		specific token in the initial tokenized result.

	tokens = s.split('[').split(']')
"""
print("tokens is:",tokens,"=")

"""
	Reference:
	+ srgerg and D K, https://stackoverflow.com/a/8569258/1531728
		December 20, 2011.
"""
tokens = re.search(r"\[([A-Za-z0-9_]+)\]", s)
print("srgerg tokens is:",tokens,"=")

tokens = re.search(r"\[(\w+)\]", s)
print("srgerg tokens is:",tokens,"=")


"""
	Reference:
	+ Samuele Santi / redShadow, https://stackoverflow.com/a/8569270/1531728
		December 20, 2011.
"""
tokens = re.match(r"[^[]*\[([^]]*)\]", s).groups()[0]
print("redShadow tokens is:",tokens,"=")

"""
	Reference:
	+ OmaL, https://stackoverflow.com/a/38871907/1531728
		August 10, 2016 and May 23, 2017 (edited by Community moderator)
"""
tokens = s[s.find("[") + 1:s.find("]")]
print("OmaL tokens is:",tokens,"=")


"""
	This method can find all instances of pattern matches.
	Use this method!!!

	Reference:
	+ Brandon Keith Biggs, https://stackoverflow.com/a/31358563/1531728
		July 11, 2015 and May 23, 2017
"""
tokens = re.findall(r"\[([A-Za-z0-9_]+)\]", s)
print("Brandon Keith Biggs tokens is:",tokens,"=")
"""
	"Use re.findall or re.finditer instead."
	"re.findall(pattern, string) returns a list of matching strings."
	"re.finditer(pattern, string) returns an iterator over MatchObject objects."


	To-do:
	+ test with Albert-L{\'{a}}szl{\'{o}} Barab{\'{a}}si



	Reference:
	+ Amber Yust / Amber, Brian Burns, Fernando Wittmann, Wiktor Stribi{\.{z}}ew and Mike Fogel, https://stackoverflow.com/a/4697884/1531728
		January 15, 2011 and January 21, 2020.
"""



"""
	Mr. Jean-Fran{\c{c}}ois Fabre claims that regular expressions
		cannot handle nested brackets (or, "parenthesis nesting")
	+ https://stackoverflow.com/a/42070578/1531728
		- February 6, 2017.

	Hence, we should use the PyPi regex module instead.
	However, Wiktor Stribi{\.{z}}ew claims that it is buggy, and
		should not be used in production code.


	Reference:
	+ Wiktor Stribi{\.{z}}ew, https://stackoverflow.com/a/42073084/1531728
		February 6, 2017

	Also, the method from Ohad Eytan
"""


print("=========================================================")

# Find the number of characters in a string.


"""
	References:
	+ [Striver 2019]
		- Striver, Shubham Singh, and Nidhi, "Python String | count()," GeekstoGeeks, Noida, Uttar Pradesh, India, September 30, 2019.
			Available online from GeektoGeeks at: https://www.geeksforgeeks.org/python-string-count/; October 11, 2020 was the last accessed date.
	+ Roy, Answer to the question "Python: How to count number of letters in a string?", in Codecademy: Codecademy Forums, New York, NY, March 17, 2020.
		Available online from Codecademy: Codecademy Forums at: https://discuss.codecademy.com/t/python-how-to-count-number-of-letters-in-a-string/78055/4; October 11, 2020 was the last accessed date.





	Resources that I look at:
	+ https://www.geeksforgeeks.org/python-string-length-len/
	+ https://www.tutorialspoint.com/python/string_len.htm
	+ https://www.educative.io/edpresso/how-to-find-the-length-of-a-string-in-python
	+ https://www.guru99.com/python-string-length-len.html
	+ https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-2.php
	+ https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/
	+ https://discuss.codecademy.com/t/python-how-to-count-number-of-letters-in-a-string/78055/4

"""

# Trying method len().
one_letter_string = "x"
two_letter_string = "xy"
ten_letter_string = "abcdefghij"

if 1 == len(one_letter_string):
	print("one_letter_string has 1 letter:",one_letter_string,"=")
if 2 == len(two_letter_string):
	print("two_letter_string has 2 letters:",two_letter_string,"=")
if 10 == len(ten_letter_string):
	print("ten_letter_string has 10 letters:",ten_letter_string,"=")


print("=========================================================")

# Determine if an object is in a list.


"""
	Reference:
	+ [Baumstark 2017]
		- Niklas Baumstark, Chris Rands, and Rich "Drise" Moll, 
			https://stackoverflow.com/a/9542768/1531728
			March 3, 2012 and December 14, 2017
	+ Stephane Rolland, Niklas Baumstark, Adam Azam, and Engineero,
		- March 3, 2012 till September 4, 2018.
		- https://stackoverflow.com/q/9542738/1531728

	Notes:
	+ If the BibTeX type is "@conference{", raise an error.
		- This is because we should use the equivalent "@inproceedings{"
			to avoid redundant BibTeX types.
"""

# Method 1: Checking if something is inside [Baumstark 2017]
bibtex_types = ["@book{", "@misc{", "@phdthesis{", "@article{", "@inproceedings{", "@incollection{", "@manual{", "@proceedings{", "@techreport{", "@booklet{", "@inbook{", "@mastersthesis{", "@unpublished{"]


current_bibtex_entry_type = "@incollection{"
if current_bibtex_entry_type in bibtex_types:
	print("The current BibTeX entry type @incollection is valid in bibtex_types.")

current_bibtex_entry_type = "@random{"
if current_bibtex_entry_type not in bibtex_types:
	print("The current BibTeX entry type @random is not valid in bibtex_types.")

current_bibtex_entry_type = "@phdthesis{"
if current_bibtex_entry_type in bibtex_types:
	print("The current BibTeX entry type @phdthesis is valid in bibtex_types.")

"""
	Method 2: Filtering a collection [Baumstark 2017]

	+ Filtering a collection with an if statement in a list comprehension.
	+ Filtering a collection with an if statement in a generator expression.


	From my own Python notes, https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/computer-languages/python.md#python-based-software-development:
	+ In the Section on "Python-based Software Development", 
		"a generator expression implicitly creates an iterable object to iterate over a list/collection of elements and perform an operation on each enumerated item/element \cite[Chapter 2, pp. 35-37]{Alchin2010}".
		- Quoted from my notes:
			* Does not create a sequence-like object that can be indexed or operated like a list; "however, a generator expression can be converted into a list using the built-in list() function" \cite[Chapter 6, section on "Generator Expressions," pp. 110]{Beazley2009}.
"""
list_of_numbers = range(10,30)
# Filtering a collection with an if statement in a list comprehension.
odd_numbers_less_than_20 = [x for x in list_of_numbers if (0==(x%2)) and (20>x)]
print("odd_numbers_less_than_20 as a list:",odd_numbers_less_than_20,"=")
"""
	Filtering a collection with an if statement in a generator expression.

	This method produces a generator object (or object for generator expressions, genexpr)
"""
odd_numbers_less_than_20 = (x for x in list_of_numbers if (0==(x%2)) and (20>x))
"""
	Use the "itertools.tee() function to create [another] version of [my] generator"

	Reference:
	+ 
	https://stackoverflow.com/a/1271481/1531728
"""
print("odd_numbers_less_than_20 as a tuple:",odd_numbers_less_than_20,"=")
# Using the next() method to iterate the generator object, or generator expression.
print("Next element in the sequence:",next(odd_numbers_less_than_20),"=")
print("Next element in the sequence:",next(odd_numbers_less_than_20),"=")
print("Next element in the sequence:",next(odd_numbers_less_than_20),"=")
print("Next element in the sequence:",next(odd_numbers_less_than_20),"=")
for item in odd_numbers_less_than_20:
	print("The next element in sequence is:",item,"=")
generator_obj_to_list = list(odd_numbers_less_than_20)
print("Converted generator object to list:",generator_obj_to_list,"=")







print("--------------------------------------------------------")

"""
	From [DrakeJr2023b, from 5. Data Structures: 5.1. More on Lists]

	https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
"""

# Select a subset of a list without the first element.
a = [30, 41, 62, 93, 34, 505, 716, 5407]
print("a is:",a,"=")
b = a[1:]
print("b (= a[1:]) is:",b,"=")
print("Add the elements 13348 and 13432449 to the end of the list 'a'.")
a.append(13348)
a.append(13432449)
print("Updated list 'a' is:",a,"=")
print("Add the elements 62 and 505 to the end of the list 'a'.")
a.remove(62)
a.remove(505)
print("Updated list 'a' is:",a,"=")
print("")
try:
	a.remove(99)
	print("Removing 99 from list 'a' does not change 'a':",a,"=")
except ValueError:
	print("Removing 99 from list 'a', which does not include 99, would result in an error")
	print("Removing elements from lists, which do not include these elements would result in errors.")
	print("")
print("Empty list 'a'.")
a.clear()
print("Updated list 'a' is:",a,"=")
c = [4,7,6,5,3,9,1,2,8]
print("Before sorting, list 'c' is:",c,"=")
c.sort()
print("After sorting, list 'c' is:",c,"=")
c.reverse()
print("After reversing, list 'c' is:",c,"=")
d = c.copy()
if c == d:
	print("Lists 'c' and 'd' are equivalent in value.")
else:
	print("Lists 'c' and 'd' are different!!!")
if c is d:
	print("Lists 'c' and 'd' are refer to the same object!!!")
else:
	print("Lists 'c' and 'd' are refer to different objects.")
e = c
if e == c:
	print("Lists 'e' and 'c' are equivalent in value.")
else:
	print("Lists 'e' and 'c' are different!!!")
if c is d:
	print("Lists 'c' and 'd' are refer to the same object.")
else:
	print("Lists 'c' and 'd' are refer to different objects!!!")
f = [4,7,6,5,3,9,1,2,8]
print("f is:",f,"=")
x = 17
if x not in f:
	print("x is:",x,"= and is not in f.")
else:
	print("x is found in f, and has the value:",x,"=!!!")
x = 5
if x not in f:
	print("x is:",x,"= and is not in f!!!")
else:
	print("x is found in f, and has the value:",x,"=")


print("")
print("============================================================")
print("")

keyphrases_for_partial_overlap = "MOSFET device physics, transistor characteristics, CMOS processing technology, semiconductor manufacturing, VLSI design rules, design rule checking, DRC, circuit extraction, antenna rules, circuit characterization, circuit performance estimation, circuit delay estimation, logical effort, transistor sizing, power dissipation, on-chip interconnects, wire engineering, repeaters, crosstalk, VLSI design margin, process variations, VLSI design corners, reliability, process technology scaling, ITRS, International Technology Roadmap for Semiconductors, SPICE, device models, device characterization, combinational circuit design, circuit families, leakage, charge sharing, power supply noise, hot spots, process sensitivity, low-power circuit design, silicon-on-insulator circuit design, SOI, silicon-on-insulator, sequential circuit design, latches, flip-flops, dynamic circuits, dynamic logic, domino logic, skew-tolerant domino logic, synchronizer, wave pipelining, structured design strategies, VLSI design methods, VLSI design flows, VLSI design economics, VLSI design styles, interchange formats, logic verification, testbench, regression testing, change management, bug tracking, silicon debug, post-silicon validation, manufacturing test, fault modeling, observability, controllability, fault coverage, ATPG, automatic test pattern generation, DFT, design for testability, BIST, built-in self-test, IDDQ testing, DFM, design for manufacturing, boundary-scan testing, mixed-signal testing, reliability testing, datapath subsystems, adders, comparators, counters, multipliers, dividers, encoders, decoders, shifters, array subsystems, SRAM, DRAM, ROM, read-only memory, shift registers, queues, FIFOs, content-addressable memory, CAM, programmable logic arrays, memory testing, semiconductor packaging, power distribution, on-chip power distribution network, IR drops, Ldi/dt Noise, power network modeling, power supply filtering, substrate noise, I/O pad circuits, level converters, clock system architecture, global clock generation, global clock distribution, clock gating, clock skew, analog circuits, RF circuits, mixed-signal circuits, DAC, ADC, digital-to-analog converters, analog-to-digital converters, operational amplifiers, current mirrors, differential pairs, VHDL, Verilog, sequential logic design, combinational logic design"
list_of_keyphrases_for_partial_overlap = keyphrases_for_partial_overlap.split(", ")
print("list_of_keyphrases_for_partial_overlap is:",list_of_keyphrases_for_partial_overlap,"=")


keyphrases_for_subset = "MOSFET device physics, transistor characteristics, CMOS processing technology, semiconductor manufacturing, VLSI design rules, design rule checking, DRC, circuit extraction, antenna rules, circuit characterization, circuit performance estimation, circuit delay estimation, logical effort, transistor sizing, power dissipation, on-chip interconnects, wire engineering, repeaters, crosstalk, VLSI design margin, process variations, VLSI design corners, reliability, process technology scaling, ITRS, International Technology Roadmap for Semiconductors, SPICE, device models, device characterization, combinational circuit design, circuit families, leakage, charge sharing, power supply noise, hot spots, process sensitivity, low-power circuit design, silicon-on-insulator circuit design, SOI, silicon-on-insulator, sequential circuit design, latches, flip-flops, dynamic circuits, dynamic logic, domino logic, skew-tolerant domino logic, synchronizer, wave pipelining, structured design strategies, VLSI design methods, VLSI design flows, VLSI design economics, VLSI design styles, interchange formats, logic verification, testbench, regression testing, change management, bug tracking, silicon debug, post-silicon validation, manufacturing test, fault modeling, observability, controllability, fault coverage, ATPG, automatic test pattern generation, DFT, design for testability, BIST, built-in self-test, VLSI architecture, IDDQ testing, DFM, design for manufacturing, boundary-scan testing, mixed-signal testing, reliability testing, datapath subsystems, adders, comparators, counters, multipliers, dividers, encoders, decoders, shifters, array subsystems, SRAM, DRAM, ROM, read-only memory, shift registers, queues, FIFOs, content-addressable memory, CAM, programmable logic arrays, memory testing, semiconductor packaging, power distribution, on-chip power distribution network, IR drops, Ldi/dt Noise, power network modeling, power supply filtering, substrate noise, I/O pad circuits, level converters, clock system architecture, VLSI design, global clock generation, global clock distribution, clock gating, clock skew, analog circuits, RF circuits, mixed-signal circuits, DAC, ADC, digital-to-analog converters, analog-to-digital converters, operational amplifiers, current mirrors, differential pairs, VHDL, Verilog, sequential logic design, combinational logic design"
list_of_keyphrases_for_subset = keyphrases_for_subset.split(", ")
print("list_of_keyphrases_for_subset is:",list_of_keyphrases_for_subset,"=")




search_keyphrases = ['VLSI design', 'VLSI design flows', 'VLSI architecture']
print("search_keyphrases is:",search_keyphrases,"=")
search_keyphrases_copy = ['VLSI design', 'VLSI design flows', 'VLSI architecture']
search_keyphrases_diff = ['VLSI design', 'automatic test pattern generation', 'VLSI architecture']
search_keyphrases_with_duplicates = ['VLSI design', 'VLSI architecture', 'VLSI design']
search_keyphrases_with_duplicates_long = ['VLSI design', 'VLSI design flows', 'VLSI architecture', 'automatic test pattern generation', 'automatic test pattern generation', 'VLSI design', 'automatic test pattern generation', 'VLSI architecture', 'automatic test pattern generation']
list_search_keyphrases_disjoint = "machine learning, probabilistic reasoning, belief networks"
search_keyphrases_disjoint = list_search_keyphrases_disjoint.split(", ")




"""
	Method to determine if a list is a subset of another, using the Python
		"universal quantifier" operator, all() [DrakeJr2023a, from Built-in Functions]
		[manjeet042023].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.


	References:
	+ URL for [DrakeJr2023a, from Built-in Functions]
		- https://docs.python.org/3/library/functions.html#all
		- https://docs.python.org/3/library/functions.html#any
"""
def is_list_a_subset_of_another(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, are all the elements/items in the smaller list found
				in the bigger?
		"""
		if all(x in bigger_list for x in smaller_list):
			# Yes.
			return True
		else:
			# No.
			return False



print("Test the Python 'universal quantifier' operator, all().")
if is_list_a_subset_of_another(list_of_keyphrases_for_partial_overlap, search_keyphrases):
	print("search_keyphrases IS A subset of list_of_keyphrases_for_partial_overlap!!!")
else:
	print("search_keyphrases is not a subset of list_of_keyphrases_for_partial_overlap.")






if is_list_a_subset_of_another(list_of_keyphrases_for_subset, search_keyphrases):
	print("search_keyphrases is a subset of list_of_keyphrases_for_subset.")
else:
	print("search_keyphrases IS NOT A subset of list_of_keyphrases_for_subset!!!")



if is_list_a_subset_of_another(search_keyphrases, list_of_keyphrases_for_subset):
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset works.")
else:
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset does not work!!!")



if is_list_a_subset_of_another(search_keyphrases, search_keyphrases_copy):
	print("search_keyphrases_copy and search_keyphrases are identical.")
else:
	print("search_keyphrases_copy and search_keyphrases are NOT identical!!!")
if is_list_a_subset_of_another(search_keyphrases, search_keyphrases_diff):
	print("search_keyphrases_diff and search_keyphrases ARE identical!!!")
else:
	print("search_keyphrases_diff and search_keyphrases are not identical.")
if is_list_a_subset_of_another(list_of_keyphrases_for_subset, search_keyphrases_with_duplicates):
	print("search_keyphrases_with_duplicates is a subset of list_of_keyphrases_for_subset, WHEN DUPLICATES ARE IGNORED!!!")
	print("	is_list_a_subset_of_another(): all(x in bigger_list for x in smaller_list).")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_with_duplicates is not a subset of list_of_keyphrases_for_subset.")
print("Test the use case from [Karefylakis2013].")
if is_list_a_subset_of_another(search_keyphrases, search_keyphrases_with_duplicates_long):
	print("search_keyphrases_with_duplicates_long is a subset of search_keyphrases, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases_with_duplicates_long is not a subset of search_keyphrases.")
if is_list_a_subset_of_another(search_keyphrases_with_duplicates_long, search_keyphrases):
	print("search_keyphrases is a subset of search_keyphrases_with_duplicates_long, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_with_duplicates_long.")











print("")
print("------------------------------------------------------------")
print("")





"""
	Method to determine if a list is a subset of another, using the Python
		issubset() method for sets [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		[manjeet042023].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.


	References:
	+ URL for [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		- https://docs.python.org/3/library/stdtypes.html#frozenset.issubset
"""
def is_list_a_subset_of_another_subset_method(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
	# Is the smaller list actually bigger than the bigger list?
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, is the smaller list a subset of the bigger list,
				after transforming/casting the lists into sets?
		"""
		if (set(smaller_list).issubset(set(bigger_list))):
			# Yes.
			return True
		else:
			# No.
			return False



print("Test the Python approach for the issubset() method for sets.")
if is_list_a_subset_of_another_subset_method(list_of_keyphrases_for_partial_overlap, search_keyphrases):
	print("search_keyphrases IS A subset of list_of_keyphrases_for_partial_overlap!!!")
else:
	print("search_keyphrases is not a subset of list_of_keyphrases_for_partial_overlap.")






if is_list_a_subset_of_another_subset_method(list_of_keyphrases_for_subset, search_keyphrases):
	print("search_keyphrases is a subset of list_of_keyphrases_for_subset.")
else:
	print("search_keyphrases IS NOT A subset of list_of_keyphrases_for_subset!!!")



if is_list_a_subset_of_another_subset_method(search_keyphrases, list_of_keyphrases_for_subset):
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset works.")
else:
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset does not work!!!")


if is_list_a_subset_of_another_subset_method(search_keyphrases, search_keyphrases_copy):
	print("search_keyphrases_copy and search_keyphrases are identical.")
else:
	print("search_keyphrases_copy and search_keyphrases are NOT identical!!!")
if is_list_a_subset_of_another_subset_method(search_keyphrases, search_keyphrases_diff):
	print("search_keyphrases_diff and search_keyphrases ARE identical!!!")
else:
	print("search_keyphrases_diff and search_keyphrases are not identical.")
if is_list_a_subset_of_another_subset_method(list_of_keyphrases_for_subset, search_keyphrases_with_duplicates):
	print("search_keyphrases_with_duplicates is a subset of list_of_keyphrases_for_subset, WHEN DUPLICATES ARE IGNORED!!!")
	print("	is_list_a_subset_of_another_subset_method(): (set(smaller_list).issubset(set(bigger_list))).")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_with_duplicates is not a subset of list_of_keyphrases_for_subset.")
print("Test the use case from [Karefylakis2013].")
if is_list_a_subset_of_another_subset_method(search_keyphrases, search_keyphrases_with_duplicates_long):
	print("search_keyphrases_with_duplicates_long is a subset of search_keyphrases, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases_with_duplicates_long is not a subset of search_keyphrases.")
if is_list_a_subset_of_another_subset_method(search_keyphrases_with_duplicates_long, search_keyphrases):
	print("search_keyphrases is a subset of search_keyphrases_with_duplicates_long, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_with_duplicates_long.")








print("")
print("------------------------------------------------------------")
print("")





"""
	Method to determine if a list is a subset of another, using the Python
		approach for the intersection of sets [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		[manjeet042023].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.


	References:
	+ URL for [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		- https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
"""
def is_list_a_subset_of_another_set_intersection_method(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
	#print("len(smaller_list) is:",len(smaller_list),"=")
	#print("len(bigger_list) is:",len(bigger_list),"=")
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, is the smaller list a subset of the bigger list,
				after transforming/casting the lists into sets?
		"""
		if ((set(smaller_list) & (set(bigger_list))) == (set(smaller_list))):
			# Yes.
			return True
		else:
			# No.
			return False



print("Test the Python approach for the intersection of sets.")
if is_list_a_subset_of_another_set_intersection_method(list_of_keyphrases_for_partial_overlap, search_keyphrases):
	print("search_keyphrases IS A subset of list_of_keyphrases_for_partial_overlap!!!")
else:
	print("search_keyphrases is not a subset of list_of_keyphrases_for_partial_overlap.")






if is_list_a_subset_of_another_set_intersection_method(list_of_keyphrases_for_subset, search_keyphrases):
	print("search_keyphrases is a subset of list_of_keyphrases_for_subset.")
else:
	print("search_keyphrases IS NOT A subset of list_of_keyphrases_for_subset!!!")



if is_list_a_subset_of_another_set_intersection_method(search_keyphrases, list_of_keyphrases_for_subset):
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset works.")
else:
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset does not work!!!")


if is_list_a_subset_of_another_set_intersection_method(search_keyphrases, search_keyphrases_copy):
	print("search_keyphrases_copy and search_keyphrases are identical.")
else:
	print("search_keyphrases_copy and search_keyphrases are NOT identical!!!")
if is_list_a_subset_of_another_set_intersection_method(search_keyphrases, search_keyphrases_diff):
	print("search_keyphrases_diff and search_keyphrases ARE identical!!!")
else:
	print("search_keyphrases_diff and search_keyphrases are not identical.")
if is_list_a_subset_of_another_set_intersection_method(list_of_keyphrases_for_subset, search_keyphrases_with_duplicates):
	print("search_keyphrases_with_duplicates is a subset of list_of_keyphrases_for_subset, WHEN DUPLICATES ARE IGNORED!!!")
	print("	is_list_a_subset_of_another_set_intersection_method(): ((set(smaller_list) & (set(bigger_list))) == (set(smaller_list))).")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_with_duplicates is not a subset of list_of_keyphrases_for_subset.")
print("Test the use case from [Karefylakis2013].")
if is_list_a_subset_of_another_set_intersection_method(search_keyphrases, search_keyphrases_with_duplicates_long):
	print("search_keyphrases_with_duplicates_long is a subset of search_keyphrases, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases_with_duplicates_long is not a subset of search_keyphrases.")
if is_list_a_subset_of_another_set_intersection_method(search_keyphrases_with_duplicates_long, search_keyphrases):
	print("search_keyphrases is a subset of search_keyphrases_with_duplicates_long, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_with_duplicates_long.")










print("")
print("------------------------------------------------------------")
print("")





"""
	Method to determine if a list is a subset of another, using the Python
		intersection() method for sets [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		[manjeet042023].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.


	References:
	+ URL for [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		- https://docs.python.org/3/library/stdtypes.html#frozenset.intersection
"""
def is_list_a_subset_of_another_set_intersection_method_longer(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
	# Is the smaller list actually bigger than the bigger list?
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, is the smaller list a subset of the bigger list,
				after transforming/casting the lists into sets?
		"""
		if (set(smaller_list).intersection(set(bigger_list))) == set(smaller_list):
			# Yes.
			return True
		else:
			# No.
			return False



print("Test the Python approach for the issubset() method for sets - longer method.")
if is_list_a_subset_of_another_set_intersection_method_longer(list_of_keyphrases_for_partial_overlap, search_keyphrases):
	print("search_keyphrases IS A subset of list_of_keyphrases_for_partial_overlap!!!")
else:
	print("search_keyphrases is not a subset of list_of_keyphrases_for_partial_overlap.")






if is_list_a_subset_of_another_set_intersection_method_longer(list_of_keyphrases_for_subset, search_keyphrases):
	print("search_keyphrases is a subset of list_of_keyphrases_for_subset.")
else:
	print("search_keyphrases IS NOT A subset of list_of_keyphrases_for_subset!!!")



if is_list_a_subset_of_another_set_intersection_method_longer(search_keyphrases, list_of_keyphrases_for_subset):
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset works.")
else:
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset does not work!!!")


if is_list_a_subset_of_another_set_intersection_method_longer(search_keyphrases, search_keyphrases_copy):
	print("search_keyphrases_copy and search_keyphrases are identical.")
else:
	print("search_keyphrases_copy and search_keyphrases are NOT identical!!!")
if is_list_a_subset_of_another_set_intersection_method_longer(search_keyphrases, search_keyphrases_diff):
	print("search_keyphrases_diff and search_keyphrases ARE identical!!!")
else:
	print("search_keyphrases_diff and search_keyphrases are not identical.")
if is_list_a_subset_of_another_set_intersection_method_longer(list_of_keyphrases_for_subset, search_keyphrases_with_duplicates):
	print("search_keyphrases_with_duplicates is a subset of list_of_keyphrases_for_subset, WHEN DUPLICATES ARE IGNORED!!!")
	print("	is_list_a_subset_of_another_set_intersection_method_longer(): (set(smaller_list).intersection(set(bigger_list))) == set(smaller_list).")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_with_duplicates is not a subset of list_of_keyphrases_for_subset.")
print("Test the use case from [Karefylakis2013].")
if is_list_a_subset_of_another_set_intersection_method_longer(search_keyphrases, search_keyphrases_with_duplicates_long):
	print("search_keyphrases_with_duplicates_long is a subset of search_keyphrases, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases_with_duplicates_long is not a subset of search_keyphrases.")
if is_list_a_subset_of_another_set_intersection_method_longer(search_keyphrases_with_duplicates_long, search_keyphrases):
	print("search_keyphrases is a subset of search_keyphrases_with_duplicates_long, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_with_duplicates_long.")









print("")
print("------------------------------------------------------------")
print("")



print("set(x in list_of_keyphrases_for_subset for x in search_keyphrases):",set(x in list_of_keyphrases_for_subset for x in search_keyphrases),"=")
print("(x in list_of_keyphrases_for_subset for x in search_keyphrases):",(x in list_of_keyphrases_for_subset for x in search_keyphrases),"=")



"""
	Method to determine if a list is a subset of another, using the Python
		approach for sets [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		[manjeet042023].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.


	References:
	+ URL for [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		- https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
"""
def is_list_a_subset_of_another_set_method(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, is the smaller list a subset of the bigger list, by
				checking if each element in the smaller set is in the
				bigger set?
		"""
		if set(x in bigger_list for x in smaller_list):
		#if set(x in smaller_list for x in bigger_list):
			# Yes.
#			print("bigger_list is:",bigger_list,"=")
#			print("smaller_list is:",smaller_list,"=")
			return True
		else:
			# No.
			return False


print("")
print("Test the Python approach for the set-based set enumerating comparison.")
if is_list_a_subset_of_another_set_method(list_of_keyphrases_for_partial_overlap, search_keyphrases):
	print("search_keyphrases IS A subset of list_of_keyphrases_for_partial_overlap!!!")
else:
	print("search_keyphrases is not a subset of list_of_keyphrases_for_partial_overlap.")






if is_list_a_subset_of_another_set_method(list_of_keyphrases_for_subset, search_keyphrases):
	print("search_keyphrases is a subset of list_of_keyphrases_for_subset.")
else:
	print("search_keyphrases IS NOT A subset of list_of_keyphrases_for_subset!!!")



if is_list_a_subset_of_another_set_method(search_keyphrases, list_of_keyphrases_for_subset):
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset works.")
else:
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset does not work!!!")



if is_list_a_subset_of_another_set_method(search_keyphrases, search_keyphrases_copy):
	print("search_keyphrases_copy and search_keyphrases are identical.")
else:
	print("search_keyphrases_copy and search_keyphrases are NOT identical!!!")
if is_list_a_subset_of_another_set_method(search_keyphrases, search_keyphrases_diff):
	print("search_keyphrases_diff and search_keyphrases ARE identical!!!")
	print("	is_list_a_subset_of_another_set_method() fails to work for different lists of the same size.")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_diff and search_keyphrases are not identical.")
if is_list_a_subset_of_another_set_method(list_of_keyphrases_for_subset, search_keyphrases_with_duplicates):
	print("search_keyphrases_with_duplicates is a subset of list_of_keyphrases_for_subset, WHEN DUPLICATES ARE IGNORED!!!")
	print("	is_list_a_subset_of_another_functools_and_operator_method(): reduce(__and__, [x in bigger_list for x in smaller_list]) fails to work for duplicates.")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_with_duplicates is not a subset of list_of_keyphrases_for_subset.")
print("Test the use case from [Karefylakis2013].")
if is_list_a_subset_of_another_set_method(search_keyphrases, search_keyphrases_with_duplicates_long):
	print("search_keyphrases_with_duplicates_long is a subset of search_keyphrases, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases_with_duplicates_long is not a subset of search_keyphrases.")
if is_list_a_subset_of_another_set_method(search_keyphrases_with_duplicates_long, search_keyphrases):
	print("search_keyphrases is a subset of search_keyphrases_with_duplicates_long, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_with_duplicates_long.")















print("")
print("------------------------------------------------------------")
print("")






"""
	Method to determine if a list is a subset of another, using functools.reduce()
		[DrakeJr2023a, from functools - Higher-order functions and operations on callable objects]
		and [DrakeJr2023a, from operator - Standard operators as functions]
		[manjeet042023].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.


	References:
	+ URL for [DrakeJr2023a, from functools - Higher-order functions and operations on callable objects]
		- https://docs.python.org/3/library/functools.html#functools.reduce
	+ URL for [DrakeJr2023a, from operator - Standard operators as functions]
		- https://docs.python.org/3/library/operator.html#operator.__and__
"""
#def is_list_a_subset_of_another_functools_and_operator_method(bigger_list=None, smaller_list=None) -> bool:
def is_list_a_subset_of_another_functools_and_operator_method(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, is the smaller list a subset of the bigger list, by
				checking if each element in the smaller set is in the
				bigger set?
		"""
		return reduce(__and__, [x in bigger_list for x in smaller_list])



print("Test the Python approach for higher-order functions and 'and' operator.")
if is_list_a_subset_of_another_functools_and_operator_method(list_of_keyphrases_for_partial_overlap, search_keyphrases):
	print("search_keyphrases IS A subset of list_of_keyphrases_for_partial_overlap!!!")
else:
	print("search_keyphrases is not a subset of list_of_keyphrases_for_partial_overlap.")






if is_list_a_subset_of_another_functools_and_operator_method(list_of_keyphrases_for_subset, search_keyphrases):
	print("search_keyphrases is a subset of list_of_keyphrases_for_subset.")
else:
	print("search_keyphrases IS NOT A subset of list_of_keyphrases_for_subset!!!")



if is_list_a_subset_of_another_functools_and_operator_method(search_keyphrases, list_of_keyphrases_for_subset):
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset works.")
else:
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset does not work!!!")



if is_list_a_subset_of_another_functools_and_operator_method(search_keyphrases, search_keyphrases_copy):
	print("search_keyphrases_copy and search_keyphrases are identical.")
else:
	print("search_keyphrases_copy and search_keyphrases are NOT identical!!!")
if is_list_a_subset_of_another_functools_and_operator_method(search_keyphrases, search_keyphrases_diff):
	print("search_keyphrases_diff and search_keyphrases ARE identical!!!")
else:
	print("search_keyphrases_diff and search_keyphrases are not identical.")
if is_list_a_subset_of_another_functools_and_operator_method(list_of_keyphrases_for_subset, search_keyphrases_with_duplicates):
	print("search_keyphrases_with_duplicates is a subset of list_of_keyphrases_for_subset, WHEN DUPLICATES ARE IGNORED!!!")
	print("	is_list_a_subset_of_another_functools_and_operator_method(): reduce(__and__, [x in bigger_list for x in smaller_list]) fails to work for duplicates.")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_with_duplicates is not a subset of list_of_keyphrases_for_subset.")
print("Test the use case from [Karefylakis2013].")
if is_list_a_subset_of_another_functools_and_operator_method(search_keyphrases, search_keyphrases_with_duplicates_long):
	print("search_keyphrases_with_duplicates_long is a subset of search_keyphrases, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases_with_duplicates_long is not a subset of search_keyphrases.")
if is_list_a_subset_of_another_functools_and_operator_method(search_keyphrases_with_duplicates_long, search_keyphrases):
	print("search_keyphrases is a subset of search_keyphrases_with_duplicates_long, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_with_duplicates_long.")

















print("")
print("------------------------------------------------------------")
print("")



"""
	Method to determine if a list is a subset of another, using the Python
		approach for sets [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		[manjeet042023].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.


	References:
	+ URL for [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		- https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
"""
def is_list_a_subset_of_another_set_comparison_method(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, is the smaller list a subset of the bigger list, by
				using the "<=" operator to do the comparison?
		"""
		if set(smaller_list) <= set(bigger_list):
			# Yes.
			return True
		else:
			# No.
			return False



print("Test the Python approach for the set comparison method with '<='.")
if is_list_a_subset_of_another_set_comparison_method(list_of_keyphrases_for_partial_overlap, search_keyphrases):
	print("search_keyphrases IS A subset of list_of_keyphrases_for_partial_overlap!!!")
else:
	print("search_keyphrases is not a subset of list_of_keyphrases_for_partial_overlap.")






if is_list_a_subset_of_another_set_comparison_method(list_of_keyphrases_for_subset, search_keyphrases):
	print("search_keyphrases is a subset of list_of_keyphrases_for_subset.")
else:
	print("search_keyphrases IS NOT A subset of list_of_keyphrases_for_subset!!!")



if is_list_a_subset_of_another_set_comparison_method(search_keyphrases, list_of_keyphrases_for_subset):
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset works.")
else:
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset does not work!!!")



if is_list_a_subset_of_another_set_comparison_method(search_keyphrases, search_keyphrases_copy):
	print("search_keyphrases_copy and search_keyphrases are identical.")
else:
	print("search_keyphrases_copy and search_keyphrases are NOT identical!!!")
if is_list_a_subset_of_another_set_comparison_method(search_keyphrases, search_keyphrases_diff):
	print("search_keyphrases_diff and search_keyphrases ARE identical!!!")
	print("	is_list_a_subset_of_another_set_method() fails to work for different lists of the same size.")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_diff and search_keyphrases are not identical.")
if is_list_a_subset_of_another_set_comparison_method(list_of_keyphrases_for_subset, search_keyphrases_with_duplicates):
	print("search_keyphrases_with_duplicates is a subset of list_of_keyphrases_for_subset, WHEN DUPLICATES ARE IGNORED!!!")
	print("	is_list_a_subset_of_another_set_comparison_method(): set(smaller_list) <= set(bigger_list) fails to work for duplicates.")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_with_duplicates is not a subset of list_of_keyphrases_for_subset.")
print("Test the use case from [Karefylakis2013].")
if is_list_a_subset_of_another_set_comparison_method(search_keyphrases, search_keyphrases_with_duplicates_long):
	print("search_keyphrases_with_duplicates_long is a subset of search_keyphrases, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases_with_duplicates_long is not a subset of search_keyphrases.")
if is_list_a_subset_of_another_set_comparison_method(search_keyphrases_with_duplicates_long, search_keyphrases):
	print("search_keyphrases is a subset of search_keyphrases_with_duplicates_long, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_with_duplicates_long.")




















print("")
print("------------------------------------------------------------")
print("")





"""
	Method to determine if a list is a subset of another, using the Python
		issubset() method for sets [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		[manjeet042023].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.


	References:
	+ URL for [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		- https://docs.python.org/3/library/stdtypes.html#frozenset.issubset
"""
def is_list_a_subset_of_another_subset_method(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
	# Is the smaller list actually bigger than the bigger list?
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, is the smaller list a subset of the bigger list,
				after transforming/casting the lists into sets?
		"""
		if (set(smaller_list).issubset(set(bigger_list))):
			# Yes.
			return True
		else:
			# No.
			return False



print("Test the Python approach for the issubset() method for sets.")
if is_list_a_subset_of_another_subset_method(list_of_keyphrases_for_partial_overlap, search_keyphrases):
	print("search_keyphrases IS A subset of list_of_keyphrases_for_partial_overlap!!!")
else:
	print("search_keyphrases is not a subset of list_of_keyphrases_for_partial_overlap.")






if is_list_a_subset_of_another_subset_method(list_of_keyphrases_for_subset, search_keyphrases):
	print("search_keyphrases is a subset of list_of_keyphrases_for_subset.")
else:
	print("search_keyphrases IS NOT A subset of list_of_keyphrases_for_subset!!!")



if is_list_a_subset_of_another_subset_method(search_keyphrases, list_of_keyphrases_for_subset):
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset works.")
else:
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset does not work!!!")


if is_list_a_subset_of_another_subset_method(search_keyphrases, search_keyphrases_copy):
	print("search_keyphrases_copy and search_keyphrases are identical.")
else:
	print("search_keyphrases_copy and search_keyphrases are NOT identical!!!")
if is_list_a_subset_of_another_subset_method(search_keyphrases, search_keyphrases_diff):
	print("search_keyphrases_diff and search_keyphrases ARE identical!!!")
else:
	print("search_keyphrases_diff and search_keyphrases are not identical.")
if is_list_a_subset_of_another_subset_method(list_of_keyphrases_for_subset, search_keyphrases_with_duplicates):
	print("search_keyphrases_with_duplicates is a subset of list_of_keyphrases_for_subset, WHEN DUPLICATES ARE IGNORED!!!")
	print("	is_list_a_subset_of_another_subset_method(): (set(smaller_list).issubset(set(bigger_list))).")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_with_duplicates is not a subset of list_of_keyphrases_for_subset.")
print("Test the use case from [Karefylakis2013].")
if is_list_a_subset_of_another_subset_method(search_keyphrases, search_keyphrases_with_duplicates_long):
	print("search_keyphrases_with_duplicates_long is a subset of search_keyphrases, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases_with_duplicates_long is not a subset of search_keyphrases.")
if is_list_a_subset_of_another_subset_method(search_keyphrases_with_duplicates_long, search_keyphrases):
	print("search_keyphrases is a subset of search_keyphrases_with_duplicates_long, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_with_duplicates_long.")








print("")
print("------------------------------------------------------------")
print("")





"""
	Method to determine if a list is a subset of another, using the Python
		approach for the intersection of sets [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		[manjeet042023].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.


	References:
	+ URL for [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		- https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
"""
def is_list_a_subset_of_another_set_intersection_method(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
	#print("len(smaller_list) is:",len(smaller_list),"=")
	#print("len(bigger_list) is:",len(bigger_list),"=")
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, is the smaller list a subset of the bigger list,
				after transforming/casting the lists into sets?
		"""
		if ((set(smaller_list) & (set(bigger_list))) == (set(smaller_list))):
			# Yes.
			return True
		else:
			# No.
			return False



print("Test the Python approach for the intersection of sets.")
if is_list_a_subset_of_another_set_intersection_method(list_of_keyphrases_for_partial_overlap, search_keyphrases):
	print("search_keyphrases IS A subset of list_of_keyphrases_for_partial_overlap!!!")
else:
	print("search_keyphrases is not a subset of list_of_keyphrases_for_partial_overlap.")






if is_list_a_subset_of_another_set_intersection_method(list_of_keyphrases_for_subset, search_keyphrases):
	print("search_keyphrases is a subset of list_of_keyphrases_for_subset.")
else:
	print("search_keyphrases IS NOT A subset of list_of_keyphrases_for_subset!!!")



if is_list_a_subset_of_another_set_intersection_method(search_keyphrases, list_of_keyphrases_for_subset):
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset works.")
else:
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset does not work!!!")


if is_list_a_subset_of_another_set_intersection_method(search_keyphrases, search_keyphrases_copy):
	print("search_keyphrases_copy and search_keyphrases are identical.")
else:
	print("search_keyphrases_copy and search_keyphrases are NOT identical!!!")
if is_list_a_subset_of_another_set_intersection_method(search_keyphrases, search_keyphrases_diff):
	print("search_keyphrases_diff and search_keyphrases ARE identical!!!")
else:
	print("search_keyphrases_diff and search_keyphrases are not identical.")
if is_list_a_subset_of_another_set_intersection_method(list_of_keyphrases_for_subset, search_keyphrases_with_duplicates):
	print("search_keyphrases_with_duplicates is a subset of list_of_keyphrases_for_subset, WHEN DUPLICATES ARE IGNORED!!!")
	print("	is_list_a_subset_of_another_set_intersection_method(): ((set(smaller_list) & (set(bigger_list))) == (set(smaller_list))).")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_with_duplicates is not a subset of list_of_keyphrases_for_subset.")
print("Test the use case from [Karefylakis2013].")
if is_list_a_subset_of_another_set_intersection_method(search_keyphrases, search_keyphrases_with_duplicates_long):
	print("search_keyphrases_with_duplicates_long is a subset of search_keyphrases, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases_with_duplicates_long is not a subset of search_keyphrases.")
if is_list_a_subset_of_another_set_intersection_method(search_keyphrases_with_duplicates_long, search_keyphrases):
	print("search_keyphrases is a subset of search_keyphrases_with_duplicates_long, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_with_duplicates_long.")










print("")
print("------------------------------------------------------------")
print("")





"""
	Method to determine if a list is a subset of another, using the Python
		intersection() method for sets [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		[manjeet042023].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.


	References:
	+ URL for [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		- https://docs.python.org/3/library/stdtypes.html#frozenset.intersection
"""
def is_list_a_subset_of_another_set_intersection_method_longer(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
	# Is the smaller list actually bigger than the bigger list?
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, is the smaller list a subset of the bigger list,
				after transforming/casting the lists into sets?
		"""
		if (set(smaller_list).intersection(set(bigger_list))) == set(smaller_list):
			# Yes.
			return True
		else:
			# No.
			return False



print("Test the Python approach for the issubset() method for sets - longer method.")
if is_list_a_subset_of_another_set_intersection_method_longer(list_of_keyphrases_for_partial_overlap, search_keyphrases):
	print("search_keyphrases IS A subset of list_of_keyphrases_for_partial_overlap!!!")
else:
	print("search_keyphrases is not a subset of list_of_keyphrases_for_partial_overlap.")






if is_list_a_subset_of_another_set_intersection_method_longer(list_of_keyphrases_for_subset, search_keyphrases):
	print("search_keyphrases is a subset of list_of_keyphrases_for_subset.")
else:
	print("search_keyphrases IS NOT A subset of list_of_keyphrases_for_subset!!!")



if is_list_a_subset_of_another_set_intersection_method_longer(search_keyphrases, list_of_keyphrases_for_subset):
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset works.")
else:
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset does not work!!!")


if is_list_a_subset_of_another_set_intersection_method_longer(search_keyphrases, search_keyphrases_copy):
	print("search_keyphrases_copy and search_keyphrases are identical.")
else:
	print("search_keyphrases_copy and search_keyphrases are NOT identical!!!")
if is_list_a_subset_of_another_set_intersection_method_longer(search_keyphrases, search_keyphrases_diff):
	print("search_keyphrases_diff and search_keyphrases ARE identical!!!")
else:
	print("search_keyphrases_diff and search_keyphrases are not identical.")
if is_list_a_subset_of_another_set_intersection_method_longer(list_of_keyphrases_for_subset, search_keyphrases_with_duplicates):
	print("search_keyphrases_with_duplicates is a subset of list_of_keyphrases_for_subset, WHEN DUPLICATES ARE IGNORED!!!")
	print("	is_list_a_subset_of_another_set_intersection_method_longer(): (set(smaller_list).intersection(set(bigger_list))) == set(smaller_list).")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_with_duplicates is not a subset of list_of_keyphrases_for_subset.")
print("Test the use case from [Karefylakis2013].")
if is_list_a_subset_of_another_set_intersection_method_longer(search_keyphrases, search_keyphrases_with_duplicates_long):
	print("search_keyphrases_with_duplicates_long is a subset of search_keyphrases, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases_with_duplicates_long is not a subset of search_keyphrases.")
if is_list_a_subset_of_another_set_intersection_method_longer(search_keyphrases_with_duplicates_long, search_keyphrases):
	print("search_keyphrases is a subset of search_keyphrases_with_duplicates_long, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_with_duplicates_long.")









print("")
print("------------------------------------------------------------")
print("")



print("set(x in list_of_keyphrases_for_subset for x in search_keyphrases):",set(x in list_of_keyphrases_for_subset for x in search_keyphrases),"=")
print("(x in list_of_keyphrases_for_subset for x in search_keyphrases):",(x in list_of_keyphrases_for_subset for x in search_keyphrases),"=")



"""
	Method to determine if a list is a subset of another, using the Python
		approach for sets [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		[manjeet042023].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.


	References:
	+ URL for [DrakeJr2023a, from Built-in Functions: Set Types — set, frozenset]
		- https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
"""
def is_list_a_subset_of_another_set_method(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, is the smaller list a subset of the bigger list, by
				checking if each element in the smaller set is in the
				bigger set?
		"""
		if set(x in bigger_list for x in smaller_list):
		#if set(x in smaller_list for x in bigger_list):
			# Yes.
#			print("bigger_list is:",bigger_list,"=")
#			print("smaller_list is:",smaller_list,"=")
			return True
		else:
			# No.
			return False


print("")
print("Test the Python approach for the set-based set enumerating comparison.")
if is_list_a_subset_of_another_set_method(list_of_keyphrases_for_partial_overlap, search_keyphrases):
	print("search_keyphrases IS A subset of list_of_keyphrases_for_partial_overlap!!!")
else:
	print("search_keyphrases is not a subset of list_of_keyphrases_for_partial_overlap.")






if is_list_a_subset_of_another_set_method(list_of_keyphrases_for_subset, search_keyphrases):
	print("search_keyphrases is a subset of list_of_keyphrases_for_subset.")
else:
	print("search_keyphrases IS NOT A subset of list_of_keyphrases_for_subset!!!")



if is_list_a_subset_of_another_set_method(search_keyphrases, list_of_keyphrases_for_subset):
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset works.")
else:
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset does not work!!!")



if is_list_a_subset_of_another_set_method(search_keyphrases, search_keyphrases_copy):
	print("search_keyphrases_copy and search_keyphrases are identical.")
else:
	print("search_keyphrases_copy and search_keyphrases are NOT identical!!!")
if is_list_a_subset_of_another_set_method(search_keyphrases, search_keyphrases_diff):
	print("search_keyphrases_diff and search_keyphrases ARE identical!!!")
	print("	is_list_a_subset_of_another_set_method() fails to work for different lists of the same size.")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_diff and search_keyphrases are not identical.")
if is_list_a_subset_of_another_set_method(list_of_keyphrases_for_subset, search_keyphrases_with_duplicates):
	print("search_keyphrases_with_duplicates is a subset of list_of_keyphrases_for_subset, WHEN DUPLICATES ARE IGNORED!!!")
	print("	is_list_a_subset_of_another_functools_and_operator_method(): reduce(__and__, [x in bigger_list for x in smaller_list]) fails to work for duplicates.")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_with_duplicates is not a subset of list_of_keyphrases_for_subset.")
print("Test the use case from [Karefylakis2013].")
if is_list_a_subset_of_another_set_method(search_keyphrases, search_keyphrases_with_duplicates_long):
	print("search_keyphrases_with_duplicates_long is a subset of search_keyphrases, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases_with_duplicates_long is not a subset of search_keyphrases.")
if is_list_a_subset_of_another_set_method(search_keyphrases_with_duplicates_long, search_keyphrases):
	print("search_keyphrases is a subset of search_keyphrases_with_duplicates_long, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_with_duplicates_long.")















print("")
print("------------------------------------------------------------")
print("")






"""
	Method to determine if a list is a subset of another, using functools.reduce()
		[DrakeJr2023a, from functools - Higher-order functions and operations on callable objects]
		and [DrakeJr2023a, from operator - Standard operators as functions]
		[manjeet042023].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.


	References:
	+ URL for [DrakeJr2023a, from functools - Higher-order functions and operations on callable objects]
		- https://docs.python.org/3/library/functools.html#functools.reduce
	+ URL for [DrakeJr2023a, from operator - Standard operators as functions]
		- https://docs.python.org/3/library/operator.html#operator.__and__
"""
#def is_list_a_subset_of_another_functools_and_operator_method(bigger_list=None, smaller_list=None) -> bool:
def is_list_a_subset_of_another_functools_and_operator_method(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, is the smaller list a subset of the bigger list, by
				checking if each element in the smaller set is in the
				bigger set?
		"""
		return reduce(__and__, [x in bigger_list for x in smaller_list])



print("Test the Python approach for higher-order functions and 'and' operator.")
if is_list_a_subset_of_another_functools_and_operator_method(list_of_keyphrases_for_partial_overlap, search_keyphrases):
	print("search_keyphrases IS A subset of list_of_keyphrases_for_partial_overlap!!!")
else:
	print("search_keyphrases is not a subset of list_of_keyphrases_for_partial_overlap.")






if is_list_a_subset_of_another_functools_and_operator_method(list_of_keyphrases_for_subset, search_keyphrases):
	print("search_keyphrases is a subset of list_of_keyphrases_for_subset.")
else:
	print("search_keyphrases IS NOT A subset of list_of_keyphrases_for_subset!!!")



if is_list_a_subset_of_another_functools_and_operator_method(search_keyphrases, list_of_keyphrases_for_subset):
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset works.")
else:
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset does not work!!!")



if is_list_a_subset_of_another_functools_and_operator_method(search_keyphrases, search_keyphrases_copy):
	print("search_keyphrases_copy and search_keyphrases are identical.")
else:
	print("search_keyphrases_copy and search_keyphrases are NOT identical!!!")
if is_list_a_subset_of_another_functools_and_operator_method(search_keyphrases, search_keyphrases_diff):
	print("search_keyphrases_diff and search_keyphrases ARE identical!!!")
else:
	print("search_keyphrases_diff and search_keyphrases are not identical.")
if is_list_a_subset_of_another_functools_and_operator_method(list_of_keyphrases_for_subset, search_keyphrases_with_duplicates):
	print("search_keyphrases_with_duplicates is a subset of list_of_keyphrases_for_subset, WHEN DUPLICATES ARE IGNORED!!!")
	print("	is_list_a_subset_of_another_functools_and_operator_method(): reduce(__and__, [x in bigger_list for x in smaller_list]) fails to work for duplicates.")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_with_duplicates is not a subset of list_of_keyphrases_for_subset.")
print("Test the use case from [Karefylakis2013].")
if is_list_a_subset_of_another_functools_and_operator_method(search_keyphrases, search_keyphrases_with_duplicates_long):
	print("search_keyphrases_with_duplicates_long is a subset of search_keyphrases, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases_with_duplicates_long is not a subset of search_keyphrases.")
if is_list_a_subset_of_another_functools_and_operator_method(search_keyphrases_with_duplicates_long, search_keyphrases):
	print("search_keyphrases is a subset of search_keyphrases_with_duplicates_long, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_with_duplicates_long.")

















print("")
print("------------------------------------------------------------")
print("")



"""
	Method to determine if a list is a subset of another, using the Python
		approach for multisets [Karefylakis2013] and set difference
		[WikipediaContributors2023] [WikipediaContributors2023a] [WikipediaContributors2023b].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.
"""
def is_list_a_subset_of_another_multiset_method(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, is the smaller list a subset of the bigger list, by
				using the set difference "-" operator to do the comparison?
		"""
		if not (Counter(bigger_list) - Counter(smaller_list)):
			# Yes.
			return True
		else:
			# No.
			print("(Counter(bigger_list) - Counter(smaller_list)) is:",(Counter(bigger_list) - Counter(smaller_list)),"=")
			return False



print("Test the Python approach for the set comparison method with 'multiset'.")
if is_list_a_subset_of_another_multiset_method(list_of_keyphrases_for_partial_overlap, search_keyphrases):
	print("search_keyphrases IS A subset of list_of_keyphrases_for_partial_overlap!!!")
else:
	print("search_keyphrases is not a subset of list_of_keyphrases_for_partial_overlap.")






if is_list_a_subset_of_another_multiset_method(list_of_keyphrases_for_subset, search_keyphrases):
	print("search_keyphrases is a subset of list_of_keyphrases_for_subset.")
else:
	print("search_keyphrases IS NOT A subset of list_of_keyphrases_for_subset!!!")



if is_list_a_subset_of_another_multiset_method(search_keyphrases, list_of_keyphrases_for_subset):
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset works.")
else:
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset does not work!!!")



if is_list_a_subset_of_another_multiset_method(search_keyphrases, search_keyphrases_copy):
	print("search_keyphrases_copy and search_keyphrases are identical.")
else:
	print("search_keyphrases_copy and search_keyphrases are NOT identical!!!")
if is_list_a_subset_of_another_multiset_method(search_keyphrases, search_keyphrases_diff):
	print("search_keyphrases_diff and search_keyphrases ARE identical!!!")
	print("	is_list_a_subset_of_another_multiset_method() fails to work for different lists of the same size.")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_diff and search_keyphrases are not identical.")
if is_list_a_subset_of_another_multiset_method(list_of_keyphrases_for_subset, search_keyphrases_with_duplicates):
	print("search_keyphrases_with_duplicates is a subset of list_of_keyphrases_for_subset, WHEN DUPLICATES ARE IGNORED!!!")
	print("	is_list_a_subset_of_another_multiset_method(): set subtract approach fails to work for duplicates.")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_with_duplicates is not a subset of list_of_keyphrases_for_subset.")
print("Test the use case from [Karefylakis2013].")
if is_list_a_subset_of_another_multiset_method(search_keyphrases, search_keyphrases_with_duplicates_long):
	print("search_keyphrases_with_duplicates_long is a subset of search_keyphrases, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases_with_duplicates_long is not a subset of search_keyphrases.")
if is_list_a_subset_of_another_multiset_method(search_keyphrases_with_duplicates_long, search_keyphrases):
	print("search_keyphrases is a subset of search_keyphrases_with_duplicates_long, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_with_duplicates_long.")

if is_list_a_subset_of_another_multiset_method(search_keyphrases_disjoint, search_keyphrases):
	print("search_keyphrases IS A subset of search_keyphrases_disjoint!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_disjoint.")
if is_list_a_subset_of_another_multiset_method(search_keyphrases, search_keyphrases_disjoint):
	print("search_keyphrases_disjoint IS A subset of search_keyphrases!!!")
else:
	print("search_keyphrases_disjoint is not a subset of search_keyphrases.")




















print("")
print("------------------------------------------------------------")
print("")



"""
	Method to determine if a list is a subset of another, using the Python
		approach for multisets [Karefylakis2013] and set difference
		[WikipediaContributors2023] [WikipediaContributors2023a] [WikipediaContributors2023b] [Kenny2017].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.
"""
def is_list_a_subset_of_another_multiset_method_with_comparisons(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, does the value of a key in smaller list greater than
				the value of the same key in the bigger list, by
				using the Counter ">" operator to do the comparison?
		"""
		bigger_count = Counter(bigger_list)
		smaller_count = Counter(smaller_list)
		"""
			Enumerate each key in the smaller Counter object or multiset.

			Counter no longer has a has_key() method [DrakeJr2023a].

			Use the "in" operator (or contains(seq, obj) function)
				instead [Kenny2017] [Guerrero2022] [Nguyen2019] [Reddy2018].


			[DrakeJr2023a, from Functional Programming Modules: operator — Standard operators as functions]
			https://docs.python.org/3/library/operator.html#operator.contains


			[DrakeJr2023a, from Functional Programming Modules: operator — Standard operators as functions: Mapping Operators to Functions]
			https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
		"""
		for key in smaller_count:
			"""
				For the currently enumerated key (or key-value pair)
					in the smaller list or Counter object, is it not
					found in the larger list or Counter object?
			"""
			if (key in bigger_count) == False:
				# It is not found in the larger list or Counter object.
				return False
			"""
				Is item of the smaller list, or key of the smaller
					Counter, occuring more in the smaller list than
					in the bigger list?

				For the currently enumerated key (or key-value pair)
					in the smaller list, is its value greater than
					that of the larger list?
			"""
			if smaller_count[key] > bigger_count[key]:
				"""
					Yes, the smaller list has more instances of an
						item than the bigger list.
				"""
				return False
		return True



print("Test the Python approach for Counter/'multiset' approach with '>'.")
if is_list_a_subset_of_another_multiset_method_with_comparisons(list_of_keyphrases_for_partial_overlap, search_keyphrases):
	print("search_keyphrases IS A subset of list_of_keyphrases_for_partial_overlap!!!")
else:
	print("search_keyphrases is not a subset of list_of_keyphrases_for_partial_overlap.")






if is_list_a_subset_of_another_multiset_method_with_comparisons(list_of_keyphrases_for_subset, search_keyphrases):
	print("search_keyphrases is a subset of list_of_keyphrases_for_subset.")
else:
	print("search_keyphrases IS NOT A subset of list_of_keyphrases_for_subset!!!")



if is_list_a_subset_of_another_multiset_method_with_comparisons(search_keyphrases, list_of_keyphrases_for_subset):
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset works.")
else:
	print("Swapped search_keyphrases and list_of_keyphrases_for_subset does not work!!!")



if is_list_a_subset_of_another_multiset_method_with_comparisons(search_keyphrases, search_keyphrases_copy):
	print("search_keyphrases_copy and search_keyphrases are identical.")
else:
	print("search_keyphrases_copy and search_keyphrases are NOT identical!!!")
if is_list_a_subset_of_another_multiset_method_with_comparisons(search_keyphrases, search_keyphrases_diff):
	print("search_keyphrases_diff and search_keyphrases ARE identical!!!")
	print("	is_list_a_subset_of_another_multiset_method_with_comparisons() fails to work for different lists of the same size.")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_diff and search_keyphrases are not identical.")
if is_list_a_subset_of_another_multiset_method_with_comparisons(list_of_keyphrases_for_subset, search_keyphrases_with_duplicates):
	print("search_keyphrases_with_duplicates is a subset of list_of_keyphrases_for_subset, WHEN DUPLICATES ARE IGNORED!!!")
	print("	is_list_a_subset_of_another_multiset_method_with_comparisons(): set subtract approach fails to work for duplicates.")
	print("	Do not use this approach!!!")
else:
	print("search_keyphrases_with_duplicates is not a subset of list_of_keyphrases_for_subset.")
print("Test the use case from [Karefylakis2013].")
if is_list_a_subset_of_another_multiset_method_with_comparisons(search_keyphrases, search_keyphrases_with_duplicates_long):
	print("search_keyphrases_with_duplicates_long is a subset of search_keyphrases, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases_with_duplicates_long is not a subset of search_keyphrases.")
if is_list_a_subset_of_another_multiset_method_with_comparisons(search_keyphrases_with_duplicates_long, search_keyphrases):
	print("search_keyphrases is a subset of search_keyphrases_with_duplicates_long, WHEN DUPLICATES ARE IGNORED!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_with_duplicates_long.")

if is_list_a_subset_of_another_multiset_method_with_comparisons(search_keyphrases_disjoint, search_keyphrases):
	print("search_keyphrases IS A subset of search_keyphrases_disjoint!!!")
else:
	print("search_keyphrases is not a subset of search_keyphrases_disjoint.")
if is_list_a_subset_of_another_multiset_method_with_comparisons(search_keyphrases, search_keyphrases_disjoint):
	print("search_keyphrases_disjoint IS A subset of search_keyphrases!!!")
else:
	print("search_keyphrases_disjoint is not a subset of search_keyphrases.")



















