import requests
from app import Users, engine
from sqlalchemy.orm import Session


def get_users_information():
    req = requests.get("http://185.225.232.111:8000/user/")
    users_from = req.json()
    user_id = [i['id'] for i in users_from]
    data = []
    for i in user_id:
        response = requests.get(f'http://185.225.232.111:8000/user/{i}')
        all_info = response.json()
        data.append({"name": all_info.get('name'), "email": all_info.get('email'), "age": all_info.get('age')})
    return data


def database_request():
    with Session(engine) as session:
        user_info = get_users_information()
        all_users = []
        for user in user_info:
            with Session(engine) as db:
                name = user["name"]
                email = user["email"]
                age = user["age"]
                users = [name, email, age]
                all_users.append(users)
        return all_users



def upload_db():
    user_info = get_users_information()
    for user in user_info:
        with Session(engine) as db:
            name = user["name"]
            email = user["email"]
            age = user["age"]
            arts = Users(user_name=name, email=email, age=age)
            db.add(arts)
            db.commit()


def delete_db():
    user_info = get_users_information()
    with Session(engine) as db:
        db.query(Users).delete()
        db.commit()


def sync_db():
    delete_db()
    upload_db()


#
print(database_request())
