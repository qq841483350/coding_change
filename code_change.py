# coding:utf8
__author__ = 'liyatao'
#python三种编码转换为中文的方法
#1、第一种编码以&#开头为特征，转换为中文方法     利于python的HTMLparser来转换，代码如下：
import HTMLParser
s1='&#27979;&#35797;'
s2='&#x6D4B;&#x8BD5;'
s1=HTMLParser.HTMLParser().unescape(s1)  #s1转换为中文
s2=HTMLParser.HTMLParser().unescape(s2)  #s2转换为中文
print s1
print s2

#第2种编码以\u为特征，是unicode 字面值，要想获得真正的unicode方法如下：
u=unicode('\u6d4b\u8bd5','unicode_escape')
#u='\u6d4b\u8bd5'.decode('unicode-escape')
print u

#第3种编码以\x 或%开头为特征，转换为中文代码如下：
import urllib
s1=urllib.unquote('\xe6\xb5\x8b\xe8\xaf\x95')
s2=urllib.unquote('%e6%b5%8b%e8%af%95')
print s1
print s2

