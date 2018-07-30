#raise TypeError('类型错误')

'''
自定义的类需要继承于  BaseException
'''
#class LxsError:   #TypeError: exceptions must derive from BaseException
class LxsError(BaseException):
    def __init__(self,msg):
        self.msg = msg

# raise LxsError('自定义')
print(LxsError('自定义'))
