from flask import Flask, request, jsonify
from firebase_config import db
import auth
import recommendation

app = Flask(_name_)

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

# Recommendation API
@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id')
    return recommendation.get_recommendations(user_id)

if _name_ == '_main_':
    app.run(debug=True)