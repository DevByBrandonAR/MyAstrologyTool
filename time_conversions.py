from datetime import datetime, date, time
from datetime import UTC 
from zoneinfo import ZoneInfo, available_timezones
from zoneinfo import available_timezones


def show_all_timezones(): 
	available = list(available_timezones())
	x = "" 
	i = 0 
	for i in range(len(available)):
		x += list(available_timezones())[i] + " " 
		if i % 10 == 0 and i > 0: 
			x += "\n" 
	print(x) 

def get_timezone(): 
	available = list(available_timezones())
	x = input("Enter timezone. Enter HELP to see options:").strip() 	
	if x == "HELP": 
		show_all_timezones()
		x = input("Enter timezone. Enter HELP to see options:").strip()	
	else: 
		while x not in available:
			x = input("Could not find " + x + " , please try again: ").strip()
	return x 
	
def read_date_time(zone): 
	x = input("Please enter date and time as d/m/yyyy,hh:mm (24-hour): ").strip() 
	x = x.split(",")
	dateparts = x[0].split("/") 
	timeparts = x[1].split(":") 
	d = int(dateparts[1]) 
	m = int(dateparts[0]) 
	y = int(dateparts[2]) 
	h = int(timeparts[0]) 
	mo = int(timeparts[1]) 
	local = datetime.combine(date(y, m,d), time(h,mo), tzinfo=ZoneInfo(zone))
	return (local.astimezone(ZoneInfo("UTC")), local) 


	
		
		
		
	
	
	
	



		
