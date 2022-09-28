"""
Brian Yang & Kevin Wang
SoftDev
k05 --
2022/9/28
time spent: .5 hr
Disco:
QCC:
OPS Summary:
"""

info = open('krewes.txt')
strFile = info.read().replace('\n','').split('@@@')
krewes = {}
for i in strFile:
    
