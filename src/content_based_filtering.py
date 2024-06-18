import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def content_based_filtering(data_path):
    
    # Loading the dataset
    df = pd.read_csv(data_path)
    
    # Vectorizer
    tfidf = TfidfVectorizer(stop_words='english')
    df['tagline'] = df['tagline'].fillna('')
    tfidf_matrix = tfidf.fit_transform(df['tagline'])
    
    # Compute the similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    return cosine_sim