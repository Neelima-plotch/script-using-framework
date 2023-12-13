'''class SubApp1Service:

    def __init__(self, params, headers):
        self.params = params
        self.headers = headers

    def get_static_api_response(self):
        return self.params, 'success'
'''
from app.v1.users.coordinator import sql_connection
class MovieVisitors:
    def __init__(self, movie_id):
        self.movie_id = movie_id

    def get_movie_visitors(self):
        try:
            query = "SELECT SUM(visits) AS visitors_count FROM visitors WHERE movie_id = %s"
            params = (self.movie_id,)
            result = sql_connection.query_db_one(query, params=params, parsed=True)
            visitors_count = result['visitors_count'] if result else 0
            return {'movie_id': self.movie_id, 'visitors_count': visitors_count, 'message': 'success'}
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
          