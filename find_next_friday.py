from datetime import datetime

def find_next_friday():
    months_and_days = {1: 31,
2: 28 ,
3: 31 ,
4: 30 ,
5: 31 ,
6: 30 ,
7: 31 ,
8: 31 ,
9: 30 ,
10: 31 ,
11: 30,
12: 31 ,
}
    today = datetime.today()
    if today.isoweekday() == 5:
        print("today is friday")
        next_friday =  datetime.strftime(today, '%Y-%m-%d')
        return next_friday
    else: 
        next_friday = today
        day = next_friday.day
        month = next_friday.month
        year = next_friday.year

        while next_friday.isoweekday() != 5:
            #print(next_friday)
            day += 1
            
            if day > months_and_days[month]:
                month += 1
                day =1
                if month > 12:
                    month = 1
                    year += 1

                next_friday= next_friday.replace(day=day, month=month, year=year)
            else:
                next_friday= next_friday.replace(day=day)

    next_friday =  datetime.strftime(next_friday,'%Y-%m-%d')
    return next_friday

    
if __name__ == "__name__":
    print(find_next_friday())

