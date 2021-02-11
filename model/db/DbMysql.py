from mysql import connector
import ujson
from pathlib import Path
from os import path



class DbMysql():
    def __init__(self):
        self.mConfig: dict = ujson.load(open(path.join(Path.cwd().parent.parent, "cfg", "mySqlConfig.json")))
        self.mConn = connector.connect(
            host=self.mConfig["host"],
            user=self.mConfig["user"],
            password=self.mConfig["password"],
            database=self.mConfig["database"],
            port=self.mConfig["port"]
        )