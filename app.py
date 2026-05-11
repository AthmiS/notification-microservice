import os
import logging
from flask import Flask, request, jsonify

# Setup professional logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# In-memory database
users = [
    {"id": 1, "name": "Ammu"}
]

@app.route('/', methods=['GET'])
def index():
    """Professional Landing Page for the Microservice"""
    return jsonify({
        "message": "Welcome to the OpenBluff User Microservice 🚀",
        "version": "1.0.0",
        "endpoints": {
            "get_users": "/api/v1/users",
            "health_check": "/health"
        },
        "status": "Running"
    }), 200

@app.route('/health', methods=['GET'])
def health_check():
    """Service Health Monitoring"""
    return jsonify({
        "status": "healthy",
        "internship": "@OpenBluff",
        "task": "Task 1"
    }), 200

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    """Returns the professional user list"""
    logger.info("GET /api/v1/users called")
    return jsonify({
        "success": True,
        "data": users,
        "total": len(users)
    }), 200

@app.route('/api/v1/users', methods=['POST'])
def add_user():
    """Adds a user with validation"""
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({
            "success": False, 
            "error": "The 'name' field is required."
        }), 400

    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data['name']
    }
    
    users.append(new_user)
    logger.info(f"Created user: {new_user['name']}")
    
    return jsonify({
        "success": True,
        "data": new_user
    }), 201

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({
        "success": False, 
        "error": "Resource not found. Please visit / for available endpoints."
    }), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port, debug=False)
