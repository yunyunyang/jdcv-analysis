from sklearn.feature_extraction.text import CountVectorizer

def extract_keywords(texts):
    vectorizer = CountVectorizer(stop_words='english', max_features=10)
    X = vectorizer.fit_transform(texts)
    return vectorizer.get_feature_names_out()
