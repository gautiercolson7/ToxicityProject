
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
    severeScore = 99
    dictionaryTotransform = {'toxicity': '0.9653', 'severe_toxicity': '0.0052', 'obscene': '0.0797', 'threat': '0.0027', 'insult': '0.6963', 'identity_attack': '0.0158'}
 
    
    def test_loadModel(self):
        assert(type(model)) != None
    
    def test_negativePredictionToxicity(self):
        dictionary = prediction(self.sentenceNegative)
        toxicity = dictionary.split(',')
        assert toxicity[0] == '{"toxicity": "0.9653"'

    def test_negativePredictionSevereToxicity(self):
        dictionary = prediction(self.sentenceNegative)
        severeToxicity = dictionary.split(',')
        assert severeToxicity[1] == ' "severe_toxicity": "0.0052"'

    def test_negativePredictionObscene(self):
        dictionary = prediction(self.sentenceNegative)
        obscene = dictionary.split(',')
        assert obscene[2] == ' "obscene": "0.0797"'

    def test_negativePredictionThreat(self):
        dictionary = prediction(self.sentenceNegative)
        obscene = dictionary.split(',')
        assert obscene[3] == ' "threat": "0.0027"'

    def test_negativePredictionInsult(self):
        dictionary = prediction(self.sentenceNegative)
        obscene = dictionary.split(',')
        assert obscene[4] == ' "insult": "0.6963"'

    def test_negativePredictionIdentity(self):
        dictionary = prediction(self.sentenceNegative)
        obscene = dictionary.split(',')
        assert obscene[5] == ' "identity_attack": "0.0158"}'

    def test_neutralPredictionToxicity(self):
        dictionary = prediction(self.sentenceNeutral)
        toxicity = dictionary.split(',')
        assert toxicity[0] == '{"toxicity": "0.4223"'
       
    def test_neutralPredictionSevereToxicity(self):
        dictionary = prediction(self.sentenceNeutral)
        toxicity = dictionary.split(',')
        assert toxicity[1] == ' "severe_toxicity": "0.0004"'

    def test_neutralPredictionObscene(self):
        dictionary = prediction(self.sentenceNeutral)
        toxicity = dictionary.split(',')
        assert toxicity[2] == ' "obscene": "0.0062"'

    def test_neutralPredictionThreat(self):
        dictionary = prediction(self.sentenceNeutral)
        toxicity = dictionary.split(',')
        assert toxicity[3] == ' "threat": "0.0010"'

    def test_neutralPredictionInsult(self):
        dictionary = prediction(self.sentenceNeutral)
        toxicity = dictionary.split(',')
        assert toxicity[4] == ' "insult": "0.0557"'

    def test_neutralPredictionIdentity(self):
        dictionary = prediction(self.sentenceNeutral)
        toxicity = dictionary.split(',')
        assert toxicity[5] == ' "identity_attack": "0.0015"}'


    def test_positiveToxicity(self):
        dictionary = prediction(self.sentencePositive)
        toxicity = dictionary.split(',')
        assert toxicity[0] == '{"toxicity": "0.0017"'
    
    def test_positiveSevereToxicity(self):
        dictionary = prediction(self.sentencePositive)
        toxicity = dictionary.split(',')
        assert toxicity[1] == ' "severe_toxicity": "0.0001"'

    def test_positiveObscene(self):
        dictionary = prediction(self.sentencePositive)
        toxicity = dictionary.split(',')
        assert toxicity[2] == ' "obscene": "0.0002"'

    def test_positiveThreat(self):
        dictionary = prediction(self.sentencePositive)
        toxicity = dictionary.split(',')
        assert toxicity[3] == ' "threat": "0.0001"'

    def test_positiveInsult(self):
        dictionary = prediction(self.sentencePositive)
        toxicity = dictionary.split(',')
        assert toxicity[4] == ' "insult": "0.0002"'
    
    def test_positiveIdentity(self):
        dictionary = prediction(self.sentencePositive)
        toxicity = dictionary.split(',')
        assert toxicity[5] == ' "identity_attack": "0.0002"}'
       
    def test_jsonTransform(self):
        dictionary = jsonTransform(self.dictionaryTotransform)
        assert dictionary == {'values': {'identity_attack': 2.0, 'insult': 70.0, 'obscene': 8.0, 'severe_toxicity': 1.0, 'threat': 1.0, 'toxicity': 97.0}}
    
    def test_findImages(self):
        images = findImages(self.toxicityScore)
        assert  images == 'tmp/neutre.jpg'

    def test_findImagesSad(self):
        images = findImages(self.severeScore)
        assert  images == 'tmp/triste.jpg'
   #pytest --cov=.
        
        
