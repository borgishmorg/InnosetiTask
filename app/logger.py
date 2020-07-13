import pymongo
import datetime
import os


IP = 'localhost'
PORT = 27017

    
class Logger:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
            cls.instance.clients = dict()
            cls.instance.logs = dict()
        return cls.instance
    
    def _logs(self):
        pid = os.getpid()
        if pid not in self.clients:
            self.clients[pid] = pymongo.MongoClient(IP, PORT)
            self.logs[pid] = self.clients[pid].calc_log.log
        return self.logs[pid]
    
    def write(self, tag, **kwargs):
        kwargs.update({
            'tag': tag,
            'datetime': datetime.datetime.now()
        })
        self._logs().insert_one(kwargs)
        
    def log(self, **kwargs):
        self.write('LOG', **kwargs)

    def debug(self, **kwargs):
        self.write('DEBUG', **kwargs)

    def error(self, **kwargs):
        self.write('ERROR', **kwargs)
        