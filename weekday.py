import datetime

weekday = datetime.datetime.today().weekday()   

print(weekday)

if weekday<5:
    print("Weekday")
else:
    print("Weekend")    



