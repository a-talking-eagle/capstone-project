import requests

url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key=AIzaSyCgkwLXOcAjQyodMh2lZjeyiSJMNCxj0Sk"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)