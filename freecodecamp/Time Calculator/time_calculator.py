# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

def add_time(start, duration, weekday=""):
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    # separating time components
    start_time = start.split()[0].split(":")
    day_div = start.split()[1]
    duration_time = duration.split(":")

    # converting 12h format to 24h format
    start_time_in_min = None
    duration_in_min = int(duration_time[0]) * 60 + int(duration_time[1])

    if day_div == "AM":
        start_time_in_min = int(start_time[0]) * 60 + int(start_time[1])
    elif day_div == "PM":
        start_time_in_min = 720 + int(start_time[0]) * 60 + int(start_time[1])

    # calculating the new_time
    end_time = start_time_in_min + duration_in_min

    end_days = end_time // 1440
    end_hours = (end_time % 1440) // 60
    end_minutes = (end_time % 1440) % 60

    # AM or PM
    if end_hours == 0:
        end_hours_div = 12
    elif end_hours <= 12:
        end_hours_div = end_hours
    else:
        end_hours_div = end_hours - 12

    end_day_div = "AM" if (end_time // 720) % 2 == 0 else "PM"

    # calculating the new_time day number
    day_later = ""
    if 1440 < end_time < 2880:
        day_later = "(next day)"
    elif end_time >= 2880:
        day_later = f'({end_days} days later)'

    # calculating the new_time weekday (if given)
    end_weekday = ""
    if weekday:
        weekday_index = weekdays.index(weekday.lower()) if weekday.lower() in weekdays else ""
        end_weekday = weekdays[weekday_index + (end_days % 7) - 7].capitalize()

    # formatting new_time
    new_time = f'{end_hours_div}:{end_minutes:02d} {end_day_div}{", " + end_weekday if weekday else ""}{" " + day_later if day_later else ""}'

    return new_time


print(add_time("11:59 PM", "24:04"))
# print(add_time("11:50 PM", "48:10", "tuesday"))
# print(add_time("11:50 PM", "48:10", "friday"))
# print(add_time("8:16 PM", "466:02", "tuesday"))
