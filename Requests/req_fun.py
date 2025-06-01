import requests

response = requests.get("https://api.github.com")
# print(response.status_code)
# print(response.json())

data = {"username": "admin", "password": "secret"}
response = requests.post("https://httpbin.org/post", data=data)
# print(response.text) 

params = {"q":"python","page":1}
response = requests.get("https://httpbin.org/get",params=params)
# print(response.json())

headers = {"User-Agent": "MyApp/1.0", "Authorization": "Bearer token123"}
response = requests.get("https://api.github.com/user", headers=headers)
print(response.json())

try:
    response = requests.get("https://httpbin.org/delay/5", timeout=3)  # Fails after 3 sec
except requests.exceptions.Timeout:
    print("Request timed out!")

# Session
session = requests.Session()
session.headers.update({"User-Agent": "MyApp"})

# Reuse session for multiple requests
response1 = session.get("https://httpbin.org/cookies/set/sessioncookie/123")
response2 = session.get("https://httpbin.org/cookies")  # Cookies persist
print(response2.json())  # Shows saved cookies

#upload file
files = {"file": open("report.pdf", "rb")}
response = requests.post("https://httpbin.org/post", files=files)

proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
response = requests.get("http://example.com", proxies=proxies)


# Mock
from unittest.mock import patch

with patch("requests.get") as mock_get:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"key": "value"}
    response = requests.get("https://api.example.com")
    assert response.json()["key"] == "value"