import os
import base64

from dotenv import load_dotenv

load_dotenv()

TOKEN = base64.b64decode(os.getenv("TOKEN")).decode("utf-8")
admin_id = base64.b64decode(os.getenv("ADMIN_ID")).decode("utf-8")
host = base64.b64decode(os.getenv("PGHOST")).decode("utf-8")
PG_USER = base64.b64decode(os.getenv("PG_USER")).decode("utf-8")
PG_PASS = base64.b64decode(os.getenv("PG_PASS")).decode("utf-8")
