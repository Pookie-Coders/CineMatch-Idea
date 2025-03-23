from flask import Flask, jsonify, request
from recommendations import recommend_movies

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Movie Recommendation API is running!"})

@app.route('/recommend', methods=['GET'])
def get_recommendations():
    """
    API Endpoint: /recommend
    - Expects 'user_id' as a query parameter.
    - Returns a list of recommended movies.

    Example Request: GET /recommend?user_id=some_user_456
    """
    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify({"error": "Missing user_id parameter"}), 400

    # Get movie recommendations
    recommended_movies = recommend_movies(user_id)

    if not recommended_movies:
        return jsonify({"message": "No recommendations found"}), 404

    return jsonify({"user_id": user_id, "recommendations": recommended_movies})

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False in production
