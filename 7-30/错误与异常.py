# def test():
#     print('TEST--')
#
# choice_dic={
#     '1':test
# }
#
# while True:
#     choice = input('>>:').strip()
#     if not choice or choice not in choice_dic:
#         print('请重新输入')
#         continue
#     choice_dic[choice]()


#
# try:
#     age = input('>>>>>>:')
#     int(age)
#
#     num = input('------:')
#     int(num)
#
# except ValueError as e:
#     print(e)

while True:
    try:
        age = input('>>>>>>:')
        int(age)
        break
    except ValueError as e:
        print('请重新输入',e)

print('----END----')