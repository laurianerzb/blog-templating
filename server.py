import datetime
from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_current_year():
    current_year = datetime.datetime.now().year
    return current_year


@app.route('/')
def home():
    current_year = get_current_year()
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    data = response.json()
    return render_template("index.html", current_year=current_year, data=data)


@app.route('/blog/<int:num>')
def get_blog(num):
    current_year = get_current_year()
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    data = response.json()
    return render_template("post.html",current_year=current_year, data=data, num=num)


if __name__ == "__main__":
    app.run(debug=True)
