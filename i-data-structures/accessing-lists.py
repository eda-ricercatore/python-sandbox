#!/usr/local/bin/python3

###	#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
###	#!/Users/zhiyang/anaconda3/bin/python3
###	#!/Users/zhiyang/anaconda3/bin/python




"""
	This is written by Zhiyang Ong to experiment with indexing lists,
		or accessing elements in lists, using negative indices/indexes.
	
	This script can be executed as follows:
		./accessing-lists.py




	References:
	+ [DrakeJr2023m, The Python Tutorial: 3. An Informal Introduction to Python: 3.1. Using Python as a Calculator: 3.1.2. Text and 3.1.3. Lists]


	Revision History:
	June 9, 2024				Version 0.1	Script.
"""





__author__ = 'Zhiyang Ong'
__version__ = '0.2'
__date__ = 'June 9, 2024'

#	The MIT License (MIT)

#	Copyright (c) <2024> <Zhiyang Ong>

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




###############################################################


list_of_names_1 = ["Marcello Coppola", "Miltos D. Grammatikakis", "Riccardo Locatelli", "Giuseppe Maruccia", "Lorenzo Pieralisi"]
print("list_of_names_1 is:",list_of_names_1,"=")
print("list_of_names_1[-1] is:",list_of_names_1[-1],"=")
print("list_of_names_1[-2] is:",list_of_names_1[-2],"=")
print("list_of_names_1[-3] is:",list_of_names_1[-3],"=")
print("...............................................")
print("list_of_names_1[len('Giuseppe Maruccia'):] is:",list_of_names_1[len("Giuseppe Maruccia"):],"=")
print("list_of_names_1[:len('Giuseppe Maruccia')] is:",list_of_names_1[:len("Giuseppe Maruccia")],"=")
print("list_of_names_1[len(list_of_names_1):] is:",list_of_names_1[len(list_of_names_1):],"=")
print("list_of_names_1[len(list_of_names_1):] is:",list_of_names_1[len(list_of_names_1):],"=")
print("...............................................")
print("list_of_names_1[len('Riccardo Locatelli'):] is:",list_of_names_1[len("Riccardo Locatelli"):],"=")
print("list_of_names_1[:len('Riccardo Locatelli')] is:",list_of_names_1[:len("Riccardo Locatelli")],"=")
print("...............................................")


list_of_names_2 = ["Jeff Sharpe", "Colleen Carlton", "Cristina Favretto", "Susan Parker", "Gary Strong", "Jamie Hoang", "Alyson Wieczorek", "Scott Miller", "Jutta Weimhoff", "Tom Hudgens", "Robin Chandler", "Ann Jensen", "Jae Mauthe", "Paul Nguyen", "Marcus Lucero", "Ian White", "Kris Brix", "Norma Layton", "James Hixon", "Kelly Critch", "Matt Smith", "Anne R. Kenney", "Oya Yildirim Rieger", "Callie Lamkin"]
print("list_of_names_2 is:",list_of_names_2,"=")
print("list_of_names_2[-1] is:",list_of_names_2[-1],"=")
print("list_of_names_2[-2] is:",list_of_names_2[-2],"=")
print("list_of_names_2[-3] is:",list_of_names_2[-3],"=")










