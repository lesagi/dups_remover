import hashlib


class HashUtil:
    def __init__(self):
        self.hash_util = hashlib.sha1()

    def reset(self):
        self.hash_util = hashlib.sha1()

    def update(self, data):
        self.hash_util.update(data)

    def digest(self):
        return self.hash_util.digest()