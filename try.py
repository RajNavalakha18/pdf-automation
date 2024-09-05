from datetime import datetime, timedelta

today = datetime.today()
#get the start_time and end_time from frontend and then use that for filtering the data

start_time = today.replace(year=2021,month=4,day=20, hour=0, minute=0, second=0).strftime('%Y-%m-%d %H:%M %p')
end_time = today.replace(year=2020,month=5,day=2,hour=20, minute=0, second=0).strftime('%Y-%m-%d %H:%M %p')


#CONVERT STRING DATE TO DATETIME FORMAT
# Python provides the strptime() method, in its datetime class, to convert a string representation of the​ date/time into a date object.
date_time_str = '2001/08/07 11:55:02'
d1 = '07/08/2001'
d2 = '05/03/2001'

#Required format
# '%Y/%m/%d %H:%M:%S' - To be converted from backend

date_time_obj = datetime.strptime(date_time_str, '%Y/%m/%d %H:%M:%S')
print('Date:', date_time_obj)
datetimed1 = datetime.strptime(d1, '%m/%d/%Y')
datetime2 = datetime.strptime(d2, '%m/%d/%Y')
print('d1 is greater than d2:', datetimed1 > datetime2)

date_time_str_start = '2001/08/07 11:55:02'
date_time_str_end = '2001/08/07 11:55:02'
start_time = datetime.strptime(date_time_str_start, '%Y/%m/%d %H:%M:%S').strftime('%Y-%m-%d %H:%M %p')
end_time = datetime.strptime(date_time_str_end, '%Y/%m/%d %H:%M:%S').strftime('%Y-%m-%d %H:%M %p')
print(start_time)
print(end_time)