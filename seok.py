from flask import Flask, request, jsonify
import requests
import sys
app = Flask(__name__)
from datetime import datetime
a = datetime.today().strftime("%Y%m%d")
response = requests.get(f'http://seokwoo.ms.kr/lunch.view?date={a}')
html = response.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser') 
for tag in soup.select('div[class=menuName]'):
    abc1212 = tag.text
@app.route('/keyboard')
def Keyboard():
    dataSend = {
    }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']
    
    if content == u"안녕":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : abc1212
                                }
                            ]
                        }
                    }
                ]
            }
        }
    else :
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText":{
                            "text" : "아직 공부하고있습니다."
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
