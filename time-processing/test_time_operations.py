#!/usr/local/bin/python3
###	#!/Users/zhiyang/anaconda3/bin/python3

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