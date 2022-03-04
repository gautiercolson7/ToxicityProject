
import sys 

sys.path.append('..')

from Backend.app import *

from Model.app import *

from Frontend.app import *


class TestApp:
    model = Detoxify('original')
    sentencePositive = "I love human"
    sentenceNegative = 'I hate you because you are lazy'
    sentenceNeutral = 'you are my dog'
    toxicityScore = 59
    dictionaryTotransform = {'toxicity': '0.9653', 'severe_toxicity': '0.0052', 'obscene': '0.0797', 'threat': '0.0027', 'insult': '0.6963', 'identity_attack': '0.0158'}
 
    
    def test_load_model(self):
        assert(type(model)) != None
    
    def test_negative_prediction(self):
        dictionary = prediction(self.sentenceNegative)
        assert dictionary == '{"toxicity": "0.9653", "severe_toxicity": "0.0052", "obscene": "0.0797", "threat": "0.0027", "insult": "0.6963", "identity_attack": "0.0158"}'

    def test_neutral_prediction(self):
        dictionary = prediction(self.sentenceNeutral)
        assert dictionary == '{"toxicity": "0.4223", "severe_toxicity": "0.0004", "obscene": "0.0062", "threat": "0.0010", "insult": "0.0557", "identity_attack": "0.0015"}'


    def test_positive_prediction(self):
        dictionary = prediction(self.sentencePositive)
        assert dictionary == '{"toxicity": "0.0017", "severe_toxicity": "0.0001", "obscene": "0.0002", "threat": "0.0001", "insult": "0.0002", "identity_attack": "0.0002"}'
       
    def test_jsonTransform(self):
        dictionary = jsonTransform(self.dictionaryTotransform)
        assert dictionary == {'values': {'identity_attack': 2.0, 'insult': 70.0, 'obscene': 8.0, 'severe_toxicity': 1.0, 'threat': 1.0, 'toxicity': 97.0}}
    
    def test_findImages(self):
        images = findImages(self.toxicityScore)
        assert  images == 'tmp/neutre.jpg'
    #def test_jsonTransform(prediction):