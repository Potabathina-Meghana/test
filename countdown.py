import time
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")
countdown(5)


#Capitalize
my_string="programiz is lit"
print(my_string[0].upper()+my_string[1:])

#Capitalize using inbuilt
my_string="programiz is lit"
cap_string=my_string.capitalize()
print(cap_string)

