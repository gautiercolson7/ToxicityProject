from detoxify import Detoxify
import pickle
import pandas as pd
import numpy as np
import json
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

model = Detoxify('original')
app = Flask(__name__)
@app.route('/',methods=['POST']) 
def predict():
    value =  request.json['sentences']
    results = model.predict(value)
    converterResults = {
                        label: f'{percentage:.4f}'
                        for label, percentage in results.items()
                        }
    return json.dumps(converterResults)
 
'''
def main():
    filename = "loaded_model.pkl"
    #pickle.dump(model,open(filename,'wb'))
    predict('I hate you because you are lazy')

if __name__ == '__main__':
    main()
'''