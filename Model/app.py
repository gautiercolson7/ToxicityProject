from detoxify import Detoxify

import json
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

model = Detoxify('original')
app = Flask(__name__)
@app.route('/',methods=['POST'])
def get_data():
    return prediction(request.json['sentences'])

def prediction(sentence):
   
    results = model.predict(sentence)
    converterResults = {
                        label: f'{percentage:.4f}'
                        for label, percentage in results.items()
                        }
    return json.dumps(converterResults)

 