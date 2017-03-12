import urllib.request
import json
from API_KEYS import WEATHER_UNDERGROUND_KEY

# getting the url
f = urllib.request.urlopen('http://api.wunderground.com/api/' + WEATHER_UNDERGROUND_KEY + '/geolookup/conditions/q/IN/Martinsville.json')

# decoding the text
json_string = f.read().decode('utf-8')

# parsing the information
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']

# printing the location and temperature
print('Current temperature in %s is: %s' % (location, temp_f))
f.close()
