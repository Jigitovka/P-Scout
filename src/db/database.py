import sqlite3
from src.utils import get_project_root
import os

class Database:
    # Default database location search: in var/db/p-scout.sqlite3. Otherwise, specify your own
    def __init__(self, db_path = os.path.join(get_project_root(), 'var', 'db', 'p-scout.sqlite3')):
        self.db_path = db_path
    
    def _connnect(self):
        pass

    def init_schema(self) -> None:
        pass
    


    