import os
from pathlib import Path
import os
TOKEN = 'TOKEN'

BASE_DIR = Path(__file__).resolve().parent
DB_NAME = os.path.join(BASE_DIR, 'db\db', 'dayOF.sqlite')

ADMIN_PASSWORD = 'ADMINPASSWORD'

PROMOCODE = 'PROMOCODE'
