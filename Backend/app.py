from flask_cors import CORS
from flask import Flask, request
import requests
import json
from dotenv import load_dotenv
import pandas as pd
import numpy as np

load_dotenv()

app = Flask(__name__)
cors = CORS(app)
@app.route('/',methods=['POST']) 
def getmodel():
    value =  request.json['sentences']
    response =requests.post('http://localhost:5002', data=json.dumps({'sentences': value}), headers={'content-type': 'application/json'})
    content = json.loads(response.content.decode('utf-8'))
    return jsonTransform(content)
    


def jsonTransform(prediction):
    converterResults = {
                        label: float(percentage)
                        for label, percentage in prediction.items()
                        }
    df = pd.DataFrame(converterResults, index=['values'])
    df.toxicity = (df.toxicity*100).apply(np.ceil) 
    df.severe_toxicity = (df.severe_toxicity*100).apply(np.ceil) 
    df.obscene = (df.obscene*100).apply(np.ceil) 
    df.threat = (df.threat*100).apply(np.ceil) 
    df.insult = (df.insult *100).apply(np.ceil) 
    df.identity_attack  = (df.identity_attack*100).apply(np.ceil) 
    result = df.to_json(orient="index")
    parsed = json.loads(result)
    json.dumps(parsed, indent=4)  

    return parsed

"""
    toxicity = 'Toxicity = ' + str(value['values']['toxicity'])+' %'
    severe_toxicity = 'Severe toxicity = ' + str(value['values']['severe_toxicity'])+' %'
    obscene = 'Obscene = ' + str(value['values']['obscene'])+' %'
    threat = 'Threat = ' + str(value['values']['threat'])+' %'
    insult = 'Insult = ' + str(value['values']['insult'])+' %'
    idd_attack = 'Identity attack = ' + str(value['values']['identity_attack'])+' %'
"""