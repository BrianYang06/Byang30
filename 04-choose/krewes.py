"""
Harry Zhu
SoftDev
k04 -- Krewes/Dictionary/Creating a dictionary to help with selecting a random Devo.
2022/9/22
time spent: .5 hr
Disco: You can put multiple values per key
QCC: Can you randomly select a number from a list of values rather than a range of numbers?
OPS Summary: We tested how dictionary worked and how you can apply a random element to it.
"""
import random as rng
x = rng.randrange(1,5)
krewes = {1:[3,7],2:[8,4],3:[4,5,4,3,3,8],4:[1,1,1,4]}
print(krewes[x])
