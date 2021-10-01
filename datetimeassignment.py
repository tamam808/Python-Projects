import datetime
import pytz
from pytz import timezone

def getTimes():
    PST = pytz.timezone('US/Pacific')
    NYC = pytz.timezone('US/Eastern')
    LON = pytz.timezone('Europe/London')
    ny_time = datetime.datetime.now(NYC)
    port_time = datetime.datetime.now(PST)
    lon_time = datetime.datetime.now(LON)
    port_hour = port_time.strftime('%H')
    port_open(port_hour)
    ny_hour = ny_time.strftime('%H') 
    ny_open(ny_hour)
    lon_hour = lon_time.strftime('%H')
    lon_open(lon_hour)
    

def port_open(port_hour):
    print('Portland HQ Hours: 0900 - 1700')
    hrs_open = ''
    if 9 <= int(port_hour) < 17:
        hrs_open = 'open'
    else:
        hrs_open = 'closed'
    print('The current Portland hour is {}00. This branch is currently {}.'.format(port_hour, hrs_open))
    
def ny_open(ny_hour):
    print('NYC Branch Hours: 0900 - 1700')
    hrs_open = ''
    if 9 <= int(ny_hour) < 17:
        hrs_open = 'open'
    else:
        hrs_open = 'closed'
    print('The current NYC hour is {}00. This branch is currently {}.'.format(ny_hour, hrs_open))


def lon_open(lon_hour):
    print('London Branch Hours: 0900 - 1700')
    hrs_open = ''
    if 9 <= int(lon_hour) < 17:
        hrs_open = 'open'
    else:
        hrs_open = 'closed'
    print('The current London hour is {}00. This branch is currently {}.'.format(lon_hour, hrs_open))

getTimes()
