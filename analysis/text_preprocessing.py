import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
nltk.download('stopwords')

def preprocess_text(file_path):    
    with open(file_path, 'r') as file:
        content = file.read()
        
        text = content.lower()        
        text = re.sub(r'[^\w\s]', '', text)
        
        tokens = word_tokenize(text)

        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words]
    
    print(len(filtered_tokens), filtered_tokens)
    return ' '.join(filtered_tokens)