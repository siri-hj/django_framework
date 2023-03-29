import hashlib

def md5_password(self):
    m = hashlib.md5()
    m.update(self.encode(encoding='utf-8'))
    return m.hexdigest()

