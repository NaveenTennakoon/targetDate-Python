#!/usr/bin/env python 3
"""
OPS435 Assignment 1 - Fall 2019
Program: a1_[student_id].py (replace student_id with your Seneca User name)
Author: "Student Name"
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
"""

import sys
import os

def usage():
    """
    usage() takes no arguments inside the parameters. This shows the usage 
    of how many arguments should be provided to the script to make it run 
    properly if the entered arguments are in an incorrect format.
    e.g. a1_rchan.py --step 2018/01/02 
            -> "Usage: a1_rchan.py [--step] YYYY/MM/DD +/-n"
         a1_rchan.py 2018/01/02        
            -> "Usage: a1_rchan.py [--step] YYYY/MM/DD +/-n"
    """
    print("Usage: "+ sys.argv[0] + " [--step] YYYY/MM/DD +/-n")

def after(date):
    """
    after() takes a valid date string in 'YYYY/MM/DD' format and return a 
    date string for the next day in 'YYYY/MM/DD' format.
    e.g. after('2017/12/31') -> '2018/01/01'
         after('2018/01/31') -> '2018/02/01'
         after('2018/02/28') -> '2018/03/01' 
    """
    str_year, str_month, str_day = date.split('/')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    days_in_month = days_in_mon(year)

    tmp_day = day + 1

    if tmp_day > days_in_month[month]:
        to_day = tmp_day % days_in_month[month]
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0
        
    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0
    next_date = str(year)+"/"+str(to_month).zfill(2)+"/"+str(to_day).zfill(2)
    
    return next_date

def before(date):
    """
    before() takes a valid date string in 'YYYY/MM/DD' format and return a 
    date string for the previous day in 'YYYY/MM/DD' format.
    e.g. before('2018/01/01') -> '2017/12/31'
         before('2018/02/01') -> '2018/01/31'
         before('2018/03/21') -> '2018/02/28' 
    """
    str_year, str_month, str_day = date.split('/')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    days_in_month = days_in_mon(year)

    tmp_day = day - 1

    if tmp_day < 1:
        if month == 1:
            tmp_month = 12
            to_day = days_in_month[tmp_month]
            year = year - 1
        else:
            to_day = days_in_month[month - 1]
            tmp_month = month - 1
    else:
        to_day = tmp_day
        tmp_month = month + 0
    
    to_month = tmp_month + 0
    previous_date = str(year)+"/"+str(to_month).zfill(2)+"/"+str(to_day).zfill(2)
    
    return previous_date

def days_in_mon(year):
    """
    days_in_mon() takes a valid year string in 'YYYY' format and return a 
    dictionary object in the form of an array for the number of days 
    in each month for the particular year.
    e.g. days_in_mon('2018') -> mon_max { 1:31, 2:28, 3:31, 4:30, 
                                        5:31, 6:30, 7:31, 8:31, 
                                        9:30, 10:31, 11:30, 12:31} 
    This method also uses leap_year function to
    check if current date is a leap year.
    """
    if leap_year(year):
        feb_max = 29
    else:
        feb_max = 28

    mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return mon_max

def valid_date(date):
    """
    valid_date() takes a date string and returns true if the string is 
    in 'YYYY/MM/DD' format, else it returns False with an 
    appropriate error message.
    e.g. valid_date('2018/01/01') -> 'True'
         valid_date('2018/02/41')    -> 'Error: Wrong day entered'
         valid_date('2018')          -> 'Error: Wrong date entered' 
    """
    if len(date) != 10:
        return (False,"Error: Wrong date entered")
    else:
        str_year, str_month, str_day = date.split('/')
        month = int(str_month)
        day = int(str_day)
        if month < 1 or month > 12:
            return (False,"Error: Wrong month entered")
        elif day < 1 or day > 31:
            return (False,"Error: Wrong day entered")
        else:
            return (True,"")

def leap_year(year):
    """
    leap_year() takes a year string in 'YYYY/MM/DD' format and returns a bool
    to confirm the year being a leap year or not.
    e.g. leap_year('2018') -> 'True'
         leap_year('2016') -> 'False'
    """
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def dbda(date, days):
    """
    dbda() takes two parameters, one a date string in 'YYYY/MM/DD' format, 
    and an integer value for the number of days and outputs the date 
    corresponding to the integer value added to the provided date.
    e.g. dbda('2018/01/01',15) -> '2018/01/16'
         dbda('2018/12/31'2) -> '2019/01/02'
    """
    if(step):
        if int(days) > 0:
            for i in range(int(days)):
                date = after(date)
                print(date)
        elif int(days) < 0:
            for i in range(-int(days)):
                date = before(date)
                print(date)
    else:
        if int(days) > 0:
            for i in range(int(days)):
                date = after(date)
        elif int(days) < 0:
            for i in range(-int(days)):
                date = before(date)
        return date

if __name__ == "__main__":

    if len(sys.argv) == 3:
        date = sys.argv[1]
        days = sys.argv[2]
        # BEGIN bonus functionality
        if len(days) == 10:
            flag = True
            i = 0
            if days > date:
                while flag:
                    date = after(date)
                    i += 1
                    if date == days:
                        break
            elif days < date:
                while flag:
                    days = after(days)
                    i += 1
                    if date == days:
                        break
            print(i)
        # END of bonus functionality
        else:
            step = False
            if valid_date(date)[0]:
                print(dbda(date, days))
            else:
                print(valid_date(date)[1])
    elif (len(sys.argv) == 4 and 
            sys.argv[1] == "--step"):
        date = sys.argv[2]
        days = sys.argv[3]
        step = True
        if valid_date(date)[0]:
            dbda(date, days)
        else:
            print(valid_date(date)[1])
    else:
        usage()

