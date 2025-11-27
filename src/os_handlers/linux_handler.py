from base import OSHandler
from pathlib import Path

class LinuxHandler(OSHandler):
    @property
    def home_dir(self):
        return str(Path.home())
    
    @property
    def scan_hidden(self):
        return False
    
