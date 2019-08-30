"""
Set env vars:

export APP_ID=<app_id>
export APP_SECRET=<app_secret>
export API_VERSION=<api_version>
"""

import os

import facebook

APP_ID = os.environ.get('APP_ID')
APP_SECRET = os.environ.get('APP_SECRET')
API_VERSION = os.environ.get('API_VERSION')

graph = facebook.GraphAPI(version=API_VERSION)
token = graph.get_app_access_token(app_id=APP_ID, app_secret=APP_SECRET, offline=True)
