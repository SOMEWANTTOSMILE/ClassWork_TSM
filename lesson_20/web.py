from flask import Flask, render_template, request, jsonify
from app import Article, Author, engine
from sqlalchemy.orm import Session
import json


app = Flask(__name__)


@app.route('/')
def hello():
    return "hello, World!"


@app.route('/create_article',  methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        name_article = request.form['name_article']
        content = request.form['content']
        new_article = {
            "name": name_article,
            "content": content
        }
        print(new_article)
        article_name, content = new_article.get("name"), new_article.get("content")
        with Session(engine) as db:
            arts = Article(article_name=article_name, content=content)
            db.add(arts)
            db.commit()
    return render_template('main.html')


@app.route('/article/')
def main_page():
    with Session(engine) as sess:
        count = sess.query(Article).count()
        return f"Total count - {count}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5400, debug=True)
