from flask import Flask, render_template, request
import requests
import json
from sqlalchemy.orm import Session
from app import Users, engine
from function import upload_db, sync_db, delete_db

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def work_with_data():
    if request.method == 'GET':
        with Session(engine) as session:
            users = session.query(Users).all()
        return render_template('Users.html', users=users)

    elif request.method == 'POST':
        upload = Users(
            name=request.form['name'],
            carbs=request.form['email'],
            age=request.form['age'],

        )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5400, debug=True)