from app.connections import SqlConnection

# Define the database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'neelima_2012',
    'database': 'movie_visits',
}

# Create an instance of SqlConnection with the specified db_config
sql_connection = SqlConnection(db_config)