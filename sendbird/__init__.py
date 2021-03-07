from os import environ

from . import exceptions
from .api_resources import *


api_token = environ.get("SENDBIRD_API_TOKEN")
api_app_id = None
api_base = "https://api.sendbird.com/v3/"
