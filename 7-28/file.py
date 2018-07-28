import sys

print(sys.argv)
print(sys.version)
print(sys.path)
print(sys.platform)
# sys.exit(1)
for i in sys.path:
    print(i)


print('--------------------------------------->>>>')

import os
print(os.getcwd())

print(os.listdir(os.getcwd()))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(__file__)
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(os.path.dirname(os.path.abspath(__file__)),'pinjie','aaa.txt'))