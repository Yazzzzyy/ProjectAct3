from requests import get

print("The information regarding your IP address is shown below")

print ("IP Address: ", get('https://ipapi.co/ip/').text)

print ("City: ", get('https://ipapi.co/city/').text)

print("Region: ", get('https://ipapi.co/region/').text)

print ("Country: ", get('https://ipapi.co/country_name/').text)

print("Top level Domain: ", get('https://ipapi.co/country_tld/').text)

print("Currency: ", get('https://ipapi.co/currency/').text)

print("Currency Name: ", get('https://ipapi.co/currency_name/').text)

print("Language: ", get('https://ipapi.co/languages/').text)

print("Autonomous System Number: ", get('https://ipapi.co/asn/').text)

print("Organization: ", get('https://ipapi.co/org/').text)
