from flask import Flask, render_template
import parser
import json

app = Flask(__name__)
page_url = 'https://vc.ru'

@app.route('/')
def start():
    parser.publish_report('articles.json',
                          parser.find_articles(
                              parser.get_html_page('https://www.livejournal.com/category/nauka-i-tehnika/')))
    with open("articles.json", "r") as read_file:
        data = json.load(read_file)
        link = data["url"]
        articles = data["articles"]
    return render_template('report.html', link=link, list=articles)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
