import datetime
from calendar import monthrange

class MeetupDayException(ValueError):
	pass

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def meetup_day(year, month, day, arg):
    
    days = {'Monday' : 0, 'Tuesday' : 1, 'Wednesday' : 2, 'Thursday' : 3, 'Friday' : 4, 'Saturday' : 5, 'Sunday' : 6}
    days_pos = {'teenth' : 12, '1st' : 1, '2nd' : 7, '3rd' : 14, '4th' : 21, 'last' : monthrange(year, month)[1] - 7, '5th' : 28}
    new_arg = days_pos[arg]
    d = datetime.date(year, month, new_arg)
    next_day = next_weekday(d, days[day])
    if next_day.month != month:
        raise MeetupDayException('Invalid input.')
    return(next_day)