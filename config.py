import os
from dotenv import load_dotenv, find_dotenv


if os.environ.get('FLASK_DEBUG') == 1:
    # Disabled dotenv TODO decide how to get env vars!
    load_dotenv()
