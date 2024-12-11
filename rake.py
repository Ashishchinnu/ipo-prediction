# rake.py
import pandas as pd
from rake_nltk import Rake
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load your dataset only once when the module is imported
df = pd.read_csv('your_file_with_keywords.csv')
df['Full Description'] = df['Full Description'].fillna('').astype(str)

# Function to extract keywords using RAKE
def extract_keywords(text):
    rake = Rake()
    rake.extract_keywords_from_text(text)
    return ' '.join(rake.get_ranked_phrases())

# Function to find top N similar entries based on a description
def find_unique_similar_entries(description, df, top_n=10):
    description_keywords = extract_keywords(description)
    df['keywords'] = df['Full Description'].apply(extract_keywords)
    vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
    corpus = df['keywords'].tolist() + [description_keywords]
    X = vectorizer.fit_transform(corpus)
    similarities = cosine_similarity(X[-1], X[:-1]).flatten()
    df['similarity'] = similarities
    top_entries = df.sort_values(by='similarity', ascending=False).drop_duplicates(subset='Organization Name')
    top_entries = top_entries.head(top_n)
    return top_entries[['Organization Name', 'Full Description', 'similarity']].to_dict(orient='records')
