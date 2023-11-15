from databases import Database
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, MetaData

load_dotenv()
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"


database = Database(DATABASE_URL + "?min_size=1&max_size=6")
metadata = MetaData()
engine = create_engine(DATABASE_URL)
