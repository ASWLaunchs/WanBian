import time
import hashlib


class Hash:
    def __init__(self):
        # hash
        now = str(time.time()).encode('utf-8')
        self.hashV = hashlib.md5()
        self.hashV.update(now)
        self.hashV.hexdigest()

    def hash(self):
        return self.hashV
