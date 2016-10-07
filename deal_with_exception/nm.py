# encoding=utf8
import re

t = u'无法删除 路由lkjlkpkpkk"An unknown exception occurred." jwefokwljof123 "12321434"id:29384'
s = u"An unknown exception occurred."
z = u"你好"
print re.sub(s, z, t)