#hacker rank calender module
#calender module allows you to output calenders and provide aditional useful functions for them

# class calender.TextCalender([firstweekday])
import calendar
print(calendar.firstweekday())

m,d,y = 9,19,1995
ans =calendar.weekday(y,m,d)

print(calendar.day_name[ans])
