'''
with obj as f:     等同于f = obj.__enter()
    pass
sith obj ---->触发obj.__enter__(),拿到返回值
as f ----->f = 返回值
执行代码块：
    无异常，整个代码块运行完触发__exit__(),三个参数都为None
    有异常，从异常出现的位置直接触发__exit__:
        如果__exit__返回值为true，代表吞掉异常，不显示
        如果__exit__返回值不为true，代表吐出异常
        __exit__的运行完毕代表整个with语句的执行完毕



'''
class Open:
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('ENTER')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  #异常类，异常值，追踪信息
        print('EXIT')
        print('异常类',exc_type)
        print('异常信息',exc_val)
        print('追踪信息',exc_tb)
        return True   #吞掉异常，不报告




#f = Open('a.txt')
with Open('a.txt') as f:    #with过程触发__enter__()
    print('-----------')
    print(f)
    print(f.name)
    print(sdagjhtrj) #异常
    print('>>>>>>>>>')

    #执行完毕触发__exit__()
print('********')
