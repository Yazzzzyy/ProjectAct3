from requests import get

print("The information regarding your IP address is shown below") 

print ("IP Address: ", get('https://ipapi.co/ip/').text) #Gets the IP address and prints it

print ("City: ", get('https://ipapi.co/city/').text) #Gets the City and prints it

print("Region: ", get('https://ipapi.co/region/').text) #Gets the Region and prints it

print ("Country: ", get('https://ipapi.co/country_name/').text) #Gets the Country and prints it

print("Top level Domain: ", get('https://ipapi.co/country_tld/').text) #Gets the Top level Domain and prints it

print("Currency: ", get('https://ipapi.co/currency/').text) #Gets the Currency and prints it

print("Currency Name: ", get('https://ipapi.co/currency_name/').text) #Gets the Currency Name and prints it

print("Language: ", get('https://ipapi.co/languages/').text)  #Gets the Language and prints it

print("Autonomous System Number: ", get('https://ipapi.co/asn/').text) #Gets the Autonomous Systen Number and prints it

print("Organization: ", get('https://ipapi.co/org/').text) #Gets the Organization and prints it

print("Postal Code: ", get('https://ipapi.co/postal/').text) #Gets the Postal Code and prints it

print("Capital: ", get('https://ipapi.co/country_capital/').text) #Gets the Capital and prints it

print("European union: ", get('https://ipapi.co/in_eu/').text) #Gets the Europian union and prints it

print("Latitude / Longitude: ", get('https://ipapi.co/latlong/').text) #Gets the Latitude / Longitude and prints it

print("Time zone: ", get('https://ipapi.co/timezone/').text) #Gets the Time zone and prints it

print("Continental Code: ", get('https://ipapi.co/continent_code/').text) #Gets the Continental Code and prints it

print("Country Area: ", get('https://ipapi.co/country_area/').text) #Gets the Country Area and prints it

print("Country Population: ", get('https://ipapi.co/country_population/').text) #Gets the Country Population and prints it

