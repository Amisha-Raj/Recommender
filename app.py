from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import requests

app = Flask(__name__)
@app.route('/')
def hello_world():
    return "hello world"

# # Load pre-computed data (assuming these files exist)
# movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movie_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# API_KEY = "5b591c9935761215110546d7fc36b0f3"  # Replace with your TMDB API key

# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#     response = requests.get(url)
#     data = response.json()
#     poster_path = data.get('poster_path')
#     if poster_path:
#         full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
#         return full_path
#     else:
#         return None

# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movie_list[1:6]:
#         movie_id = movies.iloc[i[0]].movie_id
#         poster_url = fetch_poster(movie_id)
#         if poster_url:
#             recommended_movies.append(movies.iloc[i[0]].title)
#             recommended_movies_posters.append(poster_url)
#         if len(recommended_movies) >= 5:
#             break
#     return recommended_movies, recommended_movies_posters

# @app.route('/')
# def recommend_movies():
#     """Renders the movie recommendation form."""
#     selected_movie_name = movies['title'].values.tolist()  # List of movie titles
#     return render_template('index.html', movie_list=selected_movie_name)

# @app.route('/recommend', methods=['POST'])
# def recommend_movies_api():
#     """Handles POST requests for recommendations and returns JSON data."""
#     selected_movie_name = request.form['movie']
#     recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

#     # Error handling: Check if movie exists
#     if not recommended_movie_names:
#         return jsonify({'error': 'Movie not found. Please try a different movie.'}), 404

#     recommendations = [{'title': title, 'poster_url': poster} for title, poster in zip(recommended_movie_names, recommended_movie_posters)]
#     return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)