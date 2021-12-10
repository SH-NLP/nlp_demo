from datetime import datetime
import sqlite3

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config

def create_table():
    conn = sqlite3.connect("nlp_demo.db")   # splite3 db 연결
    conn.execute("CREATE TABLE IF NOT EXISTS Feedback(context TEXT, date TEXT)")

db = SQLAlchemy()
migrate = Migrate()

class Feedback(db.Model):
    context = db.Column(db.String(1000), primary_key=True, nullable=False)
    date = db.Column(db.String(20))

    def __init__(self, context, date):
        self.context = context
        self.date = date

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    Bootstrap(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/search')
    def search():
        return render_template('search.html')

    @app.route('/qa')
    def qa():
        return render_template('qa.html')

    @app.route('/dictionary')
    def dictionary():
        return render_template('dictionary.html')

    @app.route('/ner')
    def ner():
        return render_template('ner.html')

    @app.route('/sensitive')
    def sensitive():
        return render_template('sensitive.html')

    @app.route('/feedback', methods=["GET","POST"])
    def feedback():
        if request.method == 'POST':
            context = request.form['context']
            date = datetime.now().strftime("%Y-%m-%d")
            member = Feedback(context, date)
            db.session.add(member)
            db.session.commit()
            return redirect(url_for("feedback"))
        else:
            feedback_list = Feedback.query.all()
            return render_template("feedback.html", feedback_list = feedback_list)
    
    return app



if __name__ == '__main__':
    create_table()
    app = create_app()
    app.run(debug=True)
