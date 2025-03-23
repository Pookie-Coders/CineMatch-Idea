import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase (Run this ONCE when importing this file)
cred = credentials.Certificate("backend/dataset/firebase_service_key.json")  # 🔹 Path to your Firebase service account key
firebase_admin.initialize_app(cred)

# Connect to Firestore
db = firestore.client()

def get_liked_movie_ids(user_id: str):
    """
    Fetches the list of liked movie IDs from Firestore for a specific user.

    Args:
        user_id (str): The user’s unique ID in Firestore.

    Returns:
        list: A list of liked movie IDs.
    """
    user_ref = db.collection("users").document(user_id)  # 🔹 Adjust collection name if needed
    user_data = user_ref.get()

    if user_data.exists:
        liked_movies = user_data.to_dict().get("liked_movies", [])  # Default to empty list if no liked movies found
        return liked_movies
    else:
        print(f"User {user_id} not found in Firestore.")
        return []

# Example usage (REMOVE in production)
if __name__ == "__main__":
    test_user_id = "sample_user_123"
    movie_ids = get_liked_movie_ids(test_user_id)
    print(f"Liked Movie IDs for {test_user_id}: {movie_ids}")
