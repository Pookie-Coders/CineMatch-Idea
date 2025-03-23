from flask import Flask, jsonify, request
from recommendations import recommend_movies
import auth

# Initialize Flask app
app = Flask(_name_)

@app.route('/')
def home():
    return jsonify({"message": "Movie Recommendation API is running!"})

@app.route('/recommend', methods=['GET'])
def get_recommendations():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id parameter"}), 400

    recommended_movies = recommend_movies(user_id)

    if not recommended_movies:
        return jsonify({"message": "No recommendations found"}), 404

    return jsonify({"user_id": user_id, "recommendations": recommended_movies})

# Register API
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    return auth.register_user(data)

# Login API
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    return auth.login_user(data)

# Swipe API
@app.route('/swipe', methods=['POST'])
def swipe():
    data = request.json
    user_id = data.get('user_id')
    return auth.save_swipe(user_id, data)

if _name_ == "_main_":
    app.run(debug=True)