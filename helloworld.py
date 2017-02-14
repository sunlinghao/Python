import urllib
import urllib2
import re

s = 'adfad asdfasdf asdfas asdfawef asd adsfas '
reObj1 = re.compile('(\w+)\s+\w+')
print reObj1.findall(s)
