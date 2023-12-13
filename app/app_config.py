# app/app_config.py
from flask import Flask
from app.v1.users.urls import v1_movies

app = Flask(__name__)

VERSION_OBJECT_MAPPING = {
    '1': v1_movies,
}

def get_url_prefix(version):
    return '/api/v{version_number}'.format(version_number=str(version))

def register_versions(allowed_versions):
    for version in allowed_versions:
        blueprint = VERSION_OBJECT_MAPPING[version]
        app.register_blueprint(blueprint, url_prefix=get_url_prefix(version), name=f'{version}_bp')