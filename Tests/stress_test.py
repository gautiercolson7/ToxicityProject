import sys
import time 

sys.path.append('..')

from Backend.app import *

from Model.app import *

from Frontend.app import *

class TestApp:
    sentencePositive = "I love human"
   
    def test_stress(self):
        start = time.time()
        for i in range(100):
            #front ask data to back and back ask prediction to model. 
            request = requests.post('http://localhost:5000', data=json.dumps({'sentences': self.sentencePositive}), headers={'content-type': 'application/json'} )
            json.loads(request.content.decode('utf-8')) #prediction
        end = time.time()
        assert((end-start)/1000) < 0.1