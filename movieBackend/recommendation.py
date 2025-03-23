import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from firebase_config import get_liked_movie_ids

PICKLE_FILE_PATH = "backend/dataset/vectorized_movies.pkl"

# Load vectorized movies
with open(PICKLE_FILE_PATH, "rb") as file:
    movie_data = pickle.load(file)

movie_vectors = np.stack(movie_data.values)
movie_ids = list(movie_data.index)


def recommend_movies(user_id, top_n=5):
    liked_movie_ids = get_liked_movie_ids(user_id)
    if not liked_movie_ids:
        print(f"No liked movies found for user {user_id}.")
        return []

    liked_indices = [movie_ids.index(mid) for mid in liked_movie_ids if mid in movie_ids]

    if not liked_indices:
        print("Liked movies not found in dataset.")
        return []

    liked_vectors = movie_vectors[liked_indices]
    similarities = cosine_similarity(liked_vectors, movie_vectors)
    avg_similarity = np.mean(similarities, axis=0)

    recommended_indices = np.argsort(avg_similarity)[::-1][:top_n]
    return [{"movie_id": movie_ids[i], "title": movie_data.index[i]} for i in recommended_indices if movie_ids[i] not in liked_movie_ids]