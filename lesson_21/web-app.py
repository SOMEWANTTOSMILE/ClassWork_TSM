from flask import Flask, render_template, request, redirect
from sqlalchemy.orm import Session
from app import Users, engine
from function import upload_db, sync_db, delete_db, database_request


app = Flask(__name__)


@app.route("/", methods=['GET'])
def work_with_data():
    if request.method == 'GET':
        all_users = database_request()
        return render_template('Users.html', all_users=all_users)


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == 'POST':
        upload_db()
    return redirect('/')
    # return render_template("Users.html")


@app.route("/delete", methods=['POST'])
def delete():
    if request.method == 'POST':
        delete_db()
    return redirect('/')


@app.route("/sync", methods=['POST', 'GET'])
def sync():
    if request.method == 'POST':
        sync_db()
    return redirect('/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5400, debug=True)
