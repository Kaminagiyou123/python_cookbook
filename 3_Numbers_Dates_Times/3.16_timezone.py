from datetime import datetime, timedelta
from pytz import timezone

d=datetime(2012,12,21,9,30,0)

central=timezone('US/Central')
loc_d=central.localize(d)
print(f"{loc_d} is local time now")
later=central.normalize(loc_d+timedelta(minutes=300))
print(later)