import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


# template = """
# {instance

def get_fact():
    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def get_pig_latin(quote):

    payload = {'input_text': quote}

    response = requests.post("http://hidden-journey-62459.herokuapp.com/piglatinize/", data = payload)
    #response = requests.get("http://hidden-journey-62459.herokuapp.com", params = payload)

    #response = requests.get('http://hidden-journey-62459.herokuapp.com/get', params = payload)
    #response = requests.post('http://hidden-journey-62459.herokuapp.com/post', params=payload)
    print('getpiglattenresponse: ', response.url)
    return response.url


@app.route('/')
def home():
    fact = get_fact().strip()
    print('fact',fact)
    header = get_pig_latin(fact)
    print('header',header)
    print('test ', Response(response=header, mimetype='gzip'))
    return Response(response=header, mimetype='gzip')
    # return


'''
Request URL https://hidden-journey-62459.herokuapp.com/piglatinize/
Request Method: POST
input_text: Two paths diverge
https://hidden-journey-62459.herokuapp.com/
Location: http://hidden-journey-62459.herokuapp.com/esultray/a4de5f6cbef49165d0cc5d49b4ae4b4b/
http://hidden-journey-62459.herokuapp.com/esultray/a4de5f6cbef49165d0cc5d49b4ae4b4b/

'''
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
