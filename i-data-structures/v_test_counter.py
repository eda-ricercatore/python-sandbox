#!/usr/local/bin/python3


"""
	This is copied by Zhiyang Ong from [Kenny2017] to demonstrate how
		to use Counters for determining if a set is a subset of another
		set.



	References:
	+ [DrakeJr2023a]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Standard Library," Python Software Foundation, Beaverton, OR, February 26, 2023. Available online from *Welcome to Python.org: Docs: Python 3.11.2 documentation: Library Reference* at: https://docs.python.org/3/library/; February 26, 2023 was the last accessed date.
	+ [Kenny2017]
		- Eamonn Kenny, Answer to "How can I verify if one list is a subset of another?", Stack Exchange Inc., New York, NY, November 14, 2017. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/47282975/1531728; March 2, 2023 was the last accessed date.
	+ [Guerrero2022]
		- Igor "igorgue" Guerrero, SilentGhost, smci, and Mateen Ulhaq, "Should I use 'has_key()' or 'in' on Python dicts? [duplicate]", Stack Exchange Inc., New York, NY, April 10, 2022. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/q/1323410/1531728 and https://stackoverflow.com/questions/1323410/should-i-use-has-key-or-in-on-python-dicts; March 2, 2023 was the last accessed date.
	+ [Nguyen2019]
		- Anh Nguyen (or Anh Nguyen Viet), Trooper Z, and Prateek "Morse" Mahendrakar, "How to replace has_key in python3?", Stack Exchange Inc., New York, NY, January 24, 2019. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/q/54337239/1531728 and https://stackoverflow.com/questions/54337239/how-to-replace-has-key-in-python3; March 2, 2023 was the last accessed date.
	+ [Reddy2018]
		- Sai Kumar Reddy, aircraft, iBug, and smci, "Why dict.has_key() does not work in Python? [duplicate]", Stack Exchange Inc., New York, NY, November 29, 2018. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/q/48071232/1531728 and https://stackoverflow.com/questions/48071232/why-dict-has-key-does-not-work-in-python; March 2, 2023 was the last accessed date.
	+ [Karefylakis2013]
		- James "jamylak" Karefylakis, Answer to "How can I verify if one list is a subset of another?", Stack Exchange Inc., New York, NY, May 16, 2013. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/16579133/1531728 and https://stackoverflow.com/questions/16579085/how-can-i-verify-if-one-list-is-a-subset-of-another/16579133#16579133; March 26, 2023 was the last accessed date.











"""

###############################################################
#	Import modules from The Python Standard Library.








###############################################################

a = [1, 3, 3, 3, 5]
b = [1, 3, 3, 4, 5]
print("a is:",a,"=")
print("b is:",b,"=")
print("set(b) > set(a):",set(b) > set(a),"=")
print("set(a) > set(b):",set(a) > set(b),"=")

###############################################################


from collections import Counter

def containedInFirst(a, b):
	a_count = Counter(a)
	b_count = Counter(b)
	"""
		Counter no longer has a has_key() method [DrakeJr2023a].

		Use the "in" operator (or contains(seq, obj) function)
			instead [Kenny2017] [Guerrero2022] [Nguyen2019] [Reddy2018].


		[DrakeJr2023a, from Functional Programming Modules: operator — Standard operators as functions]
		https://docs.python.org/3/library/operator.html#operator.contains


		[DrakeJr2023a, from Functional Programming Modules: operator — Standard operators as functions: Mapping Operators to Functions]
		https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
	"""
	for key in b_count:
		if (key in a_count) == False:
			return False
		if b_count[key] > a_count[key]:
			return False
	return True


a = [1, 3, 3, 3, 5]
b = [1, 3, 3, 4, 5]
print("a is:",a,"=")
print("b is:",b,"=")
print("b in a: ", containedInFirst(a, b),"=")
print("a in b: ", containedInFirst(b, a),"=")

a = [1, 3, 3, 3, 4, 4, 5]
b = [1, 3, 3, 4, 5]
print("a is:",a,"=")
print("b is:",b,"=")
print("b in a: ", containedInFirst(a, b),"=")
print("a in b: ", containedInFirst(b, a),"=")


# [Karefylakis2013]