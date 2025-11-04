import sqlite3 #We're going to work with an SQL database later, so let's get this started
from datetime import datetime #we need dates

#The purpose of this programme is to pick a colour scheme given the day of the week
#And an outfit choice given the formality of the day's activities and the temperature (this requires SQL)
#And a selection of accessories given the day's activities (this is also SQL)
#Eventually, I'll also add functionality for evening activities and sports

weekday=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
today=datetime.today().strftime('%d-%m-%Y')
day=datetime.strptime(today,"%d-%m-%Y")
day_of_the_week=weekday[day.isoweekday()-1]
print("The day today is {0}".format(day_of_the_week))
correct=input("Is that correct? Y/N ")
if correct.upper()=="Y":
    picker_day=day_of_the_week
else:
    picker_day=input("What day is it? Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday ")

def colour_picker(picker_day): 
    colour_dict={"Monday":"Gray","Tuesday":"Blue", "Wednesday":"Black","Thursday": "Red","Friday":"Green","Saturday":"Brown","Sunday": "Brown"}
    colour=colour_dict.get(picker_day)
    print("The colour for your selected day is {0}".format(colour))

def workday(picker_day):
    if picker_day =="Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
        double_check=input("I'm assuming you'll be working today, correct? Y/N ")
        if double_check.upper()=="Y":
            print("Great! We'll take note of that.")
            daytype="workday"
        if double_check.upper()=="N":
            print("Great! We'll take note of that.")
            daytype="holiday"
        print("Today is a {0}.".format(daytype))
        return daytype
            
colour_picker(picker_day)
workday(picker_day)