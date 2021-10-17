from requests import get

print("The information regarding your IP address is shown below")

print ("IP Address: ", get('https://ipapi.co/ip/').text)

print ("City: ", get('https://ipapi.co/city/').text)

print("Region: ", get('https://ipapi.co/region/').text)

print ("Country: ", get('https://ipapi.co/country_name/').text)

print("Top level Domain: ", get('https://ipapi.co/country_tld/').text)

print("Postal Code: ", get('https://ipapi.co/postal/').text)

print("Capital: ", get('https://ipapi.co/country_capital/').text)

print("European union: ", get('https://ipapi.co/in_eu/').text)

print("Latitude / Longitude: ", get('https://ipapi.co/latlong/').text)

print("Time zone: ", get('https://ipapi.co/timezone/').text)

print("Continental Code: ", get('https://ipapi.co/continent_code/').text)

print("Country Area: ", get('https://ipapi.co/country_area/').text)

print("Country Population: ", get('https://ipapi.co/country_population/').text)
