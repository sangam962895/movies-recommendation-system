# app.py
import pickle
import streamlit as st
import requests

import os

# ----------------------------
# Download helper for big files
# ----------------------------
def download_file(url, filename):
    """Download file if not present locally."""
    if not os.path.exists(filename):
        try:
            with st.spinner(f"📥 Downloading {filename} ..."):
                response = requests.get(url, allow_redirects=True, timeout=30)
                response.raise_for_status()
                with open(filename, "wb") as f:
                    f.write(response.content)
                st.success(f"{filename} downloaded successfully ✅")
        except Exception as e:
            st.error(f"❌ Failed to download {filename}: {e}")



# --- Hybrid Movie Info Fetcher ---
def fetch_movie_info(title, tmdb_id=None):
    """
    Fetch poster, IMDb rating, and genre.
    Returns dict with {poster, rating, genre}.
    """
    poster_url = "https://via.placeholder.com/500x750.png?text=No+Poster"
    imdb_rating = "N/A"
    genre = "Unknown"

    # Try TMDB poster first
    if tmdb_id:
        try:
            url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key=76b64f689ed420b78b21d05a0b813306&language=en-US"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            if data.get('poster_path'):
                poster_url = f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
        except Exception:
            pass

    # Fetch details from OMDb (poster + rating + genre)
    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey=12834eba"
        response = requests.get(url, timeout=10)
        data = response.json()
        if data.get('Poster') and data['Poster'] != "N/A":
            poster_url = data['Poster']
        if data.get('imdbRating') and data['imdbRating'] != "N/A":
            imdb_rating = data['imdbRating']
        if data.get('Genre') and data['Genre'] != "N/A":
            genre = data['Genre']
    except Exception:
        pass

    return {"poster": poster_url, "rating": imdb_rating, "genre": genre}

# --- Recommendation Logic ---
def recommend(movie):
    """
    Recommend top 5 movies using cosine similarity.
    """
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

        recommendations = []

        for i in distances[1:6]:  # skip itself
            movie_id = movies.iloc[i[0]].movie_id
            title = movies.iloc[i[0]].title
            info = fetch_movie_info(title, movie_id)
            recommendations.append({
                "title": title,
                "poster": info["poster"],
                "rating": info["rating"],
                "genre": info["genre"]
            })

        return recommendations

    except Exception as e:
        st.error(f"Recommendation error: {e}")
        return []

# --- Streamlit UI ---
st.header('🎬 Movie Recommender System')

# ✅ Auto-download big files if missing
MOVIES_URL = "https://drive.google.com/uc?id=1J-0i_QUX8U73SCWR0hXiROf7l9i_tKAO"
SIMILARITY_URL = "https://drive.google.com/uc?id=1e5UUGH69RA_Y2vfmhVHNNW54UuaASiPZ"


download_file(MOVIES_URL, "movies.pkl")
download_file(SIMILARITY_URL, "similarity.pkl")


try:
    movies = pickle.load(open('movies.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    movie_list = movies['title'].values
except FileNotFoundError:
    st.error("⚠️ Model files not found. Please add 'movies.pkl' and 'similarity.pkl'.")
    movies, similarity, movie_list = None, None, []

selected_movie = st.selectbox("🔎 Type or select a movie", movie_list)

if st.button('Show Recommendation'):
    if movies is not None and similarity is not None:
        recommendations = recommend(selected_movie)
        if recommendations:
            cols = st.columns(5)
            for col, rec in zip(cols, recommendations):
                with col:
                    st.text(rec["title"])
                    st.image(rec["poster"])
                    st.markdown(f"⭐ IMDb: **{rec['rating']}**")
                    st.markdown(f"🎭 Type: *{rec['genre']}*")
    else:
        st.warning("Model not loaded. Please check your files.")
