#!/usr/local/bin/python3

###	#!/Users/zhiyang/anaconda3/bin/python3



"""
	This is written by Zhiyang Ong to generate/synthesize Haikus.


	Synopsis:
	Functions to generate/synthesize Haikus.


	References from my BibTeX database.
	+ 




	Revision History:
	July 3, 2023			Version 0.1	Script.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'July 3, 2023'

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

# [DrakeJr2023a, from Numeric and Mathematical Modules: random — Generate pseudo-random numbers]
from random import randrange
from random import choice


# ===================================================================

# Global Variables


# List of terms based on their number of syllables.
one_syllable_terms = ["wise", "smart", "strong", "cool", "great"]
two_syllable_terms = ["doctor", "dentist", "teacher", "mentor", "parent", "fancy", "rockstar", "superb", "leader", "artist", "surgeon", "athlete", "world-class", "surgeon", "lawyer", "awesome"]
three_syllable_terms = ["über-cool", "engineer", "role model", "CAMACer", "outstanding", "fantastic", "designer", "artistic", "venturesome", "globetrotting", "musician", "researcher", "feminist", "resilient", "tenacious", "amazing", "scholar", "fabulous", "physician"]
four_syllable_terms = ["developer", "multilingual", "neurosurgeon", "anti-racist", "compassionate", "data scientist"]
five_syllable_terms = ["IC designer", "rockstar engineer", "multilingual pro"]
six_syllable_terms = ["EECS rockstar", "cultural chameleon", "rockstar developer", "computer architect", "machine learning scientist", "resident assistant", "medical resident"]
seven_syllable_terms = ["cardiothoracic surgeon", "future ACM fellow"]
# Dictionary to map number of syllables (to be generated) to the specific list of terms for that number.
map_number_of_syllables_to_lists = {1:one_syllable_terms, 2:two_syllable_terms, 3:three_syllable_terms, 4:four_syllable_terms, 5:five_syllable_terms, 6:six_syllable_terms, 7:seven_syllable_terms}


# Number of syllables used by existing terms.
number_of_syllables_used_by_existing_terms = 0
# Current generated line in the Haiku.
current_generated_line_in_the_Haiku = ""
# Line enumeration of Haiku: 3rd/last line, 2nd line, 1st line.
line_enumeration_of_Haiku = [17, 12, 5]



# ===================================================================

def get_term():
	print()


def 




def haiku_generator_fsm():
	# Are there more lines to enumerate?
	while not line_enumeration_of_Haiku:
		# Yes. Are there more terms to be generated for current line in Haiku?
		if (number_of_syllables_used_by_existing_terms != line_enumeration_of_Haiku):
			






