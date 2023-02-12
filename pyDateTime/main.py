import datetime
from datetime import date

# today = datetime.date.today()
# print(today.year, today.month, today.day)

date1 = date.fromisoformat('2022-02-03')
date2 = datetime.date.today()
datediff = date2 - date1
print(datediff)
print(type(datediff))