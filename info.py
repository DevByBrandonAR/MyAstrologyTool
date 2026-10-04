"""
This is used in test.py but will also be of use
when almuten figuris logic is added
"""
DOMICILES = {
	"Saturn": ["Capricorn", "Aquarius"], 
	"Jupiter": ["Sagittarius", "Pisces"], 
	"Mars" : ["Aries", "Scorpio"], 
	"Sun" : ["Leo"], 
	"Venus" : ["Taurus", "Libra"], 
	"Mercury": ["Gemini", "Virgo"], 
	"Moon" : ["Cancer"]
}

EXALTATIONS = {
	"Saturn" : "Libra", 
	"Jupiter" :"Cancer",
	"Mars" : "Capricorn", 
	"Sun" : "Aries", 
	"Venus" : "Pisces", 
	"Mercury" : "Virgo" , 
	"Moon" : "Taurus" , 
	"North Node" : "Gemini", 
	"South Node" : "Sagittarius" 
	
}

OPPOSITE = {
	"Aries" : "Libra", 
	"Taurus" : "Scorpio", 
	"Gemini" : "Sagittarius" , 
	"Cancer" : "Capricorn", 
	"Leo" : "Aquarius", 
	"Virgo" : "Pisces", 
	"Libra" : "Aries", 
	"Scorpio": "Taurus", 
	"Sagittarius" : "Gemini", 
	"Capricorn" : "Cancer", 
	"Aquarius" : "Leo" , 
	"Pisces" : "Virgo" 
}

TRIPLICITIES = {
	"Aries": { "Day": "Sun" , "Night": "Jupiter", "Participating" : "Saturn"}, 
	"Leo" : { "Day": "Sun" , "Night": "Jupiter", "Participating" :"Saturn" }, 
	"Sagittarius" : { "Day": "Sun", "Night": "Jupiter", "Participating" : "Saturn"}, 
	"Taurus" : { "Day": "Venus" , "Night":"Moon" , "Participating" : "Mars"},  
	"Virgo": { "Day": "Venus", "Night": "Moon", "Participating" :"Mars"}, 
	"Capricorn" : { "Day": "Venus", "Night": "Moon", "Participating" :"Mars" }, 
	"Gemini": { "Day": "Saturn", "Night": "Mercury", "Participating" : "Jupiter"}, 
	"Libra" : { "Day": "Saturn", "Night": "Mercury", "Participating" : "Jupiter"}, 
	"Aquarius" : { "Day": "Saturn" , "Night":"Mercury" , "Participating" : "Jupiter"}, 
	"Cancer" : { "Day": "Venus", "Night": "Mars", "Participating" : "Moon"}, 
	"Scorpio" : { "Day": "Venus", "Night":"Mars" , "Participating" : "Moon"}, 
	"Pisces" : { "Day": "Venus" , "Night": "Mars", "Participating" : "Moon"}
}
#Chaldean scheme of Decan rulers; angle ranges are in whole degrees, 
#each range (x,y) tuple represents the range [x, y)
DECANS = {
	"Aries":{(0,10): "Mars", (10,20): "Sun", (20,30)  : "Venus"}, 
	"Taurus": {(0, 10): "Mercury", (10,20): "Moon", (20,30): "Saturn"}, 
	"Gemini": {(0,10): "Jupiter", (10,20): "Mars", (20,30): "Sun" }, 
	"Cancer": {(0,10): "Venus", (10,20): "Mercury", (20,30): "Moon" }, 
	"Leo": { (0,10): "Saturn", (10,20): "Jupiter", (20,30): "Mars"}, 
	"Virgo": {(0,10): "Sun", (10,20): "Venus", (20,30): "Mercury" }, 
	"Libra": {(0,10): "Moon", (10,20): "Saturn", (20,30): "Jupiter" }, 
	"Scorpio":{(0,10): "Mars", (10,20): "Sun", (20, 30): "Venus" }, 
	"Sagittarius": { (0,10) : "Mercury", (10,20) : "Moon", (20,30) : "Saturn"}, 
	"Capricorn": {(0,10): "Jupiter", (10,20): "Mars", (20,30): "Sun" }, 
	"Aquarius": {(0,10): "Venus", (10,20): "Mercury", (20, 30): "Moon" }, 
	"Pisces": { (0,10): "Saturn", (10,20): "Jupiter", (20,30): "Mars"}
}

def get_decan_ruler(sign, angle): 
	"""Helper for using DECANS_in_sign dictionary
	Args:
		sign(str): Sign
		angle(int): Degree measure
	Returns: 
		(str) ruler
	"""
	decans_in_sign = DECANS[sign] 
	for key in decans_in_sign.keys(): 
		if angle >= key[0] and angle < key[1]: 
			return decans_in_sign[key] 

#Egyptian term rulers; same bound logic as decan listing
terms = {
	"Aries": {(0,6):"Jupiter", (6,12):"Venus", (12,20): "Mercury", (20,25):"Mars", (25,30):"Saturn"}, 
	"Taurus":  {(0,8): "Venus", (8,14): "Mercury", (14,22): "Jupiter", (22,27):"Saturn", (27,30):"Mars"}, 
	"Gemini":  {(0,6):"Mercury", (6,12):"Jupiter", (12,17):"Venus", (17,24):"Mars", (24,30):"Saturn"}, 
	"Cancer":  {(0,7):"Mars", (7,13):"Venus", (13,19):"Mercury", (19,26):"Jupiter", (26,30):"Saturn"}, 
	"Leo":  {(0,6):"Jupiter", (6,11):"Venus", (11,18):"Saturn", (18,24):"Mercury", (24,30):"Mars"}, 
	"Virgo":  {(0,7): "Mercury", (7,17):"Venus", (17,21):"Jupiter", (21,28):"Mars", (28,30):"Saturn"}, 
	"Libra":  {(0,6):"Venus", (6,14):"Mercury", (14,21):"Jupiter", (21,28):"Mars", (28,30):"Saturn"}, 
	"Scorpio":  {(0,7):"Mars", (7,11):"Venus", (11,19):"Mercury", (19,24):"Jupiter", (24,30):"Saturn"}, 
	"Sagittarius": {(0,12):"Jupiter", (12,17):"Venus", (17,21):"Mercury", (21,26):"Saturn", (26,30):"Mars"}, 
	"Capricorn":  {(0,7):"Mercury", (7,14):"Jupiter", (14,22):"Venus", (22,26):"Saturn", (26,30):"Mars"}, 
	"Aquarius":  {(0,7):"Mercury", (7,13):"Venus", (13,20):"Jupiter", (20,25):"Mars", (25,30):"Saturn"}, 
	"Pisces" :   {(0,12):"Venus", (12,16):"Jupiter", (16,19):"Mercury", (19,28):"Mars", (28,30):"Saturn"}
}	

def get_term_ruler(sign, angle): 
	"""Helper for terms listings
	Args:
		sign(str): Sign
		angle(int): Degree measure
	Returns: 
		(str) ruler
	"""
	terms_in_sign = terms[sign] 
	for key in terms_in_sign.keys():
		if angle >= key[0] and angle < key[1]: 
			return terms_in_sign[key] 

