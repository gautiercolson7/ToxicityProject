from flask import Flask, render_template, url_for,request
from dotenv import load_dotenv
import requests
import json

load_dotenv()

app = Flask(__name__)
@app.route('/')
@app.route('/index/')
def index():
    description = """
    """
    return render_template('index.html',
                            user_name='',
                            user_image=url_for('static', filename='img/profile.png'),
                            description=description,
                            blur=True)

@app.route('/result/',methods = ['POST'])
def result():
    result = request.form
    sentences = result['sentences']
    response= requests.post('http://localhost:5000', data=json.dumps({'sentences': sentences}), headers={'content-type': 'application/json'})
    response = json.loads(response.content.decode('utf-8'))
   
    toxicity = 'Toxicity = ' + str(response['values']['toxicity'])+' %'
    severe_toxicity = 'Severe toxicity = ' + str(response['values']['severe_toxicity'])+' %'
    obscene = 'Obscene = ' + str(response['values']['obscene'])+' %'
    threat = 'Threat = ' + str(response['values']['threat'])+' %'
    insult = 'Insult = ' + str(response['values']['insult'])+' %'
    idd_attack = 'Identity attack = ' + str(response['values']['identity_attack'])+' %'
    toxicity_text = toxicity + severe_toxicity + obscene + threat + insult + idd_attack
    
    return render_template('result.html',
                            user_name=sentences,
                            user_image=url_for('static', filename=findImages(response['values']['toxicity'])),
                            description=toxicity_text)

def findImages(toxicity):
    if toxicity > 40 and toxicity < 60 :
        return 'tmp/neutre.jpg'
    if toxicity < 50:
        return 'tmp/happy.jpg'
    else:
        return 'tmp/triste.jpg'