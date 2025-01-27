#!/Library/Frameworks/Python.framework/Versions/Current/bin/python3
###	#!/opt/anaconda3/bin/python
###	#!/usr/local/bin/python3


"""
	This Python script is written by Zhiyang Ong to perform
		randomized bipartite matching between entities in
		two categories.


	Synopsis:
	Perform randomized bipartite matching.

	This script can be executed as follows:
	./randomized_bipartite_matching_clean.py


	Notes:
	+ Has a bug due to the aliasing problem, where members of
		a pseudo-random generated category can have the same value.
		- Mimics real-world scenarios where/when people
			can have the same name.


	References from my BibTeX database.
	+ [Loreto2019]

	Revision History:
	January 6, 2025			Version 1.0	Script.
	January 6, 2025			Version 1.1	Script. Cleaned version.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.1'
__date__ = 'January 6, 2025'

#	The MIT License (MIT)

#	Copyright (c) <2025> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; print " "; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d "\n" | tr -d 'ir' | tr y "\n"
#	Che cosa significa?


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

# For random number generation.
#import random
from random import randrange
from random import choice


# ===================================================================


"""
	Python method to generate a sequence/category of integers.
	The default size of the generated sequence/category is: 20.
"""
def generate_category(default_size=20):
	# Allow for the maximum integer size, which is bounded by the main/physical memory subsystem that the computer has.
	#category_1_size = randrange(sys.maxsize)
	# Pseudo-randomly generate the positive-value size of the category.
	category_i_size = 0
	while 0 == category_i_size:
		category_i_size = randrange(default_size)
	print("Size of 'category i':",category_i_size,"=")
	category_i = [ randrange(category_i_size) for i in range(category_i_size) ]
	#print("'category i' is:",category_i,"=")
	# Create a set from the list/category.
	set_list_i = set(category_i)
	# Create a list/category from the set/category.
	category_i = list(set_list_i)
	return category_i


###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	print("================================================")
	# Simulate two categories of members via pseudo-random number generation.
	# Create a list/sequence/category of members.
	category_1 = generate_category(15)
	print("'category 1' is:",category_1,"=")
	# Create another list/sequence/category of members.
	category_2 = generate_category(21)
	print("'category 2' is:",category_2,"=")
	print("................................................")
	print("Perform randomized bipartite matching.")
	# Select a member from 'category 1'.
	chosen_category_1_member = choice(category_1)
	print("Chosen 'category 1' member is:",chosen_category_1_member,"=")
	# Select a member from 'category 2'.
	chosen_category_2_member = choice(category_2)
	print("Chosen 'category 2' member is:",chosen_category_2_member,"=")










# ===================================================================