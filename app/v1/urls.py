'''from flask import Blueprint
from app.v1.users import views as sample_subapp_views


v1 = Blueprint('v1', __name__)


# subapp1 urls
sample_subapp_prefix = '/users'

v1.add_url_rule(sample_subapp_prefix + '/getUserName', view_func=sample_subapp_views.GetUserName.as_view('endpoint_1'))

'''
# app/v1/urls.py
from flask import Blueprint
from app.v1.users.urls import v1_users

# Provide a unique name for the v1 blueprint
v1 = Blueprint('v1', __name__, name='v1_blueprint')

# Users API URLs
users_prefix = '/users'

v1.add_url_rule(users_prefix + '/getvisitors',
                view_func=v1_users.GetUserName.as_view('get_user_visitors'))