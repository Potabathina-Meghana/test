'''
In Python, strftime() is a method available for datetime objects.
 It stands for "string format time" and is used to convert a datetime object into a formatted string representing the date and time. 
 The method allows you to specify a format string that defines how the date and time components should be represented in the output string.
 '%Y-%m-%d %H:%M:%S'
'''


from datetime import datetime

import unittest
class test_datetime(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(function_format(my_date_string1),'2011-03-11 11:31:00' )
    def test_case2(self):
        self.assertEqual(function_format(my_date_string2),'2011-04-03 23:31:00' )
def function_format(my_data):
    datetime_object = datetime.strptime(my_data, '%b %d %Y %I:%M%p')
    return datetime_object.strftime('%Y-%m-%d %H:%M:%S')
my_date_string1 = "Mar 11 2011 11:31AM"
my_date_string2 = "Apr 3 2011 11:31PM"
result1=function_format(my_date_string1)
print(result1)
result2=function_format(my_date_string2)
print(result2)

if __name__=='__main__':
  unittest.main()

