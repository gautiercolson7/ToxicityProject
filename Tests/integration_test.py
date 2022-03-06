
import sys
from urllib import response 
import time 

sys.path.append('..')

from Backend.app import *

from Model.app import *

from Frontend.app import *
sys.path.append('Frontend/static/css')


class TestApp:
    model = Detoxify('original')
    sentencePositive = "I love human"
    sentenceNegative = 'I hate you because you are lazy'
    sentenceNeutral = 'you are my dog'
    toxicityScore = 59
    dictionaryTotransform = {'toxicity': '0.9653', 'severe_toxicity': '0.0052', 'obscene': '0.0797', 'threat': '0.0027', 'insult': '0.6963', 'identity_attack': '0.0158'}
 

    def test_port_front(self):
        response =  requests.get('http://localhost:5001')
        assert response.status_code == 200
    
    
    def test_port_back(self):
        response =  requests.get('http://localhost:5000')
        assert response.status_code == 405

    def test_port_model(self):
        response =  requests.get('http://localhost:5002')
        assert response.status_code == 405
    
    
    def test_back_to_model(self):
        response = requests.post('http://localhost:5002', data=json.dumps({'sentences': self.sentencePositive}), headers={'content-type': 'application/json'} )
        assert response.status_code == 200

    def test_model_to_back(self):
        response = requests.post('http://localhost:5000', data=json.dumps({'sentences': self.sentencePositive}), headers={'content-type': 'application/json'} )
        assert response.status_code == 200

    def test_front_to_back(self):
        response = requests.post('http://localhost:5001', data=json.dumps({'sentences': self.sentencePositive}), headers={'content-type': 'application/json'} )
        assert response.status_code == 405





   

