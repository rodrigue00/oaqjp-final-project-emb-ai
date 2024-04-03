import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    
    def test_happy_statement(self):
        result = emotion_detector("Je suis content que cela soit arrivé")
        self.assertIn('emotion_dominante', result)
    
    def test_angry_statement(self):
        result = emotion_detector("Je suis vraiment en colère à propos de ça")
        self.assertIn('emotion_dominante', result)
    
    def test_disgusted_statement(self):
        result = emotion_detector("Je me sens dégoûté rien qu'en entendant ça")
        self.assertIn('emotion_dominante', result)
    
    def test_sad_statement(self):
        result = emotion_detector("Je suis tellement triste à ce sujet")
        self.assertIn('emotion_dominante', result)
    
    def test_fearful_statement(self):
        result = emotion_detector("J'ai vraiment peur que cela arrive")
        self.assertIn('emotion_dominante', result)

if __name__ == '__main__':
    unittest.main()
