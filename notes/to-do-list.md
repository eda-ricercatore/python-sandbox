>	# ⚠️ To-Do List

>	List of concepts and features to try.
>
>	Similarly, we should avoid naming packages and modules based on
>		commands in UNIX-like operating systems.
>		This caused problems with C++ classes and packages/modules.
>

>	## ⚠️ Reminders!!!

>	Remember to place the UNIX/Linux shebang, so that I can run it as an
>		executable script from the command line (via the "Terminal" application).
>
>	Fix the URLs in this script, especially for the Table of Contents.









#	Notes About *Python*

##	Table of Contents

+ [Differences between *Python 3.x* and *Python 2.y*](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#differences-between-python-3x-and-python-2y)
+ [Design Decisions](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#design-decisions)
+ [Syntax Rules Regarding Identifiers](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#syntax-rules-regarding-identifiers)
+ [Importing *Python* Classes, Modules, and Packages](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#importing-python-classes-modules-and-packages)
+ [*Python* Classes](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#python-classes)
	- [Object management](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#object-management)
	- [*Python* Functions](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#python-functions)
		* [Functional Programming with *Python*](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#functional-programming-with-python)
+ [*Python*-based Software Development](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#python-based-software-development)
	- [*Python*ic Coding Style](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#pythonic-coding-style)
	- [*Python* Documentation](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#python-documentation)
	- [Input/Output Operations](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#inputoutput-operations)
	- [Modules in *The Python Standard Library*](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#modules-in-the-python-standard-library)
		* [Built-in Collections](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#built-in-collections)
	- [Software Testing, Verification, and Validation](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#software-testing-verification-and-validation)
		* [Software Tuning and Performance Optimization](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#software-tuning-and-performance-optimization)
		* [Software Debugging](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#software-debugging)
	- [Industrial-Strength High-Performance Computing](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#industrial-strength-high-performance-computing)
	- [Developing Mixed-Language Software](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#developing-mixed-language-software)
	- [Packaging *Python* Programs](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#packaging-python-programs)
		* [References for Packaging *Python* Programs](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#references-for-packaging-python-programs)
	- [Database Administration](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#database-administration)
	- [Software Development Process Methodologies](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#software-development-process-methodologies)
		* [Integrated Development Environments (IDEs)](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#integrated-development-environments-ides)
+ [*Python* Strings](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#python-strings)
+ [Exception Handling](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#exception-handling)
	- [Warnings](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#warnings)
	- [Ancillary Note](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#ancillary-note)
+ [*Python* Virtual Machine (PVM)](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#python-virtual-machine-pvm)
+ [Concurrent and Parallel Programming with *Python*](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#concurrent-and-parallel-programming-with-python)
	- [System Resource Management](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#system-resource-management)
+ [*Python*-based Data Science](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#python-based-data-science)
	- [Probability Theory, Statistical Analysis, Random Processes, Stochastic Modeling, and Noise](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#probability-theory-statistical-analysis-random-processes-stochastic-modeling-and-noise)
	- [Machine Learning](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#machine-learning)
	- [Data Visualization](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#data-visualization-and-information-visualization)
	- [Additional Information and Resources](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#additional-information-and-resources)
+ [Miscellaneous](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#miscellaneous)
	- [Regular Expressions](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#regular-expressions)
	- [Generic Programming](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#generic-programming)
	
+ [References](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#references)
	- [Object-Oriented *Python* Programming](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#object-oriented-python-programming)
	- [Domain Applications of *Python* Programming](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#domain-applications-of-python-programming)
	- [Mixed-Language Software Development](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#mixed-language-software-development)
	- [Additional Python Resources](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#additional-python-resources)
	- [Books Covered](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#books-covered)
+ [Random](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#random)
+ [Author Information](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#author-information)








##	Differences between *Python 3.x* and *Python 2.y*

The `print` statement in *Python 2.y* has been replaced by the
	`print()` function in *Python 3.x*.
	A pair of parentheses, or round brackets, are used in the `print()`
	function to print the string within the parentheses.
	The `print` statement needs to be appended by a string, and these
	tokens (the `print` statement and the string) are whitespace
	delimited \cite{vanRossum2017}.

Comparing *Python* 3.x to *Python* 2.y, the former has significant
		differences in printing information (to standard output)
		\cite{vanRossum2017}.
	This can cause compatibility problems between different versions
		of *Python* in a given *Python* software.

Definitions of classes between *Python 3.x* and *Python 2.y* are different
	\cite[Chapter 4, pp. 103]{Alchin2010}.

Unlike *Python 3.x*, properties in *Python 2.y* do not have mutator methods
	\cite[Chapter 4, pp. 129]{Alchin2010}.

When a function descriptor on a class is accessed, the function descriptor
	returns itself and shows up as any function in *Python 3.x*;
	however, in *Python 2.y*, this returns an instance method object
	\cite[Chapter 4, pp. 129]{Alchin2010}.  

*Python 3.x* and *Python 2.y* represent boolean values differently, **True** and
	**False** as opposed to **0** and **1** \cite[Chapter 4, pp. 143]{Alchin2010}.

Unlike *Python 2.y*, the **round()** method in *Python 3.x* would return a number
	of the same type \cite[Chapter 5, pp. 154]{Alchin2010}.

Backward compatibility support for *Python 2.y* in *Python 3.x*:
+ implement the **\_\_next\_\_()** method to call the **next()** method
	\cite[Chapter 5, pp. 156]{Alchin2010}.


References for *Python 3.0*:
+ \cite[Appendix, pp. 621-638]{Beazley2009}
+ \cite{Hall2009b}
+ \cite[Appendix C, pp. 1451--1463]{Lutz2013}
+ \cite[Appendix A, pp. 295--326]{Pilgrim2009}


















##	Design Decisions

Use either keyword arguments or positional arguments in my
	implementation of *Python* methods to process input parameters
	\cite[Chapter 3, pp. 53]{Alchin2010};
	don't use both (keyword and positional arguments) of these types.






##	Syntax Rules Regarding Identifiers

*Python* identifiers for variables, functions, classes, and modules
	have to be alphanumeric and can include underscores
	\cite[from \S *Python* Basic Syntax]{Mohtashim2017}
	\cite[\S2.3 Identifiers and keywords]{DrakeJr2016f}
	\cite[\S2.3 Identifiers and keywords]{DrakeJr2016a}.
	Otherwise, the *Python* interpreter would report a syntax error,
	since the syntax is invalid.
	These identifiers are case sensitive and cannot be *Python*
	keywords [ParewaLabsPvtLtdStaff20XY, \S "*Python* Keywords and Identifier"].

They should not include dashes. Else, an interpreting/compiling error
	would result.





##	Importing *Python* Classes, Modules, and Packages

Tasks that I can do:
+ Create and define a class, and use static methods in the class
	(within the same script).
+ Use static methods of a class, from another *Python* script.
+ Create, define, and use my own *Python* modules, from any *Python*
	script.
+ Create, define, and use my own *Python* packages, from any *Python*
	script.
	- Determine the importance and usefulness packages, with respect to
		modules.
	- Resources and references:
		* \cite{PythonPackagingAuthorityMembers2020b}






Tasks that I want to do, but can't yet (or have yet to try):
+ BLAH






Notes about *Python* modules:
+ "A module is a file containing *Python* definitions and statements."
	\cite[\S6 Modules]{Brandl2017a} \cite[\S6 Modules]{Brandl2017}
	\cite[Importing Modules: Module? What's a Module?]{Thurlow2012}
	\cite[Chapter 11, pp. 241]{Hall2009b}.
	**This is different from how I define modules in *C++* and *Java*.**
+ The filename of the file containing the code for a *Python* module should be
	the same as the name of the aforementioned *Python* module
	\cite[Chapter 10, pp. 209]{Hetland2005}.














Pages in \cite{Ziade2008} that deal with
	importing *Python* classes and modules (Not helpful):
+ Naming, (pp. 91--116)
	- Application of naming to (pp. 92):
		* Variables: constants and public/private variables
		* Functions and methods
		* Properties
		* Classes
		* Modules
		* Packages
+ Packages, (pp. 117--165)
+ Documentation, (pp. 223--250)



With regards to importing *Python* modules, circular dependencies is
	forbidden/discouraged during interpretation of *Python* programs
	\cite[Chapter 11, pp. 241]{Hall2009b}.
+ That is, don't import a *Python* module *A*, which imports another
	*Python* module *B* that imports *Python* module *A*.
+ Or rather, **if *Python* module *A* imports *Python* module *B*, *Python*
	module *B* should not import *Python* module *A* **.
+ - This "import-only-once behavior" avoids cyclical imports that result in
		"endless loops of imports" \cite[Chapter 10, pp. 204]{Hetland2005}

A *Python* package is a collection of *Python* modules \cite[Chapter 11, pp. 241]{Hall2009b},
	and is effectively a subdirectory of *Python* modules that includes a file
	named **\_\_init\_\_.py** \cite[Chapter 11, pp. 252]{Hall2009b}
	\cite[Chapter 10, pp. 210]{Hetland2005};
	the file **\_\_init\_\_.py** can be an empty file \cite[Chapter 11, pp. 252]{Hall2009b}.
	That is, a *Python* package is a "hierarchical directory structure" of
		*Python* files \cite[Chapter 11, pp. 252]{Hall2009b}.

To import all the modules from a package *A*, try: *import A*.

To import a module *B* from a package *A*, try: *import A.B*.  

To import a class *C* from module *B* that belongs to package *A*, try:
	*from A.B import C*.

Use the error *ImportError* to catch errors associated with importing modules
	that have been moved or renamed.
	Provide fallback imports, so that in the *try-except* block, or *try-catch* block, we can provide
		another statement to import the module from its old/new location
		(or with its old/new name);
	if the *try* block uses the old location/name, the *catch* block shall use
		the new location/name, and vice versa;
	if the module is not critical to the function of the software, it is recommended
		to assign the module to *None* (i.e., *[module name] = None*)
	\cite[Chapter 2, pp. 45-46]{Alchin2010}.

Use the internal method **\_\_import\_\_** to conditionally import modules
	\cite[Chapter 11, pp. 245]{Hall2009b}.

A module can be imported under another name
	\cite[Chapter 11, pp. 245]{Hall2009b}.

Import statements should be placed at the top of each *Python* file
	\cite[Chapter 11, pp. 246]{Hall2009b}.

Importing *Python* submodules \cite[Chapter 11, pp. 253-254]{Hall2009b}:
+ Explicitly with an empty **\_\_init\_\_.py** file
	\cite[Chapter 11, pp. 253]{Hall2009b}.
	- **from pirate import \*** does not allow all submodules of **pirate** to be
		imported.
+ Implicitly
	-  Using **\_all\_** as the list variable, which is comparable to using an
		import statement with the wildcard **\***.
		* Enables the use of import statements such as
			**from [*pirate import*] \***
	- Execute import statements in the **\_\_init\_\_.py** file.
		* To reload any module imported in the **\_\_init\_\_.py** file, explicitly
			reload those modules.
		* The **\_\_init\_\_.py** file can contain *Python* code just like any
			*Python* script.








The **import** statements of a *Python* source file can execute code in a library
	module, within its own namespace
	\cite[Chapter 7, section on "Execution as the Main Program," pp. 146]{Beazley2009}.
+ Use case with test code:
	- Test code can be placed in modules and imported by users.
	- The test code is wrapped with an **if-else** statement, such that the test
		code would only execute when running as the main program
		\cite[Chapter 7, section on "Execution as the Main Program," pp. 146-147]{Beazley2009}.
















A **weakly internal** variable is a variable with a leading underscore,
	**_[variable name]**, that is explicitly imported
	\cite[Chapter 11, pp. 246]{Hall2009b}.



While literate programming
	\cite{Knuth1984,Knuth1992a,McConnell2004,Subramaniam2006,Schach2007,Oram2007,MullerHannemann2010}
	is recommended, self-documenting code would suffice
	\cite[Chapter 11, pp. 246-247]{Hall2009b}.

If the functionality of an imported module is changed/modified and updated, use
	the *imp* module from *The Python Standard Library*
	\cite{DrakeJr2016e,DrakeJr2016b} to clear "*Python*'s internal cache of
	[certain] imported modules" \cite[Chapter 11, pp. 249-250]{Hall2009b} and
	reload the cache with the update modules;
	this is useful when modules have to be created again or recompiled during
		program execution \cite[Chapter 11, pp. 249-250]{Hall2009b}.


When a *Python* script imports a module, it \cite[Chapter 11, pp. 250]{Hall2009b}:
+ Locates the *Python* script/file containing the module.
	- **PYTHONPATH** is a set of relative or absolute paths of *Python* modules,
		and *The Python Standard Library*, which helps the *Python*
		interpreter/compiler and the operating system locate *Python* modules
		\cite[Chapter 11, pp. 251]{Hall2009b}.
	- Alternatively, use the path configuration file (with the ***.pth*** file extension)
		to add directories of custom *Python* modules to **sys.path**
		\cite[Chapter 10, pp. 209]{Hetland2005}.
+ Loads the *Python* module into memory, and creates an internal representation
	for the *Python* module
	- *Python* processes/"compiles" the *Python* modules into *Python* byte
		code, which are saved in *.pyc* files (the "c" in ".pyc" refers to
		compiled), for faster execution \cite[Chapter 11, pp. 251]{Hall2009b}
		\cite[Chapter 10, pp. 204]{Hetland2005}.
+ Executes the aforementioned internal representation, after loading this *Python*
	module for the first time \cite[Chapter 10, pp. 204]{Hetland2005}.
	- Subsequently loadings of the module do not redfine the variables, functions,
		and classes in the module;
		hence, loading of a[/any] module is not performed multiple times, and
			the module is not executed \cite[Chapter 10, pp. 204]{Hetland2005}.
	- This "import-only-once behavior" avoids cyclical imports that result in
		"endless loops of imports" \cite[Chapter 10, pp. 204]{Hetland2005};
		see circular dependencies in \cite[Chapter 11, pp. 241]{Hall2009b}.
	- To reload a *Python* module that has been modified during execution of
		a *Python* program, try \cite[Chapter 10, pp. 205]{Hetland2005}:
		*[module-name]* = **reload(** *[module-name]* **)**













In the transition period from upgrading old locations/names to new
	locations/names, use the special module **\_\_module\_\_** to make the
	import of non-critical modules conditional \cite[Chapter 2, pp. 46-47]{Alchin2010}.

Explicit module imports, by specifying the module (and package) names are
	preferred over implicit imports of all (or a subset of) modules within a
	package \cite[Chapter 2, pp. 47-48]{Alchin2010}.

Relative imports are supported by providing relative paths to modules that are
	being imported \cite[Chapter 2, pp. 48-49]{Alchin2010}.

*Python* modules allow *Python* software to be modularized, which improves
		support for code reuse \cite[Chapter 11, pp. 241]{Hall2009b}.







## *Python* Classes


Notes on *Python* Classes:
+ Concepts in object-oriented programming for
	\cite[Chapter 7, pp. 139]{Hetland2005}  
	- ***polymorphism***
	- ***encapsulation***
	- methods, or functions of the class
		\cite[Chapter 7, section on "The class Statement," pp. 117]{Beazley2009}.
		* They are also known as instance methods
		\cite[Chapter 7, section on "The class Statement," pp. 118]{Beazley2009}.
	- attributes, or properties
		\cite[Chapter 7, section on "The class Statement," pp. 117]{Beazley2009}.
	- superclasses
	- ***inheritance***
	- constructors
+ A class is a particular type of object has a logical group of functions, and
	"encapsulates the behavior of an object" \cite[Chapter 4, pp. 103]{Alchin2010}.
	- A *Python* class definition is a template for custom data types that contain
		data (i.e., attributes, or object-specific variables
		\cite[Chapter 7, pp. 144]{Hetland2005}) and commands (i.e., methods,
		or functions belonging to this *Python* class)
		\cite[Chapter 9, pp. 181]{Hall2009b}.
	- A class variable is a variable that is part of a class
		\cite[Chapter 7, section on "The class Statement," pp. 117]{Beazley2009}.
	- A static variable is common to all instances of the class that it belongs to
		\cite[\S8.6.4, pp. 390]{Langtangen2009}
		\cite[\S7.6, pp. 387-388]{Langtangen2012}.
		* Access a static variable via **class-name.static-variable-name**,
			rather than **instance-object-name.static-variable-name**,
			since an assignment to **instance-object-name.static-variable-name**
			creates a new **instance-object-name** instance attribute
			**static-variable-name**;
			this new instance attribute **static-variable-name** covers/hides
				the static variable **class-name.static-variable-name**
			\cite[\S8.6.4, pp. 390]{Langtangen2009}.
	- The dot (**.**) operator between the name of an instance object and an
		attribute/function binds the attribute/function to that instance object
		\cite[Chapter 7, section on "Class Instances," pp. 118]{Beazley2009}.
	A class defines a namespace, but it does not create a unique scope for
		names inside each of its method;
		hence, for each method, references to attributes and other methods in
			the class must be qualified through **self**
		\cite[Chapter 7, section on "Scoping Rules," pp. 118]{Beazley2009}.
+ "An instance of the class represents the data for the object"
	\cite[Chapter 4, pp. 103]{Alchin2010} \cite[Chapter 9, pp. 183]{Hall2009b}.
	- A class definition "is a factory for creating instances" of the class
		\cite[Chapter 7, section on "Object Memory Management," pp. 128]{Beazley2009}.
	- Encapsulation enables the treatment of an object as a black box
		\cite[Chapter 9, pp. 183]{Hall2009b} to hide its internal state (or details)
		"from the outside world" \cite[Chapter 7, pp. 139,157]{Hetland2005}.
		* This is similar to polymorphism, because encapsulation and
			polymorphism are concepts/principles of abstraction;
			however, polymorphism can exist without encapsulation
			\cite[Chapter 7, pp. 143]{Hetland2005}.
		* Encapsulation enables the usage of objects without knowing the
			details of how these objects are constructed
			\cite[Chapter 7, pp. 143]{Hetland2005}.
	- **self** refers to the instance object that the instance methods are
		operating with \cite[Chapter 9, pp. 183]{Hall2009b}
		\cite[Chapters 7, pp. 148]{Hetland2005};
		**self** in *Python* is analogous to **this** in *C++*/*Java*
			\cite[Chapter 7, section on "Scoping Rules," pp. 119]{Beazley2009}.
		the required, explicit usage of **self** enables the differentiation of
			instance attributes/variables from local variables
			\cite[Chapter 7, section on "Scoping Rules," pp. 119]{Beazley2009}.
	- **dir(*[instance object]*)** shows a list of attributes and methods
		supported by the ***[instance object]*** within its namespace
		\cite[Chapter 9, pp. 184]{Hall2009b}.
	- Each instance object is associated with an unique identity (number), which
		can be obtained with **id(*[instance object]*)**.
		This identity (number) is an integer (or, positive integer)
			\cite[Chapter 9, pp. 184]{Hall2009b}.
	- The namespace of an object can be implemented by a dictionary object,
		and has the organization of a family tree or directory structure
		\cite[Chapter 9, pp. 185]{Hall2009b}.
	- Name binding is used to map/connect a name to an object
		\cite[Chapter 9, pp. 184]{Hall2009b}.
	- The state of an instance object is determined by the values of its
		attributes/properties/fields/characteristics
		\cite[Chapter 9, pp. 185]{Hall2009b}
		\cite[Chapter 7, pp. 145]{Hetland2005}.
	- Note that in \cite[Chapter 7, pp. 145; Chapter 9, pp. ???]{Hetland2005},
		properties are distinguished from attributes.
	- An attribute is private to objects of a class
		\cite[Chapter 7, pp. 145]{Hetland2005}.
+ Difference instances of a class has different sets of data, but have the same
	behavior that is determined by the class definition;
	this behavior can be defined, extended, or altered
	\cite[Chapter 4, pp. 103]{Alchin2010}.
+ Inheritance allows a derived/child class to have a different fundamental
	behavior from its base/parent class \cite[Chapter 4, pp. 103]{Alchin2010}
	\cite[Chapter 9, pp. 181]{Hall2009b}
	\cite[Chapter 7, section on "Inheritance," pp. 119]{Beazley2009}.
	- Inheritance allows specialized classes of objects to be created from
		general classes of objects \cite[Chapter 7, pp. 139]{Hetland2005},
		by addition or modification of attributes and methods
		\cite[Chapter 7, section on "Inheritance," pp. 119]{Beazley2009}.
	- When a derived/child class defines the **\_\_init\_\_()** method, it has to
		call the the **\_\_init\_\_()** methods of the base classes (if desired);
		this is because the **\_\_init\_\_()** methods of the base classes are
			not automatically invoked when the **\_\_init\_\_()** method is
			redefined by a derived/child class;
		if a base/parent class has not defined the **\_\_init\_\_()** method,
			just call the **\_\_init\_\_()** method without any arguments
		\cite[Chapter 7, section on "Inheritance," pp. 120]{Beazley2009}.
	- Duck typing enables developers to modify and manipulate objects, which
		are related via class inheritance, while ensuring type safety
		\cite{WikipediaContributors2018a}.
	- Polymorphism allows operators to be overloaded with *special methods*
		\cite{DrakeJr2016a} (which are known as "magic methods" in
		\cite{Hall2009b}) \cite[Chapter 9, pp. 184]{Hall2009b}.
	- Polymorphism enables type/class -dependent functions to be performed
		on an object \cite[Chapter 7, pp. 140]{Hetland2005}.
		* That is, polymorphism not only allows objects of child classes
			(subclasses, or derived classes) to inherit functions from parent
			classes (superclasses, or base classes) but also customizes them
			for the child classes \cite[Chapter 7, pp. 140]{Hetland2005}.
		* This type of *Pythonic* programming exploits "duck typing"
			\cite[Chapter 7, pp. 143]{Hetland2005}.
		* Polymorphism enables the usage of an object' methods without
			detailed information about what it is (i.e., its type/class)
			\cite[Chapter 7, pp. 143]{Hetland2005}.   
		* An object of a child class is also an instance of the parent class;
			hence, using the **isinstance()** method for type/class checking
			is an inadequate solution \cite[Chapter 7, pp. 140]{Hetland2005}.
			+ **isinstance()** method for checks if an object is of the
				specified class or a subclass of the specified class
				\cite{Saha20XY}
				- It supports class inheritance
					\cite{abbot2018,Dewes2018,Dewes2018a,Nyffenegger2018,ParewaLabsStaff20XYb,Saha20XY}
					\cite[From Built-In Functions: Object Oriented Functions: isinstance]{Przywoski2015}.
			+ **type()** does not support class inheritance
				\cite{abbot2018,Dewes2018,Dewes2018a,Nyffenegger2018,ParewaLabsStaff20XYb,Saha20XY}
				\cite[From Built-In Functions: Object Oriented Functions: isinstance]{Przywoski2015}.
			+ Developers should use duck typing over checking if an object
				belongs to a particular type/class \cite{Saha20XY}.
		* Polymorphism applies to \cite[Chapter 7, pp. 142]{Hetland2005}:
			+ methods
			+ built-in operators
			+ built-in functions
		* The advantages/benefits of polymorphism are mitigated/negated with
			type checking functions \cite[Chapter 7, pp. 143]{Hetland2005}:
			+ **type()**
			+ **isinstance(obj, cls)**
				- Or, **\_\_instancecheck\_\_(cls, obj)**
					\cite[Chapter 3, subsection on "Type Checking," Table 3.15, pp. 57]{Beazley2009}.
			+ **issubclass(subcls, cls)**
				- Or, **\_\_subclasscheck\_\_(cls, subcls)**
					\cite[Chapter 3, subsection on "Type Checking," Table 3.15, pp. 57]{Beazley2009}.
		* Instead of type checking (or checking the class), ask if the object is
			behaving according to what I want
			\cite[Chapter 7, pp. 143]{Hetland2005}.
	- Dynamic binding (or polymorphism in the context of inheritance) enables
		an instance object to use a method without concern for the types
		required for its method parameters/arguments;
		this is because of **duck typing**
		\cite[Chapter 7, section on "Polymorphism Dynamic Binding and Duck Typing," pp. 122]{Beazley2009}
+ The built-in type **object** is "a foundation type that underpins the entire
	system \cite[Chapter 4, pp. 103]{Alchin2010}.
+ Codify relationships between packages, modules, and classes to represent
	actual/real relationships between (concrete or abstract) nouns
	\cite[Chapter 4, pp. 105]{Alchin2010}.
+ *Python* supports multiple inheritance \cite[Chapters 7, pp. 155]{Hetland2005}
	\cite[Chapter 7, section on "Inheritance," pp. 120]{Beazley2009},
	and enables each class to be build as another component of the software
	\cite[Chapter 4, pp. 105]{Alchin2010}.
	- "Inheritance is specified with a comma-separated list of base-class names
		in the class statement."
		\cite[Chapter 7, section on "Inheritance," pp. 119,121]{Beazley2009}.
	- E.g., **class Grandchild-name(Parent-1-name, Parent-2-name, relative-3-name, relative-4-name, relative-5-name):**
		\cite[Chapter 7, section on "Inheritance," pp. 119,121]{Beazley2009}.
	- A child class can have multiple parent classes
		\cite[Chapters 7, pp. 155]{Hetland2005}.
	- The order of superclasses in the class statement determines which class
		methods will override the methods of the other class(es);
		methods of the earlier classes will override the methods of the later
			classes \cite[Chapters 7, pp. 155]{Hetland2005}.
	- Multiple inheritance enables mixins, or support classes, to provide minor
		add-on features that can be used by a variety of classes.
		\cite[Chapter 4, pp. 105]{Alchin2010}
		\cite[Chapter 7, section on "Inheritance," pp. 122]{Beazley2009}.
		* **Compare mixins with traits.**
		* "[A mixin does] not provide full functionality on [its] own."
		* The minor add-on features are "mixed in" with the other classes
			\cite[Chapter 7, section on "Inheritance," pp. 122]{Beazley2009}.
	- If possible, avoid multiple inheritance
		\cite[Chapter 7, section on "Inheritance," pp. 122]{Beazley2009}.
+ Method resolution order (MRO) determines "the order in which *Python*
	resolves which method to use" in software that uses "multi-level or multiple
	inheritance" \cite[Chapter 4, pp. 106]{Alchin2010}
	\cite[Chapters 7, pp. 155]{Hetland2005}.
	- Since *Python* does not know the class hierarchy, it has "to account for all
		the possibilities" \cite[Chapter 4, pp. 108]{Alchin2010} in which it
		determines which method to use.
	- It traverses the list of all base class, in the order from "most specialized"
		class to "least specialized" class
		\cite[Chapter 7, section on "Inheritance," pp. 121]{Beazley2009};
		here, specialization refers to the "depth" of the class in the inheritance
			graph/tree/diagram, such that a grandchild is more specialized
			than a grandparent  
		\cite[Chapter 7, section on "Inheritance," pp. 121,122]{Beazley2009}.
+ **\_\_init\_\_()** is a class, when it shoud be considered as an instance object
	(**self**), which inherits from **type** \cite[Chapter 4, pp. 122]{Alchin2010}
	\cite[Chapter 7, pp. 102-103]{Pilgrim2009}.
+ The (software) plugin framework allows software plugins and plugin systems
	to be additively added to it \cite[Chapter 4, pp. 122]{Alchin2010}.
	- The plugin framework allows easy access to plugins and plugin systems
		in use \cite[Chapter 4, pp. 122]{Alchin2010}.
	- A plugin extends a base class by using Python's extension features, such
		as the built-in subclass syntax and the support "for common plugin
		needs", so that it can complement the functionality of the base class
		\cite[Chapter 4, pp. 123]{Alchin2010}.
	- An example of support "for common plugin needs" would be input
		validation \cite[Chapter 4, pp. 123]{Alchin2010}:
	- The plugin, or plugin system, should be well documented, in terms of its
		expectations and assumptions \cite[Chapter 4, pp. 123]{Alchin2010}.
	- The plugin can be extended by more specialized plugins as subclasses
		(also known as derived classes and child classes)
		\cite[Chapter 4, pp. 124]{Alchin2010}.
	- Provide an iterator to enumerate plugins mounted to the plugin
		framework's plugin mount point \cite[Chapter 4, pp. 124]{Alchin2010}.
	- The metaclass for the plugin framework should register/connect plugins
		to the plugin mount class by adding the plugin objects to the plugin list
		(list of plugins) for subsequent access
		\cite[Chapter 4, pp. 124]{Alchin2010}.
	- The plugin mount class needs to have a switch to enable or disable the
		plugin mount (or plugin framework)
		\cite[Chapter 4, pp. 124]{Alchin2010}.
	- An individual/standard plugin inherits from the metaclass, and obtains its
		plugin behavior automatically \cite[Chapter 4, pp. 125]{Alchin2010}.
	- Use the metaclass **\_\_prepare\_\_()** to prepare a class declaration for
		immediate processing \cite[Chapter 4, pp. 125]{Alchin2010}.
	- An instantiated object stores data via an instance-specific namespace
		dictionary that can be accessed by the attributes if the instantiated
		object;
		access these attributes with "a trio of functions"
		\cite[Chapter 4, pp. 125]{Alchin2010}.
+ Define a property using the built-in @property decorator function, so that it
	can allow attributes to be assessed by methods
	\cite[Chapter 4, pp. 127]{Alchin2010}.
+ A descriptor of an assigned class allows an object definition to behave just
	like the properties of the assigned class \cite[Chapter 4, pp. 129]{Alchin2010}
	\cite[Chapter 7, section on "Descriptors," pp. 126]{Beazley2009}.
	- Since a descriptor cannot use the namespace dictionary of the instance
		object, the descriptor has to use a dictionary to access instance objects
		\cite[Chapter 4, pp. 131]{Alchin2010}.
	- Only instantiate a descriptor at the class level, and not "on a per-instance
		basis" via the method **\_\_init\_\_()** (or other methods)
		\cite[Chapter 7, section on "Descriptors," pp. 127]{Beazley2009}.
+ A method is a function belonging to a class \cite[Chapter 4, pp. 131]{Alchin2010}.
	- That is, a method is a function that is bound to object attributes (or,
		attributes of an object/class) \cite[Chapter 7, pp. 141]{Hetland2005}
		\cite[Chapter 7, pp. 144]{Hetland2005}.
	- Unlike functions that do not belong to a class, a method can access class
		information \cite[Chapter 4, pp. 131]{Alchin2010}.
	- Categories of methods \cite[Chapter 4, pp. 131]{Alchin2010}:
		* unbound methods
		* bound methods
	- A function also serves as a descriptor of a class
		\cite[Chapter 4, pp. 131]{Alchin2010}.
	- Like descriptors, a class and its instances can access a method
		\cite[Chapter 4, pp. 131]{Alchin2010}.
	- An unbound method is a method that is accessed by a class, which is
		received by the descriptor \cite[Chapter 4, pp. 131]{Alchin2010}
		\cite[Chapters 7, pp. 150]{Hetland2005}.
		* It is unbound to any **self** parameter
			\cite[Chapters 7, pp. 150]{Hetland2005}.
	- A bound method requires an instance of a class to for access
		\cite[Chapter 4, pp. 131]{Alchin2010}
		\cite[Chapters 7, pp. 149]{Hetland2005}.
	- When an unbound method on a class is accessed, a function object for
		the unbound method is returned \cite[Chapter 4, pp. 131]{Alchin2010}.
	- A function can support bound and unbound methods;
		a bound method uses the instance object, which is
			passed as a positional argument, of the class to receive the first
			argument;
		hence, the positional argument does not need to be **self**
		\cite[Chapter 4, pp. 132]{Alchin2010}.
	- To implement method binding with an unbound method, explicitly use an
		 instance objects in the first argument to mimic/imitate bound methods;
		 this can be helpful "when passing functions around as callbacks"
		\cite[Chapter 4, pp. 133]{Alchin2010}.
	- To use a method without instantiating a class, use either of the following
		\cite[Chapter 4, pp. 133-135]{Alchin2010}:
		* Class methods
		* Static methods
	- A class method is a method that needs access to the attached class, and
		the built-in *@classmethod* decorator supports it
		\cite[Chapter 4, pp. 133-135]{Alchin2010}.
	- A class method treats the class as an object, and operates on the object
		\cite[Chapter 7, section on "Static Methods and Class Methods," pp. 123]{Beazley2009}.
	- An "unbound" class method is a bound instance method that accepts an
		instance object as the first positional argument
		\cite[Chapter 4, pp. 133]{Alchin2010}.
	- A method can be defined on a metaclass, since a class is an instance of a
		metaclass \cite[Chapter 4, pp. 134]{Alchin2010}.;
		hence, each instance of a class can access that method, just like any
			bound method of that class \cite[Chapter 4, pp. 134]{Alchin2010};
		however, a class instance can call unclass methods, but not bound
			class methods \cite[Chapter 4, pp. 134]{Alchin2010};
		a bound class method can only be called by the class itself.
			\cite[Chapter 4, pp. 134]{Alchin2010}.
	- While a metaclass-based class method has less visibility by instances of
		a class than standard decorated class methods, it allows
		metaclass-using applications to add class methods to classes that use
		the metaclass \cite[Chapter 4, pp. 134]{Alchin2010};
		this avoids the need for a separate/extra class just to contain the
		aforementioned class methods (and nothing else)
		\cite[Chapter 4, pp. 134]{Alchin2010}.
	- A static method enables a method to interact with properties of the class,
		and other static methods of the class, without requiring an instance
		object of the class to perform various operations and functions
		\cite[Chapter 4, pp. 134]{Alchin2010};
		this also avoids the need to implement a function at the module level,
			without being embedded in any *Python* class
			\cite[Chapter 4, pp. 134]{Alchin2010};
		a static method shall be defined within a *Python* class with the
			**@staticmethod** decorator \cite[Chapter 4, pp. 134]{Alchin2010}
			\cite[Chapter 1, section on "Objects and Classes," pp. 22]{Beazley2009}
			just before the static method definition
			\cite[Chapter 7, section on "Static Methods and Class Methods," pp. 123]{Beazley2009}.
		* A static method exists within the namespace defined by a class, but
			"it does not operate on any kind of instance";
			call a static method using the following format: **class-name.static-method(*[arguments]*)**
			\cite[Chapter 7, section on "Static Methods and Class Methods," pp. 123]{Beazley2009}.
	- Class and static methods can be invoked by an instance object;
		e.g., **instance-object.static-method()** or **instance-class-method()**
		\cite[Chapter 7, section on "Static Methods and Class Methods," pp. 124]{Beazley2009}.
	- The definition of static and class methods specifies using a property
		function to handle these methods differently
		\cite[Chapter 7, section on "Properties," pp. 125]{Beazley2009}.
+ There exists various ways to instantiate/create, modify, or invalidate *Python*
	instance objects \cite[Chapter 4, pp. 135]{Alchin2010}.
	- Creating *Python* instance objects via instantiation of a *Python* class
		 \cite[Chapter 4, pp. 136]{Alchin2010}:
		* Use **\_\_new\_\_()** to instantiate/create an object of a *Python*
		 	class \cite[Chapter 4, pp. 137]{Alchin2010}.
		 	\cite[Chapter 7, section on "Object Memory Management," pp. 129]{Beazley2009}
		* Use **\_\_init\_\_()** to initialize an object of a *Python* class to
			implement behavior (i.e., perform functions and operations) that is
		 	specific/unique to that *Python* instance object;
		 	that is, use the constructor **\_\_init\_\_()** to initialize instance
				variables of the class as a basic setup of the instance object
				and to perform common tasks for each instance object of the
				class (such as file input operations, validation of
				initial/preliminary user input, or to collect information
				regarding a given running process)
			\cite[Chapter 4, pp. 136]{Alchin2010}
			\cite[Chapter 7, section on "Object Memory Management," pp. 129]{Beazley2009}.
		* Default values for instance variables of the class serve as placeholders
			until they will be updated \cite[Chapter 4, pp. 136]{Alchin2010}.
		* For a given *Python* instance object, the **\_\_new\_\_()** method
			should be called before the **\_\_init\_\_()** method
			\cite[Chapter 4, pp. 137]{Alchin2010}.
		* The method **\_\_new\_\_()** does not automatically call the method
			**\_\_init\_\_()**
			\cite[Chapter 7, section on "Object Memory Management," pp. 129]{Beazley2009}.
		* A class can define the method **\_\_new\_\_()** to do either of the
			following \cite[Chapter 7, section on "Object Memory Management," pp. 129]{Beazley2009}:
			+ Modify values of instance objects inherited from a base class with
				immutable variables.
			+ To define metaclasses.
	- Accessing and modifying attributes of a *Python* class
		\cite[Chapter 4, pp. 138]{Alchin2010} \cite[Chapter 9, pp. 197]{Hall2009b}:
		* The name of an attribute of an instance object can be accessed or
			modified directly via *instance.attribute* \cite[Chapter 4, pp. 138]{Alchin2010};
			other methods for accessing or modifying *instance.attribute* can
				provide more control \cite[Chapter 4, pp. 138]{Alchin2010}.
		* The special attribute **\_\_bases\_\_** is a tuple of base classes, and
			it connects classes to their base classes
			\cite[Chapter 7, section on "Object Representation and Attribute Binding," pp. 131]{Beazley2009}
		* Use the **\_\_getattr\_\_()** function to obtain the value of an attribute
			(of the instance object) \cite[Chapter 4, pp. 138]{Alchin2010};
			e.g., use the **getattr(instance, attribute_name)** to obtain the
				name of the attribute \cite[Chapter 4, pp. 138]{Alchin2010}.
		* Also, use the **\_\_getattr\_\_()** function to control implicitly (or
			rather, not explicitly) managed attributes
			\cite[Chapter 4, pp. 138]{Alchin2010}.
		* For requests to access undefined attributes, and if the
			**\_\_getattr\_\_()** function is defined, call the **\_\_getattr\_\_()**
			function \cite[Chapter 4, pp. 138]{Alchin2010}.
		* For defined attributes that exists with an instance object of the class,
			use the **\_\_getattribute\_\_()** function, which takes the same
			set of input arguments as the **\_\_getattr\_\_()** function
			\cite[Chapter 4, pp. 139]{Alchin2010}.
		* Use the **\_\_setattr\_\_()** function, with the input arguments **self**,
			**name**, and **value** to assign the **value** to the attribute
			called **name** for the instance object **self** (of a class)
			\cite[Chapter 4, pp. 139]{Alchin2010}.
		* For defined attributes, they can be modified with the function
			**setattr()** \cite[Chapter 4, pp. 139]{Alchin2010}.
		* Use **del** to delete an attribute from an object;
			however, it does not work for fake attributes that are controlled by
			special methods
			\cite[Chapter 4, pp. 139]{Alchin2010}.
		* Use the **\_\_delattr\_\_()** function to handle/manage fake attributes
			\cite[Chapter 4, pp. 139]{Alchin2010}.
		* Overridden attributes may have errors or exceptions that when
			raised may indicate another exception (for an overridden or a fake
			attribute) \cite[Chapter 4, pp. 140]{Alchin2010}.  
	- A string representation of an instance object is provided by the
		implementation of the **\_\_str\_\_()** method to coerce the instance
		object to a string \cite[Chapter 4, pp. 140]{Alchin2010}.
		* The implementation of the **\_\_str\_\_()** method should list the
			list of attributes and their corresponding values to enable users to
			create a clone of that instance object
			\cite[Chapter 4, pp. 141-142]{Alchin2010}.
		* Alternatively, the **\_\_repr\_\_()** method can provide more
			information about the instance object
			\cite[Chapter 4, pp. 141-142]{Alchin2010}.
+ Access specifiers (or access modifiers):
	- In *C++*, access specifiers are: public, protected, and private
		\cite[Chapter 12]{Deitel2012} \cite[Chapter 11]{Deitel2014}
		\cite[Chapter 7, pp. 392]{Gaddis2011} \cite[\S7.2, pp.. 349]{Lippman2013}.
		\cite[Chapters 5-6]{Sutherland2015} \cite{Gregoire2014}
	- In *Java*, access specifiers are also: public, protected, and private
		\cite[Chapter 2, pp. 23; Chapter 7, pp. 138]{Schildt2007}
		\cite[pp. 20, 145, & 153]{Eckel2006}
	- *Python* does not directly support keyword-based access specifiers (or
		access modifiers) \cite[Chapter 7, pp. 145]{Hetland2005};
		however, an attribute or method can be set to be pseudo-"private" by
			adding the prefix "\_\_" (i.e., two/double underscores)
			\cite[Chapter 7, pp. 145-146]{Hetland2005}
			\cite[pp. 87, subsubsection on "Class privates"]{Lutz2010}.
		\cite[Chapter 7, section on "Data Encapsulation and Private Attributes," pp. 127]{Beazley2009}.
		* Alternatively, redefine the **\_\_dir\_\_()** method to make it more
			difficult to access quasi-/pseudo- "private" variables
			\cite[Chapter 7, section on "Data Encapsulation and Private Attributes," pp. 128]{Beazley2009}.
		* Wrap private variables that can be modified via mutator methods with
			the built-in **@property** decorator function, so that users would
			use the properties rather than modify the instance variables
			directly
			\cite[Chapter 7, section on "Data Encapsulation and Private Attributes," pp. 128]{Beazley2009}.
	-  Attributes and methods of a *Python* class with the prefix "\_\_" are
		accessible as public methods \cite[Chapter 7, pp. 146]{Hetland2005};  
		hence, I call them pseudo-"private" attributes and methods.
	- If the prefix "\_" (single underscore) is used to indicate pseudo-"private"
		attributes and methods of a *Python* class, these attributes and
		methods would not be "imported with starred imports"
		(**from [module] import \***) \cite[Chapter 7, pp. 146]{Hetland2005}
		\cite[Chapter 7, section on "Data Encapsulation and Private Attributes," pp. 128]{Beazley2009}.
	- \cite[\S8.6.3, pp. 389]{Langtangen2009} suggests using "\_\_" (i.e.,
		two/double underscores) for pseudo-"private" attributes and "\_" (single
		underscore) for pseudo-"protected" attributes.
	- *Python* does not have access specifiers;
		hence, its member variables (attributes) and methods cannot be
			private nor protected \cite[Appendix A, pp. 552]{Hetland2005}.
+ Access and manage polymorphic objects by adhering to its interface (or
	"protocol" \cite[Chapter 9, pp. 179]{Hetland2005}), which is definied by its list of accessible methods and attributes
	\cite[Chapter 7, pp. 155]{Hetland2005}.
	- Unlike *Java* and *C++*, explicit interfaces (i.e., *Java* interfaces and
		*C++* header files) are not required by *Python*
		\cite[Chapter 7, pp. 155-156]{Hetland2005}.
	- The methods **hasattr()** and **getattr()** can be used to determine if
		a given object has certain methods or attributes
		\cite[Chapter 7, pp. 156]{Hetland2005}.
	- Use the **\_\_dict\_\_** attribute to examine all the attributes of a *Python*
		object and their associated values \cite[Chapter 7, pp. 156]{Hetland2005}.
		* The local **\_\_dict\_\_** attribute manages all modifications to an
			instance object
			\cite[Chapter 7, section on "Object Representation and Attribute Binding," pp. 131]{Beazley2009}.
	- Use the **inspect** module to examine all the attributes and methods of a
		*Python* object \cite[Chapter 7, pp. 156]{Hetland2005}.




A suggested method/approach for object-oriented design and analysis (OOAD)
	is mentioned in \cite[Chapter 7, pp. 156-157]{Hetland2005}.

By using sound OOAD methods to design the software architecture, the resultant
	*Python* program would have a modular software architecture that can
	facilitate code reuse \cite[Chapter 10, pp. 206]{Hetland2005}.















Protocols masked by *Python* syntactic sugar
	\cite[Chapter 5, pp. 143]{Alchin2010}:
+ Use the built-in **bool()** method to implement the **\_\_bool\_\_()** method
	to check if the attributes of a class complies with certain class invariants
	(e.g., assertions) are satisfied \cite[Chapter 5, pp. 143]{Alchin2010}.
+ To perform arithmetic operations via arithmetic operators, they require custom
	implementations of the certain methods \cite[Chapter 5, pp. 145]{Alchin2010}:
	- Arithmetic operations \cite[Chapter 5, pp. 145]{Alchin2010}:
		* addition
		* subtraction
		* multiplication
		* division
		* modulo operation \cite[Chapter 5, pp. 146-147]{Alchin2010}
		* exponentiation \cite[Chapter 5, pp. 147]{Alchin2010}
	- arithmetic operators \cite[Chapter 5, pp. 145]{Alchin2010}:
		* **+**
		* **-**
		* **\***
		* **/**
		* **//** \cite[Chapter 5, pp. 146]{Alchin2010}
		* **%** \cite[Chapter 5, pp. 146]{Alchin2010}
		* **\*\*** \cite[Chapter 5, pp. 147]{Alchin2010}
	- Customized implementations of the following methods
		\cite[Chapter 5, pp. 145]{Alchin2010}:
		* **\_\_add\_\_()**
		* **\_\_sub\_\_()**
		* **\_\_mul\_\_()**
		* **\_\_truediv\_\_()** (true division)
		* **\_\_floordiv\_\_()** (floor division) \cite[Chapter 5, pp. 146]{Alchin2010}
		* **\_\_mod\_\_()** (for "perform[ing] standard variable interpretation")
			\cite[Chapter 5, pp. 146]{Alchin2010}
		*  **\_\_divmod\_\_()** (floor division with modulo operation, which is
			called by the **divmod()** method) \cite[Chapter 5, pp. 147]{Alchin2010}
		* **\_\_pow\_\_()** (exponentiation, which is called by the built-in
			**pow()** function) \cite[Chapter 5, pp. 147]{Alchin2010}
	- True division returns the numerical value of the division operation
		\cite[Chapter 5, pp. 145]{Alchin2010}.
	- Floor division returns the lower of the two operands, if the true division of
		these operands lie between the operands on the number line
		\cite[Chapter 5, pp. 146]{Alchin2010}.
+ Bitwise operations \cite[Chapter 5, pp. 148-152]{Alchin2010}
	- **<<**, supported by **\_\_lshift()\_\_** implementation
	- **>>**, supported by **\_\_rshift()\_\_** implementation
	- Bitwise comparison operations \cite[Chapter 5, pp. 149-150]{Alchin2010}:
		* **&**, AND operation or conjunction, implemented by **\_\_and\_\_()**
		* **|**, OR operation or disjunction, implemented by **\_\_or\_\_()**
		* **^**, exclusive OR operation (XOR), implemented by **\_\_xor\_\_()**
		* **~**, inversion operation, implemented by **\_\_invert\_\_()**;
			the **\_\_invert\_\_()** method only works with two's-complement
			encoding \cite[Chapter 5, pp. 150]{Alchin2010}
		* See the table at the bottom of \cite[Chapter 5, pp. 151]{Alchin2010}
			and the top of \cite[Chapter 5, pp. 152]{Alchin2010} for alternate
			ways to place custom objects (e.g., on the right-hand side, and
			in-line via in-place operators)
+ Additional Operations with Numbers
	- Use the **\_\_index\_\_()** method to use an instance object as an index
		in a sequence (e.g., list) \cite[Chapter 5, pp. 152]{Alchin2010}.
	- To round off numbers, use methods such as **floor()** (or rather,
		**\_\_floor\_\_()**) method and **ceil()** (or rather, **\_\_ceil\_\_()**)
		method \cite[Chapter 5, pp. 153]{Alchin2010}.
	- Use the method **round()** (or rather, **\_\_round\_\_(self, number of
		significant figures)**) to round numbers to the nearest number (with
		the specified number of significant figures, which is an optional
		argument) \cite[Chapter 5, pp. 153]{Alchin2010}.
	- For sign operations, use the **\_\_neg\_\_()** to negate the sign of a value,
		and **\_\_abs\_\_()** to obtain the absolute value of the number
		\cite[Chapter 5, pp. 154]{Alchin2010}.
	- For comparison operations that return either **True** or **False**
		\cite[Chapter 5, pp. 154]{Alchin2010}
		\cite[Chapter 9, pp. 197, Table 9.2]{Hall2009b}:
		* **is**, can compare known constants (e.g., **None**)
			+ Compare object IDs (and locations in memory).
		* **is not**, can compare known constants (e.g., **None**)
			+ Compare object IDs (and locations in memory).
		* **==**, or **\_\_eq\_\_()**
			+ Check if objects are equivalent, rather than if they are
				the same object.
		* **!=**, or **\_\_ne\_\_()** (i.e., not equal)
		+ Check if objects are equivalent, rather than if they are
			the same object.
		* **<**, or **\_\_lt\_\_()**
		* **>**, or **\_\_gt\_\_()**
		* **<=**, or **\_\_lte\_\_()**
		* **>=**, or **\_\_gte\_\_()**
		* Default method for comparison **\_\_cmp\_\_()** compares **self**
			with **other** \cite[Chapter 5, pp. 155]{Alchin2010}
+ Iterables \cite[Chapter 5, pp. 155]{Alchin2010}:
	- To determine if an object is iterable, use the built-in **iter()** function (or
		rather, **\_\_iter\_\_()**) to obtain an iterator;
		if an iterator is returned, the object is iterable
		\cite[Chapter 5, pp. 155]{Alchin2010}.
	- The **\_\_iter\_\_()** method, which includes the **\_\_init\_\_()** method
		to instantiate the iterator and returns **self** \cite[Chapter 5, pp. 155]{Alchin2010};
		an iterator is itself iterable \cite[Chapter 5, pp. 155]{Alchin2010}.
	- The **\_\_next\_\_()** is another required method, which retrieves a value
		from the iterator for use (by the caller of the **\_\_next\_\_()** method)
		\cite[Chapter 5, pp. 155]{Alchin2010};
		the **\_\_next\_\_()** method terminates at the end of enumerating all
			elements of a collection, due to the raised **StopIteration**
			exception \cite[Chapter 5, pp. 156]{Alchin2010};
		this is because **None** is a valid object, and the iterator cannot
			compare the instance object pointed to by itself to **None**
			\cite[Chapter 5, pp. 156]{Alchin2010}.
	- If the **\_\_iter\_\_()** method is not implemented, the **\_\_getitem\_\_()**
		method is used to access the element at the current position of the
		iterator \cite[Chapter 5, pp. 157]{Alchin2010}.
+ *Python* supports sequences, such as lists, tuples, sets, and strings
	\cite[Chapter 5, pp. 159]{Alchin2010}:
	- Each type of these sequences \cite[Chapter 5, pp. 159]{Alchin2010}:
		* has a specialized type of iterator
		* can provide information regarding attributes about the sequence
		* has behaviors that can be performed on the sequence
		* E.g., determine the size/length of the sequence \cite[Chapter 5, pp. 159]{Alchin2010},
			or traverse the sequence in reverse order \cite[Chapter 5, pp. 160]{Alchin2010}.
		* **\_\_len\_\_()**, **\_\_setitem\_\_()**, **\_\_append\_\_()**,
			**\_\_insert\_\_()**, **del sequence[index]**, **\_\_delitem\_\_()**,
			and **\_\_contains\_\_()**
	- \cite[Chapter 3, subsubsection on "Operations Common to All Sequences," Table 3.2, pp. 39-40]{Beazley2009}
		lists a set of operations and methods that can be applied to all
		sequences, including immutable tuples.
	- \cite[Chapter 3, subsubsection on "Operations Common to All Sequences," Table 3.3, pp. 40]{Beazley2009}
		lists a set of operations that can be applied to all mutable sequences
		only.
+ A mapping is a set of individual pairs, where each pair has a key and a
	corresponding value \cite[Chapter 5, pp. 164]{Alchin2010}.
	- The ordering of the pairs by their keys is not important, since a map is
		typically not traversed/enumerated.
	- For a given key, it enables instant access to a the key's corresponding
		value (which is referenced by its key).
	- Use the **key()** method to enumerate each key/pair in the mapping,
		without paying attention to its ordering.  
	- Use the **items()** method to obtain the set of all *(key,value)* pairs in the
		mapping \cite[Chapter 5, pp. 165]{Alchin2010}.
+ Callable functions and classes \cite[Chapter 5, pp. 165]{Alchin2010}
	- The **\_\_call\_\_()** method calls the class itself, using **self** as the first
		argument
+ Context manager \cite[Chapter 5, pp. 166]{Alchin2010}
	- Use objects as context managers with the **with** statement (which
		includes the **as** clause), so that they can set things up
		(preprocessing), do some processing within the context, and clean up
		after the processing (or post-processing)
		\cite[Chapter 5, pp. 166]{Alchin2010}.
	- Examples of contexts include:
		* **file handling** \cite[Chapter 5, pp. 166]{Alchin2010}
	- Set things up (preprocessing):
		* **\_\_enter\_\_()** method
	- Clean up after the processing (or post-processing):
		* **\_\_exit\_\_()** method
			+ When exceptions terminate the processing, this **\_\_exit\_\_()**
				method would receive information about the exception for
				post-processing and debugging (or troubleshooting)
				\cite[Chapter 5, pp. 166]{Alchin2010}.
			+ When no exceptions are raised during processing, and clean up
				proceeds as expected, it would receive **None** objects
				instead of information for debugging (or troubleshooting)
				\cite[Chapter 5, pp. 167]{Alchin2010}.
+ Multiple protocols can be used simultaneously, since they are not mutually
	exclusive \cite[Chapter 5, pp. 168]{Alchin2010}.




By default, each *Python* function is a virtual function \cite{Ucoluk2012}.

Additional information about object-oriented programming:
+ accessor and mutator functions \cite[\S7.3.1, pp. 206-208]{Ucoluk2012}
+ inheritance \cite[\S7.3.2, pp. 209-210]{Ucoluk2012}
	- virtual functions \cite[\S7.3.2, pp. 209-210]{Ucoluk2012}
+ operator overloading \cite[\S7.3.4, pp. 211-212]{Ucoluk2012}
	\cite[Chapter 7, section on "Operator Overloading," pp. 133-134]{Beazley2009}.
	- Type conversion by coercion is not supported in *Python 2.6* or *Python 3*
		for mixed-type arithmetic
		\cite[Chapter 7, section on "Operator Overloading," pp. 134]{Beazley2009}.
+ asbtract base classes \cite[Chapter 7, section on "Abstract Base Classes," pp. 136-138]{Beazley2009},
	which cannot "be instantiated directly";
	similarly, abstract derived classes cannot "be instantiated directly"
	\cite[Chapter 7, section on "Abstract Base Classes," pp. 137]{Beazley2009}
	- "Abstract class[es] [do] not [carry out] conformance checking on arguments
		or return values"
		\cite[Chapter 7, section on "Abstract Base Classes," pp. 137]{Beazley2009}.




"A property is a special [category]/kind of attribute that computes its value
	when accessed";
	it is defined/implemented like a function, such that when it is accessed, it
		executes the function-like definition to determine its value;
	it is declared with the **@property** decorator just before its
		definition/implementation
	\cite[Chapter 7, section on "Properties," pp. 124-125]{Beazley2009}.

A property can carry out operations in the background to modify or delete an
	attribute, via connecting/binding the methods for modification and deletion
	to the property
	\cite[Chapter 7, section on "Properties," pp. 125]{Beazley2009}.


Use the *Uniform Access Principle* to faciliate the design of uniform programming
	interfaces, so that attribute-like (accessor) methods should be specified as
	properties to ease the confusion between including the parentheses
	(or round brackets) when using attribute-like (accessor) methods and ignoring
	the parentheses when using attributes
	\cite[Chapter 7, section on "Properties," pp. 125]{Beazley2009}.



**An aside: See the following for information about [partially evaluated functions](https://www.boost.org/doc/libs/1_44_0/libs/spirit/classic/phoenix/doc/basic_concepts.html) in **C++**.*



When an instance object access a method like an attribute, it would return a
	**bound method** object, instead of a function object, since the method
	access would invoke the **()** operator and execute the method
	\cite[Chapter 7, section on "Properties," pp. 125]{Beazley2009};
	this is similar to **partially evaluated function**s, since the **self** parameter
		"has a value" and I would have to supply the remaining/additional
		arguments using the **()** operator;
	a **property** (function) executes in the background to create this bound
		method
	\cite[Chapter 7, section on "Properties," pp. 125]{Beazley2009}.






To do post-processing after the definition of a class
	\cite[Chapter 7, section on "Class Decorators," pp. 141]{Beazley2009}:
+ Customize the class creation process with the definition of a metaclass.
+ Use a **class decorator** that receives a class object as input, and returns a
	class object as output.






Other information about classes:
+ Comparison between classes and modules:
	- \cite[Chapter 29, section on "Classes Versus Modules", pp. 884]{Lutz2013}
		* "Because they're both about namespaces, the distinction can be
			confusing."
		* "Classes also support extra features that modules don't, such as
			operator overloading, multiple instance generation, and inheritance.
			Although both classes and modules are namespaces, you should
				be able to tell by now that they are very different things."
		* Modules
			+ "Implement data/logic packages"
			+ "Are created with Python files or other-language extensions"
			+ "Are used by being imported"
			+ "Form the top-level in Python program structure"
		* Classes
			+ "Implement new full-featured objects"
			+ "Are created with class statements"
			+ "Are used by being called"
			+ "Always live within a module"














###	Object management

"All objects in Python are said to be `first class.'
	This means that all objects that can be named by an identifier have equal
		status.
	It also means that all objects that can be named can be treated as data."
		\cite[Chapter 3, section on "First-Class Objects," pp. 37]{Beazley2009}.
+ Compared to other object-oriented programming languages, "*Python*'s
	built-in types are organized into a relatively flat hierarchy"
	\cite[Chapter 7, section on "Abstract Base Classes," pp. 137]{Beazley2009}.
+ A **metaclass** is a special category/kind of object that creates and manages
	classes;
	a class definition in *Python* becomes a class object, which needs to be
		created and managed by the **metaclass**
	\cite[Chapter 7, section on "Metaclasses," pp. 138]{Beazley2009}.
	- The constructor of the metaclass uses the following information to create
		the corresponding class object \cite[Chapter 7, section on "Metaclasses," pp. 138]{Beazley2009}:
		* "name of the class"
		* "list of base classes"
		* a private dictionary containing the body of the class, as a series of
			statements








+ In the object-oriented programming (OOP) paradigm, an object (or an instance
	of a class) has a set of methods (member functions) and attributes (i.e.,
	fields or data members) that enable manipulation (or control) of its behavior
	\cite[Chapter 6, pp. 169]{Alchin2010} \cite[Chapter 9, pp. 181]{Hall2009b}.
	- Methods; also known as functions belonging to an object, or member
		functions. These capture the behavior of the objects.
	- Attributes; also known as fields, data members, or instance variables and
		static variables. These capture the data of the objects.
+ An object is an instance of a class; a class can have many instances of objects
	\cite[Chapter 7, pp. 147]{Hetland2005}.
	- A subclass can be defined by: defining more methods; overriding existing
		methods; and having more attributes \cite[Chapter 7, pp. 146]{Hetland2005}.
+ In *Python*, an object is a combination of the following
	\cite[Chapter 6, pp. 169]{Alchin2010}:
	- identity, which is its unique address in memory; it is constant in its lifetime;
		this can be determined by "the built-in **id()** function".
	- type, which is defined by its class and parent class (or supporting base
		classes); an object has a reference to the class that it is an instance
		of (or belongs to).
	- value(s) of its attributes, which distinguishes objects of a class from each
		other.
		* Use the method **super()** to access the overridden method in the
			parent class \cite[Chapter 6, pp. 170]{Alchin2010}
			\cite[Chapter 7, section on "Inheritance," pp. 120]{Beazley2009}.
		* Use the **\_\_init\_\_()** method and the **\_\_new\_\_()** method to
			set up the default values \cite[Chapter 6, pp. 170]{Alchin2010}.
+ Guidelines about using mixins:
	- The use of **super()** may not allow us to control the mixin's class and
		base class \cite[Chapter 6, pp. 171]{Alchin2010};
		resolve this problem using the method **\_\_new\_\_()**, so that a
			new dictionary can be created for each encountered class.
	- Note that if a dictionary is created within a **cachedproperty()** function,
		each property would have its own private namespace;
		this results in memory leaks
		\cite[Chapter 6, pp. 176]{Alchin2010}.   
+ *Python* has automatic garbage collection \cite[Chapter 6, pp. 176]{Alchin2010}
	\cite[Chapter 5, pp. 103]{Hetland2005}
	\cite[Chapter 3, section on "Reference Counting and Garbage Collection," pp. 34-35]{Beazley2009}
	\cite[Chapter 7, section on "Object Memory Management," pp. 129]{Beazley2009}.
	- Effective garbage collection depends on
		\cite[Chapter 6, pp. 176]{Alchin2010}:
		* ability to reliably identify/recognize an object as garbage that will
			cause memory leaks in the *Python* application
		* ability to remove garbage from (main) memory
	- Techniques for garbage collection \cite[Chapter 6, pp. 177]{Alchin2010}:
		* Reference counting \cite[Chapter 7, section on "Object Memory Management," pp. 129]{Beazley2009}
			+ The method **\_\_del\_\_()** is automatically called when the
				reference count for an object reaches zero
				\cite[Chapter 7, section on "Object Memory Management," pp. 129]{Beazley2009}.
			+ Note that for classes that redefine the method **\_\_del\_\_()**,
				the "*Python's* cyclic garbage collector" cannot automatically
				call the method **\_\_del\_\_()**;
				do not perform dynamic memory management manually
				\cite[Chapter 7, section on "Object Memory Management," pp. 129]{Beazley2009}.
		* Cyclical references, which is inefficient but leads to more consistent
			and reliable outcomes \cite[Chapter 6, pp. 178-179]{Alchin2010}
		* Weak references \cite[Chapter 6, pp. 180-181]{Alchin2010}
+ The **pickle** module in *The Python Standard Library* \cite{DrakeJr2016e,DrakeJr2016b}
	enables data stored in *Python* objects to be exported to external software
	as strings \cite[Chapter 6, pp. 182]{Alchin2010}.
	- Its "pickling" process serializes a *Python* object structure by converting
		a *Python* object hierarchy into a byte stream \cite{DrakeJr2016e,DrakeJr2016b}.
	-  "Unpickling" is the inverse operation of "pickling";
		it de-serializes a *Python* object structure by converting a byte stream
		into a *Python* object hierarchy \cite{DrakeJr2016e,DrakeJr2016b}.
	- Picking is also known as serialization, marshalling, or flattening
		\cite{DrakeJr2016e,DrakeJr2016b}.
	- The functions for performing pickling are **dump()** and **dumps()**
		\cite[Chapter 6, pp. 182]{Alchin2010}, and the functions for unpickling
		are **load()** and **loads()** \cite[Chapter 6, pp. 183]{Alchin2010}.
+ Objects can be copied using a shallow copy or deep copy method
	\cite[Chapter 6, pp. 186-189]{Alchin2010}
	\cite[Chapter 3, section on "References and Copies," pp. 36]{Beazley2009}.
	- Perform shallow copying with **copy()** to get a shallow copy of an object;
		the copy object has the same data values (of the same type), but with a
		new identity, and modifying the copy object would not modify the
		original object \cite[Chapter 6, pp. 187]{Alchin2010}.  
	- One-level deep copying, which is considered shallow copying, only
		provides a copy of the references, and does not copy the objects
		\cite[Chapter 6, pp. 188]{Alchin2010};
		"a namespace is a mapping from names to objects"
		\cite{Brandl2017,Brandl2017a}
+ To make a deep copy, use the **deepcopy()** method to copy the structure
	and objects referenced by the original object;
	modification of the deep copy does not affect the original copy, and vice
		versa \cite[Chapter 6, pp. 188]{Alchin2010}.






















Pages in \cite{Hetland2005} that deal with importing
	*Python* classes and modules:
+ Modules and The Standard Library, pp. 203--254 (Chapter 10)
+ Summaries: pp. 547--570 (Appendices A-B)
+ Online resources: pp. 571--573 (Appendix C)




###	Data Types

Immutable data types are \cite{Sturtz2020}:
+ tuples
	- [Examples of trying to add an element to a tuple and of trying to remove an element from a tuple. Errors for trying to do these were caught.](https://github.com/eda-ricercatore/python-sandbox/blob/main/i-data-structures/tuple_operations.py)

Dictionary keys have to be ([hashable](https://docs.python.org/3/glossary.html#term-hashable))
	data types \cite{Sturtz2020}, such as the following: 
+ tuples
+ integers
+ floats
+ strings
+ boolean
+ frozensets

From \cite{PythonSoftwareFoundationcontributors2020}:
+ "An object is hashable if it has a hash value which never changes during its lifetime (it needs a ***\_\_hash\_\_()*** method), and can be compared to other objects (it needs an ***\_\_eq_\_()*** method)."


Since the following are not [hashable](https://docs.python.org/3/glossary.html#term-hashable),
	they cannot be used as dictionary keys \cite{Sturtz2020}.
+ lists
+ dictionaries
+ sets



Use the functions ***id()*** and ***type()*** to determine the "ID" and type
	 of a data type or object \cite{Sengupta2018}.








### *Python* Functions

Notes on *Python* functions:
+ For functions that have no **return** statement, they return the **None** object
	\cite[Chapter 6, section on "Parameter Passing and Return Values," pp. 96]{Beazley2009}.
	- By default, *Python* functions return *None* \cite[Chapter 1, pp. 15]{Alchin2010}.
+ Return multiple values from a function by placing them in a tuple, which is
	returned to the function caller
	\cite[Chapter 6, section on "Parameter Passing and Return Values," pp. 96]{Beazley2009}.
	- \cite{saffsd2017}, \cite{Agrawal20XY}, and \cite{Lathkar2018} show other methods of
		returning multiple values;
		the methods are listed as follows.
		* As a named **tuple**
			+ Or, tuples \cite{MantidContributors20XY}.
			+ \cite{LaRooy2013} indicates that returned variables without
				surrounding round brackets are returned as a tuple, rather
				than multiple separate variables;
				the individual elements of the tuple can be accessed separately.
		* As a **dictionary**
		* As a **list**
		* As an **object**, using the instantiation of a *Python* class.
	- We can also use a generator to return multiple values \cite{rlms2014}.
	- As of September 2017, 2018, I cannot create a function with optional
		input parameters.
		* I can assign variables to default values.
		* However, I cannot assign optional variables to default values before
			assigning values to optional variables.
	- To return a variable number of values, try using a list, dictionary,
		or object,
+ No *Python* function is given special privileges over other *Python* functions
	\cite[Chapter 3, pp. 53]{Alchin2010}.
+ *Python* functions encapsulate code into individual units, which facilitates
	code reuse \cite[Chapter 3, pp. 53]{Alchin2010}.
+ *Python* treats functions as full-fledged objects, so that they can be
	\cite[Chapter 3, pp. 53]{Alchin2010}:
	- stored and transferred via data structures
	- "wrapped [around by] other functions"
	- "replaced by new implementations"
+ "Input data are arguments, output data are returned."
	\cite[Appendix B, \SB.3.2, pp. 708]{Langtangen2009}.
+ Arguments of a *Python* function:
	- positional arguments (or order-based arguments)
		\cite[Chapter 3, pp. 53]{Alchin2010} are grouped in an immutable tuple
		\cite[Chapter 3, pp. 56]{Alchin2010}.
	- Keyword arguments are specified by parameter-value assignments
		during keyword argument function calls/invocations
		\cite[Chapter 6, section on "Functions," pp. 94]{Beazley2009}.
	- keyword arguments \cite[Chapter 3, pp. 53]{Alchin2010} are placed in
		a mutable dictionary \cite[Chapter 3, pp. 56]{Alchin2010}.
	- It is recommended that arguments of a given *Python* function have
		default values \cite[Chapter 3, pp. 53]{Alchin2010}.
		* In the signature of a function, the first parameter defined with a
			default value and subsequent parameters are considered optional
			\cite[Chapter 6, section on "Functions," pp. 93]{Beazley2009}.
		* Each optional parameter requires an assignment to a default value
			\cite[Chapter 6, section on "Functions," pp. 93]{Beazley2009}.
		* Note that (as aforementioned) "argument validation assigns default
			values to optional arguments" \cite[Chapter 3, pp. 66-67]{Alchin2010}.
	- Keyword arguments are explicitly specified during function calls,
		and are favored over positional arguments that are implictly specified
		during function calls \cite[Chapter 3, pp. 54]{Alchin2010}.
		* Keyword arguments also *Python*ic in terms of coding style
			\cite[Chapter 3, pp. 56]{Alchin2010}.
	- When a function call has positional arguments and keyword arguments in
		its function signature, the positional arguments have to be placed in
		front of keyword arguments
		\cite[Chapter 6, section on "Functions," pp. 94]{Beazley2009}.
	- No argument in a function call/signature can appear multiple times
		  \cite[Chapter 6, section on "Functions," pp. 94]{Beazley2009}.
	- Develop code that supports overriding via flexibility
		\cite[Chapter 3, pp. 54]{Alchin2010}.
	- *Python* functions can have variable arity
		\cite[Chapter 6, section on "Functions," pp. 94]{Beazley2009},
		which is indicated by prefixing the name of the last parameter in the
		function signature with an asterisk
		* E.g., **def function\_name(param1, param2, \*param-last)**.
		* The term **\*param-last** in the above example is a tuple
			representing the set of variable/remaining arguments
			\cite[Chapter 6, section on "Functions," pp. 94]{Beazley2009}.
	- Prefix the name of the last parameter in the function signature with two
		consecutive asterisks to place **additional/extra keyword arguments**
		in a dictionary, which is passed to the function so that the function can
		"accept a large number of potentially open-ended configuration options
		that would be too unwieldy to list as parameters"
		\cite[Chapter 6, section on "Functions," pp. 95]{Beazley2009}.
		* E.g., **def function\_name(param1, param2, \*\*param-last)**.
		* To use variable-length argument lists with additional/extra keyword
			arguments, place the **\*\*param-last** term, which represents
			additional/extra keyword arguments, at the end of the function
			signature
			\cite[Chapter 6, section on "Functions," pp. 95]{Beazley2009}.
		* The **\*\*param-last** term can be passed to another function as
			**\*\*param-last**, since it is placed in a dictionary
			\cite[Chapter 6, section on "Functions," pp. 95]{Beazley2009}.
		* **\*\*kwargs** is an example of using an arbitrary number of
			keyword arguments \cite[\S4.7.3 'Arbitrary Argument Lists' and \S4.7.4 'Unpacking Argument Lists']{Brandl2017a}.
		* When calling a multi-value returning function, I can assign
			"**_**" to an unwanted return value (or "**_BLAH**, **_BLAH_BLAH**, **_BLAH_BLAH_BLAH**" to unwanted
			return values.
		* I can use a parameterized method/function call to determine
			the number of values that I should return;
			an input parameter/argument is used as a switch to determine
				the number of return values, and I should call the
				method/function with this "extra" input argument.
		* \cite[Section on "Functional Programming Modules," and subsection on "functools - Higher-order functions and operations on callable objects"]{DrakeJr2016b} show how to use
			**functools.partial(func, \*args, \*\*keywords**) to obtain
			variable output values;
			this enables multiple output values to be returned.
	- Use the terms **\*param-last** and **\*\*param-last** to write wrappers
		and proxies for other functions, so that these wrappers/proxies can
		pass these terms to those other functions
		\cite[Chapter 6, section on "Functions," pp. 95]{Beazley2009}.
	- Types of arguments listed in order of precedence/priority
		\cite[Chapter 3, pp. 56-59]{Alchin2010}:
		* required arguments (ensures/guarantees that required positional
			arguments are processed before optional arguments are processed)
		* optional arguments (ensures/guarantees that optional arguments are
			processed before variable arguments)
		* variable positional arguments (ensures/guarantees that variable
			positional arguments are processed before variable keyword
			arguments);
			**all the variable positional arguments of a function have to be
				group into one set**;
			multiple sets of variable positional arguments have to be group into
				one set
		* variable keyword arguments;
			**all the variable keyword arguments of a function have to be
				group into one set**;
			multiple sets of variable keyword arguments have to be group into
				one set
	- "Preloading arguments" (or"Partial application of a function") occurs when it "preload[s] some of the
		arguments in advance", so that fewer arguments have to be assigned
		values later \cite[Chapter 3, pp. 60]{Alchin2010}.
	- Currying in functional programming is subtly different from preloading
		arguments \cite[Chapter 3, pp. 60]{Alchin2010};
		* A pure curried function shall be called repeatedly till all the arguments
			are assigned values -- the number of unassigned arguments is
			reduced as the pure curried function is iteratively called till all
			arguments are assigned values, before the most recently
			returned/created function (for which all of its arguments are
			assigned) is executed;
		* Partial application will return a function that can be subsequently
			executed, regardless of whether it has any unassigned arguments
			-- note that executing a function with unassigned arguments will
			result in raising a *TypeError*.
+ Functions can modify input objects passed to them, and this can result in side
	effects; hence, parameter passing cannot be classified into "pass-by-value"
	nor "pass-by-reference"
	\cite[Chapter 6, section on "Parameter Passing and Return Values," pp. 95]{Beazley2009}.
+ For functions that can result in side effects, use locks to protect input objects
	passed to these functions, so that parallel and concurrent programs can
	function correctly
	\cite[Chapter 6, section on "Parameter Passing and Return Values," pp. 95-96]{Beazley2009}.
+ "Python supports nested function definitions"
	\cite[Chapter 6, section on "Scoping Rules," pp. 97]{Beazley2009}.
+ Types of *Python* functions \cite[Chapter 3]{Alchin2010}:
	- decorators
	- function annotations \cite[Chapter 3, pp. 78]{Alchin2010}.
		* Attach an expression to each input argument and the return value.
	- generators
		* A generator has the "flexibility of a function and the performance of
			an iterator";
			it uses the **yield** statement to enable a value to be read externally,
				and it is analogous to the **return** statement \cite[Chapter 3, pp. 94]{Alchin2010}.
		* See [Miscellaneous](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#miscellaneous).
	- lambdas
		* Has a return value in the body of a lambda, and omits any explicit
			return statement;
			only allows a single expression \cite[Chapter 3, pp. 97]{Alchin2010}.
	- introspection
		* Any access/examination of information at run-time, such as
			\cite[Chapter 3, pp. 97]{Alchin2010}:
			+ object attributes
			+ module contents
			+ documentation
			+ generated bytecode
+ A decorator is a technique for obtaining a (new) function from passing a
	function (function to be decorated) into another function (decorator)
	\cite[Chapter 3, pp. 61,68]{Alchin2010};
	- It is used to support preloading arguments (or partial application of a
		function) \cite[Chapter 3, pp. 61]{Alchin2010};
	- Use a decorator to execute boilerplate code in a set of input functions
		before/after the execution of the returned function
		\cite[Chapter 3, pp. 68]{Alchin2010}.
	- Use decorators to avoid boilerplate code and simplify the functions
		\cite[Chapter 3, pp. 77]{Alchin2010}.
	- Applications of decorators \cite[Chapter 3, pp. 67-68]{Alchin2010}:
		* access control
		* cleanup of temporary objects
		* error handling
		* caching
		* logging
	- A closure is a function, which is defined in another function, and can be
		passed to another function as an object
		\cite[Chapter 3, pp. 69]{Alchin2010}.
		* It can involve \cite[Chapter 3, pp. 69]{Alchin2010}:
			+ lexical scope
			+ free variables
			+ upvalues
			+ variable extent
		* A function *A* passed into another function *B* cannot be the closure
			of function *B*, since *A* is not defined in *B*
			\cite[Chapter 3, pp. 70]{Alchin2010}.
	- A wrapper is a function contained within another function and additional
		behavior executed before or/and after the execution of the wrapped
		function \cite[Chapter 3, pp. 71]{Alchin2010}.
		* To call the wrapper "as if it [was] the original function," pass variable
			positional arguments and keyword arguments together (for
			"maximum flexibility") internally into the original function
			\cite[Chapter 3, pp. 71]{Alchin2010}.
		* Execute the wrapper within a *try-except* block to catch any raised
			error;
			if an error is raised, implicitly return **None**;
			a value (or **None**) is returned to the original function
			\cite[Chapter 3, pp. 71]{Alchin2010}.
		* Information lost by the wrapped function can be obtained by the
			*wrap* decorator in the *functools* module;
			here, a decorator is used inside another decorator to avoid
				code duplication
			\cite[Chapter 3, pp. 71]{Alchin2010}.
	- A decorator with arguments is implemented by the "original" function
		having extra arguments that are passed to the wrapper, which returns
		the decorator \cite[Chapter 3, pp. 72]{Alchin2010}.
	- Beware of side effects of decorators \cite[Chapter 3, pp. 75]{Alchin2010}.
	- A decorator enables memoization by storing the result of a function;
		this is carried out by the argument list as a key to automatically cache
		the result \cite[Chapter 3, pp. 75]{Alchin2010}.
	- Factoring out the boilerplate code \cite[Chapter 3, pp. 86]{Alchin2010}:
		* An annotation determines "if [a] value is appropriate, and raises an
			exception" for inappropriate values.
		* Use a decorator to factor out the boilerplate code as a new function,
			connect it to the rest of the code, and process the annotation for each
		value \cite[Chapter 3, pp. 86]{Alchin2010}.
	- A decorator can make use of annotation for type coercion
		\cite[Chapter 3, pp. 88]{Alchin2010}.
		- Either require an argument to accept values of a specific type, or
			coerce an input value to the required type
			\cite[Chapter 3, pp. 88]{Alchin2010}.
		* **The robustness principle allows input arguments to accept values
			of a small range of types, which can be converted to the
			required types prior to further processing;
			hence, the type of the return value would always be consistent
			with the type expected by external code, so that
			postconditions would be satisfied.**
	- Provide an annotation directly to the code that needs it, and/or use a
		decorator with input argument to annotate the code
		\cite[Chapter 3, pp. 90]{Alchin2010}.
	- Stacking multiple decorators "together on a function" provides "a built-in
		way to manage each corresponding framework";
		each decorator has a corresponding framework
		\cite[Chapter 3, pp. 90]{Alchin2010}.
+ A flexible function can be customized into a simpler and less flexible function
	so that its reduced flexibility can be handled by existing API/libraries
	\cite[Chapter 3, pp. 61]{Alchin2010}.
+ The transparency of *Python* allows different aspects of *Python* objects,
	including functions, to be examined/inspected at run-time
		\cite[Chapter 3, pp. 61]{Alchin2010};
	- the *inspect* module from *The Python Standard Library* has introspection
		features that enable the examination/inspection of function arguments  
		-- "a named tuple of information about [a] function's arguments" is
		returned from processing the input function
		\cite[Chapter 3, pp. 61]{Alchin2010};
	- argument values of a function's arguments can be identified and be used to
		generate argument lists \cite[Chapter 3, pp. 62]{Alchin2010}.
	- call a function with another function, a tuple of its positional arguments, and
		a dictionary keyword arguments \cite[Chapter 3, pp. 62]{Alchin2010}.
	- exploit the transparency of *Python* while refactoring functions to make
		the functions more concise \cite[Chapter 3, pp. 62]{Alchin2010}.
	- perform argument validation to reduce the risk of raising errors due to
		unassigned arguments by checking if arguments are assigned values
		and if all arguments are known (i.e., "Are there any unknown
		arguments?") \cite[Chapter 3, pp. 66]{Alchin2010}.
	- argument validation assigns default values to optional arguments, and
		returns a dictionary of required arguments (such that each
		unassigned argument has a message indicating that it needs to be
		assigned a value or that it is an unknown argument)
		\cite[Chapter 3, pp. 66-67]{Alchin2010}.
+ Aspects of a function that is code invariant
	\cite[Chapter 3, pp. 78]{Alchin2010}:
	- name of function
	- set of input arguments
	- optional docstring
+ From *Python* 2.2 onwards, scopes in *Python* programs can be nested
	  \cite[Chapter 6, pp. 128]{Hetland2005}.
	- That is, we can nest a function definition within another function definition.
	- Alternatively, a function can be embedded within another function.  
	- When the outer function gets called, the inner function is redefined, and
		the outer function "returns the inner function" by returning the return
			value of the inner function.
	- The outer local scope (i.e., local scope of the outer function) is accessible
		within the inner function (i.e., local scope of the inner function).
	- That is, the following are equivalent:
		* outer_function(*param_1*)(*param_2*)
		* The following pair of statements:
			+ temp_function = outer_function(*param_1*)
			+ temp_function(*param_2*)
+ *Python* supports "functional programming" via the
	following functions \cite[Chapter 6, pp. 133]{Hetland2005}:  
	- **map** \cite[Chapter 6, pp. 133-134]{Hetland2005}:
		* Maps a sequence to another sequence of equivalent length, via the
			application of a function to each element in the input sequence.
		* E.g., **map(***[lambda expression]*, input_sequence **)**.
		* E.g., **map(***[a function that accepts a sequence as its input parameter]*, input_sequence **)**.
	- **filter** \cite[Chapter 6, pp. 133-135]{Hetland2005}:
		* The **filter** function returns a subset of the input sequence by
			applying a function, which has a boolean return value, on each
			element in the input sequence.
		* The input parameters for the **filter** function are:
			an explicitly specified input function for the input sequence,
			and an input sequence;
			note that the explicitly specified input function would be applied to
				each element in the input sequence, and must return a
				boolean value.
		* E.g., **map(** *[lambda expression]*, input_sequence **)**.
		* E.g., **map(** *[input function]*, input_sequence **)**.
	- **reduce** \cite[Chapter 6, pp. 135-137]{Hetland2005}:
		* The **reduce** function performs an explicitly specified input function
			with the first two elements in the input sequence, and the outcome
			and the next available element, till the input sequence has been
			processed/enumerated \cite[Chapter 6, pp. 135]{Hetland2005}.
		* E.g., **reduce(** *[lambda expression]*, input_sequence **)**.
		* E.g., **reduce(** *[an input function]*, input_sequence **)**.
		* A **for** loop can implement any **reduce** function
			\cite[Chapter 6, pp. 135-137]{Hetland2005}.
		* Using a **for** loop instead of the **reduce** function can improve
			the comprehensibility of the source code.
	- **apply** \cite[Chapter 6, pp. 137]{Hetland2005}:
		* The **apply** function calls the explicitly specified input function,
			which is provided as an input argument.
		* E.g., **apply(** *[input function]* **)**.
		* E.g., **apply(** *[input function]*, *[tuple of positional arguments]* **)**.
		* E.g., **apply(** *[input function]*, *[dictionary of keyword arguments]* **)**.
		* E.g., *[input function]*(\**[dictionary of keyword arguments]*).
		* E.g., *[input function]*(\**[tuple of positional arguments]*).
		* Note that \**[dictionary of keyword arguments]* unpacks the dictionary
			of keyword ararguments.
		* Note that \**[tuple of positional arguments]* unpacks the tuple of
			positional ararguments.
	- lambda expressions \cite[Chapter 6, pp. 134]{Hetland2005}:
		* small, unnamed functions that contains an expression, which value is
			returned.
		* Note that the term **lambda** is a reserved word (or keyword) in
			*Python*.
		* **lambda** [parameters, delimited by a comma] : [an expression]
		* Also, note that full-fledged functions with names facilitate
			self-documention;
			lambda expressions can make the code difficult to read and
				understand.
		* Use **lambda** statements to define anonymous functions
			\cite[Chapter 6, section on "Declarative Programming," pp. 112]{Beazley2009};
			+ Syntax: ***lambda args : expression***
				\cite[Chapter 6, section on "Declarative Programming," pp. 112]{Beazley2009}:
				- "***args*** is a comma-separated list of arguments"
				- ***expression*** is a valid combination of arguments in
					***args***;
					i.e. a valid expression of arguments in ***args***;
					***expression*** cannot include multiple statements, or
						statements that are not expressions;
					"***lambda*** expressions follow the same scoping rules
						as functions"
		* Use **lambda** statements to "specify short callback functions"
			\cite[Chapter 6, section on "Declarative Programming," pp. 112]{Beazley2009}
	- Note on **map**, **filter**, and list comprehension
		\cite[Chapter 6, pp. 134-135]{Hetland2005}:
		* A list comprehension can implement any **filter** or **map**
			\cite[Chapter 6, pp. 135]{Hetland2005}.
		* Using list comprehensions, instead of **map**s or **filter**s, can
			improve the comprehensibility of the source code
			\cite[Chapter 6, pp. 135]{Hetland2005}.
		* Note that using **map**s or **filter**s, instead of list comprehensions,
			would result in faster execution (i.e., better performance)
			\cite[Chapter 6, pp. 135]{Hetland2005}.




A **coroutine** is a function "that processes a sequence of inputs," rather than a
	set of input arguments (like normal functions)
	\cite[Chapter 1, section on "Generators," pp. 20]{Beazley2009}
	\cite[Chapter 6, section on "Coroutines and yield Expressions," pp. 104]{Beazley2009}.
+ Make an initial call of the **next()** function, "so that the **coroutine** executes
	statements leading to the first **yield** expression" (or executes statements
	prior to the first **yield** expression)
	\cite[Chapter 6, section on "Coroutines and yield Expressions," pp. 104]{Beazley2009}.
	- To avoid errors attributed to missing this initial **next()** function call,
		wrap the **coroutine** with a decorator
		\cite[Chapter 6, section on "Coroutines and yield Expressions," pp. 104]{Beazley2009}.
+ To operate on the next (set of) input in the sequence, it uses the **yield**
	statement \cite[Chapter 1, section on "Coroutines," pp. 20]{Beazley2009}.
+ To send the next (set of) input in the sequence for processing by the
	**coroutine**, it uses the **send function**
	\cite[Chapter 1, section on "Coroutines," pp. 20]{Beazley2009}.
+ The **yield** statement would suspend execution of the **coroutine**
	\cite[Chapter 1, section on "Coroutines," pp. 20]{Beazley2009}.
+ Processing of the next (set of) input in the sequence ends when the
	**coroutine** returns or the **close()** function is called
	\cite[Chapter 1, section on "Coroutines," pp. 20]{Beazley2009}
	\cite[Chapter 6, section on "Coroutines and yield Expressions," pp. 105]{Beazley2009}.
+ **Coroutine**s facilitate the modeling of producer-consumer problems, where
	the **coroutine**(s) model(s) data consumption/processing and the
	**generator**s model(s) data generation/production
	\cite[Chapter 1, section on "Coroutines," pp. 20-21]{Beazley2009}.
+ An exceptions can be thrown inside a **coroutine**;
	however, **throw()** shall not be used to asynchronously control a
		**coroutine**
	\cite[Chapter 6, section on "Coroutines and yield Expressions," pp. 105]{Beazley2009}.
+ For a **yield** function with supplied values, it allows a coroutine to receive and
	produce/return values
	\cite[Chapter 6, section on "Coroutines and yield Expressions," pp. 105]{Beazley2009}.


Use generators and coroutines together in the following applications, where there
	is a frequent reception and production of values in sequences
	\cite[Chapter 6, section on "Using Generators and Coroutines," pp. 106]{Beazley2009}:
+ computer systems, including file systems
+ computer networking
+ distributed computing, which involves message queues and message passing
	for communication \cite[Chapter 6, section on "Using Generators and Coroutines," pp. 108]{Beazley2009}:
+ dataflow processing
	\cite[Chapter 6, section on "Using Generators and Coroutines," pp. 107]{Beazley2009}:
	- Organize programs "like inverted pipelines"
	- "Send values into a collection of linked coroutines"
+ concurrent computing
	\cite[Chapter 6, section on "Using Generators and Coroutines," pp. 108]{Beazley2009}:




Advantages of using generators and coroutines together are:
+ memory efficiency
	\cite[Chapter 6, section on "Using Generators and Coroutines," pp. 107]{Beazley2009}:
	- No usage of temporary lists or large data structures.



Notes about using recursive functions to carry out recursion:
+ The (current) maximum recursion depth is indicated by **sys.getrecursionlimit()**,
	which can be modified with **sys.setrecursionlimit()**
	\cite[Chapter 6, section on "Recursion," pp. 112]{Beazley2009}.
	- Setting the maximum recursion depth beyond "stack size limits enforced
		by the host operating system" has no effect.
+ "When the maximum recursion depth is exceeded, a **RuntimeError** exception
	is raised"
	\cite[Chapter 6, section on "Recursion," pp. 112]{Beazley2009}.
+ Unlike some (other) functional programming languages, "*Python* does not
	[carry out] tail-recursion optimization"
	\cite[Chapter 6, section on "Recursion," pp. 112]{Beazley2009}.
+ Avoid using recursion with:
	- decorators
		\cite[Chapter 6, section on "Functions as Objects and Closures," pp. 101]{Beazley2009}
		\cite[Chapter 6, section on "Recursion," pp. 113]{Beazley2009}
		* Avoid using recursion when decorators are used for system management,
			such as synchronization or locking
			\cite[Chapter 6, section on "Recursion," pp. 113]{Beazley2009}.
	- generator, or generator functions
		\cite[Chapter 6, section on "Recursion," pp. 112]{Beazley2009}.
	- coroutines
		\cite[Chapter 6, section on "Recursion," pp. 112]{Beazley2009}.













####	Functional Programming with *Python*

Functional programming features of *Python* include
	\cite[Chapter 6, pp. 93]{Beazley2009}:
+ scoping rules
	- When mutable variables are avoided, or forbidden, scoping rules enable
		developers to differentiate between global and local variables.
	- Use the **global** statement (e.g., **global *[variable-name]***) to allow
		local modifications of the global variable ***[variable-name]***
		\cite[Chapter 6, section on "Scoping Rules," pp. 96]{Beazley2009}.
	- We can use **global** statement anywhere in a function body, and
		repeatedly use such statements
		\cite[Chapter 6, section on "Scoping Rules," pp. 96-97]{Beazley2009}.
	- Declare variables to be **nonlocal** to use values of local variables
		defined in an outer function
		\cite[Chapter 6, section on "Scoping Rules," pp. 97]{Beazley2009};
		for functions nested more than two levels deep, such as nested
			functions embedded in nested functions, be careful of trying to
			access/modify local variables defined in the outermost function.
		**nonlocal** declarations use dynamic scoping (or dynamic scope), and
			"don't bind name[s] to local variables defined inside arbitrary
			functions further down on the current call-stack"
			\cite[Chapter 6, section on "Scoping Rules," pp. 97]{Beazley2009}.
+ closures
	- Since "functions are first-class objects in *Python*," the following (operations)
		are permissible \cite[Chapter 6, section on "Functions as Objects and Closures," pp. 98]{Beazley2009}:
		* pass a function as an argument to another function
		* place a function in a data structure
		* return "a function (as a result)"
	- To bind free variables (as bound variables), the function is treated as data
		that includes information of the surrounding environment of the function
		definition;
		this data is used to bind the free variables.  
		\cite[Chapter 6, section on "Functions as Objects and Closures," pp. 98]{Beazley2009}
	- \cite[Chapter 6, section on "Functions as Objects and Closures," pp. 99]{Beazley2009}
		mentions "**lazy or delayed evaluation**" \cite{WikipediaContributors2018c}.
	- A closure is a object resulting from packaging the code block associated
		with a function and its execution environment
		\cite[Chapter 6, section on "Functions as Objects and Closures," pp. 99]{Beazley2009}.
	- To exploit lazy evaluation, use closures and nested functions
		\cite[Chapter 6, section on "Functions as Objects and Closures," pp. 99]{Beazley2009}.
	- Use a closure to preserve the state across a series of function calls faster
		than code that do likewise with customized objects
		\cite[Chapter 6, section on "Functions as Objects and Closures," pp. 100]{Beazley2009}.
+ decorators
	- A decorator is a function that wraps another function (i.e., inner function) or
		class, so that the behavior of the wrapped function/class object is
		modified/improved
		\cite[Chapter 6, section on "Decorators," pp. 101]{Beazley2009}.
	- Denote a decrorator by prefixing the symbol "**@**" to a token
		\cite[Chapter 6, section on "Decorators," pp. 101]{Beazley2009}.
	- We can apply multiple decorators to a function/class definition, each of
		which is provided on a single line;
		these decorators must be listed just before the definition of functions
			or classes
		\cite[Chapter 6, section on "Decorators," pp. 101]{Beazley2009}.
	- A decorator for a class shall return a class object, instead of another type
		of object
		\cite[Chapter 6, section on "Decorators," pp. 102]{Beazley2009}.
	- There may be unexpected/strange interactions between decorators and
		aspects of functions, such as \cite[Chapter 6, section on "Decorators," pp. 102]{Beazley2009}:
		* recursion
		* documentation strings
			\cite[Chapter 6, section on "Decorators," pp. 102]{Beazley2009}
			\cite[Chapter 6, section on "Documentation Strings," pp. 113]{Beazley2009}:
			+ (Re)write decorators to enable propagation of the function name
				and documentation string
				\cite[Chapter 6, section on "Documentation Strings," pp. 114]{Beazley2009}
			+ Use the decorator (function) **wraps(*[function-name]*)** in the
				**functools** module to automatically copy the documentation
				string
				\cite[Chapter 6, section on "Documentation Strings," pp. 114]{Beazley2009}
		* function attributes
			+ A dictionary stores the (arbitrary) attributes of a function
				\cite[Chapter 6, section on "Function Attributes," pp. 114]{Beazley2009}.
			+ The dictionary is available as the **\_\_dict\_\_** attribute of the
				function
				\cite[Chapter 6, section on "Function Attributes," pp. 114]{Beazley2009}.
			+ These function attributes provide "parser generators and
				application frameworks" "additional information to function
				objects"
				\cite[Chapter 6, section on "Function Attributes," pp. 114]{Beazley2009}
			+ Use the decorator (function) **wraps(*[function-name]*)** in the
				**functools** module to automatically copy these function
				attributes
				\cite[Chapter 6, sections on "Documentation Strings" and "Function Attributes," pp. 114]{Beazley2009}
+ generators
	- See [Miscellaneous](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#miscellaneous).
+ coroutines






Operations in declarative programming tend to include operations such as
	\cite[Chapter 6, section on "Declarative Programming," pp. 110]{Beazley2009}:
+ **list comprehensions**
+ **generator expressions**


Miscellaneous notes on declarative programming:
+ The origin of [the features **list comprehensions** and **generator expressions**] is loosely derived from ideas in mathematical set theory
	\cite[Chapter 6, section on "Declarative Programming," pp. 110]{Beazley2009}.
+ Organize programs as a series of operations performed on all of the data
	concurrently, as opposed to procedural programs that iterate over data
	\cite[Chapter 6, section on "Declarative Programming," pp. 110]{Beazley2009}.
	- \cite[Chapter 6, section on "Declarative Programming," pp. 110-111]{Beazley2009}
		has a **good example about performing data processing on text file**.



Use **lambda** statements to define anonymous functions
	\cite[Chapter 6, section on "Declarative Programming," pp. 112]{Beazley2009};
	see [*Python* Functions](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#python-functions).








## *Python*-based Software Development

Try to use a *Python*ic approach to software development.
	This can facilitate the design and implementation of software (architectures)
		that can be refactored easily \cite[Chapter 1]{Alchin2010}.


Use a **list comprehension** to perform a conditional operation iteratively on
	a collection of elements \cite[Chapter 2, pp. 35]{Alchin2010}
	\cite[Chapter 6, section on "List Comprehensions," pp. 108]{Beazley2009}.
+ A **list comprehension** can also perform an (unconditional) operation on
	a collection of elements
	\cite[Chapter 6, section on "List Comprehensions," pp. 109]{Beazley2009}.
+ When using tuples with **list comprehensions**, ensure that parentheses
	(or round brackets) are used to represent those tuples
	\cite[Chapter 6, section on "List Comprehensions," pp. 109]{Beazley2009}.
+ Use square brackets for **list comprehensions**
	\cite[Chapter 6, section on "Generator Expressions," pp. 109]{Beazley2009}.
+ **Create a list with the resulting data**; or create a list with the resultant
	sequence of data
	\cite[Chapter 6, section on "Generator Expressions," pp. 110]{Beazley2009}.
+ Examples of *Python* list comprehension \cite{ParewaLabsStaff20XYa}, with comparisons to:
	- lambda functions (or anonymous function, function literal, lambda abstraction, or lambda expression) \cite{WikipediaContributors2017u}
		* Additional resources for lambda functions:
			+ https://www.w3schools.com/python/python_lambda.asp
				- \cite[from Python Tutorial: Python Lambda]{RefsnesDataStaff2017}
			+ https://realpython.com/python-lambda/
				- \cite{Burgaud20XY}
			+ https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
				- \cite{Lenka2018}
	- "for" loops
		* Has an example of converting nested "for" loops into a list
			comprehension.
+ Generic form:
	- "\[expression for item in list\]" \cite{ParewaLabsStaff20XYa}
	- "\[expression for item in list Optional_Conditional_Statement\]" \cite{ParewaLabsStaff20XYa}
		* The "Optional_Conditional_Statement" optional conditional statement
			can include: 
			+ an "if" statement \cite{PythonForBeginnersContributors2020}
			+ a nested "if" statement
			+ an "if-else" statement
+ Suggestions:
	- "List comprehension is an elegant way to define and create lists based on existing lists" \cite{ParewaLabsStaff20XYa}.
	- "List comprehension is generally more compact and faster than normal functions and loops for creating list" \cite{ParewaLabsStaff20XYa}.
	- "avoid writing very long list comprehensions in one line to ensure that code is user-friendly" \cite{ParewaLabsStaff20XYa}.
	- "every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension" \cite{ParewaLabsStaff20XYa}.







Similarly, a **generator expression** implicitly creates an iterable object to
	iterate over a list/collection of elements and perform an operation on each
	enumerated item/element \cite[Chapter 2, pp. 35-37]{Alchin2010};
+ A generator expression needs to be surrounded by parentheses, which can
	belong to a function (or an operation) performed on the collection of objects
	\cite[Chapter 2, pp. 35-37]{Alchin2010}.
+ It behaves like a **list comprehension**, but "iteratively produces the result"
	\cite[Chapter 6, section on "Generator Expressions," pp. 109]{Beazley2009}.
+ Use parentheses for **generator expression**s
	\cite[Chapter 6, section on "Generator Expressions," pp. 109]{Beazley2009}.
+ **It creates a generator object to iteratively prodice values on demand**,
	so that it does not have to create a list or immediately evaluate the expression
	inside the parentheses
	\cite[Chapter 6, section on "Generator Expressions," pp. 110]{Beazley2009}.
	- This can yield better performance and memory usage than **list
		comprehension**
		\cite[Chapter 6, section on "Generator Expressions," pp. 110]{Beazley2009}.
	- Use **generator expression**s for efficient file processing
		\cite[Chapter 6, section on "Generator Expressions," pp. 110]{Beazley2009}.
	- Does not create a sequence-like object that can be indexed or operated
		like a list;
		"however, a generator expression can be converted into a list using the
			built-in **list()** function"
		\cite[Chapter 6, section on "Generator Expressions," pp. 110]{Beazley2009}.



Likewise, a **set comprehension** performs the built-in set() function on a
	collection of unsorted elements \cite[Chapter 2, pp. 37]{Alchin2010}.

Comparably, a **dictionary comprehension** is an unordered linear ("1-D")
	collection of (key,value) pairs, such that each pair is donoted by *key: value*
	\cite[Chapter 2, pp. 37-38]{Alchin2010}.

Compare this to **ordered dictionaries** \cite[Chapter 2, pp. 38]{Alchin2010}.


+ Try to follow the *Don't Repeat Yourself* principle during software development
	\cite[Chapter 4, pp. 120]{Alchin2010}.



+ \cite[Appendices A and B]{Langtangen2006}.
+ \cite[Appendices A and B]{Langtangen2009}.
+ \cite[Chapter 21]{Lutz2011}.
	- No information on object-oriented programming.
+ \cite[Chapter 15]{Lutz2013}.
+ \cite{Younker2008}.
	- No information on object-oriented programming.
































### *Python*ic Coding Style







\cite{vanRossum2013} describes *Python*ic software development, including
	how to program in a *Python*ic coding style.
	Note that the term "coding style" can be used interchangeably with "coding
		scheme", "coding standard", "coding style guide",
		and "programming style".






Resources for adopting a *Python*ic approach to software development:
+ \cite[Appendix B, \SB.3.2, pp. 706--710]{Langtangen2009}
+ \cite[Chapter 41]{Lutz2013}
	- The core values/ideals of the *Python*ic approach to software development are
		\cite[Chapter 41, section on "The Python Paradox," pp. 1409]{Lutz2013}:
		* explicitness
		* simplicity
		* lack of redundancy
	- Helpful concepts to acquire as part of my "required knowledge base"
		\cite[Chapter 41, subsection on "On `Optional' Language Features," pp. 1409]{Lutz2013}:
		* generators
		* decorators
		* slots
		* properties
		* descriptors
		* metaclasses
		* context managers
		* closures
		* super
		* namespace packages
		* Unicode
		* function annotations
		* relative imports
		* keyword-only arguments
		* class methods
		* static methods
		* (applications of) comprehensions
		* (applications of) operator overloading
	- "A sampling of redundancy (in functionality and toolbox size) and feature explosion in Python" \cite[Chapter 41, subsection on "Against Disquieting Improvements," pp. 1411, Table 41-1]{Lutz2013}.
	- There exists trade-offs between complexity and power
		\cite[Chapter 41, subsection on "Complexity Versus Power," pp. 1412]{Lutz2013},
		and between simplicity and elitism
		\cite[Chapter 41, subsection on "Simplicity Versus Elitism," pp. 1412-1413]{Lutz2013}.



















Table about *Python*'s redundant features and feature explosion
	\cite[Chapter 41, subsection on "Against Disquieting Improvements," pp. 1411, Table 41-1]{Lutz2013}

| **Category**				| **Specifics**							|
| ------------------------------------ | ---------------------------------------------------- |
| 3 major paradigms			| Procedural, functional, object-oriented		|
| 2 incompatible lines			| 2.X and 3.X, with new-style classes in both	|
| 3 string formatting tools		| % expression, str.format, string.Template		|
| 4 attribute accessor tools		| **\_\_getattr\_\_**, **\_\_getattribute\_\_**, properties, descriptors	|
| 2 finalization statements		| try/finally, with							|
| 4 varieties of comprehension	| List, generator, set, dictionary				|
| 3 class augmentation tools		| Function calls, decorators, metaclasses		|
| 4 kinds of methods			| Instance, static, class, metaclass			|
| 2 attribute storage systems	| Dictionaries, slots						|
| 4 flavors of imports			| Module, package, package relative, namespace package	|
| 2 superclass dispatch protocols	| Direct calls, super + MRO				|
| 5 assignment statement forms	| Basic, multiname, augmented, sequence, starred	|
| 2 types of functions			| Normal, generator						|
| 5 function argument forms		| Basic, name=value, \*pargs, \*\*kargs, keyword-only	|
| 2 class behavior sources		| Superclasses, metaclasses				|
| 4 state retention options		| Classes, closures, function attributes, mutables	|
| 2 class models				| Classic + new-style in 2.X, mandated new-style in 3.X	|
| 2 Unicode models			| Optional in 2.X, mandated in 3.X			|
| 2 PyDoc modes				| GUI client, required all-browser in recent 3.X	|
| 2 byte code storage schemes	| Original, **\_\_pycache\_\_** only in recent 3.X	|
































Note that \cite{Franca2014} mentions that modern *C++1X*, such as *C++11*,
	*C++14*, and *C++17*, is becoming more like *Python*;
	that is, modern *C++1X* has become *Python*ic.   





### *Python* Documentation


Use documentation generators to produce documentation for the [software
	(library) \cite{WikipediaContributors2018b}](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#python-documentation),
	from the comments in the code.


Use the **\_\_doc\_\_** attribute of modules, classes, and functions to access
	docstrings \cite[Chapter 8, pp. 209]{Alchin2010}.






Place documentation strings, or docstrings, at the start of each function, class,
	and package
	\cite[Chapter 6, section on "Documentation Strings," pp. 113]{Beazley2009}.




Guidelines on what to include in docstrings \cite[Chapter 8, pp. 209]{Alchin2010}:
+ "Describe the function[/method]"
+ "Explain the arguments"
+ "Don't forget the return value"
+ "Include any expected exceptions" \cite[Chapter 8, pp. 210]{Alchin2010}



Endeavor to provide additional documentation for the following
	\cite[Chapter 8, pp. 210]{Alchin2010}:
+ Information about the installation, configuration, and execution of the software.
+ Tutorials on how to use the software.
+ "Reference documents"



\cite[Chapter 2, pp. 16]{Hall2009b} suggests the following *Python* docstring
	to provide built-in documentation for the *Python* software:
+ Usage: [E.g., *How to execute/run this program?*]
	\cite[Chapter 9, pp. 201]{Hall2009b}
+ Options: [E.g., Input *options/flags that are supported by this program.*]
+ Problem/Purpose: [E.g., *What does the **Python** software do?*]
+ Target Users: [E.g., *People who want to perform data analytics or
	other operations on their **BibTeX** databases.*]
+ Target Systems: [E.g., *UNIX-like operating systems.*]
	\cite[Chapter 9, pp. 201]{Hall2009b}
+ Interface: [E.g., *Command-line.*] \cite[Chapter 9, pp. 201]{Hall2009b}
+ Functional Requirements: \cite[Chapter 9, pp. 202]{Hall2009b}
	- [E.g., *Input **BibTeX** file.*]
	- [E.g., *Perform data processing on the **BibTeX** file.*]
	- [E.g., *Perform statistical analysis, or data analytics operations, on the **BibTeX**
		file.*]
	- [E.g., *Validate the integrity of the **BibTeX** file.*]
+ Maintainer(s): [E.g., *Zhiyang Ong*]
+ Expected Results: [E.g., *Perform (specific) tasks to address the
	(specified) problem statement.*]
+ Testing methods/modules: [E.g., *List of methods and modules used to
	test software.*] \cite[Chapter 9, pp. 202]{Hall2009b}
+ Test values: [E.g., *Values used to test software.*]
+ Limitations: [E.g., *Limitations of the software.*] \cite[Chapter 9, pp. 202]{Hall2009b}
+ \_\_version\_\_ = 0.1 \cite[Chapter 9, pp. 202]{Hall2009b}
+ \_\status\_\_ = "Prototype" \cite[Chapter 9, pp. 202]{Hall2009b}
+ \_\_date\_\_ = "March 19, 2018" \cite[Chapter 9, pp. 202]{Hall2009b}
+ \_\maintainer\_\_ = "Zhiyang Ong" \cite[Chapter 9, pp. 202]{Hall2009b}
+ \_\credits\_\_ = "Thanks to everyone."






Produce documentation using documentation generators, such as:
+ *Javadoc*
+ *Doxygen*
+ *Sphinx* \cite{WikipediaContributors2018b}
+ *pydoc*

The command **help(*[Python module]*)** enables a user to read documentation
	about the *[Python module]* that is automatically produced by documentation
	generators, such as *pydoc* \cite[Chapter 11, pp. 248]{Hall2009b}.
	This documentation is extracted from the comments in the *[Python module]*
		\cite[Chapter 11, pp. 248]{Hall2009b}.








### Input/Output Operations

\cite[Chapter 2, pp. 23]{Alchin2010} shows how to log errors that have been
	raised during input/output operations.
	They can be recorded/stored by the *logging* module from *The Python
		Standard Library* \cite{DrakeJr2016e,DrakeJr2016b}



Resources for passing command-line arguments
+ \cite[Chapter 8, \S8.1.1, pp. 319-322]{Langtangen2009}
+ Louie Dinh, "Command Line Parser", from Python Practice Projects,
	Vancouver, British Columbia, Canada, no date. 
	Available from Python Practice Projects at: http://pythonpracticeprojects.com/command-line-parser.html;
		February 7, 2020 was the last accessed date.


For file input/output objects/streams:
+ From \cite{Bader2018a}, ["Working With File I/O in Python" blog post](https://dbader.org/blog/python-file-io):
	- to open and close an input file object/stream.
		* Closing an output file object/stream ensures that pending or
			buffered data would be written the output file.
		* Releases resources allocated to the file objects/streams,
			allows resource management to be more efficient, and
			helps the computer programs or software to deal with
			space or memory constraints.













###	Modules in *The Python Standard Library*

The following modules in *The Python Standard Library* \cite{DrakeJr2016e,DrakeJr2016b}
	can be useful in developing *Python* software .
+ *itertools*
	Enables a set/chain of functions to be performed on each element in a
		collection \cite[Chapter 2, pp. 38]{Alchin2010}.
	- The *zip()* function enables multiple iterables to be combined
		together \cite[Chapter 2, pp. 38]{Alchin2010};
		an iterable is a collection "object" that can generate an iterator to
			iterate over each element in the collection \cite[Chapter 5, pp. 155]{Alchin2010}.
+ \cite[Chapter 10, pp. 215-253]{Hetland2005}.
	- **difflib** module \cite[pp. 251]{Hetland2005}
		* Determine how similar two sequences are.
		* Choose the sequence from a list of sequences that is most
			similar to a given sequence.
	- **csv** module enables file read/write (or input/output) operations
		regarding tabular data stored in the comma-separated values (CSV)
		format \cite[pp. 251]{Hetland2005}.



####	Built-in Collections

From \cite[Chapter 2, pp. 39]{Alchin2010}
+ lists \cite[\S5.1]{Brandl2017a}
	- [A list can contain elements that are objects of multiple classes,
		which are not of the basic numeric data types](https://github.com/eda-ricercatore/python-sandbox/blob/main/numbers/very_abnormal_operations_with_numbers.py).
		* Note that this can cause TypeErrors to occur when I perform
			arithmetic (and logic) operations.
			+ This requires methods (or functions) that use/implement
				arithmetic (and logic) operations, which can only be
				performed on numbers, to check for the class/type of
				objects in the list before enumerating the list to perform
				these arithmetic (and logic) operations.
	- [Examples of: embedded lists, or a list of a single list of a single list...; of enumerating a list and the index of each enumerated object; and of enumerating multiple lists with the index of the currently/concurrently enumerated objects](https://github.com/eda-ricercatore/python-sandbox/blob/main/i-data-structures/performing_operations_on_lists.py)
		* includes an example on [list comprehension](https://en.wikipedia.org/wiki/List_comprehension), which is exploited in functional programming (for monad comprehension, set comprehension, dictionary comprehension, parallel list comprehension)
		* "List comprehension results in faster operations than explicit *for* loops" \cite{ParewaLabsStaff20XYa}.
		* [Using the *range(start,end,incremental_step)* function to create a list ranging from *start* to *end*, with increments of *incremental_step*, and using it to create lists of powers of 2 (e.g., 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, ...)](https://github.com/eda-ricercatore/python-sandbox/blob/main/i-data-structures/range_list_enumeration.py)
			- Also, uses a range of floating-point numbers with increments that are floating-point numbers, and demonstrates different solutions for doing this.
	- From the [subsubsection on *Python* Functions (section *Python* Classes)](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#python-functions), check out the comparisons between the following:
		* list comprehensions versus (loops and *Python* Functions) \cite{ParewaLabsStaff20XYa}.
		* list comprehensions versus (maps and filters) \cite[Chapter 6, pp. 135]{Hetland2005}.
+ tuples (and lists, sequences, and ranges) \cite[\S5.3]{Brandl2017a}
	- Tuples are immutable \cite[Chapter 1, section on "Tuples", pp. 14]{Beazley2009}.
		* [Examples of trying to add an element to a tuple and of trying to remove an element from a tuple. Errors for trying to do these were caught.](https://github.com/eda-ricercatore/python-sandbox/blob/main/i-data-structures/tuple_operations.py)
	- From \cite{ParewaLabsStaff20XYc}:
		* Since tuples are immutable,  it can be faster to enumerate a
			tuple than a list.
		* Elements of an tuple are immutable; this ensure that they
			remain read-only (or write-protected).
		* Try to use tuples for heterogeneous (multiple) data types, and
			lists for homogeneous (only one) data type.
	- [Can store objects from different classes](https://github.com/eda-ricercatore/python-sandbox/blob/main/i-data-structures/tuple_operations.py)
	- [A tuple of a single tuple cannot be defined/represented within
		two sets of round brackets `((an-object))`.](https://github.com/eda-ricercatore/python-sandbox/blob/main/i-data-structures/tuple_operations.py)
		* Such tuples of a single tuple have to defined/represented
			within two sets of round brackets, with a comma appended
			to the object `((an-object,),)` \cite{Krishna2020,Uppalapati20XY}.
	- [Examples of enumerating a tuple with the index of each object in the tuple, and enumerating multiple tuples (of equal lengths) with the index of the currently/concurrently enumerated objects in the tuples](https://github.com/eda-ricercatore/python-sandbox/blob/main/i-data-structures/tuple_operations.py)
+ sets \cite[Chapter 2, pp. 39]{Alchin2010} \cite[\S5.4]{Brandl2017a}
	- Disallow duplicates
	- The standard constructor accepts the following as inputs:
		* sequences
		* lists
		* tuples
		* dictionary keys
		* custom iterable objects
	- Unordered data structure that is only concerned about membership.
	- Has the following operations \cite[Chapter 2, pp. 40-43]{Alchin2010}:
		* *{element}* in *{set}*
		* *{set}*.add(*{element}*)
		* *{set}*.update(*{element}*)
		* *{set}*.remove(*{element}*)
		* *{set}*.discard(*{element}*)
		* *{set}*.pop(*{element}*)
		* *{set}*.clear(*{element}*)
		* OR operation, disjunction: *{set 1} | {set 2}*, *{set 1}.union({set 2})*
		* AND operation, disjunction: *{set 1} & {set 2}*, *{set 1}.intersection({set 2})*
		* difference operation, *{set 1} - {set 2}*, *{set 1}.difference({set 2})*
		* symmetric difference operation, *{set 1} ^ {set 2}*, *{set 1}.symmetric_difference({set 2})*
			+ Either in {set 1} or {set 2}, but not both sets
				\cite[Chapter 1, section on "Sets," pp. 15]{Beazley2009}
				\cite[Chapter 3, subsection on "Set Types," Table 3.7, pp. 46]{Beazley2009}.
		* *{set 1}*.issubset(*{set 2}*)
		* *{set 1}*.issuperset(*{set 2}*)
		* ({set 1} - {set 2}); Or, not ({set 1} - {set 2})
	- Use *set()* to represent the empty set, so that it can be differentiated from
		an empty dictionary *{}* \cite[Chapter 2, pp. 41]{Alchin2010}.
+ named tuples \cite[Chapter 2, pp. 43]{Alchin2010}
	- The *factory* function, namedtuple(), from the *collections* module in
		*The Python Standard Library* returns a new class that is
		customized for a given set of named fields, rather than a "named tuple"
		object with named fields.
	- For functions that return multiple values, named tuples can be used to
		return these sets of values.
		They allow the returned values to be accessible by named fields, just
			like dictionaries.
+ dictionaries \cite[Chapter 2, pp. 44]{Alchin2010} \cite[\S5.5]{Brandl2017a}
	- unordered data structure
+ ordered dictionaries \cite[Chapter 2, pp. 44]{Alchin2010}
	- ordered data structure
	- Has all the features of a dictionary, while having a reliable ordering of keys
		for its *(key,value)* pairs.
	- From [my sample code](https://github.com/eda-ricercatore/python-sandbox/blob/main/i-data-structures/ordered_dict_color_enumeration.py),
		instantiating an ordered dictionary, OrderedDict, with a dictionary
		will not create an ordered dictionary in which the keys are ordered;
		 however, when instantiated with a list of tuples, it does order its
		 	elements when the *sort()* operation is performed on the input
		 	argument;
		a dictionary passed to the ordered dictionary, OrderedDict, can be
			sorted using lambda expressions based on keys, values, and
			length of keys.
+ dictionaries with defaults \cite[Chapter 2, pp. 44-45]{Alchin2010}
	- A dictionary with defaults is assumed to have (optimal) default values for
		keys that cannot be found in the mapping.
	- Lambda functions can be used to create and process dictionaries with
		defaults.








###	Software Testing, Verification, and Validation

*Python* software testing, verification, and validation concepts and methods:
+ Unit testing
	- \cite[Chapter 9, pp. 217]{Alchin2010}
	- \cite[Chapter 16, pp. 341]{Hetland2005}
	- \cite[Appendix B, \SB.4.6, pp. 726--728]{Langtangen2009}
	- \cite[Chapter 9]{Pilgrim2009}:
		* Potential/possible benefits of unit testing \cite[Chapter 9, pp. 132]{Pilgrim2009}
			+ It encourages developers to detail software requirements via
				unit tests, and other aspects of their test suite for automated
				regression testing.
			+ It encourages developers to write code that is tailored to the unit
				tests, and other aspects of their test suite for automated
				regression testing.
			+ It can be used to ensure that software refactoring does not
				cause unit tests, and other aspects of their test suite for
				automated regression testing, to fail.
			+ To validate the work of a developer by demonstarting that all the
				unit tests, and other aspects of their test suite for
				automated regression testing, pass.
			+ For team-developed software projects, use the unit tests by each
				individual to check and validate that each software developer's
				contribution or modification to the code base does not cause
				existing unit tests to fail.
		* "Unit tests can give you the confidence to do large-scale refactoring"
			\cite[Chapter 10, section on "Refactoring,"pp. 166]{Pilgrim2009}.
		* "Comprehensive unit testing means never having to rely on a programmer who says, `Trust me.' "
			\cite[Chapter 10, section on "Handling Changing Requirements,"pp. 162]{Pilgrim2009}.
		* Use unit testing to reduce software maintenance cost and improve
			adaptability in software project management
			\cite[Chapter 10, section on "Refactoring,"pp. 166]{Pilgrim2009}.
+ Test-driven development \cite[Chapter 9, pp. 217]{Alchin2010}
	\cite[Chapter 16, pp. 341-342]{Hetland2005}
	- Test-driven development helps us achieve good/decent software test
		coverage \cite[Chapter 16, pp. 343]{Hetland2005}.
	- An outline of test-driven development is described in
		\cite[Chapter 16, pp. 344]{Hetland2005}.
+ Doctests
	- \cite[Chapter 9, pp. 218-221]{Alchin2010}
	- \cite[Chapter 1, pp. 5--6]{Pilgrim2009}
	- Facilitates validation of software documentation and supports unit testing
		\cite[Chapter 16, pp. 344]{Hetland2005}.
	- Use docstrings to document software requirements for each method,
		function, class, module, and package
		\cite[Chapter 16, pp. 344-345]{Hetland2005}.
	- The **doctest.testmod(** *[module name]* **)** function checks if the
		docstrings in the *[module name]* module contain examples of using
		functions or methods in the module, and if these examples (for
		specific sets of inputs and outputs) can be replicated, reproduced, and
		repeated \cite[Chapter 16, pp. 345]{Hetland2005}.
	- \cite[Chapter 11, section on "Documentation Strings and the doctest Module," pp. 181-183]{Beazley2009}
+ **unittest** module \cite[Chapter 9, pp. 221-230]{Alchin2010}, which is "a
	generic testing framework" \cite[Chapter 16, pp. 344]{Hetland2005} (or
	test framework) \cite[Chapter 16, pp. 347]{Hetland2005}.
	- A **test fixture** are a pair of methods, **startUp()** and **tearDown()**,
		which are "executed before and after each test method" (or method in
		the test suite) "to provide common initialization and cleanup code for
		all the tests" \cite[Chapter 16, pp. 347]{Hetland2005}.
	- \cite[Chapter 11, section on "Unit Testing and the unittest Module," pp. 183-186]{Beazley2009}
		* Use methods from **unittest.TestCase**, where **t** is an instance of
			**unittest.TestCase** \cite[Chapter 11, section on "Unit Testing and the unittest Module," pp. 184-185]{Beazley2009}:
			+ t.setUp()
			+ t.tearDown()
			+ t.assert_(expr [, msg])
			+ t.assertEqual(x, y [,msg])
			+ t.assertNotEqual(x, y [, msg])
			+ t.assertAlmostEqual(x, y [, places [, msg]])
			+ t.assertNotAlmostEqual(x, y, [, places [, msg]])
+ Use the *Python* debugger **pdb** to step through the code
	\cite[Chapter 11, section on "The Python Debugger and the pdb Module," pp. 186-190]{Beazley2009}.
+ automated regression testing
	\cite[Appendix B, \SB.4.1-B.4.4, pp. 711--724]{Langtangen2009}
	- It facilitates software development, and **software maintenance** (for
		fixing software bugs, refactoring, performance improvement, and to add
		features) \cite[Chapter 16, pp. 343]{Hetland2005}.
	- It enables software developers to find and fix software bugs earlier in
		the software development process, and avoid an **unmanageable
		accumulation** of such software bugs.
		\cite[Chapter 16, pp. 343]{Hetland2005}.
	- Software development is an **organic process**, which may involve making
		multiple changes to the software architecture, algorithms, and data
		structures \cite[Chapter 16, pp. 343]{Hetland2005};
		automated regression testing can help us refactor our software to
			improve **fault isolation** by decoupling modules and decreasing
			inter-module dependencies (especially interdependencies)
			\cite[Chapter 16, pp. 343]{Hetland2005};
		**refactor the software** to **keep software changes/modifications
			localized**, so that we do not have to extensively rewrite most of
			the software each time we make modifications to the software
			\cite[Chapter 16, pp. 343]{Hetland2005}.
	- A sufficiently **decent software test coverage** gives us confidence that
		when we make modifications to the software (e.g., **bug fixing** or
		**software refactoring**), we can quickly determine the impact of these
		modifications on other components of the software
		\cite[Chapter 16, pp. 343]{Hetland2005}.
	- Automated regression testing allows us to know which component(s) of our
		software is(/are) working /failing \cite[Chapter 16, pp. 343]{Hetland2005}.
+ Advice for software testing, verification, and validation:
	- Each build of the software (or commit pushed to a software repository)
		should satisfy all existing test cases
		\cite[Chapter 16, pp. 344]{Hetland2005};
		bug fixes, software refactoring, and software maintenance should not
			result in the failure of test cases for unmodified components of the
			software.
+ To performing logging, choose a non-empty subset of the following:
	- trace/print statements, printed to standard output/error.
	- trace/print statements, output to a text file
		\cite[Chapter 19, pp. 385-386]{Hetland2005}:
		* Open and close file at the beginning and the end of the *Python*
			program.
		* Open and close file at the beginning and the end of each (set of) trace
			statement in the *Python* program.
	- trace/print statements, via the **logging** module \cite[Chapter 19, pp. 386]{Hetland2005}
		of *The Python Standard Library* \cite{DrakeJr2016e,DrakeJr2016b}.
		* Configure the **logging** module to customize the log entries/files
			\cite[Chapter 19, pp. 387]{Hetland2005}







Other types of software testing:
+ functional testing \cite[Chapter 10, section on "Refactoring,"pp. 166]{Pilgrim2009}
+ integration testing \cite[Chapter 10, section on "Refactoring,"pp. 166]{Pilgrim2009}
+ user acceptance testing \cite[Chapter 10, section on "Refactoring,"pp. 166]{Pilgrim2009}








*Python* software analysis and verification concepts and methods:
+ static (code) analysis \cite[Chapter 16, pp. 341, 349-352]{Hetland2005}:
	- *PyChecker*
	- *PyLint*
+ dynamic analysis
+ taint analysis
+ formal verification
+ memory debugging
+ software profiling \cite[Chapter 16, pp. 341, 349, 353-354]{Hetland2005}:
	- *profile* and *cProfile* \cite[Chapter 11, section on "Program Profiling," pp. 190-191]{Beazley2009}:
		* *cProfile* is faster than *profile* \cite[Chapter 11, section on "Program Profiling," pp. 190]{Beazley2009}
	- *hotshot*
	- *timeit*
+ software linting \cite[Chapter 16, pp. 349]{Hetland2005}





Software testing, verification, and validation should be performed with respect to
	satisfying the requirements and specifications of the software (i.e., software
	requirements specification) \cite[Chapter 16, pp. 342]{Hetland2005}.




Use executable-requirement specification \cite{Bailey2005} to reduce or augment
	non-executable requirements specification
	\cite[Chapter 16, pp. 342]{Hetland2005}.




Types/categories of requirements specification
	\cite[Chapter 16, pp. 342]{Hetland2005}:
+ functional requirements
+ non-functional requirements
	- client satisfaction



Resources for software testing, verification, and validation:
+ \cite[From Development Tools section, TestSoftware subsection, PythonTestingToolsTaxonomy subsubsection]{PythonWikiContributors2018}
	- [PythonTestingToolsTaxonomy subsubsection](https://wiki.python.org/moin/PythonTestingToolsTaxonomy)  
	- \cite[From Writing Great Python Code section, Testing Your Code subsection]{Reitz2016a}
		* [Testing Your Code subsection](https://docs.python-guide.org/writing/tests/)
+ Vijaykumar Shinde, "Top 6 BEST Python Testing Frameworks [Updated 2020 List]", SoftwareTestingHelp, Kharadi, Pune, Maharashtra, India, December 28, 2019.
	Available from SoftwareTestingHelp at: https://www.softwaretestinghelp.com/python-testing-frameworks/;
		February 7, 2020 was the last accessed date.
+ Anthony Shaw, "Getting Started With Testing in Python", from
	Real Python Tutorials, dbader software co, Vancouver, British Columbia,
	Canada, 2018.
	Available from Real Python Tutorials at: https://realpython.com/python-testing/;
		February 7, 2020 was the last accessed date.










####	Software Tuning and Performance Optimization

Use timing measurements to determine the time taken for each different parts of
	the program
	\cite[Chapter 11, subsection on "Making Timing Measurements," pp. 191]{Beazley2009}.
+ Resources on timng measurements:
	- \cite[Chapter 21]{Lutz2013}






Use memory measurements to determine the amount of memory usage (i.e.,
	memory footprint) in my program
	\cite[Chapter 11, subsection on "Making Memory Measurements," pp. 192-193]{Beazley2009}








Suggestions on software/program tuning strategies and performance optimization:
+ \cite[Chapter 11, subsection on "Tuning Strategies," pp. 194-197]{Beazley2009}





####	Software Debugging

Use **assert** statements to check if invariants \cite{Lee2017a,Lee2015b,Lee2014a,Backhouse2011,Lee2011,Zeller2009,Baier2008,Tucker2007,Hailperin1999,Manna1992},
	such as preconditions, assertions, and postconditions \cite{Pierce2017,Laplante2014,Dale2012,Kourie2012,Kundu2011,Zeller2009,Tucker2007,Baldwin2004,Huth2004,Monin2003,Hailperin1999},
	are true \cite[Appendix B, pp. 566]{Hetland2005}
	\cite[Chapter 5, section on "Assertions and \_\_debug\_\_," pp. 91]{Beazley2009}.

The format for an assert statement is \cite[Appendix B, pp. 566]{Hetland2005}:
	**assert [** *boolean condition* **]**, **[Error message to notify user that
		the asssertion failed]**.

The *\_\_debug\_\_* variable, which is set to **True** by default, allows *Python*
	developers in the to test their program in the debug mode
	\cite[Chapter 5, section on "Assertions and \_\_debug\_\_," pp. 91]{Beazley2009}.

*Python* programs can be executed in the non-debugging mode by specifying
	the **-O** option for the *Python* interpreter so that it would execute the
	*Python* program in optimized mode (and avoid executing code associated
	with **if \_\_debug\_\_** statements);
	that is, use **if \_\_debug\_\_** statements) for non-essential testing and
		validation of *Python* programs, so that the execution of (these)
		*Python* programs can be optimized to run faster without such checks
	\cite[Chapter 5, section on "Assertions and \_\_debug\_\_," pp. 91]{Beazley2009}.

\cite[Chapter 8, section on "Module Loading and Compilation," pp. 148]{Beazley2009}
	has more information about compiling modules with the **-O** option
	(removes assertions, line numbers, and other debugging information), and
	the **-OO** option (i.e., **-O** option with removal of docstrings).


Resources about software debugging:
+ Guidelines for software development and debugging
	\cite[Appendix F, \F.2.1, pp. 738-740]{Langtangen2012}









###	Industrial-Strength High-Performance Computing

To develop *Python* software for industrial-strength high-performance computing,
	use this method to improve its performance (i.e., execution time)
	\cite[Chapter 17, pp. 357]{Hetland2005}
	\cite[Chapter 5, \S5.1.1, pp. 190]{Langtangen2009}
	\cite[Appendix G, pp. 753]{Langtangen2012}:
+ Develop a modular prototype for the software only in *Python*.
	- "Encapsulate potential bottlenecks"
		\cite[Chapter 17, pp. 357-358, 370]{Hetland2005}.
+ Carry out performance profiling (as opposed to memory profiling) on the
	*Python* prototype, and determine its performance bottlenecks.
+ Implement components/modules of the *Python* prototype in a programming
	language with better run-time performance, such as *C*, *C++*, *FORTRAN*,
	or *Java*.
+ The result is a mixed-language software based on *Python* and at least one
	other software programming language, which should have a faster
	performance than the *Python* prototype;
	this is because the performance-critical components/modules are developed
		in programming languages with better run-time performance.
+ If the reimplemented performance-critical components/modules have a faster
	run-time performance than the initial *Python*-based, performance-critical
	components/modules, but the resultant, integrated, mixed-language software
	has a slower run-time performance, the integration of the mixed-language
	software is the cause for the performance degradation.
	- To resolve the problem, try another method for developing mixed-language
		software with *Python* components.
















###	Developing Mixed-Language Software


Developing mixed-language software
	\cite[Chapter 17, pp. 357-358]{Hetland2005}:
+ Extension philosophy \cite[Chapter 17, pp. 370]{Hetland2005}:
	- To use existing (legacy) code (e.g., in *C*, *C++*, *FORTRAN*, ...), which are
		not developed in *Python*
	- To speed up bottlenecks; see [Industrial-Strength High-Performance Computing](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#industrial-strength-high-performance-computing).
+ Developing wrappers around existing legacy code to add *Python* extension
	library \cite[Chapter 17, pp. 358]{Hetland2005}:
	- Craft a custom wrapper
		* Develop *C* programs that uses the *Python C* API \cite{DrakeJr2018a}
			directly \cite[Chapter 17, pp. 365]{Hetland2005}.
	- Use an existing wrapper tool, such as:
		* *SWIG*
		* *CPython*, for *C* programs
			+ I can use *CPython* in my *C* programs
				\cite[Chapter 17, pp. 360]{Hetland2005}.
		* *Jython*, for *Java* programs (can access modules and classes)
			+ Use **jythonc** to compile my *Python* classes into *Java*
				classes, which can be merged with *Java* programs
				\cite[Chapter 17, pp. 359]{Hetland2005}.
			+ I can use *Jython* in my *Java* programs
				\cite[Chapter 17, pp. 360]{Hetland2005}.
		* *IronPython*, for programs developed for the *.Net* platform (can
			access modules and classes)
			+ I can use *IronPython* in my programs for the *.Net* platform
				\cite[Chapter 17, pp. 360]{Hetland2005}.
		* As aforementioned, *CPython*, *Jython*, and *IronPython* enable
			extending [*C* | *Java* | *programming languages for the .Net platform*]
				programs with *Python* code
				\cite[Chapter 17, pp. 360]{Hetland2005}.
		* To extend *Python* programs with *CPython*, *Jython*, or *IronPython*,
			adhere to the requirements of their API (i.e., API of *CPython*,
			*Jython*, or *IronPython*) when developing extensions in
			[*C* | *Java* | *programming languages for the .Net platform*]
			\cite[Chapter 17, pp. 360]{Hetland2005}.
+ Use *Psyco* as a "specialized just-in-time compiler for *Python*" to speed up
	run-time performance of the *Python* programs
	\cite[Chapter 17, pp. 360]{Hetland2005}.
+ Use **[Numba](http://numba.pydata.org/)** \cite{NumbaContributors2018} as a
	high-performance Python compiler. It is a NumPy-aware, LLVM-based dynamic compiler \cite{NumbaContributors2018a}.
+ Use *Pyrex*, which is a "dialect" of *Python*, to develop extensions for *Python*
	programs and to compile *Pyrex* programs
	\cite[Chapter 17, pp. 361]{Hetland2005}.
+ Use *Weave* (from *SciPy* distributions) to integrate *C*/*C++* code (as strings)
	into *Python* programs \cite[Chapter 17, pp. 361]{Hetland2005};
	this can speed up some mathematical computations
		\cite[Chapter 17, pp. 361]{Hetland2005}.
+ Use *NumPy* with *Weave* (from *SciPy* distributions), or with *Pyrex*, to speed
	up computations with numeric arrays \cite[Chapter 17, pp. 361]{Hetland2005};
	avoid using lists and *for*-loops for computing with numeric arrays
		\cite[Chapter 17, pp. 361]{Hetland2005}.
+ Use the *ctypes* library (**need to be imported in the *Python* program**) to
	"import preexisting (shared) C libraries" to execute a restricted subset of *C*
	code, without using wrappers or APIs \cite[Chapter 17, pp. 361]{Hetland2005}.
+ Use the *subprocess* module in *The Python Standard Library*
	\cite{DrakeJr2016e,DrakeJr2016b} to enable *Python* programs to execute
	external programs (in *C*/*C++*/otherwise), and interact with their
	input/output (I/O) interface via the command-line arguments, and standard
	input, output, and error streams \cite[Chapter 17, pp. 361]{Hetland2005}.
+ Use the **modulator** script from the **Tools** directory of my *Python*
	distribution "to generate boilerplate code needed for *C* extensions"
	\cite[Chapter 17, pp. 361]{Hetland2005}.
+ Use *Boost.Python* \cite{Abrahams2015a}.
+ Use *SIP* \cite{RiverbankComputingLimitedStaff2016}.















*SWIG* (Simple Wrapper and Interface Generator) allows me to
	\cite[Chapter 17, pp. 361-362]{Hetland2005}:
+ extend programs in *Python* (and/or another programming/scripting language)
	with *C*/*C++* extensions.
+ generate automatic wrappers for *C*/*C++* extensions, so that they can be
	used (as "a shared library") with programs developed in other
	programming/scripting languages.
+ To generate the shared library \cite[Chapter 17, pp. 362]{Hetland2005}:
	- Develop a *SWIG* interface file for my *C*/*C++* program/extension,
		which is similar to *C*/*C++* header files.
		* The interface file enables customization of the *SWIG* wrapper by
			specifying what to export, and/or what not to export, to *Python*
			\cite[Chapter 17, pp. 363]{Hetland2005}.
		* By selecting of small subset of a *C*/*C++* library to export to *Python*,
			we do not have to export the large *C*/*C++* library.
	- Via the command-line interface, use *SWIG* (with the *SWIG* interface file
		as an input) to automatically generate the wrapper code for my
		*C*/*C++* program/extension.
		* Use the "Man page" (from the *UNIX*/*Linux* "manual") to view the
			complete list of options for running *SWIG* \cite{Fulton2011} from
			the command-line interface
			\cite[Chapter 17, pp. 363-364]{Hetland2005}.
		* The wrapper code consist of a pair of files for each *SWIG* interface
			file; the *C*/*C++* wrapper and its corresponding *Python* file
			\cite[Chapter 17, pp. 364]{Hetland2005}.
	- Compile the *C*/*C++* program/extension with the automatically generated
		wrapper code to generate the shared library.
		* Details of compiling, linking, and using the *SWIG*-generated wrappers
			are found in \cite[Chapter 17, pp. 364]{Hetland2005}.
		* This requires access to the following header files that are found in the
			source code of my *Python* distribution (or location of my *Python*
			installation): **pyconfig.h** and **Python.h**
			\cite[Chapter 17, pp. 364]{Hetland2005}.
		* If I cannot find the location of my *Python* installation because I had
			used a package manager to install *Python*, install a separate
			package (i.e., **python-dev**) so that I can access the required
			header files and the **Include** subdirectory of
			**$PYTHON\_HOME** \cite[Chapter 17, pp. 364]{Hetland2005}.
		* The resultant output file is a shared library with a **.so** extension,
			which can be added to my **PYTHONPATH** so that my *Python*
			code can access the *C*/*C++* program/extension
			\cite[Chapter 17, pp. 365]{Hetland2005}.
+ \cite{Fulton2011}, which is the official source about *SWIG*, contains more
	information about *SWIG*.
+ To simplify the compilation steps during build automation (with a *Makefile* or
	otherwise), use **Distutils** \cite[Chapter 17, pp. 365]{Hetland2005}.





Suggested framework for developing *C*/*C++* programs/extensions for
	mixed-language software \cite[Chapter 17, pp. 367-368]{Hetland2005}:
+ Include the **Python.h** header file first \cite[Chapter 17, pp. 367]{Hetland2005}
	- Include other standard header files later.
	- This enables some platforms to carry out redefinitions that would be used
		by other header files.
+ Define a static function that \cite[Chapter 17, pp. 367]{Hetland2005}:
	- Two parameters:
		* pointers "to an object of the *PyObject* type"
		* **self** object, which is a self-object (in bound methods),
			or **NULL** (otherwise -- for other methods).
		* **args** object, which is "a tuple of arguments" passed to the function
			\cite[Chapter 17, pp. 368]{Hetland2005}
	- Returns a pointer (or owned reference) "to an object of the *PyObject* type".










References for developing mixed-language software
+ \cite[Chapter 26, pp. 591-620]{Beazley2009}:
+ \cite[Chapters 5,9-10]{Langtangen2009}.
+ \cite[Appendix G]{Langtangen2012}




###	Packaging *Python* Programs

Use the *Distutils* toolkit to distribute *Python* packages
	\cite[Chapter 18, pp. 373]{Hetland2005}:
+ Develop *Python*-based install scripts for a *Python* package; the install script
	shall:
	- Build archive files for distribution
	- Use archive files for compiling and installing *Python* libraries.
+ Build *(Microsoft) Windows* installers for *Python* packages.
+ Build *(Microsoft) Windows* executable *Python* programs, using the
	**py2exe** extension to the *Distutils* toolkit
	\cite[Chapter 18, pp. 379-380]{Hetland2005}.
+ Build self-installing archives for my binaries




\cite{Ward2018a} \cite[Distributing Python Modules (Legacy version)]{DrakeJr2017c,DrakeJr2016d}
	shows how to write a setup script to install *Python* programs
	\cite[Chapter 18, pp. 373-374]{Hetland2005}:
 + Universal conventions for *Distutils*-based setup scripts
 	\cite[Chapter 18, pp. 374]{Hetland2005}:
 	- The setup script is named: **setup.py**.
	- Run the install command \cite[Chapter 18, pp. 374]{Hetland2005}:
		**./setup.py install**
		* Automatically runs the build command:
			**./setup.py build**
	- The setup script adds my/our custom modules to **PYTHONPATH**.
	- Use the **ext\_modules** argument in **setup.py** to provide
		a list of *Python* modules as a list of **Extension** instances
		\cite[Chapter 18, pp. 378]{Hetland2005}.
		* When used with *SWIG* for developing mixed-language software,
			add the *SWIG* interface (**.i**) files to the list of **Extension**
			instances \cite[Chapter 18, pp. 378-379]{Hetland2005}.
	- Use the **--inplace** option to compile/build the *Python*
		modules/extensions in the current directory
		\cite[Chapter 18, pp. 378]{Hetland2005}.
+ There are no universal conventions for:
	- uninstall \cite[Chapter 18, pp. 375]{Hetland2005}
+ Additional commands of interest:
	- **sdist** ("for `source distribution' "); to create an archive file for the
		installed *Python* program \cite[Chapter 18, pp. 376]{Hetland2005};
		**./setup.py sdist**.
+ *Distuils* directives \cite[Chapter 18, pp. 376]{Hetland2005}:
	- **py\_modules**: to install *Python* modules \cite[Chapter 18, pp. 376]{Hetland2005}
	- **packages**: to install *Python* packages \cite[Chapter 18, pp. 376]{Hetland2005}
+ Create **configuration files** for *Distutils* to set up properties for the *Python*
	program to be installed \cite[Chapter 18, pp. 376]{Hetland2005}.
+ To specify what and where to install, provide various options to **setup.py**
	and the *Distutils* **configuration files** so that they have command-line
	switches and can accept keyword arguments
	\cite[Chapter 18, pp. 376]{Hetland2005}.
+ To distribute the *Python* modules as an archive file for installation, use the
	**sdist** command for wrapping the *Python* modules for source distribution
	\cite[Chapter 18, pp. 376]{Hetland2005}.
	- **python** [*Python* modules] **sdist**
	- **python setup.py sdist**
	- Suggested information for the **setup.py** script are
		\cite[Chapter 18, pp. 376]{Hetland2005}:
		* Contact information of the author, or a co-author: **author\_email**
		* Name of the author, or list of co-authors: **author**
		* **README**/**README.txt** text file, which can be written in
			*Markdown* and it can be empty.
		* *MANIFEST.in* file, which can be empty
	- The output of running **python setup.py sdist** is a **gzip**'ed tar archive
		(or tar ball) \cite[Chapter 18, pp. 377]{Hetland2005}.
	- To specify the distribution format of the output archive, use the
		command-line switch **--formats** *[option]*, where *[option]* can be
		\cite[Chapter 18, pp. 377]{Hetland2005}:
		* **bztar**
		* **gztar** (default archive format)
		* **tar**
		* **zip**
		* **ztar**
+ The *MANIFEST.in* file helps the *Distuils* setup/install process to locate all
	required files for my/our installed *Python* program  
	\cite[Chapter 18, pp. 376]{Hetland2005}.
	- When my *Python* package has been restructured, or when I want to
		repackage it, delete the *MANIFEST.in* file
		\cite[Chapter 18, pp. 377]{Hetland2005}.
		Else, if the *MANIFEST.in* file exists, it will be read instead of being
			overwritten \cite[Chapter 18, pp. 377]{Hetland2005}.
+ To distribute the *Python* modules as an archive file for installation, use the
	**bdist** command for creating binary distributions for the *Python* modules
	that are operating system-specific (OS-specific)
	\cite[Chapter 18, pp. 377]{Hetland2005}.
	- **python** [*Python* modules] **bdist --formats=***[option]*
	- Available values for *[option]* are:
		* **rpm** (for distributions of the *Linux* operating systems)
		* **wininst** (for *Windows* operating systems)




+ To create binary installers with an option to uninstall the *Python* package(s),
	use the following options to create binary installers
	\cite[Chapter 18, pp. 378]{Hetland2005}:
	- *py2exe* with *Inno Setup*
	- *McMillan installer*
	- *InstallShield*
	- *Wise installer*
	- *Installer VISE*
	- *Nullsoft Scriptable install System*
	- *Youseful Windows Installer*
	- *Ghost Installer*
+ For more information on creating (binary) installers for *Windows* operating
	systems, see \cite{Wilson2004a}.











####	References for Packaging *Python* Programs


References for packaging *Python* programs \cite[Chapter 18, pp. 373]{Hetland2005}:
+ [\cite[\S27, Software Packaging and Distribution]{DrakeJr2016e}](https://docs.python.org/2/library/distribution.html)
	- [\cite[\S27.1, distutils -- Building and installing *Python* modules]{DrakeJr2016e}](https://docs.python.org/2/library/distutils.html)
+ [\cite[\S28, Software Packaging and Distribution]{DrakeJr2016b}](https://docs.python.org/3/library/distribution.html)
	- [\cite[\S28.1, distutils -- Building and installing *Python* modules]{DrakeJr2016b}](https://docs.python.org/3/library/distutils.html)
+ [\cite{Ward2018} \cite[Installing *Python* Modules (Legacy version)]{DrakeJr2017c,DrakeJr2016d}](https://docs.python.org/3/install/)
+ [\cite{Ward2018a} \cite[Distributing Python Modules (Legacy version)]{DrakeJr2017c,DrakeJr2016d}](https://docs.python.org/3/distutils/)
+ \cite[Chapter 8, section on "Distributing Python Programs and Libraries," pp. 152-154]{Beazley2009}










###	Database Administration

Notes regarding the management of information systems, or database
	administration \cite[Chapter 13, pp. 285-290]{Hetland2005}:
+ Use the *Python* Database (DB) API to connect to *SQL* databases, which
	allows *SQL*-based queries and execution of *SQL* databases
	\cite[Chapter 13, pp. 285-286]{Hetland2005}.  
+ Global variables required for compliance with the *Python* Database API (or
	*Python* DB API) \cite[Chapter 13, pp. 286-287]{Hetland2005}:
	- **apilevel**: version of the *Python* Database API being used;
		its acceptable values are: "1.0" and "2.0".
	- **threadsafety**: level of thread safety supported/provided by the
		*Python* Database API-compliant database module;
		its acceptable values are: {0, 1, 2, 3}.
	- **paramstyle**: the type of parameter style chosen for *SQL* queries;
		its acceptable values are: "format", "pyformat", "qmark", "numeric",
			and "named".
+ Exceptions defined by the *Python* Database API enable fine-grained error
	handling \cite[Chapter 13, pp. 287]{Hetland2005}.
+ The function **connect()** allows the *Python* software to connect to the
	database system \cite[Chapter 13, pp. 287-288]{Hetland2005}.
	- **Beware of using this function with the parameters user name and
		password, since I could end up divulging secrets of my company,
		research group, or personal liofe.**
	- Other functions to help *Python* software manipulate objects in the
		database systems \cite[Chapter 13, pp. 288]{Hetland2005}:
		* close()
		* commit(), allows open connections to be closed automatically during
			garbage collection \cite[Chapter 13, pp. 288]{Hetland2005}.
		* rollback()
		* cursor()
	- There exists *cursor object methods* that allow users/developers to:
		execute *SQL* operations on, and fetch data from, the *SQL* database;
		traverse/enumerate the elements in the *SQL*  database; and perform
		procedures on the *SQL* database \cite[Chapter 13, pp. 289]{Hetland2005}.
	The *Python* Database API has "constructors and constants/singletons"
		for various types and values \cite[Chapter 13, pp. 289]{Hetland2005}.
+ \cite[Chapter 6, section on "Declarative Programming," pp. 111]{Beazley2009}
	suggests using **list comprehensions and database queries** togerther
	concurrently, using functional/declarative programming.




Some *SQL* database engines, such as *SQLite*, do not require being run as a
	server program nor require administrator privileges to install them
	\cite[Chapter 13, pp. 290]{Hetland2005}.



*SQL* database engines can work with \cite[Chapter 13, pp. 290]{Hetland2005}:
+ local files
+ centralized database storage systems
+ distributed database storage systems


See \cite{Molinaro2006} for further information about *SQL* database management
	and administration.

\cite{Beazley2009}









###	Software Development Process Methodologies

Use extreme programming (XP) \cite[Chapter 19, pp. 381]{Hetland2005} \cite{Pressman2010,Sommerville2007,Jayaswal2007,Wells2009,Jalote2008,DeLucia2008,Beck2005,Larman2003,Beck2001,Wells1999},
	or other agile software development methodologies \cite{Stellman2015,Kelly2015,Laplante2014,Crookshanks2012,Rasmusson2010,Shore2008,Larman2004,Boehm2004},
	to develop *Python* software/programs.
+ Be adaptive and flexible \cite[Chapter 19, pp. 382]{Hetland2005}.
+ Have the courage to refactor the software to improve certain qualities/aspects
	of the software \cite[Chapter 19, pp. 382]{Hetland2005}.
	- This involves modifying the software architecture and selection of
		algorithms to implement \cite[Chapter 19, pp. 382]{Hetland2005}.
	- Extract symbolic constants, which are global variables that are treated as
		constants (preferably named in upper case with underscores), and
		provide users/developer access to these so that they can
		customize/configure these symbolic constants easily
		\cite[Chapter 19, pp. 383-384]{Hetland2005}.
		* Replace multiple instances of numbers or strings as symbolic constants
			\cite[Chapter 19, pp. 383-384]{Hetland2005}.
		* These symbolic constants can be placed at the top of a module
			or together in a separate module for configuration.
			\cite[Chapter 19, pp. 384]{Hetland2005}.
		* Use the *ConfigParser* module from The Python Standard Library
			\cite{DrakeJr2016b,DrakeJr2016e} to create a configuration file
			for configuring symbolic constants \cite[Chapter 19, pp. 384]{Hetland2005}.
		* When creating the configuration file for the *ConfigParser* module,
			split the symbolic constants into named sections using the format
			*[section-name]*; the square brackets are required
			\cite[Chapter 19, pp. 384]{Hetland2005}.
		* Making the software configurable/parameterizable allows the software
			to be customizable \cite[Chapter 19, pp. 385]{Hetland2005}.
	- Use software refactoring to improve the quality, performance (i.e., in terms
		of execution time), memory usage, and maintainability
		\cite[Chapter 10, section on "Refactoring,"pp. 162]{Pilgrim2009}.
+ Embrace prototyping early in my software development process
	\cite[Chapter 19, pp. 382]{Hetland2005}.
	- Since programming in *Python* involves writing less boilerplate code than
		*C++*/*Java*, it is more amenable to facilitate prototyping than these
		latter programming languages \cite[Chapter 19, pp. 383]{Hetland2005}.
	- Prototyping facilitates iterative and incremental development (IID) \cite{Brown2017,Babar2014,Boehm2014,Wysocki2014,Kumar2013,Robertson2013,Sifakis2013,Jalote2008,Shore2008,Schach2007,Sommerville2007,37signals2006,Subramaniam2006,Larman2005,Boehm2004,Larman2004,Wickens2004a,Wickens2004b,Larman2003,Larman2002,Felleisen2001,BrooksJr1995},
		instead of up-front detailed analysis and design
		\cite[Chapter 19, pp. 383]{Hetland2005}.
	- The executable prototypes (in *Python*) enable software developers to
		notice problems, weaknesses, and incompleteness of the
		prototypes \cite[Chapter 19, pp. 383]{Hetland2005}, which can be
		fixed in subsequent iterations of the project (during the IID process).  
+ Embrace automated software testing to facilitate software refactoring
	\cite[Chapter 19, pp. 382]{Hetland2005}; see subsection on [Software Testing, Verification, and Validation](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#software-testing-verification-and-validation).
+ Practice the "good enough" philosophy \cite[Chapter 19, pp. 383]{Hetland2005}
	\cite{Martelli2016a,Martelli2016}, which is also espoused by Prof. Jiang Hu
	during his classes and research lab meetings (*personal communication*).
	- This helps me to avoid problems associated with perfectionism, which
		keeps me from completing or releasing "imperfect" work, which
		Prof. Derek Abbott and Prof. Laszlo Bela Kish during our reunion
		in early November 2016.



Suggested reading from \cite[Chapter 19, pp. 387]{Hetland2005}:
+ \cite{Hunt1999}
+ \cite{Fields2010,Fowler1999}
+ \cite{Gamma1995}
+ \cite{Beck2003}
+ \cite{Raymond2004}
+ \cite{Cormen2009,Cormen2001,Cormen2002}
+ \cite{Knuth2005,Knuth1997,Knuth1997a,Knuth1998,Knuth2011}


####	Integrated Development Environments (IDEs)

List of integrated development environments (IDEs):
+ [Spyder](https://github.com/spyder-ide/spyder)
	- \cite{SpyderProjectContributors2018}
+ [Jupyter](http://jupyter.org/)
+ [PyCharm Edu](https://www.jetbrains.com/pycharm-edu/)
+ [JetBrains Student](https://www.jetbrains.com/student/)





## *Python* Strings

In *Python* 3.x:
+ *exec("ls -al")* does not work.
	- *exec()* only executes *Python* code, in a *Python* environment
		\cite[Chapter 8, pp. 172]{Hall2009b}.
+ ***exec()* and *eval()* pose software security threats**, if they execute
	malicious *Python* code \cite[Chapter 8, pp. 173]{Hall2009b}.
	- The function **eval(str [,globals [,locals]])** evaluates the expression
		contained in the string **str**, and returns the result
		\cite[Chapter 6, section on "eval(), exec(), and compile()," pp. 115]{Beazley2009}.
	- The function **exec(str [, globals [, locals]])** executes the *Python* code
		contained in the string **str**
		\cite[Chapter 6, section on "eval(), exec(), and compile()," pp. 115]{Beazley2009}.
	- Since the compilation of *Python* code, including expressions, is expensive,
		use the function **compile(str,filename,kind)** to compile the string
		(contain *Python* code or an expression) into bytecode for faster
		performance (including traceback generation, when the code is executed
		multiple times)
		\cite[Chapter 6, section on "eval(), exec(), and compile()," pp. 115]{Beazley2009}.

To compare the content of two strings, try:

	string1 == string2

To compare the identities of two strings, try:

	string1 is string2

[Reference for string comparison](https://stackoverflow.com/questions/1504717/why-does-comparing-strings-in-python-using-either-or-is-sometimes-produce)







##	Exception Handling


An exception stops the execution of the *Python* software/program due to
	an encountered error \cite[Chapter 10, pp. 221]{Hall2009b}.

Exception handling is also known as \cite[Chapter 8, pp. 162]{Hetland2005}:
+ exception trapping
+ trapping the exceptions
+ exception catching
+ catching the exceptions



Use **try...except...else...finally** statements to handle exceptions
	\cite[Chapter 10, pp. 221]{Hall2009b} \cite[Chapter 8, pp. 162]{Hetland2005}
	\cite[Chapter 5, section on "Exceptions," pp. 84-89]{Beazley2009},
	so that the *Python* program does not have to terminate execution
	\cite[Chapter 8, pp. 159]{Hetland2005}.

Here are some examples of catching multiple specific exceptions
	\cite[Chapter 8, pp. 164]{Hetland2005}.

*Example 1*:

	try:
		...
		statements
		...
	except [Specific Exception #1]:
		statements
	except [Specific Exception #2]:
		statements

*Example 2*:

	try:
		...
		statements
		...
	except ([Specific Exception #1], [Specific Exception #2]):
		statements

**This does not work with *Python 3.6* (or *Python 3.7* and beyond).**



*Example 3*:

	try:
		...
		statements
		...
	except ([Specific Exception #1], [Specific Exception #2]), e:
		print e

In *Example 3*, the specific exception caught, which could be either
	***[Specific Exception #1]*** or ***[Specific Exception #2]*** (or both????), 
	can be printed, and execution of the *Python* program resumes
	\cite[Chapter 8, pp. 165]{Hetland2005}.

**This does not work with *Python 3.6* (or *Python 3.7* and beyond).**




*Example 4*:

	try:
		...
		statements
		...
	except:
		statements

In *Example 4*, the **except** clause catches all exceptions (i.e., catchall) that
	can occur in the **try** block, and executes the statements in the **except**
	block of the *Python* program \cite[Chapter 8, pp. 165-166]{Hetland2005}.

*Example 5*:

	try:
		...
		statements
		...
	except Exception, e:
		statements

**This does not work with *Python 3.6* (or *Python 3.7* and beyond).**




In *Example 5*, the **except** clause catches all exceptions (i.e., catchall) that
	can occur in the **try** block, and executes the statements in the **except**
	block of the *Python* program \cite[Chapter 8, pp. 165-166]{Hetland2005}.
	It can also perform some type checking on the Exception object *e* to help
		the developers determine the specific exception that occurred.

With **try...except...else...finally** statements, the **else** block enables its
	statements to be executed unless exceptions happen
	\cite[Chapter 8, pp. 166-168]{Hetland2005}.

With **try...except...else...finally** statements, statements in the **finally** block
	are guaranteed to be executed, regardless of exceptions occur in the **try**
	block \cite[Chapter 8, pp. 168]{Hetland2005}.

When propagated exceptions cause the *Python* program to halt, use the *stack
	trace* to determine what happened \cite[Chapter 8, pp. 168]{Hetland2005}.

From \cite[\S8.3 Handling Exceptions]{Brandl2017a}:
+ "A class in an except clause is compatible with an exception if it is the same class or a base class thereof (but not the other way around — an except clause listing a derived class is not compatible with a base class)."
+ "If no exception occurs, the except clause is skipped and execution of the try statement is finished."
+ "If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try statement."
+ "If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with a message."
+ "A try statement may have more than one except clause, to specify handlers for different exceptions. At most one handler will be executed. Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same try statement. An except clause may name multiple exceptions as a parenthesized tuple."
+ "A class in an except clause is compatible with an exception if it is the same class or a base class thereof (but not the other way around - an except clause listing a derived class is not compatible with a base class)."
+ "The last except clause may omit the exception name(s), to serve as a wildcard. Use this with extreme caution, since it is easy to mask a real programming error in this way! It can also be used to print an error message and then re-raise the exception (allowing a caller to handle the exception as well)."
+ "The try ... except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception."
+ "The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn't raised by the code being protected by the try ... except statement."
+ "The exception instance arguments stored in .args __str__ allows args to be printed directly, but may be overridden in exception subclasses"
+ "When an exception occurs, it may have an associated value, also known as the exception's argument. The presence and type of the argument depend on the exception type."
+ "The except clause may specify a variable after the exception name. The variable is bound to an exception instance with the arguments stored in instance.args. For convenience, the exception instance defines __str__|() so the arguments can be printed directly without having to reference .args. One may also instantiate an exception first before raising it and add any attributes to it as desired."



From \cite[\S8.4 Raising Exceptions]{Brandl2017a}:
+ "The sole argument to raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from Exception). If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments: ***raise ValueError  # shorthand for 'raise ValueError()'***"




From \cite[\S8.5 User-defined Exceptions]{Brandl2017a}:
+ "Exception classes can be defined which do anything any other class can do, but are usually kept simple, often only offering a number of attributes that allow information about the error to be extracted by handlers for the exception."
+ "When creating a module that can raise several distinct errors, a common practice is to create a base class for exceptions defined by that module, and subclass that to create specific exception classes for different error conditions"





From \cite[\S8.6 Defining Clean-up Actions]{Brandl2017a}:
+ "The try statement has another optional clause (the finally clause) which is intended to define clean-up actions that must be executed under all circumstances."
+ "A finally clause is always executed before leaving the try statement, whether an exception has occurred or not. When an exception has occurred in the try clause and has not been handled by an except clause (or it has occurred in an except or else clause), it is re-raised after the finally clause has been executed."
+ "The finally clause is also executed `on the way out' when any other clause of the try statement is left via a break, continue or return statement."
+ "The finally clause is executed in any event."
+ "In real world applications, the finally clause is useful for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful."


From \cite[\S8.7 Predefined Clean-up Actions]{Brandl2017a}:
+ "The with statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly."
	- See https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#system-resource-management.
+ From \cite{Brandl2017a}: [\S8 Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)




![Illustration of the try-except-else-finally block in *Python*](https://github.com/eda-ricercatore/admin-notes/blob/main/pics/try-except-else-finally-block.jpg)
Figure 1, Illustration of the try-except-else-finally block in *Python*.



The *Python* Exception class hierarchy is described in \cite{PowellMorse2017} and \cite[From Learn Python Programming, The Definitive Guide: Python Errors and Built-in Exceptions]{ParewaLabsStaff20XY}.






Any unhandled exception would terminate execution of the *Python* program and
	produce a *traceback* (i.e., error message)
	\cite[Chapter 8, pp. 160]{Hetland2005}.



Exception chaining is a method of tracebacks that enable exceptions raised
	during exception handling to be differentiated from the original
	raised/thrown exception \cite[Chapter 10, pp. 235-236]{Hall2009b}.





\cite[Chapter 2, pp. 23-28,29-30]{Alchin2010} shows how to catch multiple
	errors that have been raised.

To raise an exception, try either of the following
	\cite[Chapter 8, pp. 160]{Hetland2005}:
+ raise Exception, "[Error message.]"
+ raise Exception("[Error message.]")
+ raise \cite[Chapter 8, pp. 163]{Hetland2005}
	- When raising a specific exception that has been caught.

In \cite[\S5]{DrakeJr2016b} discusses all the "built-in exceptions" provided by the
	the "The *Python* Standard Library" \cite[Chapter 8, pp. 161]{Hetland2005}.

To create custom exception classes, create a derived class of the *Exception*
	class \cite[Chapter 8, pp. 162]{Hetland2005}.

Use customized exception classes to address violations of invariants \cite{Lee2017a,Lee2015b,Lee2014a,Backhouse2011,Lee2011,Zeller2009,Baier2008,Tucker2007,Hailperin1999,Manna1992},
	such as preconditions, assertions, and postconditions \cite{Pierce2017,Laplante2014,Dale2012,Kourie2012,Kundu2011,Zeller2009,Tucker2007,Baldwin2004,Huth2004,Monin2003,Hailperin1999},
	that can be handled/mitigated, so that the *Python* program can resume
	execution (and avoid termination).



###	Warnings

To avoid termination of the program by mild errors, use a warning to notify users
	of the mild error message, and allow the *Python* program to keep executing
	\cite[Chapter 8, pp. 159-160]{Hetland2005}.

To use a warning, import the **warnings** module and/or its methods/functions
	\cite[Chapter 8, pp. 160]{Hetland2005}.





###	Ancillary Note

The philosophy of "look before you leap" (LBYL) discourages exception handling
	\cite[Chapter 10, pp. 238]{Hall2009b}.

The Pythonic philosophy of "easier to ask forgiveness than permission" (EAFP)
	encourages trying something, and use exception handling to deal with
	uncommon outcomes/circumstances \cite[Chapter 10, pp. 238]{Hall2009b}.
















##	*Python* Virtual Machine (PVM)

Notes about the *Python* Virtual Machine (PVM):
+ \cite{Pattis2016}













##	Concurrent and Parallel Programming with *Python*

From my [Notes about Scala](https://github.com/eda-ricercatore/sardegna-scala/blob/master/notes/scala-notes.md):
+ "Concurrent programming (compare: parallel programming) \cite{WikipediaContributors2017k} -- Concurrent computing concurrently execute multiple computations during overlapping time periods; each computation/process has a separate execution point or thread of control. That is, in concurrent computing, a computation can advance independently of other computations, which may be incomplete."
+ "Parallel computing (compare: concurrent programming) \cite{WikipediaContributors2017n} -- Parallel computing is defined as the simultaneous execution of processes or calculations/computation on a computer. The types of parallel computing are: bit-level parallelism, instruction-level parallelism, data parallelism, and task parallelism. Bit-level parallelism and instruction-level parallelism are implicitly parallel. Explicitly parallel algorithms, especially those that involve concurrency, are more difficult to develop and test than sequential algorithms; concurrency in such algorithms can lead to race conditions, and other types/classes of software bugs. It is difficult to manage communication and synchronization between subtasks, such that the parallel computation would have a significant speed-up over the serial/sequential implementation."




References on concurrent and parallel programming with *Python*:
+ \cite[Chapter 20, pp. 413-447]{Beazley2009}
+ \cite{Lutz2011}
+ \cite{Gift2008}























###	System Resource Management

Use mutual exclusion (mutex) to manage system resources, such as locks, files,
	and network connections
	\cite[Chapter 1, section on "Exceptions," pp. 23]{Beazley2009}.
+ Assign the lock, file object, or network connection to a **variable**.
+ Use the **with** statement with the aforementioned **variable** (for the lock,
	file object, or network connection) to perform operations with the lock, file
	object, or network connection (using the acquired **variable**)
	\cite[Chapter 1, section on "Exceptions," pp. 23]{Beazley2009}
	\cite[Chapter 5, section on "Context Managers and the with Statement," pp. 89-90]{Beazley2009}.
+ When execution/control of the *Python* program is outside the context of the
	**with** statement, such as a raised exception, the **variable** is
	automatically released
	\cite[Chapter 1, section on "Exceptions," pp. 23]{Beazley2009}.

See https://docs.python.org/3/reference/compound_stmts.html#the-with-statement for more information about the "with" statement.
+ https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for
+ https://effbot.org/zone/python-with-statement.htm
+ https://python3statement.org
+ https://docs.python.org/2.5/whatsnew/pep-343.html











##	*Python*-based Data Science


###	Probability Theory, Statistical Analysis, Random Processes, Stochastic Modeling, and Noise

*Python* libraries and packages for probability theory, statistical analysis (or statistical data analysis), random processes, stochastic modeling, and noise modeling/analysis:
+ [StatsModels](https://github.com/statsmodels/statsmodels)
	- \cite{Taylor2018}
	- http://www.statsmodels.org/stable/index.html
+ [PyMC3](https://docs.pymc.io/)
	- https://numfocus.org/project/pymc3
	- \cite{ThePyMCDevelopmentTeam2018,PyMC3Contributors2018}
	- \cite{Salvatier2016}
	- [PyMC](PyMCContributors2018) ... The old version.


To generate pseudo-random numbers, try using the following libraries.
+ From the Python Standard Library \cite[Version 3.81, from Numeric and Mathematical Modules: random]{DrakeJr2016b},
	I can use the following probability distributions:
	- exponential distribution, lambda = 1.5
	- beta distribution, alpha = 1, beta = 3
	- gamma distribution, k = 1.0, theta = 2.0:
	- Pareto distribution
	- Weibull distribution
	- normal/Gauss/Gaussian distribution
		* random.gauss(mu, sigma)
			+ faster implementation
				- \cite[Version 3.81, from Numeric and Mathematical Modules: random, last accessed Jan 21, 2020]{DrakeJr2016b}
				- See https://docs.python.org/3/library/random.html.
		* random.normalvariate(mu, sigma) 
			+ slower implementation
			- \cite[Version 3.81, from Numeric and Mathematical Modules: random, last accessed Jan 21, 2020]{DrakeJr2016b}
			- See https://docs.python.org/3/library/random.html.
	- log-normal (or lognormal) distribution, or Galton distribution or Galton's distribution
	- von Mises distribution, or circular normal distribution or Tikhonov distribution






References for aforementioned probability distributions:
+ Wikipedia contributors, "Beta distribution," in Wikipedia,
	The Free Encyclopedia: Continuous distributions,
	Wikimedia Foundation, San Francisco, CA, January 18, 2020.
	Available online at: https://en.wikipedia.org/wiki/Beta_distribution;
		last accessed on January 21, 2020.
+ Wikipedia contributors, "Exponential distribution," in Wikipedia,
	The Free Encyclopedia: Continuous distributions,
	Wikimedia Foundation, San Francisco, CA, January 20, 2020.
	Available online at: https://en.wikipedia.org/wiki/Exponential_distribution;
		last accessed on January 21, 2020.
+ Wikipedia contributors, "Gamma distribution," in Wikipedia,
	The Free Encyclopedia: Continuous distributions,
	Wikimedia Foundation, San Francisco, CA, January 14, 2020.
	Available online at: https://en.wikipedia.org/wiki/Gamma_distribution;
		last accessed on January 21, 2020.
+ Wikipedia contributors, "Pareto distribution," in Wikipedia,
	The Free Encyclopedia: Continuous distributions,
	Wikimedia Foundation, San Francisco, CA, January 18, 2020.
	Available online at: https://en.wikipedia.org/wiki/Pareto_distribution;
		last accessed on January 21, 2020.
+ Wikipedia contributors, "Weibull distribution," in Wikipedia,
	The Free Encyclopedia: Continuous distributions,
	Wikimedia Foundation, San Francisco, CA, November 13, 2019.
	Available online at: https://en.wikipedia.org/wiki/Weibull_distribution;
		last accessed on January 21, 2020.


Parameters of probability distributions:
+ shape parameter: https://en.wikipedia.org/wiki/Shape_parameter
	- skewness, asymmetry about the mean
		* positive skew: mode < median < mean
		* symmetric: mode = median = mean
		* negative skew: mean < median < mode
		* https://en.wikipedia.org/wiki/Skewness
	- kurtosis
		* platykurtic (<3 for univariate normal distribution), more uniform in probability distribution
		* leptokurtic (>3 for univariate normal distribution), less uniform in probability distribution
		* https://en.wikipedia.org/wiki/Kurtosis
+ scale parameter: https://en.wikipedia.org/wiki/Scale_parameter
	- How spread out is a probability distribution?





###	Machine Learning

Resources for *Python*-based machine learning:
+ [TensorFlow machine learning framework](https://www.tensorflow.org/)
	- *TensorFlow* web page and software \cite{GoogleBrainTeam2018}
+ [scikit-learn](https://scikit-learn.org/)
	- \cite{Blondel2018,Pedregosa2011}
	- \cite{Buitinck2013,Cremilleux2013,Pedregosa2018,Sonnenburg2018,Hauck2014,Avila2017}
	- \cite{Blondel2018a,Blondel2018b,Blondel2018c,Blondel2018d,Blondel2018e,Blondel2018f,Blondel2018g,Blondel2018h,Blondel2018i}
+ [Google Colaboratory](https://colab.research.google.com/)
	- A "free Google Cloud-based Jupyter notebook environment"
	- Also, see https://research.google.com/colaboratory/.
	- [Google Colaboratory @ GitHub](https://github.com/googlecolab)
	- [Using Google Colab with GitHub](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb#scrollTo=3VQqVi-3ScBC)
	- [Google Colab Free GPU Tutorial](https://medium.com/deep-learning-turkey/google-colab-free-gpu-tutorial-e113627b9f5d)
	- [Primer for Learning Google Colab](https://medium.com/dair-ai/primer-for-learning-google-colab-bb4cabca5dd6)
	- [3 Essential Google Colaboratory Tips & Tricks](https://www.kdnuggets.com/2018/02/essential-google-colaboratory-tips-tricks.html)
	- [Google Colaboratory — Simplifying Data Science Workflow](https://towardsdatascience.com/google-colaboratory-simplifying-data-science-workflow-c70059386323)
+ [pandas: Python Data Analysis Library](http://pandas.pydata.org/)
	- \cite{McKinney2018,McKinney2012,McKinney2013}
	- \cite{Chen2018a}
	- \cite{Augspurger2018e,Augspurger2018d,Augspurger2018c,Augspurger2018b,Augspurger2018a,pandasDevelopmentTeam2016,Augspurger2018}
+ [NumPy](http://www.numpy.org/index.html)
	- Books: \cite{Idris2015,Oliphant2015,Oliphant2006}
	- Other resources:
		+ \cite{NumPyCommunity2018a,NumPyCommunity2018,NumPyDevelopers2018}
		+ \cite{Jones2018k,Jones2018j,Jones2018l,Jones2018i,Jones2018h,Jones2018g,Gundersen2007c,Gundersen2007b,Gundersen2007a,Gundersen2007,Gundersen2008b,Gundersen2008a,Gundersen2008}
+ [SciPy](https://scipy.org/)
	- Books: \cite{NunezIglesias2017,Bressert2013}
	- Other resources:
		+ \cite{Varoquaux2018,SciPyCookbookContributors2015,Jones2018f,Jones2018e,Jones2018d,TheSciPyCommunity2018a,TheSciPyCommunity2018,Jones2018c,Jones2018b,Jones2018a,Jones2018,RojasG2015,BlancoSilva2013}
		+ \cite{TheSciPyCommunity2018c,TheSciPyCommunity2018b,PlanetSciPyContributors2018}
+ [PyTorch](https://pytorch.org/)
	- \cite{Paszke2018,Paszke2017,Paszke2018a}
+ [Theano](https://github.com/Theano/Theano)
	- Also, see http://www.deeplearning.net/software/theano/.
	- \cite{AlRfou2018,AlRfou2017,AlRfou2016}
	- \cite{Ketkar2017,Sjardin2016}
+ [Microsoft Cognitive Toolkit (CNTK)](https://www.microsoft.com/en-us/cognitive-toolkit/)
	- Project source code \cite{MicrosoftCognitiveToolkitContributors2018,MicrosoftCognitiveToolkitContributors2018a,MicrosoftCognitiveToolkitDocumentationContributors2017}
	- Project documention \cite{MicrosoftCognitiveToolkitDocumentationContributors2018,MicrosoftCognitiveToolkitDocumentationContributors2017a}
+ [ONNX](https://github.com/onnx/onnx)
	- \cite{OpenNeuralNetworkExchangeContributors2018,OpenNeuralNetworkExchangeContributors2018a}
	- Other resources: \cite{OpenNeuralNetworkExchangeContributors2018b,OpenNeuralNetworkExchangeContributors2018c,OpenNeuralNetworkExchangeContributors2018d}
+ [Keras](https://github.com/keras-team/keras/)
	- \cite{KerasContributors2018}
+ [Caffe2](https://github.com/caffe2/caffe2)
	- \cite{Caffe2Contributors2018}
+ [Apache MXNet](https://mxnet.apache.org/)
	- \cite{MXNetContributors2018}
+ [pomegranate](https://github.com/jmschrei/pomegranate)
	- \cite{Schreiber2018,Schreiber2018a}








Machine learning and deep learning resources:
+ \cite{DeepLearningContributors2015,DeepLearningContributors2016,DeepLearningContributors2015a}
	- List of internship and job opportunities in deep learning: \cite{DeepLearningContributors2018}











###	Data Visualization and Information Visualization

*Python* libraries and packages for data visualization and information visualization:
+ [Bokeh](https://bokeh.pydata.org/en/latest/)
	- \cite{BokehContributors2018}
	- \cite{BokehContributors2018a}
+ [seaborn: statistical data visualization](https://seaborn.pydata.org/)
+ [Yellowbrick](https://github.com/DistrictDataLabs/yellowbrick)
	- \cite{YellowbrickContributors2018}
	- http://www.scikit-yb.org/en/latest/
	- **machine learning visualization**
+ [Matplotlib](https://matplotlib.org/)
	- \cite{Caswell2018,Caswell2018a,Hunter2007}
		- Main Web page: \cite{Caswell2018}
	- \cite{Hunter2018,Hunter2018a,Hunter2016}
		* [Official documentation and report \cite{Hunter2018}](https://matplotlib.org/contents.html)
			+ Current version is: 3.1.2 (January 05, 2020)
			+ Report for 3.1.1: https://matplotlib.org/Matplotlib.pdf
			+ last accessed on January 15, 2020. 
	- Tutorial:
		* Official tutorial: \cite{MatplotlibDevelopmentTeam2020}
	- Notes:
		* Travis (Hooked) Hoppe and Fabian Ying, Answer to "What is the
			difference between pylab and pyplot? [duplicate]", from
			Stack Exchange Inc.: Stack Overflow: Questions,
			Stack Exchange Inc., New York, NY, July 23, 2018.
			Available online from Stack Exchange Inc.: Stack Overflow:
				Questions at: https://stackoverflow.com/a/11471777/1531728 and https://stackoverflow.com/questions/11469336/what-is-the-difference-between-pylab-and-pyplot/11471777#11471777;
				February 5, 2020 was the last accessed date.
			+ Use *matplotlib.pyplot* to plot non-interactive diagrams, figures, and plots.
			+ Use *Matplotlib*'s *pylab* to plot interactive diagrams, figures, and plots.
		* Thomas A. Caswell and Brad Solomon, Answer to "Which is the
			recommended way to plot: matplotlib or pylab? [closed]",
			from Stack Exchange Inc.: Stack Overflow: Questions,
			Stack Exchange Inc., New York, NY, February 22, 2018.
			Available online from Stack Exchange Inc.: Stack Overflow:
				Questions at: https://stackoverflow.com/a/16849816/1531728 and https://stackoverflow.com/questions/16849483/which-is-the-recommended-way-to-plot-matplotlib-or-pylab/16849816#16849816;
				February 5, 2020 was the last accessed date.
			+ Use *matplotlib.pyplot* to plot non-interactive diagrams, figures, and plots.
			+ Use *Matplotlib*'s *pylab* to plot interactive diagrams, figures, and plots.
		+ \cite[Section "Matplotlib, pyplot and pylab: how are they related?"]{Hunter2020}
			- [Pylab is deprecated](https://matplotlib.org/faq/usage_faq.html#matplotlib-pyplot-and-pylab-how-are-they-related)
+ [Plotly](https://plotly.com/python/v3/ipython-notebooks/)
+ [GGobi](http://www.ggobi.org/)
	- \cite{GGobiContributors20XY}
+ [Orange](https://orange.biolab.si/)
	- \cite{OrangeContributors2018}
	- https://github.com/biolab/orange3 \cite{OrangeContributors2018a}
+ [itermplot](https://github.com/daleroberts/itermplot)
+ [ggplot](http://ggplot.yhathq.com/)
	- "ggplot is a plotting system for Python based on R's ggplot2 and the Grammar of Graphics."
+ [plotnine by Hassan Kibirige, 2009](https://plotnine.readthedocs.io/en/stable/) 
+ References
	- \cite{Raman2015,Milovanovic2015,Milovanovic2013}








###	Computational Science and Engineering, & Numerical Computing

*Python* libraries for computational science (or scientific computing), computational engineering, and numerical computing:
+ [*Python(x,y)*](http://python-xy.github.io/)
	- \cite{Raybaut2015}
+ [QuTiP](https://github.com/qutip)
	- \cite{Pitchford2018}


Resources about such libraries: \cite{Avila2017,RojasG2015,Hauck2014,BlancoSilva2013,Bressert2013}



###	Additional Information and Resources

See the following regarding [database administration and information systems](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#database-administration).


Strongly recommended resource for data science:
+ **[Anaconda Distribution: The Most Popular Python/R Data Science Distribution](https://www.anaconda.com/distribution/)** \cite{AnacondaStaff2018}



Notes about the pandas library [Haire2023d] from PyData:
+ The 2-D matrix class, or n-D matrix class, in *pandas* is deprecated.
	- Just use the n-D array class from *pandas* instead.
























##	Miscellaneous


*Python* uses the off-side rule \cite{WikipediaContributors2017y}.
	"Blocks in [*Python*] are expressed by their indentation," unlike free-form
		programming languages.



Notes on global and local variables:
+ A global variable (e.g., "*x*") would be shadowed by a local variable (e.g., "*x*")
	of the same name \cite[Chapter 6, pp. 127]{Hetland2005}.
	- To access the aforementioned global variable (e.g., "*x*"), try:
		*globals()['x']*
+ To rebind a global variable (e.g., "*x*") in a function, which assigns a new value
	to the global variable, explicitly state that the global variable is global
	\cite[Chapter 6, pp. 127]{Hetland2005}.
	- E.g., including this statement ***global x*** in a function enables all instances
		of "*x*" to become a global variable after this explicit declaration.
+ The use of global variables reduces the comprehensibility and robustness of the
	software \cite[Chapter 6, pp. 128]{Hetland2005}.
+ Local variables support abstraction and encapsulation, which improves the
	comprehensibility and robustness of the software
	\cite[Chapter 6, pp. 128]{Hetland2005}.
+ Note the existence of non-local variables \cite{WikipediaContributors2017a2}.



The primary built-in object types in *Python*
	\cite[Chapter 7, pp. 139]{Hetland2005}:
+ numbers
+ strings
+ lists
+ tuples
	- Tuples are immutable \cite[Chapter 1, section on "Tuples", pp. 14]{Beazley2009}.
		* [Examples of trying to add an element to a tuple and of trying to remove an element from a tuple. Errors for trying to do these were caught.](https://github.com/eda-ricercatore/python-sandbox/blob/main/i-data-structures/tuple_operations.py)
+ dictionaries






\cite[Chapter 3, section on "Built-in Types for Representing Data," Table 3.1, pp. 38]{Beazley2009}
	shows the "built-in types for data representation":

| Type Category	| Type name	| Description		|
| -------------------- | ------------- |--------------------- |
| None			| type (**None**)	| null object None |
| Numbers		| int			| Integer 			|
|				| long		| integer with arbitary precision (*Python 2* only)	|
|				| float		| floating point	|
|				| complex	| complex number	|
|				| bool		| boolean (**True** or **False**)	|
| Sequences		| str			| Character string	|
|				| unicode		| Unicode character string		|
|				| list			| List			|
|				| tuple		| Tuple			|
|				| xrange		| A range of integers created by **xrange()** (*Python 2* only)	|
|				| range		| A range of integers created by **range()** (*Python 3* only)	|
| Mapping		| dict		| Dictionary		|
| Sets			| set			| Mutable set		|
|				| frozenset	| Imutable set		|









\cite[Chapter 3, section on "Built-in Types for Representing Program Structure," Table 3.9, pp. 47]{Beazley2009}
	shows the "built-in types for representing the structure of *Python* programs":

| Type Category	| Type name	| Description		|
| -------------------- | ------------- |--------------------- |
| Callable			| type.BuiltinFunctionType	| Built-in function or method	|
|				| type		| Type of built-in types and classes	|
|				| object		| Ancestor of all types and classes	|
|				| types.FunctionType	| User-defined function		|
|				| types.MethodType	| Class method			|
| Modules		| types.ModuleType	| Module					|
| Classes			| object		| Ancestor of all types and classes	|
| Types			| type		| Type of built-in types and classes	|






\cite[Chapter 3, section on "Built-in Types for Interpreter Internals," Table 3.9, pp. 51-54]{Beazley2009}
	has useful information on the types "of objects used by the internals of the
	[*Python*] interpreter.
	This is helpful information for parsing *Python* programs.










Types of *Python* statements \cite[Appendix B, pp. 566-570]{Hetland2005}:
+ simple statements \cite[Appendix B, pp. 566-569]{Hetland2005}:
	- expression statements \cite[Appendix B, pp. 566]{Hetland2005}
	- asset statements \cite[Appendix B, pp. 566]{Hetland2005}
	- assignment statements \cite[Appendix B, pp. 566]{Hetland2005}
	- augmented assignment statements \cite[Appendix B, pp. 566]{Hetland2005}
	- pass statements \cite[Appendix B, pp. 567]{Hetland2005}
	- del statements \cite[Appendix B, pp. 567]{Hetland2005}
	- print statements \cite[Appendix B, pp. 567]{Hetland2005}
	- return statements \cite[Appendix B, pp. 567]{Hetland2005}
	- yield statements \cite[Appendix B, pp. 567]{Hetland2005}
	- raise statements \cite[Appendix B, pp. 568]{Hetland2005}
	- break statements \cite[Appendix B, pp. 568]{Hetland2005}
	- continue statements \cite[Appendix B, pp. 568]{Hetland2005}
	- import statements \cite[Appendix B, pp. 568]{Hetland2005}
	- global statements \cite[Appendix B, pp. 569]{Hetland2005}
	- exec statements \cite[Appendix B, pp. 569]{Hetland2005}
+ compound statements \cite[Appendix B, pp. 569-570]{Hetland2005}:
	- if statement \cite[Appendix B, pp. 569]{Hetland2005}
	- while statement \cite[Appendix B, pp. 569]{Hetland2005}
		* Can include an **else** clause that is executed when the loop
			completes execution (under normal circumstances).
	- for statement \cite[Appendix B, pp. 570]{Hetland2005}
		* Can include an **else** clause that is executed when the loop
			completes execution (under normal circumstances).
	- try statement \cite[Appendix B, pp. 570]{Hetland2005}
	- function definitions \cite[Appendix B, pp. 570]{Hetland2005}
		* Create function objects
		* Bind global or local variables to these function objects.
	- class definitions \cite[Appendix B, pp. 570]{Hetland2005}
		* Create class objects
		* Bind global or local variables to these class objects.





See [Software Testing, Verification, and Validation](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#software-testing-verification-and-validation)
	about using **assert** statements and the *\_\_debug\_\_* variable in the
	debug mode.








Augmented assignment statements provide short cuts for various arithmetic
	expressions \cite[Appendix B, pp. 566]{Hetland2005}.
	E.g., **x \*= 3** is equivalent to **x = x \* 3**.
	E.g., **x += 7** is equivalent to **x = x + 7**.

The **pass** statement is used to represent "no-op" operations
	\cite[Appendix B, pp. 567]{Hetland2005}.
	It can be used in *try-except* blocks, or *try-catch* blocks.
	Note that *Python* has no switch statements.
	Similarly, it can be used in *if-elif-...-else* blocks to
		represent no-operation statements (or do-nothing statements)
		\cite[From Section 4 on "More Control Flow Tools", subsection 4.4 on "break and continue Statements, and else Clauses on Loops" and subsection 4.5 on "pass Statements"]{Brandl2017a}.

"The **del** statement unbinds variables and attributes, and removes parts (positions, slices, or slots) from data structures (mappings or sequences). It cannot be used to delete values directly because values are only deleted through garbage collection \cite[Appendix B, pp. 567]{Hetland2005}."
+ That is, the **del** statement decrements the reference count of an object
	\cite[Chapter 7, section on "Object Memory Management," pp. 129]{Beazley2009}


The **yield** statement pauses the execution of a generator iterator to provide
	a value; it can be used in **for** loops
	\cite[Appendix B, pp. 567]{Hetland2005} to generate a sequence of results
	\cite[Chapter 1, section on "Generators," pp. 19]{Beazley2009}
	\cite[Chapter 6, section on "Generators and yield," pp. 102-103]{Beazley2009}.
+ A generator, or generator function, is a function that includes a yield
	statement, such that successive calls to the generator produces a
	sequence of results
	\cite[Chapter 1, section on "Generators," pp. 19]{Beazley2009}.
	- A generator must return the **None** object when its execution ends,
		and no other object should be returned by the generator
		\cite[Chapter 6, section on "Generators and yield," pp. 103]{Beazley2009}.
	- Use the **close()** function to manually indicate that the generator is no
		longer used or is deleted
		\cite[Chapter 6, section on "Generators and yield," pp. 103]{Beazley2009}.
	- Calling the **close()** function causes the **GeneratorExit** exception to
		be raised/thrown;
		when catching the **GeneratorExit** exception, its handing shall not
			include the use of another generator or use a **yield** statement to
			produce another output
		\cite[Chapter 6, section on "Generators and yield," pp. 104]{Beazley2009}.
	- "[Pull] values through a sequence of **generator** functions"
		\cite[Chapter 6, section on "Using Generators and Coroutines," pp. 107]{Beazley2009}
+ Calling the **next()** function executes a generator until the next **yield
	statement**, so that it can return the value from the **yield** statement and
	suspend the execution of the generator
	\cite[Chapter 1, section on "Generators," pp. 19]{Beazley2009}.
	- When the **next()** function cannot find more **yield** statements, the
		generator returns (after completing execution)
		\cite[Chapter 1, section on "Generators," pp. 19]{Beazley2009}.
+ Use generators for "processing pipelines, streas, or data flow"
	\cite[Chapter 1, section on "Generators," pp. 19]{Beazley2009}.
+ Generators tend to be used "with other iterable objects, such as lists or files"
	\cite[Chapter 1, section on "Generators," pp. 20]{Beazley2009}.



\cite[Chapter 2, section on "String Literals," pp. 27-28]{Beazley2009} demonstrates
	how *Unicode* characters can be inserted into *Python* strings.

\cite[Chapter 2, section on "String Literals," Table 2.1, pp. 27-28]{Beazley2009}
	shows a list of escape characters for *Python* strings.
+ backslash: continuation of a statement on a new line.
+ Null
+ Single quote
+ Double quote
+ Line feed
+ Horizontal tab
+ Vertical tab













In *Python*, variable assignments are not storage operations, which overwrite the
	old values by storing a new value in their place
	\cite[Chapter 7, section on "Importing Selected Symbols from a Module," pp. 146]{Beazley2009}
+ Extract symbolic constants into a module for easier customization of these
	constants
+ See [Software Development Process Methodologies](https://github.com/eda-ricercatore/python-sandbox/blob/main/notes/python.md#software-development-process-methodologies)
	for more information to extract symbolic constants.






###	Regular Expressions

Notes on regular expressions:
+ The core syntax of regular expression is based on the *Perl* context in
	various programming languages (*Python*, *Ruby*, and *Tcl*) and tools
	(*Egrep*, *Vi/Vim*, and *Emacs*) \cite[\S8.2, pp. 326]{Langtangen2009}.
+ A wildcard is denoted with an asterisk **\*** \cite[pp. 236]{Hetland2005}
+ As asterisk is denoted with a backslash and an asterisk **\*** \cite[pp. 236]{Hetland2005}
	- A backslash is placed before special characters, such as a backslash,
		so that they be treated as normal characters
		\cite[pp. 236]{Hetland2005}.
+ To search for repeated patterns, enclose them in brackets "(*patterns*)",
	appended by an asterisk "\*", a plus symbol "+", or a tuple "{m,n}"
	\cite[pp. 238]{Hetland2005}.
+ Functions that can be used with regular expressions
	\cite[Table 10-8, pp. 239]{Hetland2005}:
	- compile()
	- search()
	- match()
	- split()
	- finadall()
	- sub()
	- escape()
+ Use the *re.VERBOSE* flag to verbosely describe regular expressions
	with space characters, tabs, newlines, and comments
	\cite[Tip on pp. 243]{Hetland2005}.
+ By default, the repetition operators of a regular expression are
	greedy, since they will try to "match as much as possible"
	\cite[pp. 244]{Hetland2005}.
+ By placing a question mark after a repetition operator, the repetition
	operator becomes nongreedy and it will match as little as possible \cite[pp. 244]{Hetland2005}.




Resources for regular expressions and test processing:
+ \cite[\S8.2, pp. 326-362]{Langtangen2009}
+ \cite{Friedl2006}



###	Generic Programming

+ From my [Notes about Scala](https://github.com/eda-ricercatore/sardegna-scala/blob/master/notes/scala-notes.md)
	- Generic programming has a performance advantage over object-oriented
		programming, since templates carry-out known parameterization at
		compile time while object-oriented programming leaves the
		parameterization till run time \cite[\S8.9.5, pp. 432]{Langtangen2009}.
+ "The difference between generic and object-oriented programming in *Python*
	is much smaller than in *C++* because *Python* variables are not declared
	with a specific type" \cite[\S8.9.5, pp. 435]{Langtangen2009}.

Other references for generics and generic programming
+ https://github.com/python/mypy

####	Official Documentation Involving Generics

The Python Standard Library \cite{DrakeJr2016b} has documentation on generics
	in \cite[\S27.1.4]{DrakeJr2016b}, which are available from *Python 3.5* and
	are not backwards compatible.


Concepts encountered while learning how to use generic programming in *Python*:
+ Variable Annotation





###	*Python* Interface to *Git*

To use *Python* to interface with a *Git*-based repository, I can try the
	following:
+ [dulwich](https://www.dulwich.io/)
	- [Dulwich documentation](https://www.dulwich.io/docs/)
	- https://git.samba.org/?p=jelmer/dulwich.git;a=summary
+ [pygit2 - libgit2 bindings in Python](https://github.com/libgit2/pygit2)
	- This requires installation of [libgit2](https://libgit2.org/), which
		provides *C* bindings to *Git*.
		It also provides an interface for other programming languages to
			interface with *Git*.
	- Since I am unable to install *libgit2* correctly, I cannot use *pygit2*.
	- Abandon *pygit2* solution.
+ [Gittle](https://github.com/FriendCode/gittle)
	- The installation process via *pip* requires installing *pycrypto*,
		which already exists, and terminates because of the existence of
		*pycrypto*.
	- I tried installing *pycrypto* via other means, but am unable to do so.
	- Hence, I cannot experiment with *Gittle*.
+ [GitPython](https://github.com/gitpython-developers/GitPython)
	- I cannot import the *Git* module (*git*), via my *Python* script.
	- I have used *pip install GitPython* to install it, but I still cannot
		import the *Git* module (*git*) via my *Python* script.
+ Use the *Python* module *subprocess* to run commands via the command-line
	interface (CLI) to run *Git* commands to add, commit, and push additions
	and updates.








### ⚠️ Caution!!!


####	Warnings about Naming Packages and Modules

Do not name them with the same name in packages and modules of
	The Python Standard Library and other Python libraries.
Else, the naming conflict will cause packages and modules not to be
	detected/recognized. 

Similarly, we should avoid naming packages and modules based on
	commands in UNIX-like operating systems.
	This also caused problems with C++ classes and packages/modules.

####	Avoiding Certain Text Patterns In *Python* Scripts and *Jupyter* Notebooks 


Text patterns to avoid in *Python* scripts and *Jupyter* notebooks.
+ backslash "c"
	- The backslash character and the letter "c" are concatenated;
		the "c" is appended to the backslash character. 
	- For an example, check out the script *fix_order_of_names.py* in the subsubdirectory, "x-dump -> examples".
	- It will cause a syntax error.
	- `SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 5615-5616: truncated \uXXXX escape`
+ backslash "u"
	- The backslash character and the letter "u" are concatenated;
		the "u" is appended to the backslash character. 
	- For an example, check out the script *fix_order_of_names.py* in the subsubdirectory, "x-dump -> examples".
	- It will cause a syntax error.
	- `SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 5615-5616: truncated \uXXXX escape`



####	Processing Certain Text Patterns In *Python* Scripts and *Jupyter* Notebooks

The following text patterns would not be processed as it appears (or, verbatim):
+ `{\`
	- The backslash character disappears, since it and the subsequent character are not valid escape characters in Python.
+ `$\b`
	- This is because Python treats the backslash as an escape character, and `\b` translates to the backslash character.
	- This results in deleting the previous character, a `$` (open curly brace).





#	References

Citations/References that use the *LaTeX/BibTeX* notation are taken
	from my *BibTeX* database (set of *BibTeX* entries).

**If these citations/references are not found in this list of references,
	information about them can be found in my *BibTeX* database.**

+ [ParewaLabsPvtLtdStaff20XY]

	Parewa Labs Pvt. Ltd. staff, "Learn Python Programming," Parewa Labs Pvt. Ltd., Kupondole, Lalitpur, Lalitpur District, Nepal.

	Available online from {\it Programming Tutorial, Articles and Examples -- Programiz} at: \url{https://www.programiz.com/python-programming/}; last accessed on April 1, 2017.

	**[Note in my *BibTeX* database.]**

+ [WikipediaContributors2018a]

	Wikipedia contributors, "Duck typing," in *Wikipedia, The Free Encyclopedia: Type theory*, Wikimedia Foundation, San Francisco, CA, January 10, 2018.

	Available online from *Wikipedia, The Free Encyclopedia: Type theory* at: \url{https://en.wikipedia.org/wiki/Duck_typing}; March 19, 2018 was the last accessed date.

+ [WikipediaContributors2018b]

	Wikipedia contributors, "Comparison of documentation generators," in *Wikipedia, The Free Encyclopedia: Software comparisons*, Wikimedia Foundation, San Francisco, CA, February 24, 2018.

	Available online from *Wikipedia, The Free Encyclopedia: Software comparisons* at: \url{https://en.wikipedia.org/wiki/Comparison_of_documentation_generators}; March 25, 2018 was the last accessed date.

+ [WikipediaContributors2017a2]

	Wikipedia contributors, ``Non-local variable,'' in *Wikipedia, The Free Encyclopedia: Programming language theory*, Wikimedia Foundation, San Francisco, CA, September 24, 2017.

	Available online from *Wikipedia, The Free Encyclopedia: Programming language theory* at: \url{https://en.wikipedia.org/wiki/Non-local_variable}; last accessed on March 29, 2018.










## Object-Oriented *Python* Programming

+ \cite{Alchin2010}
	- Chapter 4,5-6,8.
	- Software development/engineering \cite[Chapters 8-11]{Alchin2010}.
	- Marty Alchin, "Pro Python: Advanced Coding Techniques and Tools," in The Expert's Voice$^{\textregistered}$\ in Open Source series, Apress, Berkeley, CA, 2010. DOI: https://dx.doi.org/10.1007/978-1-4302-2758-8.
+ \cite{Hall2009b}
	- Chapter 9,10,11, 8 (pp. 165).
	- Tim Hall and J.-P. Stacey, "Python 3 for Absolute Beginners: All you will ever need to start programming Python," in The Expert's Voice$^{\textregistered}$\ in Open Source series, Apress, Berkeley, CA, 2009. DOI:https://dx.doi.org/10.1007/978-1-4302-1633-9.
+ \cite{Hetland2005}
	- Chapters 6-8,9,11,13,16-19.
	- Magnus Lie Hetland, "Beginning Python: From Novice to Professional," in The Expert's Voice$^{\textregistered}$\ in Open Source series, Apress, New York, NY, 2005. DOI:https://dx.doi.org/10.1007/978-1-4302-0072-7.
+ \cite{Langtangen2006}
	- Chapter 8.6,8.8,8.10.
	- Software development/engineering \cite[Appendices A and B]{Langtangen2006}.
	- Hans Petter Langtangen, "Python Scripting for Computational Science," Second edition, Texts in Computational Science and Engineering, Volume 3, Springer-Verlag Berlin Heidelberg, Heidelberg, Germany, 2006. DOI:https://dx.doi.org/10.1007/3-540-31269-2.
+ \cite{Langtangen2009}
	- Chapter 3, 7, 9.
	- Software development/engineering \cite[Appendices A and B]{Langtangen2009}.
	- Hans Petter Langtangen, "Python Scripting for Computational Science," Third edition, in the Texts in Computational Science and Engineering series, Volume 3, Springer-Verlag Berlin Heidelberg, Heidelberg, Germany, 2009. DOI:https://dx.doi.org/10.1007/978-3-540-73916-6.
+ \cite{Langtangen2009a}
	- Chapter 8.3,8.6,8.8,8.10, Appendix B.
	- Hans Petter Langtangen, "A Primer on Scientific Programming with Python," Texts in Computational Science and Engineering, Volume 6, Springer-Verlag Berlin Heidelberg, Heidelberg, Germany, 2009. DOI:https://dx.doi.org/10.1007/978-3-642-02475-7.
+ \cite{Langtangen2011}
	- Chapter 4, 6, 7, 9.
	- Hans Petter Langtangen, "A Primer on Scientific Programming with Python," Second edition, in Springer-Verlag Berlin Heidelberg series, Texts in Computational Science and Engineering, Volume 6, Heidelberg, Germany, 2011. DOI:https://dx.doi.org/10.1007/978-3-642-18366-9.
+ \cite{Langtangen2012}
	- Chapter 4, 6, 7, 9.
	- Hans Petter Langtangen, "A Primer on Scientific Programming with Python," Third edition, in Texts in Computational Science and Engineering, Volume 6, Springer-Verlag Berlin Heidelberg, Heidelberg, Germany, 2012. DOI:https://dx.doi.org/10.1007/978-3-642-30293-0.
+ \cite{Lee2011b}
	- Chapter 4, 7.
	- Kent D. Lee, "Python Programming Fundamentals," in Undergraduate Topics in Computer Science, Springer-Verlag London, London, U.K., 2011. DOI:https://dx.doi.org/10.1007/978-1-84996-537-8.
+ \cite{Lutz2009}
	- Chapter 4,15,16-20,21-24,25-28,30-31,32-35,37,38,39.
	- Mark Lutz, "Learning Python: Powerful Object-Oriented Programming," Fourth edition, O'Reilly Media, Sebastopol, CA, 2009.
+ \cite{Lutz2010}
	- pp. 60-61, 85-88, 183-187.
	- Mark Lutz, "Python Pocket Reference: Python in your pocket," Fourth edition, O'Reilly Media, Sebastopol, CA, 2010.
+ \cite{Lutz2013}
	- Chapter 4,16-21, 22-25, 26-29, 31-32, 33-36, 39-41.
	- Software development/engineering \cite[Chapter 15]{Lutz2013}.
	- Mark Lutz, "Learning Python: Powerful Object-Oriented Programming," Fifth edition, O'Reilly Media, Sebastopol, CA, 2013.
+ \cite{Pilgrim2009}
	- Chapter 6-7, 8, 9, 10.
	- Mark Pilgrim, "Dive Into Python 3," Apress, Berkeley, CA, 2009. DOI:https://dx.doi.org/10.1007/978-1-4302-2416-7.
+ \cite{Ucoluk2012}
	- Chapter 7.
	- Gokturk Ucoluk and Sinan Kalkan, "Introduction to Programming Concepts with Case Studies in Python," Springer-Verlag Wien, Vienna, Austria, 2012. DOI:https://dx.doi.org/10.1007/978-3-7091-1343-1.






























## Domain Applications of *Python* Programming

+ Algorithm analysis.
	- \cite{Hetland2010}.
	- Table of common computational complexities cite[\S5.1.1, pp. 157]{Ucoluk2012}
+ Data structures.
	- \cite{Lutz2011,Lutz2013,Sweigart2015,Ucoluk2012}.
	-
	- **Read this!!!**
+ **Database management**.
	- \cite{Hetland2005,Lutz2010,Lutz2011,Sileika2010,Younker2008}.
+ Functional programming.
	- \cite{Beazley2009,Lutz2009,Lutz2013}.
	- **Read this!!!**
+ GUI development.
	- \cite{Gift2008,Hall2009b,Hetland2005,Langtangen2009,Lee2011b,Lutz2010,Lutz2011,Vaingast2009}.
+ **Machine learning**.
	- \cite{Unpingco2016}.
+ Network programming.
	- \cite{Goerzen2004,Hetland2005,Lutz2011,Rhodes2010,Sileika2010}.
+ **Numerical methods, or numerical computing**.
	- \cite{Langtangen2006,Langtangen2009,Langtangen2009a,Langtangen2011,Langtangen2012,Linge2016}.
+ **Parallel programming**.
	- \cite{Gift2008,Lutz2011} \cite[Chapter 20, pp. 413-447]{Beazley2009}.
+ **Scientific computing, computational science, and computational engineering**.
	- \cite{Langtangen2006,Langtangen2009}.
	- \cite{Langtangen2009a,Langtangen2011,Langtangen2012}
	- \cite{Vaingast2009}
+ **Software development** and **software engineering**.
	- \cite[Chapters 8-11]{Alchin2010}.
	- \cite[Appendices A and B]{Langtangen2006}.
	- \cite[Appendices A and B]{Langtangen2009}.
	- \cite[Chapter 21]{Lutz2011}.
	- \cite[Chapter 15]{Lutz2013}.
	- \cite{Younker2008}.
+ **Statistical analysis**.
	- \cite{Saha2015,Sileika2010,Unpingco2016}.
+ Task automation.
	- \cite{Sweigart2015}
+ UNIX/Linux system administration.
	- \cite{Gift2008,Sileika2010,Sweigart2015}.
+ Web development.
	- \cite{Hetland2005,Langtangen2006,Langtangen2009,Pilgrim2009,Rhodes2010,Sileika2010,Younker2008}.
















## Mixed-Language Software Development

+ \cite{Langtangen2006}
	- Chapter 5,10, Appendix B.
	- Hans Petter Langtangen, "Python Scripting for Computational Science," Second edition, Texts in Computational Science and Engineering, Volume 3, Springer-Verlag Berlin Heidelberg, Heidelberg, Germany, 2006. DOI:https://dx.doi.org/10.1007/3-540-31269-2.
+ \cite{Langtangen2009}
	- Chapter 5,10, Appendix B.
	- Hans Petter Langtangen, "A Primer on Scientific Programming with Python," Texts in Computational Science and Engineering, Volume 6, Springer-Verlag Berlin Heidelberg, Heidelberg, Germany, 2009. DOI:https://dx.doi.org/10.1007/978-3-642-02475-7.
+ \cite{Lutz2011}
	- Chapter 20.
	- Mark Lutz, "Programming Python: Powerful Object-Oriented Programming," Fourth edition, O'Reilly Media, Sebastopol, CA, 2011.




##	Additional *Python* Resources

Additional *Python* resources from my *BibTeX* database:
+ \cite{Brandl2017a}

	Georg Brandl and Benjamin Peterson and Senthil Kumaran and Guido {van Rossum} and Chris Jerdonek and Andrew Kuchling, "The *Python* Tutorial," Python Software Foundation, Beaverton, OR, March 26, 2017.

	Available online from *Welcome to Python.org: Python 3.6.1 documentation* at: https://docs.python.org/3/tutorial/; April 4, 2017 was the last accessed date.

+ \cite{DrakeJr2018a}

	Fred L. Drake, Jr. and David Goodger and Fredrik Lundh, "Python/C API Reference Manual," Python Software Foundation, Beaverton, OR, April 1, 2018.

	Available online from *Welcome to Python.org: Python 3.6.5 documentation* at: https://docs.python.org/3/c-api/; April 2, 2018 was the last accessed date.

+ \cite{DrakeJr2018}
	Fred L. Drake, Jr. and David Goodger and Fredrik Lundh, "Extending and Embedding the *Python* Interpreter," Python Software Foundation, Beaverton, OR, April 1, 2018.

	Available online from *Welcome to Python.org: Python 3.6.5 documentation* at: https://docs.python.org/3/extending/; April 2, 2018 was the last accessed date.

+ \cite{DrakeJr2017c}

	Fred L. Drake, Jr. and David Goodger and Fredrik Lundh, "*Python* 3.6.1 documentation," Python Software Foundation, Beaverton, OR, March 31, 2017.

	Available online at: https://docs.python.org/3/; March 31, 2017 was the last accessed date.

+ \cite{DrakeJr2016b}

	Fred L. Drake, Jr. and David Goodger and Fredrik Lundh, "The *Python* Standard Library," Python Software Foundation, Beaverton, OR, March 23, 2016.

	Available online from *Python 3.5.1 documentation* at: https://docs.python.org/3/library/; April 1, 2016 was the last accessed date.

+ \cite{DrakeJr2016a}

	Fred L. Drake, Jr. and David Goodger and Fredrik Lundh, "The *Python* Language Reference," Python Software Foundation, Beaverton, OR, March 31, 2016.

	Available online from *Python 3.5.1 documentation* at: https://docs.python.org/3/reference/index.html; April 1, 2016 was the last accessed date.

+ \cite{Thurlow2012}

	Steven Thurlow, "A Beginner's Python Tutorial," GitHub, Inc., San Francisco, CA, March 30, 2012.

	Available online from *Steven Thurlow's GitHub repository* at: https://github.com/stoive/pythontutorial; self-published; April 4, 2017 was the last accessed date.

+ \cite{Ziade2008}

	Tarek Ziade, "Expert *Python* Programming," Packt Publishing, Birmingham, West Midlands, England, U.K., 2008.


Lists of online resources can be found at:
+ \cite[Appendix C, pp. 571--573]{Hetland2005}






##	Books Covered

+ \cite{Alchin2010}
+ \cite{Beazley2009}
+ \cite{Hall2009b}
+ \cite{Hetland2005}
+ \cite{Langtangen2009}
+ \cite{Langtangen2012}
+ \cite{Lee2011b}
+ \cite{Lutz2010}
+ \cite{Lutz2011}
+ \cite{Lutz2013}
+ \cite{Pilgrim2009}
	- This book does not include academically/intellectually rigorous details.
+ \cite{Sweigart2015}






Books that I am skipping
+ \cite{Langtangen2009a}
+ \cite{Langtangen2011}





Recommendations:
+ \cite{Beazley2009,Lutz2013} are good books that provide a lot of depth in
	functional programming, object-oriented *Python* programming,




Read these:
+ \cite{}
+ \cite{}
+ \cite{}
+ \cite{}
+ \cite{}
+ \cite{}
+ \cite{}
+ \cite{}
+ \cite{}


































# Random

+ https://www.tutorialspoint.com/python/python_if_else.htm
+ https://dev.to/ogwurujohnson/distinguishing-instance-variables-from-class-variables-in-python-81
+ https://softwareengineering.stackexchange.com/questions/340383/assigning-instance-variables-in-function-called-by-init-vs-function-called
+ http://www.dummies.com/programming/python/working-with-variables-in-python/
+ https://medium.com/the-renaissance-developer/python-101-object-oriented-programming-part-2-8e0db3ddd531
+ https://www.tutorialspoint.com/python/python_classes_objects.htm
+ https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/Python1_Basics.html
+ http://kronosapiens.github.io/blog/2014/05/10/from-ruby-to-python.html
+ https://docs.python.org/3.5/tutorial/classes.html?highlight=inheritance#inheritance
+ https://softwareengineering.stackexchange.com/questions/254576/is-it-a-good-practice-to-declare-instance-variables-as-none-in-a-class-in-python
+ https://syntaxdb.com/ref/python/class-variables
+ https://docs.python.org/2/tutorial/classes.html
+ https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3
+ https://www.python-course.eu/python3_class_and_instance_attributes.php
+ http://home.wlu.edu/~lambertk/pythontojava/InstanceVariables.htm
+ https://timothyawiseman.wordpress.com/2012/10/06/class-and-instance-variables-in-python-2-7/






#	Author Information

The MIT License (MIT)

Copyright (c) <2017> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.
