"""
Plot natal chart. Currently *just* shows simple natal chart with placements,  
TODO: Enable logic to show astronomical transits
TODO: Show the Hermetic lots (lot of fortune, etc) 
The adaptation in derive_planets_houses()  is necessary as the existing logic was not designed with the 
ephemeris.py choices in mind. 
"""

import numpy as np 
import matplotlib.pyplot as plt 
import math 


#majority of houses appear on chart as Roman numerals
HOUSE_MAPPINGS= {
	0: "I", 
	1: "II", 
	2: "III", 
	3: "IV", 
	4: "V", 
	5: "VI", 
	6: "VII", 
	7: "VIII", 
	8: "IX", 
	9: "X", 
	10: "XI", 
	11: "XII"
}

#logic for converting from local sign angle to angle 
#on entire circle, relative to Aries 0 
INCREMENTS = {
	"♈": 0, 
	"♉": 30, 
	"♊": 60, 
	"♋": 90,  
	"♌": 120, 
	"♍": 150, 
	"♎": 180, 
	 "♏" : 210, 
	"♐": 240, 
	"♑": 270, 
	"♒": 300, 
	"♓" :330
}

#Emojis for astrological signs are not used 
#Elsewhere in solution, but are displayed on plot 
SIGN_MAPPINGS = {
	"Aries":  "♈",
	"Taurus": "♉", 
	"Gemini": "♊", 
	"Cancer": "♋", 
	"Leo": "♌", 
	"Virgo": "♍", 
	"Libra": "♎", 
	"Scorpio":  "♏", 
	"Sagittarius": "♐", 
	"Capricorn": "♑", 
	"Aquarius": "♒", 
	"Pisces": "♓"
} 

#Planetary symbols are not used elsewhere
#in solution but are displayed on plot 
PLANET_MAPPINGS = {
	"Sun": "☉", 
	"Moon": "☽", 
	"Mercury": "☿", 
	"Venus": "♀", 
	"Mars": "♂", 
	"Jupiter": "♃", 
	"Saturn": "♄", 
	"Asc": "↑", 
	"North Node": "☊", 
	"South Node": "☋"
}	

def get_plottable_chord(a, b, r): 
	"""
	Args:
		a (float)  
		b (float) 
		r (float) radius 
	Returns: 
		tuplet: list of tuples to plot
	"""	
	ac = ( r*math.cos(a), r*math.sin(a) )
	bc = ( r*math.cos(b), r*math.sin(b))
	h = (0.5*(ac[0] + bc[0]), 0.5*(ac[1] + bc[1]) )
	return (ac, h, bc)
	
	
def get_distinct_aspects(aspects):
	"""
	Args:
		aspects(dict)
	Returns: 
		distincts(dict): reduced aspects dict; do not want to double-plot 
	"""	
	distincts = []
	for key in aspects.keys(): 
		for  planet in aspects[key].keys(): 
			for planet2 in aspects[key][planet]: 
				if (planet, planet2) in distincts or (planet2, planet) in distincts: 
					continue 
				distincts.append((PLANET_MAPPINGS[planet], PLANET_MAPPINGS[planet2]))
	return distincts
#unicode values for planet symbols 
#are necessary to display as pyplot markers 
#but do not appear elsewhere in solution 

PLANET_UCODES = {
	"Sun": r'$\odot$', 
	"Moon": '$\u263D$', 
	"Mercury": '$\u263F$', 
	"Venus":'$\u2640$',
	"Mars": '$\u2642$', 
	"Jupiter": '$\u2643$', 
	"Saturn": '$\u2644$', 
	"Asc" : '$\u2191$', 
	"North Node": "$\u260A$", 
	"South Node": "$\u260B$"
}

def derive_planets_houses(planets, houses):
	"""The plotting logic was developed before
	rest of solution was considered, this function 
	converts particular data structures to 
	the structures the plotting logic expects 
	Args:
		planets (dict) the structure returned from results in ephemeris.py 
		houses (dict) the structure returned from results in  ephemeris.py
	Returns: 
		tuple: tuple of the adapted dictionary objects required in natal_plot(), see below
	"""
	placements = {} 
	for key in planets.keys():
		angle = planets[key]["Sign/Angle"]
		placements[PLANET_MAPPINGS[key]]= { "Angle": ( SIGN_MAPPINGS[angle[0]], angle[1], angle[2]), "Ucode": PLANET_UCODES[key]}
	angle = houses["houses"][0]["Sign/Angle"]
	placements[PLANET_MAPPINGS["Asc"]] = { "Angle": (SIGN_MAPPINGS[angle[0]], angle[1], angle[2]), "Ucode": PLANET_UCODES["Asc"]}
	new_houses = {} 
	for i in range(len(houses["houses"])):
		angle = houses["houses"][i]["Sign/Angle"]
		new_houses[HOUSE_MAPPINGS[i]] = {"Angle": (SIGN_MAPPINGS[angle[0]], angle[1], angle[2]) }
	return (placements, new_houses)
	
def natal_plot(planets, houses, aspects):
	"""Plots natal chart using a polar plot. 
	Converts sign/minute/second angle to degree measures usable by the pyplot polar chart. 
	Care is taken in the logic to rotate the natal chart calculated astronomically so that 
	ascendant appears at 180 degrees on the polar chart, rotating all else as ncessary. 
	Legend is provided. 
	derive_planets_houses() is used to handle results from elsewhere in solution 
	Args:
		planets (dict) the structure returned from results in ephemeris.py 
		houses (list) the structure returned from results in  ephemeris.py
		aspects(dict) 
	Returns: 
		tuple: tuple of the adapted dictionary objects required in natal_plot(), see below
	"""
	places, houses = derive_planets_houses(planets, houses) 
	r = 0.5
	for key in places.keys(): 
		a = places[key]["Angle"] 
		places[key]["Abs"] =  INCREMENTS[a[0]] + a[1]+ a[2]/60.0
	asc_abs = places["↑"]["Abs"] 
	asc_a = places["↑"]["Angle"]
	for key in houses.keys():
		a = houses[key]["Angle"]
		houses[key]["Abs"] = INCREMENTS[a[0]] + a[1] + a[2]/60.0
	for key in places.keys():
		a = places[key]["Abs"] 
		places[key]["Plot"] = (180 - asc_abs ) + a 
	asc_plot = places["↑"]["Plot"]
	asc_inc = INCREMENTS[places["↑"]["Angle"][0]]
	for key in houses.keys():
		a = houses[key]["Abs"]
		houses[key]["Plot"] = (180 - asc_abs) + a
	for key in INCREMENTS.keys():
		INCREMENTS[key] = (180 - asc_a[1]- (asc_a[2]/60.0) - asc_inc) + INCREMENTS[key]	
		if INCREMENTS[key] <0 : 
			INCREMENTS[key] += 360 
	for key in places.keys():
		places[key]["Plot_radians"] = places[key]["Plot"]*math.pi/180.0 
	for key in houses.keys():
		if houses[key]["Plot"] < 0: 
			houses[key]["Plot"]  += 360 
		houses[key]["Plot_radians"] = houses[key]["Plot"]*math.pi/180.0

	distincts = get_distinct_aspects(aspects)
	distinct_angles = []
	chords = []
	for distinct in distincts:
		distinct_angles.append((places[distinct[0]]["Plot_radians"], places[distinct[1]]["Plot_radians"]))
	for angle in distinct_angles: 
		chords.append(get_plottable_chord(angle[0], angle[1], r))
	fix, ax = plt.subplots(subplot_kw={'projection':'polar'}, figsize=(10,5))
	ax.set_rmin(0.1)
	ax.set_xticks([houses[key]["Plot_radians"] for key in houses.keys()])
	ax.set_yticks([0.475]) 
	ax.set_yticklabels([])
	ax.set_xticklabels([ str(houses[key]["Angle"][1] )+ str(houses[key]["Angle"][0]) + 		str(houses[key]["Angle"][2]) for key in houses.keys()])

	rm = ax.get_rmax() 
	for key in houses.keys():
		a= key
		if key == "I":
			a = "(ASC)"
		elif key == "IV":
			a = "(IC)"
		elif key == "VII":
			a = "(DSC)"
		elif key == "X":
			a = "(MC)"
		ax.annotate(a, ( houses[key]["Plot_radians"], 0.25),clip_on=False, color='blue')
	for key in places.keys():
		a = places[key]["Plot_radians"]
		b =places[key]["Angle"]
		ax.scatter([a], [0.5], color='b',marker= places[key]["Ucode"] ,  label = str(b[1]) + b[0]  + str(b[2]), s =100)
		ax.annotate( str(b[1]) + b[0] + str(b[2]), (a, r), fontsize=12, clip_on=False, 	color='red') 
	plt.rcParams['mathtext.fontset'] = 'stix' 
	plt.tight_layout()
	plt.legend(loc="center left", bbox_to_anchor=(1.2, 0.5))
	cartesian_ax = fix.add_axes(ax.get_position(), frameon=False)
	cartesian_ax.set_xlim(-r,r)
	cartesian_ax.set_ylim(-r,r)
	cartesian_ax.axis('off') 
	for chord in chords: 
		#TODO: can these chords joining aspected planets look better
		cartesian_ax.plot([chord[0][0], chord[1][0], chord[2][0] ], [chord[0][1], chord[1][1], chord[2][1]], color='orange', linewidth=0.5)
	ax.set_zorder(cartesian_ax.get_zorder() + 1) 
	ax.patch.set_visible(False)
	plt.show()