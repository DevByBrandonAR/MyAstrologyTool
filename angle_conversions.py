###Converts a circular degree float angle to angle/degrees/minutes 
SIGNS = [ 
	"Aries", "Taurus", "Gemini", 
	"Cancer", "Leo", "Virgo", 
	"Libra", "Scorpio", "Sagittarius", 
	"Capricorn", "Aquarius", "Pisces" 
]

ASPECTS= {
	"Conjunction":0, 
	"Sextile": 60 ,
	"Square": 90, 
	"Trine": 120,  
	"Opposition": 180
}

def get_sign_angle(angle): 
	"""Map to signs and angles
	Args:
		angle (float) on range [0, 360)
	Returns: 
		(tuple) angle/degrees/minutes (degrees on range [0, 30), minutes [0, 60))
	"""
	for i in range(len(SIGNS) - 1, -1, -1): 
		if angle >= i*30: 
			#deg and min
			a = angle - i*30 
			d = int(a)
			m = int((a - d)*60)
			return (SIGNS[i],  d, m)

def in_bounds(x, b): 	
	return x >= b[0] and x <= b[1]
def con_sub(boo, x, y): 
	"""Conditional order in subtraction, this is a pattern that comes up in Lot calculations
	Args:
		boo (boolean)
		x (float) 
		y (float) 
	Returns: 
		(float) x - y if boo is true, y - x otherwise
	"""
	return (x - y if boo else y - x)
def print_aspects(aspects): 
	"""Show aspects 
	Args:
		aspects(dict)
	Returns:
		None
	"""
	for key in aspects.keys():
		if len(list(aspects[key])) ==0:
			continue
		print(key)
		for planet in aspects[key].keys():
			if len(aspects[key][planet])==0:
				continue
			print("\t" + planet) 
			for other_planet in aspects[key][planet]:
				print("\t\t" + other_planet)
			
def get_aspects(planets, orb): 
	"""Find aspects. TODO: expand this to lots and ASC, MC
	Args:
		planets (dict)
		orb (float) margin of tolerance
	Returns: 
		aspects (dict) 
	"""
	aspects = {} 
	for key in ASPECTS.keys(): 
		aspects[key] = {}
		for planet in planets.keys(): 
			aspects[key][planet] = [] 
			for planet2 in planets.keys(): 
				if planet2 == planet: 
					continue
				if key == "Conjunction": 
					ran =(0, orb + 1) 
				else: 	
					ran = (ASPECTS[key] - orb, ASPECTS[key] + orb + 1)
				diff = abs(planets[planet]["angle"] - planets[planet2]["angle"])	
				diff2 = abs(planets[planet]["angle"] + 360 - planets[planet2]["angle"]) 
				diff3 = abs(planets[planet]["angle"] - 360 - planets[planet2]["angle"])
				diff4 = abs(planets[planet2]["angle"] + 360 - planets[planet]["angle"]) 
				diff5 = abs(planets[planet2]["angle"] - 360 - planets[planet]["angle"])

				if  in_bounds(diff, ran) or in_bounds(diff2, ran) or  in_bounds(diff3, ran)  or in_bounds(diff4, ran) or in_bounds(diff5, ran):
					aspects[key][planet].append(planet2) 
	return aspects
		