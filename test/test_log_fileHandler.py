import logging
import datetime

workspace="./AutoEmail/logs"
subname=None
b='%s-%s.log' % (subname, str(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')),)
print(type(b))
print(b)

c="2%s"
d="whh"
print(c % (d))

a=workspace %(b,)
a=workspace % ('%s-%s.log' % (subname, str(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d'))),)
print(a)
fh = logging.FileHandler(
            workspace % ('%s-%s.log' % (subname, str(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d'))),))