from datetime import date


class MeetupDayException(Exception):
    pass


def get_isoweekday(day_of_the_week):
    if day_of_the_week == "Monday":
        return 1
    elif day_of_the_week == "Tuesday":
        return 2
    elif day_of_the_week == "Wednesday":
        return 3
    elif day_of_the_week == "Thursday":
        return 4
    elif day_of_the_week == "Friday":
        return 5
    elif day_of_the_week == "Saturday":
        return 6
    elif day_of_the_week == "Sunday":
        return 7
    else:
        raise MeetupDayException("bad format")


def get_count(which):
    if which == "1st":
        return 1
    elif which == "2nd":
        return 2
    elif which == "3rd":
        return 3
    elif which == "4th":
        return 4
    elif which == "5th":
        return 5
    elif which == "last":
        return 0
    else:
        raise MeetupDayException("impossible")


def meetup_day(year, month, day_of_the_week, which):
    count = 0
    last = None
    for day in range(1, 32):
        try:
            d = date(year, month, day)
            if d.isoweekday() == get_isoweekday(day_of_the_week):
                if which == "teenth":
                    if 13 <= day <= 19:
                        return d
                else:
                    count += 1
                    last = d
                    if get_count(which) == count:
                        return d
        except:
            break
    if which == "last":
        return last
    raise MeetupDayException("day does not exist")
