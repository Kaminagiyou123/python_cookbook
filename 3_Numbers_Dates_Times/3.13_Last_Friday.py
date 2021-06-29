from datetime import datetime,timedelta

weekdays=['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']
def get_previous_byday(dayname,start_date=None):
 if start_date is None:
  start_date=datetime.today()
 day_num=start_date.weekday()
 day_num_target=weekdays.index(dayname)
   
  