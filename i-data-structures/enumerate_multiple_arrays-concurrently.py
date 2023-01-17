#!/Users/zhiyang/anaconda3/bin/python3

"""
	This is written by Zhiyang Ong to demonstrate how to enumerate
		multiple lists (of the same length) concurrently.
	
	References:
	+ \cite{Chaudhary2019}
		- indicates how to enumerate two lists concurrently.
		- can be extended to enumerate more lists concurrently.
		- this answer also addresses how to enumerate lists of
			different lengths concurrently.
"""

import itertools



# 3 lists of even length
data1 = range(11,20)
data2 = range(111,120)
data3 = range(211,220)
data4 = range(311,330)




# Enumerate 
for index, (value1, value2) in enumerate(zip(data1, data2)):
	print(index, "value1 is:", value1, ".")
	print(index, "value2 is:", value2, ".")
	print(index, value1 + value2)


for index, (value1, value2, value3) in enumerate(zip(data1, data2, data3)):
	print(index, "value1 is:", value1, ".")
	print(index, "value2 is:", value2, ".")
	print(index, "value3 is:", value3, ".")
	print(index, value1 + value2 + value3)

for index, (value1, value2, value3) in enumerate(zip(data1, data2, data3)):
	print("value1 is:", value1, ".")
	print("value2 is:", value2, ".")
	print("value3 is:", value3, ".")
	print(value1 + value2 + value3)



#	This is an example of concurrently enumerating multiple lists.
print("===========================================")
b = [23, 34, 45, 56, 67, 78, 89]
c = [2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9]
d = [1.3, 2.4, 3.5, 4.6, 5.7, 6.8, 7.9]
for i, (bi,ci,di) in enumerate(zip(b,c,d)):
	print("index", i, "elem 1:",bi, "elem 2:",ci, "elem 3:", di)
print("===========================================")




print("	Enumerating lists of different lengths, for the longest list.")
for i in itertools.zip_longest(data1, data2, data3, data4):
	print(i)



print("	Enumerating lists of different lengths, for the shorter/shortest list, and print results as a tuple.")
print("	Print results as a tuple.")
for i in enumerate(zip(data1, data2, data3, data4)):
	print(i)


print("	Enumerating lists of different lengths, for the shorter/shortest list.")
print("	Print results separately.")
for i, (value1, value2, value3, value4) in enumerate(zip(data1, data2, data3, data4)):
	print("	i=",i,"= and value1",value1,"= and value2",value2,"= and value3",value3,"= and value4",value4)
