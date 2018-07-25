import hashlib

obj = hashlib.md5("sfdsg".encode("utf8"))   #加盐加密

obj.update("hello".encode("utf8"))

print(obj.hexdigest())

obj = hashlib.sha256("sfdsg".encode("utf8"))   #加盐加密

obj.update("hello".encode("utf8"))

print(obj.hexdigest())