
def day_of_week(day):
    if day == 1 :
        return "It is sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return " It is Tuesday"
    elif day == 4:
        return "It is Wednesday"
    elif day == 5:
        return "It is thursday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is saturday"
    else:
        return "Not Valid day"
days = day_of_week(2)
print(days)