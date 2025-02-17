import streamlit as st
import pickle
import requests

movies = pickle.load(open("../notebooks/movies_list.pkl", "rb"))
similarity = pickle.load(open("../notebooks/similarity.pkl", "rb"))
movies_list = movies["title"].values

# Create a header for the app
st.header('Movie Recommender System')

# Create a dropdown to select a movie
selectValue = st.selectbox("Select movies from dropdown", movies_list)

# fetch the poster
# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=82656e7b0d029b81910819f810da38db&language=en-US"
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://api.themoviedb.org/t/p/w500/" + poster_path
#     return full_path

# Create a function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movies = []
    # recommend_movies_poster = []
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        # recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies
#, recommend_movies_poster

# Create a button to show the recommendation
if st.button("Show Recommendation"):
    movie_names = recommend(selectValue)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_names[0])
        # st.image(movie_posters[0])
    with col2:
        st.text(movie_names[1])
        # st.image(movie_posters[1])
    with col3:
        st.text(movie_names[2])
        # st.image(movie_posters[2])
    with col4:
        st.text(movie_names[3])
        # st.image(movie_posters[3])
    with col5:
        st.text(movie_names[4])
        # st.image(movie_posters[4])
