from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
# sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "HAJSSZDVOVYPI3MQVCMJJNIEV2EVRWIMUYZI503R52P4W0ZZ"
foursquare_client_secret = "EGXLBRVS0PS21HREFXLKEXZXSPFCRE3IFCGYOVGZIEIB4GUK"


def findARestaurant(mealType,location):
  
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
	lat, lng = getGeocodeLocation(location)
  #2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sush
	url = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&v=20180323&ll={},{}&query={}'.format(foursquare_client_id, foursquare_client_secret, lat, lng, mealType)
  
	h = httplib2.Http()

	result = json.loads(h.request(url,'GET')[1])
	
	#3. Grab the first restaurant
	restaurant = result['response']['venues'][0]
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	url = 'https://api.foursquare.com/v2/venues/{}/photos?client_id={}&client_secret={}&v=20180323'.format(restaurant['id'], foursquare_client_id, foursquare_client_secret)
	
	result = json.loads(h.request(url,'GET')[1])
	
	#5. Grab the first image

	#6. If no image is available, insert default a image url

	if result['response']['photos']['count'] == 0:
		url = 'http://lorempixel.com/300/300'    		
	else:
		photo = result['response']['photos']['items'][0]		
		url = str(photo['prefix'])+'original'+str(photo['suffix'])
    
	name = restaurant['name']
	address = ''
	if 'address' in restaurant['location'].keys():
		address = restaurant['location']['address']
	elif 'cc' in restaurant['location'].keys():
    		address = restaurant['location']['cc']

	#7. Return a dictionary containing the restaurant name, address, and image url	
	print('Restaurant Name: {}'.format(name))
	print('Restaurant Address: {}'.format(address))
	print('Restaurant Photo: {}'.format(url))
	print()

	return {
		'name': name,
		'address': address,
		'image_url': url
	}


if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney Australia")