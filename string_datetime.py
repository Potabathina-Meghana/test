from datetime import datetime
my_date_time="Jul 31 2001 11:15PM"
date_time_object=datetime.strptime(my_date_time , '%b %d %Y %I:%M%p')
print(type(date_time_object))
print(date_time_object) 

#using dateutil module
from dateutil import parser

date_time = parser.parse("Mar 11 2011 11:31AM")

print(date_time)
print(type(date_time))
