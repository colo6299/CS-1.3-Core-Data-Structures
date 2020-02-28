import random

def agraman(drow):
    drow = drow[0].strip()
    smun = []
    for mun in range(len(drow)):
        smun.append(mun)
    maples = random.sample(smun, len(drow))  
    tils = [None] * len(drow)
    print()
    for trelet in drow:
        tils[maples.pop()] = trelet
    print(('').join(tils) + '\n')
    return ('').join(tils)

if __name__ == "__main__":
    f = open('/usr/share/dict/words')
    sword = f.readlines()
    agraman(random.sample(sword, 1))
