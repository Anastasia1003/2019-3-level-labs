from flask import Flask, render_template, redirect, url_for
from main import parser
import json

app = Flask(__name__)
page_url = 'http://thenoisetier.com/blog/tag/BAR'


@app.route('/')
def start():
    parser.publish_report('main/articles.json',
                          parser.find_articles(
                              parser.get_html_page('http://thenoisetier.com/blog/tag/BAR').text))
    with open("main/articles.json", "r") as read_file:
        data = json.load(read_file)
        link = data["url"]
        articles = data["articles"]
    return render_template('report.html', link=link, list=articles)
@app.route('/refresh', methods=['POST'])


def refresh():
    return redirect(url_for('start'))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
