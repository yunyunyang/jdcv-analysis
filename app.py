import os
from analysis.text_preprocessing import preprocess_text
from analysis.keyword_extraction import extract_keywords
from analysis.match_evaluation import evaluate_match

# Base path
basepath = os.path.dirname(__file__)

# CV and JD path
cv_text = "/data/cv-test.txt"
job_desc_text = "/data/jd-test.txt"

# Text preprocessing
print(basepath + cv_text)
cv_text = preprocess_text(basepath + cv_text)
job_desc_text = preprocess_text(basepath + job_desc_text)

# Extract keyword
keywords = extract_keywords(cv_text, job_desc_text)

# Match Score
match_score = evaluate_match(cv_text, job_desc_text)
print(f"Match Score: {match_score}")
