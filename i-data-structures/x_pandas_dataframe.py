#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to test the use of
		using pandas.DataFrame to read input data from a "general
		delimited file."



	References:
	+ [Pankaj2022a]
		- Pankaj and Andrea Anderson, "How To Remove Spaces from a String In Python," DigitalOcean, LLC, New York, NY, December 12, 2022. Available online from *DigitalOcean: Community: Resources: Tutorials* at: https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string; February 13, 2023 was the last accessed date.
	+ [DrakeJr2016b]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Standard Library," Python Software Foundation, Beaverton, OR, March 23, 2016. Available online from *Welcome to Python.org: Python 3.5.1 documentation* at: https://docs.python.org/3/library/; April 1, 2016 was the last accessed date.
	+ [Naveen2021]
		- Naveen, "Pandas Drop Rows From DataFrame Examples," SparkByExamples.com, Irvine, CA, September 2, 2021. Available online from *Spark By Examples: Python Pandas Tutorial* at: https://sparkbyexamples.com/pandas/pandas-drop-rows-from-dataframe/; February 13, 2023 was the last accessed date.
	+ [ActiveStateSoftwareIncStaff2022]
		- ActiveState Software Inc. staff, "How To Delete A Column/Row From A DataFrame," ActiveState Software Inc., Vancouver, British Columbia, Canada, July 11, 2022. Available online from *ActiveState: Resources: Resource Library: Quick Reads* at: https://www.activestate.com/resources/quick-reads/how-to-delete-a-column-row-from-a-dataframe/; February 13, 2023 was the last accessed date.
	+ [Haire2023a]
		- Emma Carballal Haire, Irv Lustig, JHM Darbyshire, Joris Van den Bossche, Marc Garcia, Marco Edward Gorelli, MarcoGorelli, Matthew Roeschke, MeeseeksMachine, Natalia Mokeeva, Pandas Development Team, Patrick Hoefler, Richard Shadrach, Tsvika Shapira, William Ayd, aneesh98, jakirkham, jbrockmendel, and silviaovo, "API reference," NumFOCUS, Inc., Austin, TX, January 19, 2023. Available online from *PyData: pandas: Documentation: pandas documentation: API reference* as Version 1.5.3 at: https://pandas.pydata.org/docs/reference/index.html; February 10, 2023 was the last accessed date.
	+ [Kaur2022]
		- Simran Kaur, "Pandas Read\_Table()," Linux Hint LLC, Sunnyvale, CA, June, 2022. Available online from *Linux Hint: Python* at: https://linuxhint.com/pandas-read-table/; February 13, 2023 was the last accessed date.
	+ [Hunter2016a] John Hunter, Michael Droettboom, and Thomas A. Caswell (editors),
		"Pyplot tutorial," in Matplotlib, NumFOCUS, Inc., Austin, TX, September 20, 2016.
		Available online from *Matplotlib: docs: Overview, Release 1.5.3:
			User's Guide: Beginner's Guide* at: http://matplotlib.org/users/pyplot_tutorial.html;
			November 18, 2016 was the last accessed date.
	+ [Hunter2016]
		- John Hunter, Darren Dale, Eric Firing, Michael Droettboom, the Matplotlib development team, "Beginner's Guide: Matplotlib 1.5.3 documentation," NumFOCUS, Inc., Austin, TX, December 19, 2016. Available online from *Matplotlib: docs: Overview: User's Guide* at: https://matplotlib.org/users/beginner.html; December 11, 2018 was the last accessed date.
	+ [Berg2023]
		- Sebastian Berg, Ralf Gommers, Charles Harris, Stephan Hoyer, Inessa Pawson, Matti Picus, St{\'{e}}fan {van der Walt}, Melissa Weber Mendon{\c{c}}a, and Eric Wieser, "NumPy," NumFOCUS, Inc., Austin, TX, 2023. Available online at: https://numpy.org/; January 19, 2023 was the last accessed date.
	+ [NumPyDevelopers2018]
		- NumPy Developers, "NumPy," NumFOCUS, Inc., Austin, TX, 2018. Available online at: http://www.numpy.org/index.html; December 3, 2018 was the last accessed date.
	+ [Augspurger2018]
		- Tom Augspurger, Chris Bartak, Phillip Cloud, Andy Hayden, Stephan Hoyer, Wes McKinney, Jeff Reback, Chang She, Masaaki Horikoshi, and Joris Van den Bossche, "pandas: Python Data Analysis Library," NumFOCUS, Inc., Austin, TX, August, 2018. Available online from *PyData* at: http://pandas.pydata.org/; December 3, 2018 was the last accessed date.
	+ [Hunter2023] John Hunter, Michael Droettboom, and Thomas A. Caswell (editors),
		"Controlling style of text and labels using a dictionary," in Matplotlib,
		NumFOCUS, Inc., Austin, TX, September 20, 2016.
		Available online from *Matplotlib - Visualization with Python: Examples:
		Text, labels and annotations* at: https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html#sphx-glr-gallery-text-labels-and-annotations-text-fontdict-py;
		January 17, 2023 was the last accessed date.
	+ [Hunter2023a] John Hunter, Michael Droettboom, and Thomas A. Caswell (editors),
		"Pyplot Mathtext," in Matplotlib, NumFOCUS, Inc., Austin, TX, September 20, 2016.
		Available online from *Matplotlib - Visualization with Python: Examples: pyplot* at:
		https://matplotlib.org/stable/gallery/pyplots/pyplot_mathtext.html#sphx-glr-gallery-pyplots-pyplot-mathtext-py;
		January 17, 2023 was the last accessed date.
	+ [Peitek2019a]
		- Norman Peitek, "05-save-as-file.py," GitHub, Inc., San Francisco, CA, July 26, 2019. Available online from *GitHub: Future Studio: matplotlib tutorials* at: https://github.com/futurestudio/matplotlib-tutorials/blob/master/05-save-as-file.py; January 18, 2023 was the last accessed date.
	+ [Peitek2019]
		- Norman Peitek, "Matplotlib -- Save Plots as File," Future Studio, Fellner, P{\"{o}}hls, Peitek GbR, Magdeburg, Saxony-Anhalt, Germany, August 5, 2019. Available online from *Future Studio: Future Studio Tutorials* at: https://futurestud.io/tutorials/matplotlib-save-plots-as-file; January 15, 2020 was the last accessed date.
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

# Import NumPy [NumPyDevelopers2018] [Berg2023]
import numpy as np
# Import pandas [Augspurger2018]
import pandas as pd
# Import Matplotlib [Hunter2016a].
import matplotlib.pyplot as plt
# Import string package from the Python Standard Library.
import string



"""
	Read circuit simulation data from input file.

	Use string.whitespace [Pankaj2022] [DrakeJr2016b, from Text Processing Services: string - Common string operations]
		as a delimiter.
"""
#df = pd.read_table("./input-files/invert1.cir.prn", delimiter=" ")
#df = pd.read_table("./input-files/invert1.cir.prn", delimiter=string.whitespace)
#df = pd.read_table("./input-files/invert1-clean.cir.prn", delimiter=string.whitespace)
#df = pd.read_table("./input-files/invert1.cir.csv", delimiter=string.whitespace)
df = pd.read_table("./input-files/invert1.cir.csv", delimiter=",")
print(df)
"""
	Transform/map the pandas DataFrame to NumPy n-dimensional array,
		which is a 2-D in this case.
"""
df_to_np = df.to_numpy()
print(df_to_np)


#print("Removing the last row from the DataFrame!!!")
"""
	Remove the last row from the DataFrame [Naveen2021], since it does not include
		any circuit simulation result.
	To remove the "nth" row, use "n" instead of -1 [ActiveStateSoftwareIncStaff2022] [Haire2023a, from API reference: DataFrame].
	Note that the first row is "row 0", since the row index starts with "0".
"""
#df = df.drop(df.index[-1])
"""
	Transform/map the pandas DataFrame to NumPy n-dimensional array,
		which is a 2-D in this case.
"""
#df_to_np = df.to_numpy()
#print(df_to_np)


"""
	I cannot print the 2nd column of the NumPy 2-D array, since it is
		actually a 1-D array of lists and each list contains all the columns.
"""
#print(df_to_np[:,1])
"""
	Experiment confirms that the DataFrame is a n*1 2-D array.
"""
#print("=	Print the time, Vout, and Vin columns.")
#print(df.iloc[:,0:2])



"""
	Solution fails, since it reads the NumPy 2-D array into a n*1 DataFrame.

	This is because each time instance of the circuit simulation results is
		a string embedded in a list.
	Process this be turning the string into a list of numbers.
	...
	Use the user guide [Keiter2022, Table 7-4, pp.81, \S7.3.8] and
		reference guide [Keiter2022a] to`generate CSV files, instead
		of ".prn" files, which is difficult to process [Keiter2022a].

"""
# Create the pandas DataFrame
#df_to_np_to_df = pd.DataFrame(df_to_np, columns = ["index", "time", "Vout", "Vin", "v1"])
#print(df_to_np_to_df)

# Values of time t to be plotted.
#time = []
# Values of output voltage, Vout, to be plotted.
#Vout = []
# Values of input voltage, Vin, to be plotted.
#Vin = []
#time  = [time_instance[1] for time_instance in df_to_np]
#print("=	Print the time axis.")
#print(time)



"""
	Plot the circuit simulation results [Hunter2016].

	When we plot the input and output signals, Vin and Vout, of the
		inverter, they will overlap and make it hard to read the
		graphs/plots/functions separately.

	Consequently, we choose to use subplots to stack the graphs/plots/functions
		vertically, so that they would be easier to analyze/study/examine
		[TheMatplotlibDevelopmentTeam2023a, API Reference: matplotlib.pyplot: matplotlib.pyplot.subplots: Date tick labels].
"""
#plt.plot(df["\{V(IN)+1.0\}"], df["\{V(VOUT)+1.0\}"], label="sine wave")
#plt.plot(df["{V(IN)+1.0}"], df["{V(VOUT)+1.0}"], label="inverter $V_{out}$, $V_{in}$")
#plt.plot(df["TIME"], df["{V(IN)+1.0}"], df["TIME"], df["{V(VOUT)+1.0}"], label="inverter $V_{out}$, $V_{in}$")
#fig, axs = plt.subplots(2,1)
fig, axs = plt.subplots(2,1, figsize=(10,10))
axs[0].plot(df["TIME"], df["{V(IN)+1.0}"], label="inverter $V_{in}$")
axs[1].plot(df["TIME"], df["{V(VOUT)+1.0}"], label="inverter $V_{out}$")
#plt.plot(df["V(IN)+1.0"], df["V(VOUT)+1.0"], label="sine wave")
#plt.plot(df["TIME"], df["V\(IN\)+1.0"], label="sine wave")


#plt.plot(df_to_np[:,1], df_to_np[:,2], label="sine wave")
# Add the title to the plot [Hunter2023].
#axs[0].title('Plot of $V_{in}$ against time $t$')
axs[0].set_title('Plot of $V_{in}$ (V) against time $t$ (s)')
#axs[1].title('Plot of $V_{out}$ against time $t$')
axs[1].set_title('Plot of $V_{out}$ (V) against time $t$ (s)')
#fig.title('Plot of $V_{in}$ and $V_{out}$ against time $t$')
# Add mathematical text to the plot [Hunter2023] [Hunter2023a].
#axs[0].text(300, 0.65, r'$V_{out}$ = $\neg$ $V_{in}$')
#axs[1].text(300, 0.65, r'$V_{out}$ = $\neg$ $V_{in}$')
fig.text(300, 0.65, r'$V_{out}$ = $\neg$ $V_{in}$')
# Label the y-axis.
axs[0].set_ylabel('$V_{in}$ (V)')
axs[1].set_ylabel('$V_{out}$ (V)')
# Label the x-axis.
axs[0].set_xlabel('time $t$ (s)')
axs[1].set_xlabel('time $t$ (s)')
# Add a legend to the plot [Hunter2023b].
axs[0].legend(title='Function plotted:')
axs[1].legend(title='Function plotted:')
"""
  Save plot in PDF format [Peitek2019] [Peitek2019a].
	This "save to PDF" command has to appear before the .show() command;
		else, the PDF file would be empty.
"""
plt.savefig("output-files/"+"cmos-inverter-vout-vin"+".pdf")
# Show the plot via GUI representation and the file plot.
plt.show()