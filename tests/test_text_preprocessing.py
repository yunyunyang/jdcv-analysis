import os
import unittest

from analysis.text_preprocessing import preprocess_text

class TestTextPreprocessing(unittest.TestCase):
    
    def setUp(self):
      self.basepath = os.path.dirname(__file__)
      self.cv_text = "/../data/cv-test.txt"
      self.job_desc_text = "/data/jd-test.txt"
    
    # Test text preprocessing
    def test_text_preprocessing(self):
        text = preprocess_text(self.basepath + self.cv_text)
        print(text)
        self.assertIsNotNone(text)


if __name__ == '__main__':
    unittest.main()

# python -m unittest discover -s tests