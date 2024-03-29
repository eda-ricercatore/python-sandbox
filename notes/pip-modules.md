#	List of *PIP*-based *Python* modules



## Installing and Uninstalling


To install a *PIP*-based *Python* module, try the following:

	pip install [python-module]



To uninstall a *PIP*-based *Python* module, try the following:



	pip uninstall [python-module]







##	For Boilerplate Code

List of *PIP*-based *Python* modules to add to, or install in, my Google Colab
	environment (for boilerplate code):
+ pip install [numpy](https://pypi.org/project/numpy/)
+ pip install matplotlib





##	For Stochastic Computing



List of *PIP*-based *Python* modules to add to, or install in, my Google Colab
environment (for stochastic computing):
+ pip install pycorrelate







##	Verifying *PIP*-based Installations *Python* libraries

To check if *PIP*-based installations of *Python* libraries work,
	check if the versions of the *PIP*-based installations match
	what we specified during installation.





References
+ Vikram S, Answer to "Import Error: No module named numpy", from
	Stack Exchange Inc.: Stack Overflow: Questions, Stack Exchange Inc.,
	New York, NY, September 27, 2017.
	Available online from Stack Exchange Inc.: Stack Overflow: Questions at:
		https://stackoverflow.com/a/46440464/1531728 and https://stackoverflow.com/questions/7818811/import-error-no-module-named-numpy/46440464#46440464;
		February 5, 2020 was the last accessed date.
+ lchojnacki, Answer to "no module named numpy even after installing it",
	from Stack Exchange Inc.: Stack Overflow: Questions, Stack Exchange Inc.,
	New York, NY, May 12, 2019.
	Available online from Stack Exchange Inc.: Stack Overflow: Questions at:
		https://stackoverflow.com/a/56103656/1531728 and https://stackoverflow.com/questions/56100791/no-module-named-numpy-even-after-installing-it/56103656#56103656
		February 5, 2020 was the last accessed date.





https://stackoverflow.com/questions/13237522/no-module-named-numpy








#	Problems with Common *Python* Libraries



##	Using Common *Python* Libraries on *Google Colab*

###	Via the *PIP* Platform

Use *PIP* commands to install common *Python* libraries in my *Google Colab*
	environment.





####	For Consistency, Use These Common *Python* Libraries in My Projects


For consistency, try to use these common *Python* libraries in my
	*Python*-based projects.
+ Endeavor (i.e., try to) use the same *Python* libraries, with the same versions,
	 in my *Python*-based projects.
	- Else, this may cause discrepancies to occur between my command-line
		-based *Python* software and my *Python*-based *Jupyter* notebook
		on *Google Colab*.
		* This can make tricky more complicated, since I have to mentally
			juggle the differences between the two libraries/versions.
+ With the *Anaconda* platform, it may contain *conda*-based installations of
	common *Python* libraries.
	- Hence, this may prevent users/people from using *PIP* to install such
		common *Python* libraries.
		* However, [there are ways to force an installation to occur](https://github.com/eda-ricercatore/admin-notes/blob/main/computer-languages/pip-modules.md#force-installation-of-modules-via-pip). 






#####	Force installation of modules via PIP

Command to force installation of modules via PIP [KGo2017].

	pip install --upgrade --force-reinstall <package>


From [Butnaru2017]:

	pip3 install numpy





References:
+ [orome2013] orome, "Can I force pip to reinstall the current version?", from *Stack Exchange Inc.: Stack Overflow: Questions*, Stack Exchange, Inc., New York, NY, October 23, 2013.
	Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/questions/19548957/can-i-force-pip-to-reinstall-the-current-version;
		February 5, 2020 was the last accessed date.
	- [KGo2017] KGo and Arturo MP, Answer to "Can I force pip to reinstall the current version?", from *Stack Exchange Inc.: Stack Overflow: Questions*, Stack Exchange, Inc., New York, NY, August 14, 2017.
		Available online from Stack Exchange Inc.: Stack Overflow: Questions at:
			https://stackoverflow.com/a/19549035/1531728 and 	https://stackoverflow.com/questions/19548957/can-i-force-pip-to-reinstall-the-current-version/19549035#19549035
			February 5, 2020 was the last accessed date.
+ [Butnaru2017] Andrei Madalin Butnaru and Daniel Patru, Answer to "Import Error: No module named numpy", from *Stack Exchange Inc.: Stack Overflow: Questions*, Stack Exchange, Inc., New York, NY, December 14, 2017.
	Available online from Stack Exchange Inc.: Stack Overflow: Questions at:
		https://stackoverflow.com/a/35476722/1531728 and https://stackoverflow.com/questions/7818811/import-error-no-module-named-numpy/35476722#35476722
		February 5, 2020 was the last accessed date.






###	Via *Anaconda* Platform

Since *Google Colab* may not support the *Anaconda* platform for data science
	and scientific computing, use the *PIP* package manager to install *Python*
	packages.
+ To use the *Anaconda* platform on *Google Colab*, try:
	- https://anaconda.org/conda-forge/google-auth (may not be relevant)
	- https://rjai.me/posts/google-colab-conda/ (works for Python 2.7, not
		Python 3.X)
	- Resources that mentioned *Google Colab*:
		* \cite{McKay2019}
		* \cite{Au2019}
		* \cite{Li2018}
		* \cite{FacebookEngineers2020}


##	Module in *Python* Library Not Found

If the following error occur during execution of my *Python* scripts/programs,

	ModuleNotFoundError: No module named 'numpy'

it indicates that it cannot recognize the path for the *Python* library that the
	specified *Python* module (in this case, "*numpy*") belongs to.

Hence, I should uninstall the current version of that *Python* library, and reinstall
	it.
+ [If the *Python* library cannot be installed via *PIP* or *conda*, use these
	specified options with *PIP* to force installation of this *Python* library
	to occur](https://github.com/eda-ricercatore/admin-notes/blob/main/computer-languages/pip-modules.md#force-installation-of-modules-via-pip).
	- If the *conda*-installed version of the *Python* library is older than the
		available version via *PIP*, doing this will uninstall the
		*conda*-installed version and install the currently available version
		via *PIP*.
+ Doing this via *PIP* may not work, since the associated version of *Python*
	that is used belongs to *Python* 2.7.x (or later) rather than *Python* 3.8.x
	(or later).
	- Hence, [use *pip3* instead, as shown above](https://github.com/eda-ricercatore/admin-notes/blob/main/computer-languages/pip-modules.md#force-installation-of-modules-via-pip).
























#	Author Information

The MIT License (MIT)

Copyright (c) <2017> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.
