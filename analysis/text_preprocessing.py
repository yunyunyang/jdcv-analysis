import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
nltk.download('stopwords')

def preprocess_text(file_path):
    # File path error handling
    if not os.path.isfile(file_path):
        print(f'File path "{file_path}" does not exist.')
        return False

    print(f'file_path = {file_path}')
    # Read and preprocess file
    with open(file_path, 'r') as file:
        content = file.read()
        
        text = content.lower()
        text = re.sub(r'[^\w\s]', '', text)
        
        tokens = word_tokenize(text)

        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words]
        
    return ' '.join(filtered_tokens)