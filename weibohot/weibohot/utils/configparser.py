import configparser
import os


class MyConfigParser:

    def __init__(self):
        self.CONST_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def getCfByFileName(self, name):
        cf = configparser.ConfigParser()
        cf.read(os.path.join(self.CONST_ROOT_DIR, 'config', 'mysql.ini'))
        return cf
