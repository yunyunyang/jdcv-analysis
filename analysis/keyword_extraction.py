from sklearn.feature_extraction.text import CountVectorizer

def extract_keywords(cv_text, job_desc_text):
    if not cv_text or not job_desc_text:
        print('CV or JD is missing.')
        return
    
    texts = [cv_text, job_desc_text]    
    vectorizer = CountVectorizer(stop_words='english', max_features=10)
    X = vectorizer.fit_transform(texts)
    
    return vectorizer.get_feature_names_out()
