import sys
from urllib import response 
import time 

sys.path.append('..')

from Backend.app import *

from Model.app import *

from Frontend.app import *

class TestApp:
    sentencePositive = "I love human"
   
    dictionaryTotransform = {'values': {'toxicity': 1.0, 'severe_toxicity': 1.0, 'obscene': 1.0, 'threat': 1.0, 'insult': 1.0, 'identity_attack': 1.0}}
 

    def test_application(self):
        response = requests.post('http://localhost:5002', data=json.dumps({'sentences': self.sentencePositive}), headers={'content-type': 'application/json'} )
        content = json.loads(response.content.decode('utf-8')) #prediction
        value = jsonTransform(content) #transform 
        assert value == self.dictionaryTotransform #test value
     