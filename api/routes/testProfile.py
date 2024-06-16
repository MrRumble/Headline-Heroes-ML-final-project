from app import app
from lib.token import *
from flask import request, jsonify

@app.route("/myprofile", methods=["GET"])
def get_user(): 
    user_id = request.args.get('userId')
    try:
        token = generate_token(user_id)
        return jsonify({"post": "Token Checker almost works", "token": token}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500