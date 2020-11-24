from flask import Flask, jsonify
import re
import requests
from requests_html import HTMLSession
app = Flask(__name__)

@app.route('/getTimeStories', methods=['GET'])
def get_news():
    URL = "https://time.com/"
    try:
        session = HTMLSession()
        response = session.get(URL)

    except requests.exceptions.RequestException as e:
        print(e)

    news = [dict() for x in range(5)]
    #for(i in range(1,6):
    resp = response.html.find('body > div.homepage-wrapper > section.homepage-module.latest > ol', first=True).html
    titles = re.findall(re.compile("<a.*?>(.+?)</a>"), resp)
    ad = re.findall(re.compile(r'href=[\'"]?([^\'" >]+)'), resp)

    for n, data in enumerate(news):
        data['title'] = titles[n]
        data['link'] = ad[n]
    return jsonify({'': news})




if __name__ == '__main__':
    app.run(debug=True)