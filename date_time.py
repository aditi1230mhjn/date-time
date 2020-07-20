from datetime import date, datetime

today = date.today()
print(today.strftime("%B %d, %Y"))
now = datetime.now()
print(now.strftime("%H : %M"))