import os
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory database
users = [
    {"id": 1, "name": "Ammu"}
]

@app.route('/', methods=['GET'])
def home():
    # This returns the simple text you see in your browser
    return "Microservice Running 🚀"

@app.route('/users', methods=['GET'])
def get_users():
    """Returns the list of users as professional JSON"""
    return jsonify({"data": users, "total": len(users)}), 200

@app.route('/users', methods=['POST'])
def add_user():
    """Adds a user with validation"""
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data['name']
    }
    
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    # Dynamic port for flexible deployment
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)