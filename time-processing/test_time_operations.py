#!/usr/local/bin/python3
###	#!/Users/zhiyang/anaconda3/bin/python3

"""
	This is written by Zhiyang Ong to test operations to get timestamps
		and date-timestamps.



	Synopsis: command name and [argument(s)]
	./test_time_operations.py

	

	


	Notes/Assumptions:
	Since I would be categorizing and storing the experimental results
		based on the year and month, the filename containg experimental
		results would be named in the DD-MM-YY-HH-MM-SS-uS format so that
		I can quickly find the file of a given build (or experimental
		run) as I read the filename from left to right.



	References:
	[SaltyCrane2014]
		Eliot "Salty Crane", "How to get the current date and time in Python," from Salty Crane Blog, June 26, 2008. Available online from Salty Crane Blog at: https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/; modified on October 22, 2014; self-published; August 31, 2018 was the last accessed date

	[DrakeJr2016b, datetime module, Section 8.1.4 datetime Objects, now() function]

	[DrakeJr2023i, The Python Standard Library: Generic Operating System Services: time -- Time access and conversions: Functions]
		https://docs.python.org/3/library/time.html#time.strptime
		https://docs.python.org/3/library/time.html#time.strftime


	Revision History:
	April 17, 2017			Version 0.1, initial build.
"""


#	The MIT License (MIT)

#	Copyright (c) <2014-2017> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; print " "; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d "\n" | tr -d 'ir' | tr y "\n"
#	Che cosa significa?

#	==========================================================

__author__ = 'Zhiyang Ong'
__version__ = '0.1'
__date__ = 'Apr 17, 2017'

###############################################################


#	Import modules from The Python Standard Library.

import time
#from datetime import date
#from datetime import datetime
#from datetime import date, datetime, tzinfo, timezone
from datetime import date, datetime, timezone
#import datetime

#utctimestamp = datetime.utcfromtimestamp()
utctimestamp = date.fromtimestamp(time.time())
print("1) current time, date.fromtimestamp(time.time()), is:",utctimestamp,"=")
#utctimestamp = datetime.utcfromtimestamp(time.time())
#print("current time is:",utctimestamp,"=")
utctimestamp = time.time()
print("2) current time, time.time(), is:",utctimestamp,"=")
utctimestamp = time.time_ns()
print("2a) current time, time.time_ns(), is:",utctimestamp,"=")
#utctimestamp = datetime.utcnow()
#utctimestamp = datetime.now()
"""
utctimestamp = datetime.utcnow().timestamp()
print("3) current time is:",utctimestamp,"=")
utctimestamp = datetime.utcnow()
print("4) current time is:",utctimestamp,"=")
"""

current_milli_time = lambda: int(round(time.time() * 1000))
print("4a) current time, lambda: int(round(time.time() * 1000)), is:",current_milli_time,"=")
current_milli_time = int(round(time.time() * 1000))
print("5) current time, int(round(time.time() * 1000)), is:",current_milli_time,"=")


"""
	Conclusion:
		Use time.time() to measure time in seconds.
"""
utctimestamp = time.time()
print("current time, time.time(), is:",utctimestamp,"=")
current_date = date.fromtimestamp(utctimestamp)
print("current date, date.fromtimestamp(time.time()), is:",current_date,"=")
current_date_time = datetime.fromtimestamp(utctimestamp)
print("current date, datetime.fromtimestamp(time.time()), is:",current_date_time,"=")
current_date_time = datetime.utcfromtimestamp(utctimestamp)
print("current date, datetime.utcfromtimestamp(time.time()), is:",current_date_time,"=")
#current_date_time = datetime(tzinfo=timezone.utc).timestamp()
#current_date_time = time.time()
current_date_time = datetime.now()
current_date_time = current_date_time.replace(tzinfo=timezone.utc)
print("current date, datetime.now().replace(tzinfo=timezone.utc), is:",current_date_time,"=")
#utctimestamp = time.gmtime()
#print("current time, time.gmtime(), is:",utctimestamp,"=")

"""
	Remarks/Comments:
	
	Unix time (also known as Epoch time,[1][2][3] POSIX time,[4] seconds since the Epoch,[5] or UNIX Epoch time[6]) is a system for describing a point in time.
		References:
			Wikipedia contributors, ``Unix time,'' in *Wikipedia, The Free Encyclopedia: Calendaring standards*, Wikimedia Foundation, San Francisco, CA, September 15, 2019. Available online from *Wikipedia, The Free Encyclopedia: Calendaring standards* at: *https://en.wikipedia.org/wiki/Unix_time; last accessed on September 16, 2019.
			\cite[time — Time access and conversions]{DrakeJr2016b}
				https://docs.python.org/3/library/time.html#time.time

	Hence, using the time.time() method to obtain the timestamp will
		provide the timestamp in UTC time zone.
	
	Hence, use time.time() to record the timestamp in UTC time zone,
		and avoid confusion between time zones on projects with
		geographically distributed contributors/collaborators.
"""
print("============================================================")
"""
	From [DrakeJr2023i, The Python Standard Library: Generic Operating System Services: time -- Time access and conversions: Functions]
"""
# Has microsecond feature.
#current_time = time.strptime("%B-%d-%Y-%H-%M-%S-%f")
# Has no microsecond feature.
#current_time = time.strptime("%B-%d-%Y-%H-%M-%S")
# Has no second feature.
#current_time = time.strptime("%B-%d-%Y-%H-%M", gmtime())
current_time = time.asctime()
print("	time.asctime() is:",current_time,"=")
current_time = time.ctime()
print("	time.ctime() is:",current_time,"=")
current_time = time.localtime()
print("	time.localtime() is:",current_time,"=")


month_number_to_text = {1:"january", 2:"february", 3:"march", 4:"april", 5:"may", 6:"june", 7:"july", 8:"august", 9:"september", 10:"october", 11:"november", 12:"december"}
print("month_number_to_text is:",month_number_to_text,"=")
print("month_number_to_text[current_time.tm_mon] is:",month_number_to_text[current_time.tm_mon],"=")
date_timestamp = month_number_to_text[current_time.tm_mon] + "-" + str(current_time.tm_mday) + "-" + str(current_time.tm_year) + "-" + str(current_time.tm_hour) + "-" + str(current_time.tm_min)
print("	processed date-timestamp is:", date_timestamp, "=")
current_time = time.gmtime()
print("	time.gmtime() is:",current_time,"=")