"""
Mainly wrapping and extension of swisseph 
functionality 
TODO: replace string names for house systems with variables (do we need to do this?) 
TODO: Add functionality to locate prenatal syzygy (latest full or new moon, no later than birth) 
TODO: Add logic to calculate whether given birth time is before or after sunset 
"""

import swisseph as ep
import angle_conversions as ac
import datetime

#Want to reference planets 
#as obvious string keys in a dictionary structure; 
#map library's native flags to names 
planet_loop = {
	"Moon": ep.MOON, 
	"Mercury": ep.MERCURY, 
	"Venus": ep.VENUS, 
	"Sun": ep.SUN, 
	"Mars": ep.MARS, 
	"Jupiter": ep.JUPITER, 
	"Saturn": ep.SATURN, 
	"North Node": ep.TRUE_NODE
}
house_sys = {
	"Placidus" : b'P', 
	"Alcabitius" : b'B', 
	"Porphyry" : b'O'
}
def get_house_sys():
	print("These are some options for house systems. Enter an option from these")
	for sys in house_sys.keys():
		print(sys)
	x = input("Enter here: ").strip()
	while x not in house_sys.keys(): 
		x = input(x + " was not found. Try again: ").strip()
	return x
#This listing will be necessary for future 
#revisions implementing "almuten figuris" 
#rankings of planets
#When implemented it will compare 
#evaluated speed from ephermis 
#to the respective mean speed in longitudinal degrees
#to evaluate "Fastness" or "Slowness" of planet
#at given moment 
mean_speeds={ #mean longitudal decimal degrees
	"Moon": 13.1764, 
	"Mercury": 0.9856, 
	"Venus": 0.9856, 
	"Sun": 0.9856, 
	"Mars": 0.5241, 
	"Jupiter": 0.0831, 
	"Saturn": 0.0336
}
	
def get_julian_date(dt): 
	"""Wrapper for astromonical Julian date found by swisseph function
	Args:
		dt (datetime.datetime)
	Returns: 
		(float): the Julian date
	"""
	return ep.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute/60.0)
def get_planets(julian_date):
	"""Gets planetary placements given julian_date (semantically UTC midnight Julian) using swisseph.calc_ut()
	Args:
		julian_date(float):   this is expected semantically *in* UTC 
			as the calculations expect UTC Julian midnight 
	Returns: 
		planets (dict): listings of planets; key is planet's name as string; see keys in planet_loop,  mean_speeds, etc. 
	""" 
	planets = {} 
	for key in planet_loop.keys(): 
		res, flag = ep.calc_ut(julian_date, planet_loop[key], ep.FLG_SPEED)
		planets[key]  = { "angle": res[0], "Raw": (res, flag)} 
		planets[key]["Sign/Angle"] = ac.get_sign_angle(res[0]) 
	planets["South Node"] = {"angle" : planets["North Node"]["angle"] + 180.0}
	#South Node angle is calculated (by definition opposition to North Node) and might exceed 360 
	if planets["South Node"]["angle"] >= 360 : 
		planets["South Node"]["angle"] -= 360 
	planets["South Node"]["Sign/Angle"] = ac.get_sign_angle(planets["South Node"]["angle"])
	return planets 

def get_houses(julian_date, lat, lon, sys):
	"""Gets planetary placements given julian_date (semantically UTC midnight Julian) using swisseph.houses()
	Args:
		julian_date(float):   this is expected semantically *in* UTC 
			as the calculations expect UTC Julian midnight 
		lat (float): latitude, positive for north 
		lon(float): longitude, negative for west 
		sys(string): What house system (see house_sys); no variation in ascendant, descendant, medium coeli, imum coeli regardless
	Returns: 
		(dict) "houses": list of houses, "AC" ascendant item, "MC" medium coeli angle
	""" 
	cusps, asmc = ep.houses(julian_date, lat, lon, house_sys[sys])
	houses = [] 
	for cusp in cusps: 
		houses.append({"Sign/Angle" : ac.get_sign_angle(cusp), "angle": cusp})
	for i in range(len(houses) - 1): 
		houses[i]["Next_angle"] = houses[i+1]["angle"] 
	houses[len(houses) -1]["Next_angle"] = houses[0]["angle"] 
	return {
		"houses": houses, 
		"AC": {"Sign/Angle" : ac.get_sign_angle(asmc[0]), "angle": asmc[0]},
		"MC": {"Sign/Angle" :  ac.get_sign_angle(asmc[1]), "angle":asmc[1]}
		} 
		
def get_houses_planets(houses, planets): 
	"""Compares angles to locate planets within hoses 
	Args:
		houses(dict): 
		planets(dict): 
	Returns: 
		(dict) mapping of planets to houses
	""" 


	houses_planets ={}
	for key in planets.keys(): 
		for i in range(len(houses["houses"])): 
			house = houses["houses"][i]
			if house["angle"] < house["Next_angle"]: 
				if planets[key]["angle"] >= house["angle"]  and planets[key]["angle"] < house["Next_angle"]: 
						houses_planets[key] = i + 1 
						break 
			else: # it circles 
				if planets[key]["angle"] >= house["angle"] or planets[key]["angle"] <= house["Next_angle"]: 
						houses_planets[key] = i + 1 
						break 
	return houses_planets
		
 
def utc_from_julian(julian): #julian as tuple
	"""wrapper to simplify conversion from julian back to UTC 
	Args: 
		julian (float) 
	Returns: 
		(datetime.datetime) UTC equivalent date/time of given Julian date
	"""
	julian = ep.revjul(julian)
	y = julian[0] 
	mo = julian[1] 
	d = julian[2] 
	h = int(julian[3]) 
	m = int((julian[3] - h)*60)
	s = int(((julian[3] - h)*60) - m)*60
	return datetime.datetime(y, mo, d, h, m, s, tzinfo=datetime.timezone.utc)
