import pandas as pd
import streamlit as st
import pickle
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]


movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

option = st.selectbox('How would you like to be contacted?',movies['title'].values)
if st.button('recommend'):
    recommend(option)
    st.write(option)
