import  requests,pprint

payload = {
    "action":"list_thing",
    "id": 6
}

response = requests.Get('http://localhost/api/things/manage/',
              data=payload)

pprint.pprint(response.json())