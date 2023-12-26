import requests
from requests import Response

Responce: Response = requests.get("http://185.225.232.111:8000/user/11/")
data = Responce.json()
print(Responce.json())


class Users:
    def __init__(self, name, age, email, id):
        self.id = id
        self.name = name
        self.age = age
        self.email = email


user_1 = Users(**data)
print(user_1.id)
print(user_1.name)
print(user_1.email)
print(user_1.age)


