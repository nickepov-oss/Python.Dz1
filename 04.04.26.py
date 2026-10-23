import datetime
#datetime(year,month,day,hour=0,minute=0,second=0,microsecond=0)-Структура та послідовність Datetime
date_time = datetime.datetime(2026,4,4,9,1,24,585)
print(f"Datetime:{date_time}")
print(f"Type - {type(date_time)}")

OnlyData = date_time.date()
print(f"OnlyData - {OnlyData}")
print(f"Type - {type(OnlyData)}")

OnlyTime = date_time.time()
print(f"OnlyTime - {OnlyTime}")
print(f"Type - {type(OnlyTime)}")


OnlyDate1 = datetime.date( 2024, 3,  4) #Створення тільки доти
OnlyTime1 = datetime.time ( 23, 59) # Створення тільки часу
print(f"date = (OnlyDate1),type date = {type(OnlyDate1)}")
print(f"time = (OnlyTime1),type time = {type(OnlyTime1)}")
Again_Date_Time = datetime.datetime.combine(OnlyDate1, OnlyTime1)
date_now = datetime.datetime.now()
print(f"date_now - {date_now}")
