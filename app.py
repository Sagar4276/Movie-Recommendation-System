import streamlit as st
import pickle
import pandas as pd
import requests
from dotenv import load_dotenv
import os

movies_list = pickle.load(open('./movies.pkl', 'rb'))
similarity = pickle.load(open('./similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
print(movies.columns)
st.title('Movie Recommender System')

option = st.selectbox('Select a Movie', movies['title'].values)


def fetch_poster(movie_id):
    api_key =os.getenv("TMDB_API_KEY")
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    return "https://via.placeholder.com/500x750?text=No+Image"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    recommended_movies = []
    recommended_movies_posters = []
    
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movie_list:
        movie_id = movies.iloc[i[0]]['id']  # Ensure movie_id column exists
        recommended_movies.append(movies.iloc[i[0]]['title'])
        recommended_movies_posters.append(fetch_poster(movie_id))
    
    return recommended_movies, recommended_movies_posters


if st.button("Recommend"):
    names, posters = recommend(option)
    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.image(poster, width=150)
            st.caption(name)
