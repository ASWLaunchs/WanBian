import time
import hashlib


class Hash:
    def __init__(self):
        # hash
        self.hashV = hashlib.md5()

    def hash(self):
        now = str(time.time()).encode('utf-8')
        self.hashV.update(now)
        return self.hashV.hexdigest()