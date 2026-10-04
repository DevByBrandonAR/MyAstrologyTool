from geopy.geocoders import Nominatim

def get_coords_from_place():
	geolocator= Nominatim(user_agent="my_app")
	location = geolocator.geocode(input("Enter location: "))
	x = (location.latitude, location.longitude)
	return x