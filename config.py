import os
from pathlib import Path
import os
TOKEN = os.getenv("TOKEN") or 'BOT TOKEN' #export TOKEN = "   "

BASE_DIR = Path(__file__).resolve().parent
DB_NAME = os.path.join(BASE_DIR, 'db', 'dayOF.sqlite')
