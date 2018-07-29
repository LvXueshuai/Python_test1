class Open:
    def __init__(self,filename,mode = 'r',encoding = 'utf8'):
        # self.filename = filename
        self.file = open(filename,mode,encoding=encoding)
        self.mode = mode
        self.encoding = encoding

    # def read(self):
    #     pass
    #
    # def write(self):
    #     pass
    def __getattr__(self, item):
        #print(item,type(item))
        # self.file.read
        return getattr(self.file,item)


f1 = Open('a.txt','w')
print(f1.file)

# f1.read    #触发__getattr__

print(f1.read)

sys_f = open('b.txt','w+')
# print('-->',getattr(sys_f,'read'))
#
f1.write('dsgsafgj')
