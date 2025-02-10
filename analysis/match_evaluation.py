from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

from analysis.text_preprocessing import preprocess_text

def evaluate_match(cv_text, job_desc_text):        
    vectorizer = CountVectorizer().fit_transform([cv_text, job_desc_text])
    similarity_matrix = cosine_similarity(vectorizer)
    return similarity_matrix[0][1]
