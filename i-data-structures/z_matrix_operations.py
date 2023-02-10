#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to test different
		operations with matrices in Python, using NumPy matrices.



	References:
	+ [Nurjan2016]
		- Nurjan, "Answer to `How to add a row or column to a matrix in Python numpy [duplicate]'," Stack Exchange Inc., New York, NY, November 21, 2016. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/40712143/1531728 and https://stackoverflow.com/questions/40712095/how-to-add-a-row-or-column-to-a-matrix-in-python-numpy/40712143#40712143; February 9, 2023 was the last accessed date.
	+ [Berg2022a]
		- Sebastian Berg, Ralf Gommers, Charles Harris, Stephan Hoyer, Inessa Pawson, Matti Picus, St{\'{e}}fan {van der Walt}, Melissa Weber Mendon{\c{c}}a, and Eric Wieser, "NumPy Reference," NumFOCUS, Inc., Austin, TX, December 18, 2022. Available online from *NumPy: Documentation: NumPy documentation: API Reference* as Release 1.24 at: https://numpy.org/doc/stable/reference/index.html; January 19, 2023 was the last accessed date.
	+ [Bahaloo2021]
		- Hassan Bahaloo, Eric Leschinski, and Guillermo `nacho4d' Ignacio Enriquez Gutierrez, "Answer to `How do I add an extra column to a NumPy array?'," Stack Exchange Inc., New York, NY, April 23, 2021. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/56855933/1531728 and https://stackoverflow.com/questions/8486294/how-do-i-add-an-extra-column-to-a-numpy-array/56855933#56855933; February 9, 2023 was the last accessed date.
	+ [Smit2018]
		- Peter Smit, Eric O. Lebigot, and Peter Mortensen, "Answer to `How do I add an extra column to a NumPy array?'," Stack Exchange Inc., New York, NY, June 27, 2018. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/8486342/1531728 and https://stackoverflow.com/questions/8486294/how-do-i-add-an-extra-column-to-a-numpy-array/8486342#8486342; February 9, 2023 was the last accessed date.
	+ [han4wluc2016]
		- han4wluc, "Answer to `How do I add an extra column to a NumPy array?'," Stack Exchange Inc., New York, NY, June 27, 2018. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/8486342/1531728 and https://stackoverflow.com/questions/8486294/how-do-i-add-an-extra-column-to-a-numpy-array/8486342#8486342; February 9, 2023 was the last accessed date.
	+ [Lee2019c]
		- Lee, "Answer to `How do you extract a column from a multi-dimensional array?'," Stack Exchange Inc., New York, NY, October 30, 2019. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/58617959/1531728 and https://stackoverflow.com/questions/903853/how-do-you-extract-a-column-from-a-multi-dimensional-array/58617959#58617959; February 10, 2023 was the last accessed date.
	+ [technikue202022]
		- technikue20, ireshaupulie, and surajkr\_gupta, *How to access a NumPy array by column*, Sanchhaya Education Pvt. Ltd., Noida, Uttar Pradesh, India, September 13, 2022. Available online from *GeeksforGeeks: Python: Python Programming Language* at: https://www.geeksforgeeks.org/how-to-access-a-numpy-array-by-column/; February 10, 2023 was the last accessed date.
	+ [FernandezDelRio2014]
		- Jaime Fernandez del Rio, Answer to `Selecting specific rows and columns from {NumPy} array', Stack Exchange Inc., New York, NY, April 8, 2014. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/22927889/1531728 and https://stackoverflow.com/questions/22927181/selecting-specific-rows-and-columns-from-numpy-array/22927889#22927889; February 10, 2023 was the last accessed date.
	+ [Praveen2017]
		- Praveen, "Answer to `Selecting specific rows and columns from {NumPy} array'," Stack Exchange Inc., New York, NY, June 28, 2017. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/22931212/1531728 and https://stackoverflow.com/questions/22927181/selecting-specific-rows-and-columns-from-numpy-array/22931212#22931212; February 10, 2023 was the last accessed date.
	+ [Foo2020]
		- Fred Foo, Sardathrion -- against SE abuse, and cs95, "Answer to `Extracting specific columns in numpy array'," Stack Exchange Inc., New York, NY, August 23, 2020. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/8386737/1531728 and https://stackoverflow.com/questions/8386675/extracting-specific-columns-in-numpy-array/8386737#8386737; February 10, 2023 was the last accessed date.
	+ [yanhh2018]
		- yanhh, "Answer to `Extracting specific columns in numpy array'," Stack Exchange Inc., New York, NY, July 28, 2018. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/51554318/1531728 and https://stackoverflow.com/questions/8386675/extracting-specific-columns-in-numpy-array/51554318#51554318; February 10, 2023 was the last accessed date.
"""




__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'January 17, 2020'

#	The MIT License (MIT)

#	Copyright (c) <2020> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?











###############################################################
#	Import packages and modules from the Python Standard Library.
import math


###############################################################
#	Import Custom Python Packages and Modules


###############################################################
#	Import packages and modules Python libraries

import numpy as np





"""
	Task 1.

	Explore data structures for storing SPICE-like circuit
		simulation results, by using:
	+ a set of corresponding of lists, such that each index
		in a list corresponds to the same index in other lists
		in terms of the time stamp for obtaining the
		simulation result for voltage values.
		- This requires greater modification of the script to accommodate
			different sizes of tables reflected in the simulation
			results.
		- If the updates to the scripts for plotting circuit simulation
			results fail to track the correspondence between the lists,
			and correctly update, remove a subset of these lists, or
			add more lists (for circuit simulation results that have more
			quantities/attributes/properties to plot/visualize).
	+ a 2-D matrix from NumPy [Berg2022a, from Array objects: Standard array subclasses: numpy.matrix]
		that is constructed by adding rows to the initial
		1*n matrix, of one row.
		- This allows the script to be scalable and adjustable
			for different number of columns in the simulation results.
		- By checking if the matrix can be transposed, I can plot
			a row against another row.
		- Else, I can still plot a column against another column.
		- The only modification needed would be to remove or add
			lines of code using the Matplotlib library to plot
			the graphs.
			* Consequently, this reduces the amount of replicative code
				(snippets) in the code base, which can easily introduce
				errors into the software/program.
		- "A matrix is a specialized 2-D array that retains its 2-D nature through operations. It has certain special operators, such as * (matrix multiplication) and ** (matrix power)."
		- "It is no longer recommended to use this class, even for linear algebra. Instead use regular arrays. The class may be removed in the future."
			* Yikes!!! DO NOT USE THIS SOLUTION!!!
	+ DataFrame from pandas, as an alternative to array objects and matrix objects (a special type of 2-D array objects).
	Mimic simulation results by creating a 2-D array of 1 row,
		and n columns.
"""
# Simulation results for the initial timestamp.
simulation_results_timestamp_1 = [1.0, 7, 0, 3.5]
print(simulation_results_timestamp_1)
# Transform the results from a list to a matrix data type [Berg2022a].
simulation_results = np.matrix(simulation_results_timestamp_1)
print(simulation_results)
# Simulation results for the next timestamp.
simulation_results_timestamp_next = [1.2, 0, 7, 3.5]
print(simulation_results_timestamp_next)
"""
	Add the simulation results for the next timestamp as a new row
		to the matrix/table of simulation results [Nurjan2016].

	Or, try adding a row to the matrix.
"""
simulation_results = np.vstack([simulation_results, simulation_results_timestamp_next])
print(simulation_results)
# Add another row to the matrix representing circuit simulation results.
simulation_results_timestamp_next = [1.4, 0, 7, 7]
print(simulation_results_timestamp_next)
simulation_results = np.vstack([simulation_results, simulation_results_timestamp_next])
print(simulation_results)
# Add another row to the matrix representing circuit simulation results.
simulation_results_timestamp_next = [1.6, 0, 7, 7]
print(simulation_results_timestamp_next)
simulation_results = np.vstack([simulation_results, simulation_results_timestamp_next])
print(simulation_results)
# Add another row to the matrix representing circuit simulation results.
simulation_results_timestamp_next = [1.8, 7, 0, 0]
print(simulation_results_timestamp_next)
simulation_results = np.vstack([simulation_results, simulation_results_timestamp_next])
print(simulation_results)








#	Task 2: Add columns to a matrix or 2-D array.



x = np.array([[8.0,0,1], [8.2,1,0]]) 
print("Original x:") 
print(x) 
y = np.array([[3], [5]])
#y = np.array([[3, 5]])
print("Original y:") 
print(y) 
# Use the method from [Bahaloo2021].
print("x appended to y on axis of 1:") 
x1 = np.append(x, y, axis=1)
print(x1) 
# Modify the method to add a row instead of a column.
x2 = np.array([[8.4,1,0,9]])
#x2 = np.array([[8.4],[1],[0],[9]])
print(x2)
print("x2 appended to x1 on axis of 0:") 
x3 = np.append(x1, x2, axis=0)
print(x3)





# Use the method from [Smit2018]
#y = np.array([[3, 5]])
x4 = np.hstack([x,y])
print(x4)
# Are x1 and x3 equivalent? [Berg2022a, from Routines: Logic functions]
if np.array_equal(x1,x4):
	print("x1 == x4")
else:
	print("x1 and x4 are different.")




# Use the method from [han4wluc2016]
x5 = np.concatenate([x, y], axis=1)
print(x5)
# Are x1 and x5 equivalent? [Berg2022a, from Routines: Logic functions]
if np.array_equal(x1,x5):
	print("x1 == x5")
else:
	print("x1 and x5 are different.")
# Modify the method to add a row instead of a column.
x6 = np.concatenate([x1, x2], axis=0)
print(x6)
# Are x3 and x6 equivalent? [Berg2022a, from Routines: Logic functions]
if np.array_equal(x3,x6):
	print("x3 == x6")
else:
	print("x3 and x6 are different.")





# Use the method from [Berg2022a, Array objects: Indexing routines: Generating index arrays: numpy.c_]
x7 = np.c_[x, y]
print(x7)
# Are x1 and x7 equivalent? [Berg2022a, from Routines: Logic functions]
if np.array_equal(x1,x7):
	print("x1 == x7")
else:
	print("x1 and x7 are different.")

"""
	Use the method from [Berg2022a, Array objects: Indexing routines: Generating index arrays: numpy.r_]
		for adding a row.
"""
x8 = np.r_[x1, x2]
print(x8)
# Are x1 and x7 equivalent? [Berg2022a, from Routines: Logic functions]
if np.array_equal(x3,x8):
	print("x3 == x8")
else:
	print("x3 and x8 are different.")




"""
	Try method for the transpose of arrays, from 1-D to 2-D.
	[Berg2022a, Array objects: Array manipulation routines: numpy.transpose]

	It works for multi-dimensional arrays, but not 1-D arrays.
"""
x9 = np.transpose(x8)
print(x9)
x10 = np.transpose(x2)
print(x10)








# Try methods to access a column from a 2-D array.

# Try method from [Lee2019c]
col0 = [val[0] for val in x8]
print(col0)
col1 = [val[1] for val in x8]
print(col1)
col2 = [val[2] for val in x8]
print(col2)
col3 = [val[3] for val in x8]
print(col3)


# Try method from [Kasri2018]
col0_Kasri2018 = x8[:,0]
print(col0_Kasri2018)
# Are col0 and col0_Kasri2018 equivalent? [Berg2022a, from Routines: Logic functions]
if np.array_equal(col0,col0_Kasri2018):
	print("col0 == col0_Kasri2018")
else:
	print("col0 and col0_Kasri2018 are different.")
# ...
col1_Kasri2018 = x8[:,1]
#print(col1_Kasri2018)
# Are col1 and col1_Kasri2018 equivalent? [Berg2022a, from Routines: Logic functions]
if np.array_equal(col1,col1_Kasri2018):
	print("col1 == col1_Kasri2018")
else:
	print("col1 and col1_Kasri2018 are different.")
# ...
col2_Kasri2018 = x8[:,2]
# Are col2 and col2_Kasri2018 equivalent? [Berg2022a, from Routines: Logic functions]
if np.array_equal(col2,col2_Kasri2018):
	print("col2 == col2_Kasri2018")
else:
	print("col2 and col2_Kasri2018 are different.")
# ...
col3_Kasri2018 = x8[:,3]
# Are col3 and col3_Kasri2018 equivalent? [Berg2022a, from Routines: Logic functions]
if np.array_equal(col3,col3_Kasri2018):
	print("col3 == col3_Kasri2018")
else:
	print("col3 and col3_Kasri2018 are different.")

"""
	Additional method use:
	+ anonymous/lambda functions: https://stackoverflow.com/a/46868265/1531728
	+ zip function: https://stackoverflow.com/a/13518274/1531728
	+ map-reduce style Python:
		- https://stackoverflow.com/a/904532/1531728
		- https://stackoverflow.com/a/18594945/1531728
		- https://stackoverflow.com/a/18545262/1531728

	https://stackoverflow.com/questions/903853/how-do-you-extract-a-column-from-a-multi-dimensional-array
"""


# Try method from [technikue202022]



col2_technikue202022 = x8[...,2]
# Are col2 and col2_technikue202022 equivalent? [Berg2022a, from Routines: Logic functions]
if np.array_equal(col2,col2_technikue202022):
	print("col2 == col2_technikue202022")
else:
	print("col2 and col2_technikue202022 are different.")
# Try this method for rows.
row2_technikue202022 = np.array([x8[2,...]])
print(row2_technikue202022)
print(x2)
# Are x2 and row2_technikue202022 equivalent? [Berg2022a, from Routines: Logic functions]
if np.array_equal(x2,row2_technikue202022):
	print("x2 == row2_technikue202022")
else:
	print("x2 and row2_technikue202022 are different.")



# Try the methods from [FernandezDelRio2014]
a = np.arange(20).reshape((5,4))
print(a)
a_subset_1 = a[[[0, 0], [1, 1], [3, 3]], [[0,2], [0,2], [0, 2]]]
print(a_subset_1)
# Broadcasting method [FernandezDelRio2014]
a_subset_2 = a[[[0], [1], [3]], [0, 2]]
print(a_subset_2)
# array-based approach, rather than list based approach.
row_idx = np.array([0, 1, 3])
col_idx = np.array([0, 2])
a_subset_3 = a[row_idx[:, None], col_idx]
print(a_subset_3)

# Are a_subset_1 and a_subset_2 equivalent? [Berg2022a, from Routines: Logic functions]
if np.array_equal(a_subset_1,a_subset_2):
	print("a_subset_1 == a_subset_2")
else:
	print("a_subset_1 and a_subset_2 are different.")
# Are a_subset_1 and a_subset_3 equivalent? [Berg2022a, from Routines: Logic functions]
if np.array_equal(a_subset_1,a_subset_3):
	print("a_subset_1 == a_subset_3")
else:
	print("a_subset_1 and a_subset_3 are different.")
if np.array_equal(a_subset_2,a_subset_3):
	print("a_subset_2 == a_subset_3")
else:
	print("a_subset_2 and a_subset_3 are different.")


# Try the methods from [Praveen2017].

# Filter 2-D array "a" to get required/desired rows.
a_subset_4 = a[[0,1,3], :]
# Filter 2-D array "a" to get required/desired rows, and select the columns you want as well.
a_subset_5 = a[[0,1,3], :][:, [0,2]]
if np.array_equal(a_subset_1,a_subset_4):
	print("a_subset_1 == a_subset_4")
else:
	"""
		Expected since a_subset_4 did not select the columns to pick
			the appropriate subset of the 2-D matrix.
	"""
	print("a_subset_1 and a_subset_4 are different. Expected.")
if np.array_equal(a_subset_1,a_subset_5):
	print("a_subset_1 == a_subset_5")
else:
	print("a_subset_1 and a_subset_5 are different.")
"""
	References:
	+ [Praveen2017]
	+ [Berg2022a, Array objects: Indexing routines: Generating index arrays: numpy.ix_]
"""
a_subset_6 = a[np.ix_([0,1,3], [0,2])]
print(a_subset_6)
if np.array_equal(a_subset_1,a_subset_6):
	print("a_subset_1 == a_subset_6")
else:
	print("a_subset_1 and a_subset_6 are different.")
# Align the arrays to use the broadcasting method.
a_subset_7 = np.ix_([0,1,3], [0,2])
print(a_subset_7)
if np.array_equal(a_subset_1,a_subset_7):
	print("a_subset_1 == a_subset_7")
else:
	print("a_subset_1 and a_subset_7 are different. Does not work as expected.")


# Try the methods from [Foo2020].

# Select columns 1 and 3 together.
a_subset_8 = a[:, [1, 3]]
print(a_subset_8)
# Select columns 1 and 3 separately.
a_subset_col_1, a_subset_col_3 = a[:, 1], a[:, 3]
print(a_subset_col_1)
print(a_subset_col_3)

# Try the methods from [yanhh2018].

# Select columns 2, 1, and 3 (in this order, not the typical order) together.
a_subset_9 = a[:, [2, 1, 3]]
print(a_subset_9)



