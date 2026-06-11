import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

MAIA_API_KEY = os.getenv("MAIA_API_KEY")
MAIA_BASE_URL = os.getenv("MAIA_BASE_URL")