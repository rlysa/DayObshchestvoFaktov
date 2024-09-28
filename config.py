import os
from pathlib import Path

TOKEN = 'BOT TOKEN'

BASE_DIR = Path(__file__).resolve().parent
DB_NAME = os.path.join(BASE_DIR, 'db', 'dayOF.sqlite')
