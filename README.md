# MovieRecommendationAI

MovieRecommendationAI is a content-based movie recommendation system built with Python. It uses text data from movie overviews and genres to compute similarities between movies and suggest similar titles based on user input.

## Features

- Data cleaning & preprocessing using pandas.
- Text feature extraction with sklearn's CountVectorizer.
- Cosine similarity computation (sklearn) for unsupervised neighbor search.
- Model serialization with pickle for streamlined deployment.

## Technologies Used

- Python
- NumPy
- pandas
- scikit-learn (sklearn)
- matplotlib
- pickle

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Seal5/MovieRecommendationAI.git
    cd MovieRecommendationAI
    ```
3. **Install required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *If a `requirements.txt` is not provided, install manually:*
    ```bash
    pip install numpy pandas scikit-learn matplotlib
    ```
