# s1 = 'hello'
s1 = 123
try:
    int(s1)
except IndexError as e:
    print('IndexError',e)
except KeyError as e:
    print('KeyError',e)
except ValueError as e:
    print('ValueError',e)
except Exception as e:   #万能异常，包含所有类型
    print('Exception',e)

else:
    print('try代码块无异常时执行')
finally:
    print('无论任何情况都执行')

print('11111111111111')
print('22222222222222')