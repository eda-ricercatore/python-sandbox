#!/Users/zhiyang/anaconda3/bin/python

#	#!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to process BibTeX fields.

	Synopsis: command name
	./bibtex_processing.py


	Revision History:
	February 25, 2023			Version 0.1, initial build.
"""


#	The MIT License (MIT)

#	Copyright (c) <2023> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?

#	==========================================================

__author__ = 'Zhiyang Ong'
__version__ = '0.1'
__date__ = 'February 25, 2025'

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
	filecmp		For file comparison.
	datetime	For operations regarding date and time.
"""

import sys
import os
import os.path
from subprocess import call
import time
import warnings
import re
import filecmp
import datetime


###############################################################


"""
	Method to format the list of authors names correctly.
	@param list_of_authors - A list of names of author(s).
	@return a string containing the list of names of author(s)
		that are comma separated, rather than by " and ";
		if list_of_authors refers to a None object, return an
			empty string.
"""
def process_author_field(list_of_authors=None):
	# Is the list of author names not a None object?
	if list_of_authors is not None:
		# Yes. Delimit the names of the authors by " and ".
		list_of_authors_delimited = list_of_authors.split(" and ")
		# Final list of names of authors.
		list_of_authors_final = ""
		for index, name in enumerate(list_of_authors_delimited):
			if 0 == index:
				list_of_authors_final = name
			elif ((len(list_of_authors_delimited) - 1) == index):
				list_of_authors_final = list_of_authors_final + ", and " + name
			else:
				list_of_authors_final = list_of_authors_final + ", " + name
		return list_of_authors_final
	else:
		# No, it is a None object. Return an empty string.
		return ""





"""
	Method to format how the 'Howpublished' field is italicized.
	@param howpublished_field - string containing information for
		the 'Howpublished' field.
	@param markdown_italicization - boolean flag that indicates
		if the 'Howpublished' field should be italicized in
		Markdown format or remain in LaTeX format.
	@return a string containing the 'Howpublished' field that is
		italicized in the format specified by the boolean flag,
		'markdown_italicization'.
"""
def process_howpublished_field(howpublished_field="", markdown_italicization=True):
	"""
		Should the 'Howpublished' field should be italicized in
			Markdown format?
	"""
	if markdown_italicization:
		"""
			Yes. Change the italicization format from LaTeX to Markdown.
			Replace "{\it " substring to "*".
		"""
		howpublished_field_for_markdown = howpublished_field.replace("{\it ","*")
		# Replace "} and {\it " substring to "* and *".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}} and {\it ","* and *")
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("} and {\it ","* and *")
		#howpublished_field_for_markdown = re.sub("} and {\it ","\* and \*",howpublished_field_for_markdown)
		# Replace "}, and {\it " substring to "*, and *".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}}, and {\it ","*, and *")
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}, and {\it ","*, and *")
		#howpublished_field_for_markdown = re.sub("}, and {\it ","*, and *",howpublished_field_for_markdown)
		# Replace "} via {\it " substring to "* via *".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}} via {\it ","* via *")
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("} via {\it ","* via *")
		#howpublished_field_for_markdown = re.sub("} via {\it ","* via *",howpublished_field_for_markdown)
		# Replace "} as " substring to "* as ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}} as "," as ")
		#howpublished_field_for_markdown = re.sub("} as "," as ",howpublished_field_for_markdown)
		# Replace "}, at: \url{" substring to "*, at: ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}}, at: \\url{","*, at: ")
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}, at: \\url{","*, at: ")
		#howpublished_field_for_markdown = re.sub("}, at: \\url{","*, at: ",howpublished_field_for_markdown)
		# Replace "} at: \url{" substring to "* at: ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}} at: \\url{","* at: ")
		# Replace "} at: \url{" substring to "* at: ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("} at: \\url{","* at: ")
		#howpublished_field_for_markdown = re.sub("} at: \\url{","* at: ",howpublished_field_for_markdown)
		# Replace " at: \url{" substring to "* at: ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace(" at: \\url{"," at: ")
		#howpublished_field_for_markdown = re.sub(" at: \\url{"," at: ",howpublished_field_for_markdown)
		# Replace "}, \url{" substring to ", ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}}, \\url{",", ")
		#howpublished_field_for_markdown = re.sub("}, \\url{",", ",howpublished_field_for_markdown)
		# Replace "} and \url{" substring to " and ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}} and \\url{"," and ")
		#howpublished_field_for_markdown = re.sub("} and \\url{"," and ",howpublished_field_for_markdown)
		# Replace "}, and \url{" substring to ", and ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}}, and \\url{",", and ")
		# Replace "}; " substring to "; ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}}; ","; ")
		"""
			Replace "}, " substring to "*, ".

			This can resolve some bugs, but also introduces other bugs.
			
			This is because there are instances of "}, " that should
				be replaced, but not in other instances.
		"""
		#howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}, ","*, ")
		# Add a period to the modified 'Howpublished' field.
		howpublished_field_for_markdown = howpublished_field_for_markdown + "."
		# Replace "}." substring to "*.".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}.","*.")
		# Return the modified 'Howpublished' field in Markdown format.
		return howpublished_field_for_markdown
	else:
		# No. Return string for 'Howpublished' field without modification.
		return howpublished_field












###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	list_of_authors_names = ["Hannah Augur", "Fred L. {Drake, Jr.} and David Goodger and Fredrik Lundh", "{Yale Department of Computer Science staff}", "David Money Harris", "Jonathan W. Valvano", "H. Baher", "Alberto {Sangiovanni-Vincentelli} and Grant Martin", "W. Ces{\'{a}}rio and A. Baghdadi and L. Gauthier and D. Lyonnard and G. Nicolescu and Y. Paviot and S. Yoo and A. A. Jerraya and M. {Diaz-Nava}", "Rudolf Kruse and Christian Borgelt and Frank Klawonn and Christian Moewes and Matthias Steinbrecher and Pascal Held", "Dikembe Mutombo Mpolondo Mukamba Jean-Jacques Wamutombo", "Kenneth A. {De Jong} and Dikembe Mutombo Mpolondo Mukamba Jean-Jacques Wamutombo and {William {Strunk, Jr.} and E. B. White and Ramprasad S. Krishnamachari and Panos Y. Papalambros and {Editors of Scientific American} and Juan Carlos Cuevas and Elke Scheer and {Jean-Pierre} Launay and Michel Verdaguer"]
	for authors_names in list_of_authors_names:
		print("= Original names:",authors_names,"=")
		print("= Processed names:",process_author_field(authors_names),"=")
	"""
		Failed cases:

		Problems:
		+ Last curly brace was replaced with an asterisk, when it should not be.
		Available as software version {TLM2.0.1} and document version {JA32}
		Available as software version {TLM2.0.1} and document version {JA32*.

		Problems:
		+ Last curly brace was replaced with an asterisk, when it should not be.
		Available as: Companion {CD}
		Available as: Companion {CD*.

		Problems:
		+ "}; "
		+ "{\r" removes information from the string.
			- Missing information.
		Available online from {\it {mass:werk} -- media environments: {JS/UIX}} and {\it {mass:werk} -- media environments: Products {\rm \&}\ Demos: Legacy Demos: {JS/UIX} (2003)} at: \\url{https://www.masswerk.at/jsuix/}; June 10, 2022 was the last accessed date
		Available online from {\it {mass:werk} -- media environments: {JS/Um \&}\ Demos: Legacy Demos: {JS/UIX} (2003)} at: \\url{https://www.masswerk.at/jsuix/}; June 10, 2022 was the last accessed date
		Available online from *{mass:werk} -- media environments: {JS/UIX}} m \&}\ Demos: Legacy Demos: {JS/UIX} (2003)* at: https://www.masswerk.at/jsuix/}; June 10, 2022 was the last accessed date.

		Problems:
		+ "}, and {\it "
		+ "} "
			- or, "} via {\it "
		+ "}, \url{"
		+ "}, and \url{"
		+ "}; "
		Available online from {\it University of Illinois at Urbana-Champaign: University Library: {IDEALS} -- Illinois Digital Environment for Access to Learning and Scholarship: Graduate Dissertations and Theses at Illinois}, and {\it {ProQuesm \&}\ Theses} via {\it {ProQuest} Dissertations Publishing}, at: \url{http://hdl.handle.net/2142/57454}, \url{https://www.ideals.illinois.edu/handle/2142/57454}, and \url{https://www.proquest.com/docview/302061118}; June 15, 2022 was the last accessed date
		Available online from *University of Illinois at Urbana-Champaign: University Library: {IDEALS} -- Illinois Digital Environment for Access to Learning and Scholarship: Graduate Dissertations and Theses at Illinois}, and *{ProQuest}: Dissem \&}\ Theses} via *{ProQuest} Dissertations Publishing*, at: http://hdl.handle.net/2142/57454}, \url{https://www.ideals.illinois.edu/handle/2142/57454}, and \url{https://www.proquest.com/docview/302061118}; June 15, 2022 was the last accessed date.

		Problems:
		+ "} as Version"
		+ "} and \url{"
		+ "}; "
		Available online from {\it {PyData}: pandas: Documentation} as Version 1.5.3 at: \url{https://pandas.pydata.org/docs/} and \url{https://pandas.pydata.org/pandas-docs/stable/index.html}; February 10, 2023 was the last accessed date
		Available online from *{PyData}: pandas: Documentation} as Version 1.5.3 at: https://pandas.pydata.org/docs/} and \url{https://pandas.pydata.org/pandas-docs/stable/index.html}; February 10, 2023 was the last accessed date.

		Problems:
		+ "}, \url{"
		+ "}, and \url{"
		+ "}; "
		Available online at: \url{http://hdl.handle.net/1721.1/111880}, \url{https://dspace.mit.edu/handle/1721.1/111880}, and \url{https://dspace.mit.edu/bitstream/handle/1721.1/111880/1004959482-MIT.pdf?sequence=1&isAllowed=y}; February 25, 2023 was the last accessed date
		Available online at: http://hdl.handle.net/1721.1/111880}, \url{https://dspace.mit.edu/handle/1721.1/111880}, and \url{https://dspace.mit.edu/bitstream/handle/1721.1/111880/1004959482-MIT.pdf?sequence=1&isAllowed=y}; February 25, 2023 was the last accessed date.

		Problems:
		+ "} and {\it "
		+ "}, \url{"
		+ "}, and \url{"
		+ "}; "
		Available online from {\it The University of Utah: John and Marcia Price College of Engineering: Kahlert School of Computing: Prof. Erik Brunvand's Web page: Teaching\dots: CS 5789 Embedded Systems and Kinetic Art: Embedded Systems and Kinetic Art: Other Information\dots: From {SIGGRAPH} 2013, (Computer Graphics) July 2013: Arts/Tech Collaboration with Embedded Systems and Kinetic Art} and {\it The University of Utah: John and Marcia Price College of Engineering: Kahlert School of Computing: Prof. Erik Brunvand's Web page: Kinetic Art and Embedded Systems: From {SIGGRAPH} 2013, July 2013: Arts/Tech Collaboration with Embedded Systems and Kinetic Art} at: \url{https://my.eng.utah.edu/~cs5789/misc/SIGGRAPH-Kinetic.pdf}, \url{https://users.cs.utah.edu/~elb/Papers/SIGGRAPH-Kinetic.pdf}, and \url{https://my.eng.utah.edu/~cs5789/}; March 18, 2023 was the last accessed date
		Available online from *The University of Utah: John and Marcia Price College of Engineering: Kahlert School of Computing: Prof. Erik Brunvand's Web page: Teaching\dots: CS 5789 Embedded Systems and Kinetic Art: Embedded Systems and Kinetic Art: Other Information\dots: From {SIGGRAPH} 2013, (Computer Graphics) July 2013: Arts/Tech Collaboration with Embedded Systems and Kinetic Art} and *The University of Utah: John and Marcia Price College of Engineering: Kahlert School of Computing: Prof. Erik Brunvand's Web page: Kinetic Art and Embedded Systems: From {SIGGRAPH} 2013, July 2013: Arts/Tech Collaboration with Embedded Systems and Kinetic Art* at: https://my.eng.utah.edu/~cs5789/misc/SIGGRAPH-Kinetic.pdf}, \url{https://users.cs.utah.edu/~elb/Papers/SIGGRAPH-Kinetic.pdf}, and \url{https://my.eng.utah.edu/~cs5789/}; March 18, 2023 was the last accessed date.

		Problems:
		+ "} and \url{"
		Available online from {\it Brown University: Office of the Provost: Brown University Library: Brown Digital Repository: Discover: Browse Collections: {BDR} Collections: Department of Religious Studies: Religious Studies Theses and Dissertations} at: \url{https://dx.doi.org/10.7301/Z0ZP44G3} and \url{https://repository.library.brown.edu/studio/item/bdr:419480/}; May 2, 2022 was the last accessed date
		Available online from *Brown University: Office of the Provost: Brown University Library: Brown Digital Repository: Discover: Browse Collections: {BDR} Collections: Department of Religious Studies: Religious Studies Theses and Dissertations* at: https://dx.doi.org/10.7301/Z0ZP44G3} and \url{https://repository.library.brown.edu/studio/item/bdr:419480/}; May 2, 2022 was the last accessed date.

		Problems:
		+ "}; "
		Available online from {\it Logic Poet} at: \url{http://www.logicpoet.com/systemc/}; March 30, 2010 was the last accessed date
		Available online from *Logic Poet* at: http://www.logicpoet.com/systemc/}; March 30, 2010 was the last accessed date.



		

		Available online from {\it Logic Poet} at: \\url{http://www.logicpoet.com/systemc/}; March 30, 2010 was the last accessed date
		Available online from *Logic Poet} at: http://www.logicpoet.com/systemc/}; March 30, 2010 was the last accessed date.
	"""
	list_of_howpublished_field = ["Available online from {\it Logic Poet} at: \\url{http://www.logicpoet.com/systemc/}; March 30, 2010 was the last accessed date", "Available as Version 2.0-{Q}", "Available online from {\it Brown University: Office of the Provost: Brown University Library: Brown Digital Repository: Discover: Browse Collections: {BDR} Collections: Department of Religious Studies: Religious Studies Theses and Dissertations} at: \\url{https://dx.doi.org/10.7301/Z0ZP44G3} and \\url{https://repository.library.brown.edu/studio/item/bdr:419480/}; May 2, 2022 was the last accessed date", "Available online from {\it The University of Utah: John and Marcia Price College of Engineering: Kahlert School of Computing: Prof. Erik Brunvand's Web page: Teaching\dots: CS 5789 Embedded Systems and Kinetic Art: Embedded Systems and Kinetic Art: Other Information\dots: From {SIGGRAPH} 2013, (Computer Graphics) July 2013: Arts/Tech Collaboration with Embedded Systems and Kinetic Art} and {\it The University of Utah: John and Marcia Price College of Engineering: Kahlert School of Computing: Prof. Erik Brunvand's Web page: Kinetic Art and Embedded Systems: From {SIGGRAPH} 2013, July 2013: Arts/Tech Collaboration with Embedded Systems and Kinetic Art} at: \\url{https://my.eng.utah.edu/~cs5789/misc/SIGGRAPH-Kinetic.pdf}, \\url{https://users.cs.utah.edu/~elb/Papers/SIGGRAPH-Kinetic.pdf}, and \\url{https://my.eng.utah.edu/~cs5789/}; March 18, 2023 was the last accessed date", "Available online at: \\url{http://hdl.handle.net/1721.1/111880}, \\url{https://dspace.mit.edu/handle/1721.1/111880}, and \\url{https://dspace.mit.edu/bitstream/handle/1721.1/111880/1004959482-MIT.pdf?sequence=1&isAllowed=y}; February 25, 2023 was the last accessed date", "Available online from {\it {PyData}: pandas: Documentation} as Version 1.5.3 at: \\url{https://pandas.pydata.org/docs/} and \\url{https://pandas.pydata.org/pandas-docs/stable/index.html}; February 10, 2023 was the last accessed date", "Available online from {\it University of Illinois at Urbana-Champaign: University Library: {IDEALS} -- Illinois Digital Environment for Access to Learning and Scholarship: Graduate Dissertations and Theses at Illinois}, and {\it {ProQuest}: Dissertations {\rm \&}\ Theses} via {\it {ProQuest} Dissertations Publishing}, at: \\url{http://hdl.handle.net/2142/57454}, \\url{https://www.ideals.illinois.edu/handle/2142/57454}, and \\url{https://www.proquest.com/docview/302061118}; June 15, 2022 was the last accessed date", "Available online from {\it {mass:werk} -- media environments: {JS/UIX}} and {\it {mass:werk} -- media environments: Products {\rm \&}\ Demos: Legacy Demos: {JS/UIX} (2003)} at: \\url{https://www.masswerk.at/jsuix/}; June 10, 2022 was the last accessed date", "Available as: Companion {CD}", "Available as software version {TLM2.0.1} and document version {JA32}", "Available as Version 1.1 from the {\it Transaction Level Modeling Working Group}", "Also available from {\it Proceedings of the $2^{nd}$\ Annual International Symposium on Computer Architecture ({ISCA '75})}", "Self-published", "Available as the {\it Proceedings of the Conference on Iterative Methods for Large Linear Systems}", "{This book contains the `Proceedings of the {NATO} Advanced Study Institute on Software Systems Safety,' Summer School Marktoberdorf 2013, which was a summer program held in Marktoberdorf, Germany, July 30 -- August 11, 2013", "This chapter is part of a book containing the `Proceedings of the {NATO} Advanced Study Institute on Software Systems Safety,' Summer School Marktoberdorf 2013, which was a summer program held in Marktoberdorf, Germany, July 30 -- August 11, 2013", "Also published by Garland Publishing Company, New York, {NY}, 1979, in its {\it Outstanding Dissertations in the Computer Sciences Series}", "It is a modification of the Proceedings of the International Conference on Statistical Methods and Statistical Computing for Quality and Productivity Improvement ({ICSQP'95}), Seoul, South Korea, August 1995", "Available online from {\it Michigan State University: MSU College of Communication Arts and Sciences: School of Journalism}", "Received a copy of this report by email", "Reprinted with corrections", "Version 4.0", "Emailed course material for {\it ECEN 694 Nanobiotechnology}", "Available as Version {P2.0}, Second edition, on October 28, 2019", "Published again on January 12, 2012 by Lulu Enterprises"]
	for cur_howpublished_field in list_of_howpublished_field:
		print("= Before default:",cur_howpublished_field,"=")
		print("= After default:",process_howpublished_field(cur_howpublished_field),"=")
		print("------------------------------------------------")
		print("= Before Markdown:",cur_howpublished_field,"=")
		print("= After Markdown:",process_howpublished_field(cur_howpublished_field, True),"=")
		print("------------------------------------------------")
		print("= Before LaTeX:",cur_howpublished_field,"=")
		print("= After LaTeX:",process_howpublished_field(cur_howpublished_field, False),"=")
		print("================================================")
