#!/opt/local/bin/python3.12

###	#!/opt/anaconda3/bin/python

###	#!/Users/zhiyang/anaconda3/bin/python3

"""
	This is written by Zhiyang Ong to demonstrate how to use
		Python sets.



	Notes:
	"|=" operator is binary, and can only be used for 2 operands in
		an expression.
		Hence, "a |= b |= c" is a forbidden expression.
		Using parentheses/brackets to explicitly set the order of
			precedence does not work.
		E.g., "b4a |= (b1 |= b6)" would result in an error at run-time.
	Likewise for the "&=" operator.
		E.g., "b1a &= b3 &= b6" would result in an error at run-time.
	Likewise for the "-=" operator.
		E.g., "b3a -= b2 -= b6" would result in an error at run-time.



	#### TO BE COMPLETED
	Methods to check if a set is empty().
		Compare the performance of such methods.
	Methods to convert a list to a set.
	Methods to convert a set to a list.


	
	References:
	+  https://python-reference.readthedocs.io/en/latest/docs/comprehensions/set_comprehension.html   
		- 2015, Jakub Przywóski. Revision 9a3b94e7.
		- Section:Subsection
			* Comprehensions and Generator Expression: {} set comprehension
		- Title: Python Reference (The Right Way) - DRAFT
		- Jakub Przyw{\'{o}}ski, "{} set comprehension," in Python Reference (The Right Way) - {DRAFT}: Comprehensions and Generator Expression, Revision 9a3b94e7, Read the Docs, Inc., Portland, OR, 2015.
			Available online from Read the Docs, Inc. as Revision 9a3b94e7 at: https://python-reference.readthedocs.io/en/latest/; February 1, 2020 was the last accessed date
"""


# ============================================================
# Import packages and modules from Python libraries.
#import pandas as pd



"""
	A Python object to test performing an addition operation
		between a Python object that is not a basic data type
		and a number.
	####TO BE COMPLETED
"""
class my_object:
	property = 678


# Method implemented with set comprehension
"""
def remove_suffix(my_str,set_of_substr):
	return 
"""

###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	print("==================================================")
	my_string = "This is an substring that I want to eliminate from my sentence."
	set_of_substrings = {"substring that I ", "to eliminate from", "non-existent"}
	"""
		Note that the order of elements in the set that selected for
			processing varies between execution of this Python script.
	"""
	for x in set_of_substrings:
		print("=	substring:",x)
		if x in my_string:
			print("substring exists in my_string.")
		else:
			print("substring is not found in my_string.")
	# From \cite{Przywoski2015a}.
	a = {s**2 for s in [1, 2, 1, 0]}
	print("a is:",a,"=")
	a = {s**2 for s in range(10)}
	print("a is:",a,"=")
	a = {s for s in [1, 2, 3] if s % 2}
	print("a is:",a,"=")
	a = {(m, n) for n in range(2) for m in range(3, 5)}
	print("a is:",a,"=")
	print("==================================================")
	"""
		[DrakeJr2023i, from The Python Standard Library: Built-in Types: Set Types — set, frozenset]
		https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
	"""
	b1 = {12, 345, 567, 879, 1234}
	print("b1 is:",b1,"=")
	b2 = {12, 567, 1234}
	print("b2 is:",b2,"=")
	b3 = {4, 12, 345, 567, 879, 1234, 173432, 38457237845}
	print("b3 is:",b3,"=")
	b4 = {3, 5, 8, 9}
	print("b4 is:",b4,"=")
	b5 = {12, 345, 567, 879, 1234}
	print("b5 is:",b5,"=")
	b6 = {12, 879, 1234, 6, 67, 291, 919919, 384653430}
	print("b6 is:",b6,"=")
	print("Are b1 and b4 disjoint sets?",b1.isdisjoint(b4),"=")
	print("Is b2 a subset of b1?",b2.issubset(b1),"=b2.issubset(b1)")
	print("Is b2 a subset of b1?",b2 <= b1,"=b2 <= b1")
	print("Is b5 a subset of b1?",b5 <= b1,"=b5 <= b1")
	print("Is b2 a proper subset of b1?",b2 < b1,"=b2 < b1")
	print("Is b5 a proper subset of b1?",b5 < b1,"=b5 < b1")
	print("Is b4 a subset of b1?",b4.issubset(b1),"=b4.issubset(b1)")
	print("Is b4 a subset of b1?",b4 <= b1,"=b4 <= b1")
	print("Is b4 a proper subset of b1?",b4 < b1,"=b4 < b1")
	print("Is b1 a superset of b2?",b1.issuperset(b2),"=b1.issubset(b2)")
	print("Is b1 a superset of b2?",b1 >= b2,"=b1 >= b2")
	print("Is b1 a superset of b5?",b1 >= b5,"=b1 >= b5")
	print("Is b1 a proper superset of b2?",b1 > b2,"=b1 > b2")
	print("Is b1 a proper superset of b5?",b1 > b5,"=b1 > b5")
	print("Union of b1 and b4:",b1.union(b4),"=b1.union(b4)")
	print("Union of b1 and b4:",b1 | b4,"=b1 | b4")
	print("Union of b1, b4, b6:",b1.union(b4,b6),"=b1.union(b4,b6)")
	print("Union of b1, b4, b6:",b1 | b4 | b6,"=b1 | b4 | b6")
	print("Intersection of b1 and b6:",b1.intersection(b6),"=b1.intersection(b6)")
	print("Intersection of b1 and b6:",b1 & b6,"=b1 & b6")
	print("Intersection of b1, b3, b6:",b1.intersection(b3,b6),"=b1.intersection(b3,b6)")
	print("Intersection of b1, b3, b6:",b1 & b3 & b6,"=b1 & b3 & b6")
	print("Difference between b1 and b6:",b1.difference(b6),"=b1.difference(b6)")
	print("Difference between b1 and b6:",b1 - b6,"=b1 - b6")
	print("Difference between b1 and b2:",b1.difference(b2),"=b1.difference(b2)")
	print("Difference between b1 and b2:",b1 - b2,"=b1 - b2")
	print("Difference between b3 and b2,b6:",b3.difference(b2,b6),"=b3.difference(b2,b6)")
	print("Difference between b3 and b2,b6:",b3 - b2 - b6,"=b3 - b2 - b6")
	print("Symmetric difference between b1 and b6:",b1.symmetric_difference(b6),"=b1.symmetric_difference(b6)")
	print("Symmetric difference between b1 and b6:",b1 ^ b6,"=b1 ^ b6")
	print("Symmetric difference between b2 and b4:",b2.symmetric_difference(b4),"=b2.symmetric_difference(b4)")
	print("Symmetric difference between b2 and b4:",b2 ^ b4,"=b2 ^ b4")
	b4a = b4.copy()
	print("b4a is:",b4a,"=")
	print("b4a == b4???:",b4a == b4,"=")
	print("b4a>=b4 and b4a<=b4???:",b4a >= b4,":and:",b4a <= b4,"=")
	b4a.update(b1,b6)
	print("Update b4a with b1 and b6:", b4a,"=b4a.update(b1,b6)")
	b4a = b4.copy()
	print("	b4a after reset is:",b4a,"=")
	#b4a = b4a |= b1 |= b6
	#b4a |= (b1 |= b6)
	b4a |= b1
	b4a |= b6
	print("b4a after assignments is:",b4a,"=")
	b1a = b1.copy()
	print("b1a is:",b1a,"=")
	b1a.intersection_update(b6)
	print("Intersection update of b1a and b6:",b1a,"=b1a.intersection_update(b6)")
	b1a = b1.copy()
	print("	b1a after reset is:",b1a,"=")
	b1a &= b6
	print("Intersection update of b1a and b6:",b1a,"=b1a &= b6")
	b1a = b1.copy()
	print("	b1a after reset is:",b1a,"=")
	b1a.intersection_update(b3,b6)
	print("Intersection update of b1a, b3, b6:",b1a,"=b1.intersection_update(b3,b6)")
	b1a = b1.copy()
	print("	b1a after reset is:",b1a,"=")
	#b1a &= b3 &= b6
	b1a &= b3
	b1a &= b6
	print("Intersection update of b1a, b3, b6:",b1a,"=b1 &= b3 &= b6")
	b1a = b1.copy()
	print("	b1a after reset is:",b1a,"=")
	b1a.difference_update(b6)
	print("Difference between b1a and b6:",b1a,"=b1a.difference_update(b6)")
	b1a = b1.copy()
	print("	b1a after reset is:",b1a,"=")
	b1a -= b6
	print("Difference between b1a and b6:",b1a,"=b1a -= b6")
	b1a = b1.copy()
	print("	b1a after reset is:",b1a,"=")
	b1a.difference_update(b2)
	print("Difference between b1a and b2:",b1a,"=b1a.difference_update(b2)")
	b1a = b1.copy()
	print("	b1a after reset is:",b1a,"=")
	b1a -= b2
	print("Difference between b1a and b2:",b1a,"=b1a -= b2")
	b3a = b3.copy()
	print("	b3a after reset is:",b3a,"=")
	b3a.difference_update(b2,b6)
	print("Difference between b3a and b2,b6:",b3a,"=b3a.difference_update(b2,b6)")
	b3a = b3.copy()
	print("	b3a after reset is:",b3a,"=")
	#b3a -= b2 -= b6
	b3a -= b2
	b3a -= b6
	print("Difference between b3a and b2,b6:",b3a,"=b3a -= b2 -= b6")
	b1a = b1.copy()
	print("	b1a after reset is:",b1a,"=")
	b1a.symmetric_difference_update(b6)
	print("Symmetric difference update between b1a and b6:",b1a,"=b1a.symmetric_difference_update(b6)")
	b1a = b1.copy()
	print("	b1a after reset is:",b1a,"=")
	b1a ^= b6
	print("Symmetric difference update between b1a and b6:",b1a,"=b1a ^= b6")
	b2a = b2.copy()
	print("	b2a is:",b2a,"=")
	b2a.symmetric_difference_update(b4)
	print("Symmetric difference update between b2a and b4:",b2a,"=b2a.symmetric_difference_update(b4)")
	b2a = b2.copy()
	print("	b2a after reset is:",b2a,"=")
	b2a ^= b4
	print("Symmetric difference update between b2a and b4:",b2a,"=b2a ^= b4")
	print("==================================================")
	c = {3, 5, 7, 10, 14, 17, 29, 30, 47}
	print("c is:",c,"=")
	c.add(32)
	print("c + {32}:",c,"=c.add(32)")
	c.remove(14)
	print("c - {14}:",c,"=c.remove(14)")
	"""
		[DrakeJr2023m, The Python Tutorial: Section 8. Errors and Exceptions: Section 8.3. Handling Exceptions]
		https://docs.python.org/3/tutorial/errors.html
	"""
	try:
		c.remove(99)
	except KeyError:
		print("c.remove(99) is invalid, since c does not contain 99.")
	c.discard(7)
	print("c.discard(7):",c,"=")
	c.discard(91)
	print("c.discard(91):",c,"=")
	c.clear()
	print("c.clear():",c,"=")









