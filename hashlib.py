import hashlib

obj = hashlib.md5("sfdsg".encode("utf8"))   #加盐加密
obj3 = hashlib.sha256("sfdsg".encode("utf8"))   #加盐加密
obj1 = hashlib.md5("sfdsg".encode("utf8"))

obj.update("hello".encode("utf8"))
obj2.update("hello".encode("utf8"))
obj3.update("hello".encode("utf8"))
print(obj.hexdigest())
print(obj1.hexdigest())
print(obj3.hexdigest())




