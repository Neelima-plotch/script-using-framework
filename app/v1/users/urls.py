# app/v1/movies/urls.py
from flask import Blueprint
from app.v1.users import views as movie_views
v1_movies = Blueprint('v1_movies', __name__)
# Movie_visits API URLs
movies_prefix = '/users'
v1_movies.add_url_rule(movies_prefix + '/getvisitors/<int:movie_id>',
                       view_func=movie_views.GetMovieVisitors.as_view('get_movie_visitors'))
