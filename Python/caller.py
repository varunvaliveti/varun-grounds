import requests

apiURL = "http://127.0.0.1:8000"
event_id = 10
print("calling the api")

r = requests.get(
    url=apiURL + f"/event/{event_id}",
)

print("response is " + r.text)
