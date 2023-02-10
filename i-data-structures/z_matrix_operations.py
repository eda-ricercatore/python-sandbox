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





# Use the method from [Berg2022a, Array objects: Indexing routines, or Generating index arrays: numpy.c_]
x7 = np.c_[x, y]
print(x7)
# Are x1 and x7 equivalent? [Berg2022a, from Routines: Logic functions]
if np.array_equal(x1,x7):
	print("x1 == x7")
else:
	print("x1 and x7 are different.")

"""
	Use the method from [Berg2022a, Array objects: Indexing routines, or Generating index arrays: numpy.r_]
		for adding a row.
"""
x8 = np.r_[x1, x2]
print(x8)
# Are x1 and x7 equivalent? [Berg2022a, from Routines: Logic functions]
if np.array_equal(x3,x8):
	print("x3 == x8")
else:
	print("x3 and x8 are different.")