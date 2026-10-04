import ephemeris as ep 
import time_conversions as tc 
import angle_conversions as ac  
import info 
import plotting_eg as pe
import coord_util as cu 



(lat, long) = cu.get_coords_from_place()
system = ep.get_house_sys() 
timezone = tc.get_timezone() 
(utc, local_clock)= tc.read_date_time(timezone) 
birth = ep.get_julian_date(utc)  
planets = ep.get_planets(birth) 
houses = ep.get_houses(birth, lat, long ,system)
planets_houses =ep.get_houses_planets(houses, planets)
 
for planet in planets.keys():
	print(
		planet, 
		planets[planet]["Sign/Angle"], "in House", planets_houses[planet], 
		"decan of ", info.get_decan_ruler(
				planets[planet]["Sign/Angle"][0], 
				planets[planet]["Sign/Angle"][1]), 
		"term of ", info.get_term_ruler(
				planets[planet]["Sign/Angle"][0], 
				planets[planet]["Sign/Angle"][1])) 
for i in range(len(houses["houses"])):
	print("House", i+1, ":" ,houses["houses"][i]["Sign/Angle"])

aspects = ac.get_aspects(planets, 8)
ac.print_aspects(aspects)
pe.natal_plot(planets, houses, aspects)