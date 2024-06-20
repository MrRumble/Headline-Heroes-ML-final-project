from app import app
from flask import Flask, request, jsonify, redirect
from dotenv import load_dotenv
from lib.movie_repository import MovieRepository
from flask_cors import CORS
from lib.database_connection import get_db

@app.route("/landing-page", methods=["GET"])
def get_top_movies():
    db = get_db()
    movie_repo = MovieRepository(db)
    top_movies = movie_repo.find_top_movies(12)
    print(top_movies)
    return top_movies

