from django.shortcuts import render
import calendar
import datetime
import time


# Create your views here.


def agenda(request):
    return render(request, 'evenement/calandar.html')
    # Python code to demonstrate the working of
    # calendar() and firstweeksday()

    # importing calendar module for calendar operations
     #import calendar

    # using calender to print calendar of year
    # prints calendar of 2012
     #print("The calender of year 2012 is : ")
     #print(calendar.calendar(2012, 2, 1, 6))