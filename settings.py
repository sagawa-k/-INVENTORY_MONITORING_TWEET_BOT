import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET_KEY = os.environ.get("CONSUMER_SECRET_KEY")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
CONSUMER_TOKEN_SECRET__KEY = os.environ.get("CONSUMER_TOKEN_SECRET__KEY")