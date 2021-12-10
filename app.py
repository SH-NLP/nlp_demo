from flask import Flask
from flask import Flask, render_template
from sample_app import Bootstrap


def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
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

    @app.route('/feedback')
    def feedback():
        return render_template('feedback.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
