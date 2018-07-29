# a = '{0}{0}{0}'.format('dog')
# print(a)
#
# class Date:
#     def __init__(self,year,mon,day):
#         self.year = year
#         self.mon = mon
#         self.day = day
#
# d1 = Date(2018,7,29)
# x = '{0.year}{0.mon}{0.day}'.format(d1)
# print(x)
#
# y = '{0.year}-{0.mon}-{0.day}'.format(d1)
# print(y)


dic = {
    'a':'{0.year}-{0.mon}-{0.day}',
    'b':'{0.year}:{0.mon}:{0.day}',
    'c':'{0.year}/{0.mon}/{0.day}'
}
class Date:
    def __init__(self,year,mon,day):
        self.year = year
        self.mon = mon
        self.day = day

    def __format__(self, format_spec):

        if not format_spec or format_spec not in dic:
            format_spec = 'c'
        print("--------->>>>>", format_spec)
        fm = dic[format_spec]
        # return '{0.year}-{0.mon}-{0.day}'.format(self)
        return fm.format(self)

d1 = Date(2018,7,29)
format(d1)
print(format(d1))
print('--------------------------->')
print(format((d1),"a"))
print(format((d1),"f"))

