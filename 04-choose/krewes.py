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
listPeriods = [2,7,8]
krewes = {
           2:["NICHOLAS", "ANTHONY", "BRIAN", "SAMUEL", "JULIA", "YUSHA", "CRAIG", "FANG MIN", "JEFF", "KONSTANTIN", "AARON", "VIVIAN", "AYMAN", "TALIA", "FAIZA", "ZIYING", "YUK KWAN", "DANIEL", "WEICHEN", "MAYA", "ELIZABETH", "ANDREW", "VANSH", "JONATHAN", "ABID", "WILLIAM", "HUI", "ANSON", "KEVIN", "DANIEL", "IVAN", "JASMINE", "JEFFREY", "Ruiwen"],
           7:["DIANA", "DAVID", "SAM", "PRATTAY", "ANNA", "JING YI", "ADEN", "EMERSON", "RUSSELL", "JACOB", "WILLIAM", "NADA", "SAMANTHA", "IAN", "MARC", "ANJINI", "JEREMY", "LAUREN", "KEVIN", "RAVINDRA", "SADI", "EMILY", "GITAE", "MAY", "MAHIR", "VIVIAN", "GABRIEL", "BRIANNA", "JUN HONG", "JOSEPH", "MATTHEW", "JAMES", "THOMAS", "NICOLE", "Karen"],
           8:["ALEKSANDRA", "NAKIB", "AMEER", "HENRY", "DONALD", "YAT LONG", "SEBASTIAN", "DAVID", "YUKI", "SHAFIUL", "DANIEL", "SELENA", "JOSEPH", "SHINJI", "RYAN", "APRIL", "ERICA", "JIAN HONG", "VERIT", "JOSHUA", "WILSON", "AAHAN", "GORDON", "JUSTIN", "MAYA", "FAIYAZ", "SHREYA", "ERIC", "JEFFERY", "BRIAN", "KEVIN", "SAMSON", "BRIAN", "HARRY", "CORINA", "Wanying", "Kevin"]
         }
#input = input("Select class period:")
period = rng.choice(listPeriods)
#print(rng.choice(krewes[x]) + ' from period ' + str(period))

response,periodNum = input("Choose a class (YES Class#/NO):").split()
if response == 'YES':
    for i in listPeriods:
        if i == int(periodNum):
            print(rng.choice(krewes[int(periodNum)]),'from period', periodNum)
elif response == 'NO':
    print(rng.choice(krewes[period]), 'from period', str(period))
