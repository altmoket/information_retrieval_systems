from configparser import ConfigParser

class Configuration:
    def __init__(self) -> None:
        self.config = ConfigParser()
        self.config.read('config.ini')
        
    def get(self, section, option):
        return self.config.get(section, option)
    
class File:
    def __init__(self, path) -> None:
        self.path = path
        
    def open(self):
        with open(self.path) as f:
            return f.read()
    
    