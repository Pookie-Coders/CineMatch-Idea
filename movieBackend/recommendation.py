import pickle
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from firebase_config import get_liked_movie_ids  # Import Firebase function

# Load precomputed movie vectors
PICKLE_FILE_PATH = "backend/dataset/vectorized_movies.pkl"

# Load vectorized movies (movie_id, title, and vectorized tags)
with open(PICKLE_FILE_PATH, "rb") as file:
    movie_data = pickle.load(file)  # Loaded as a DataFrame: movie_id | title | vector

# Convert vectors back to NumPy array
movie_vectors = np.stack(movie_data["vector"].values)  # 2D NumPy array
movie_ids = movie_data["movie_id"].values  # Movie IDs
movie_titles = movie_data["title"].values  # Movie Titles

def recommend_movies(user_id, top_n=5):
    """
    Fetches liked movie IDs, computes cosine similarity, and recommends Top-N movies.

    Args:
        user_id (str): The user's unique Firestore ID.
        top_n (int): Number of recommendations to return.

    Returns:
        list: Top-N recommended movies (title & movie_id).
    """
    # Fetch liked movies from Firestore
    liked_movie_ids = get_liked_movie_ids(user_id)
    if not liked_movie_ids:
        print(f"No liked movies found for user {user_id}.")
        return []

    # Find indices of liked movies in dataset
    liked_indices = [i for i, m_id in enumerate(movie_ids) if m_id in liked_movie_ids]

    if not liked_indices:
        print("Liked movies not found in dataset.")
        return []

    # Extract liked movie vectors
    liked_vectors = movie_vectors[liked_indices]

    # Compute cosine similarity between liked movies & all movies
    similarity_scores = cosine_similarity(liked_vectors, movie_vectors)  # (num_liked_movies, total_movies)
    
    # Average similarity across all liked movies
    avg_similarity = similarity_scores.mean(axis=0)  # (total_movies, )

    # Get Top-N recommendations (excluding liked movies)
    sorted_indices = np.argsort(avg_similarity)[::-1]  # Descending order
    recommended_indices = [idx for idx in sorted_indices if movie_ids[idx] not in liked_movie_ids][:top_n]

    # Retrieve recommended movie titles and IDs
    recommended_movies = [{"movie_id": movie_ids[idx], "title": movie_titles[idx]} for idx in recommended_indices]
    
    return recommended_movies

# Example usage (REMOVE in production)
if __name__ == "__main__":
    test_user_id = "sample_user_123"
    recommendations = recommend_movies(test_user_id)
    print(f"Top Recommendations for {test_user_id}: {recommendations}")
