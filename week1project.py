import requests as r

url =  'http://randomuser.me/api/?results=100&gender=male'

response = r.get(url)

data = response.json()
for userData in range(100):
    userInfo = data['results'][userData]

    print(f"Name {userInfo['name']['first']} Gender {userInfo['gender']}")