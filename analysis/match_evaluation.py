from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# from analysis.text_preprocessing import preprocess_text

def evaluate_match(cv_text, job_desc_text):
    if not cv_text or not job_desc_text:
        print('CV or JD is missing.')
        return
    
    vectorizer = CountVectorizer().fit_transform([cv_text, job_desc_text])
    similarity_matrix = cosine_similarity(vectorizer)
    return similarity_matrix[0][1]
