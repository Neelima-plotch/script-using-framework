from flask import Flask, request
from connections import SqlConnection
from common_utils import render_success_response, render_error_response
from app_config import *
# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'neelima_2012',
    'database': 'movies'
}
# Create an instance of SqlConnection
db_connection = SqlConnection(db_config)
print("registering routes...")
# Query to create the 'movies' table
create_movies_table_query = """
    CREATE TABLE IF NOT EXISTS movies (
        id INT AUTO_INCREMENT PRIMARY KEY,
        movie_name VARCHAR(255) NOT NULL
    )
"""
# Query to create the 'visitors' table
create_visitors_table_query = """
    CREATE TABLE IF NOT EXISTS visitors (
        id INT AUTO_INCREMENT PRIMARY KEY,
        movie_id INT,
        visits INT,
        FOREIGN KEY (movie_id) REFERENCES movies(id)
    )
"""
# Execute the queries to create the tables
db_connection.query_db(create_movies_table_query)
db_connection.query_db(create_visitors_table_query)

# Function to increment the number of visitors for a movie
def increment_visitors(movie_id):
    # Increment the number of visitors for the given movie_id
    increment_visitors_query = "SELECT SUM(visits) FROM visitors WHERE movie_id = %s"
    # Execute the query using write_db
    db_connection.write_db(increment_visitors_query, (movie_id,))

@app.route('/api/v1/getvisitors', methods=['GET'])
def get_visitors():
    try:
        # Get movie_id from the request parameters
        movie_id = request.args.get('movie_id')
        if movie_id is None:
            return render_error_response('Movie ID parameter is missing', 400)
        # Increment the number of visitors using the function
        increment_visitors(movie_id)
        # Return the number of visitors as JSON in a success response
        response_data = {'movie_id': movie_id}
        return render_success_response(response_data, 'Successfully incremented number of visitors')
    except Exception as e:
        # Return an error response if an exception occurs
        return render_error_response(str(e), 500)

