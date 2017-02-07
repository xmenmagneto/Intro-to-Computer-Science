def dateBefore(year1, month1, day1, year2, month2, day2):
	"""returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, return False"""
	if year1 < year2:
		return True
	if year1 == year2:
		if month1 < month2:
			return True
		if momth1 == month2:
			return day1 < day2
	return False


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
	days = 0
	while dateBefore(year1, month1, day1, year2,month2, day2):
		year1, month1, day1 = nextDay(year1, month1, day1)
		days += 1
	return days