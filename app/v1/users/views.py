'''from flask.views import MethodView
from app.decorators import validate_request
from app.common_utils import render_success_response
from app.v1.users.service import SubApp1Service


class GetUserName(MethodView):

    @validate_request
    def get(self, params, headers, *args, **kwargs):
        response, message = SubApp1Service(params, headers).get_static_api_response()
        return render_success_response(response, message)
'''

from flask.views import MethodView
from app.decorators import validate_request
from app.v1.users.service import MovieVisitors

class GetMovieVisitors(MethodView):
    @validate_request
    def get(self, movie_id, *args, **kwargs):
        try:
            response = MovieVisitors(movie_id).get_movie_visitors()
            return response  
        except Exception as e:
            print(f"Error: {e}")
           
