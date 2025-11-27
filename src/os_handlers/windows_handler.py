from base import OSHandler
from pathlib import Path

class WindowsHandler(OSHandler):
    
    @property
    def home_dir(self):
        return str(Path.home())

    @property
    def scan_hidden(self):
        return False


"""
    def get_home_dir(self):
        return f"{Path.home()}, {type(Path.home())}
"""