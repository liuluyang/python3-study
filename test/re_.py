

import re

t = '001_13213'

m = re.match('\d{3}_\d{3,8}', t)
print (m)

mm = re.compile('[0-9a-zA-Z\.]+@[0-9a-zA-Z]+\.com')
print (mm.match('qeq@11.com'))

m3 = re.compile('^12$|com')
print  (m3.match('121'))