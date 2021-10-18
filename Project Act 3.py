from requests import get

print("The information regarding your IP address is shown below") 

print ("IP Address: ", get('https://ipapi.co/ip/').text) #Gets the IP address

print ("City: ", get('https://ipapi.co/city/').text) #Gets the City

print("Region: ", get('https://ipapi.co/region/').text) #Gets the Region

print ("Country: ", get('https://ipapi.co/country_name/').text) #Gets the Country

print("Top level Domain: ", get('https://ipapi.co/country_tld/').text) #Gets the Top level Domain

print("Currency: ", get('https://ipapi.co/currency/').text) #Gets the Currency

print("Currency Name: ", get('https://ipapi.co/currency_name/').text) #Gets the Currency Name

print("Language: ", get('https://ipapi.co/languages/').text)  #Gets the Language

print("Autonomous System Number: ", get('https://ipapi.co/asn/').text) #Gets the Autonomous Systen Number

print("Organization: ", get('https://ipapi.co/org/').text) #Gets the Organization

print("Postal Code: ", get('https://ipapi.co/postal/').text) #Gets the Postal Code

print("Capital: ", get('https://ipapi.co/country_capital/').text) #Gets the Capital

print("European union: ", get('https://ipapi.co/in_eu/').text) #Gets the Europian union

print("Latitude / Longitude: ", get('https://ipapi.co/latlong/').text) #Gets the Latitude / Longitude

print("Time zone: ", get('https://ipapi.co/timezone/').text) #Gets the Time zone
print("Continental Code: ", get('https://ipapi.co/continent_code/').text) #Gets the Continental Code

print("Country Area: ", get('https://ipapi.co/country_area/').text) #Gets the Country Area

print("Country Population: ", get('https://ipapi.co/country_population/').text) #Gets the Country Population

