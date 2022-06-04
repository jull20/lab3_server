import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '../../.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Application port
PORT = int(os.environ.get("PORT"))

DEBUG: bool = os.environ.get("DEBUG") == "True"