import numpy as np
import timeit
import datetime

def bobelkowo():
    posortowana=True
    while(posortowana):
        posortowana=False
        for i in range(1,liczbaElementow):
            if wierszB[liczbaElementow-i]<wierszB[liczbaElementow-i-1]:
                temp=wierszB[liczbaElementow-i]
                wierszB[liczbaElementow - i]=wierszB[liczbaElementow-i-1]
                wierszB[liczbaElementow - i - 1] = temp
                posortowana=True



def sortowanieSelect():

    min=1000000

    for i in range(liczbaElementow):
        min=100000000
        index=0
        for j in range(i,liczbaElementow):
            if min>wierszS[j]:
                min=wierszS[j]
                index=j
        wierszS[index]=wierszS[i]
        wierszS[i]=min



def partition(lst, start, end):
    pos = start

    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i],lst[pos] = lst[pos],lst[i]
            pos += 1

    lst[pos],lst[end] = lst[end],lst[pos]
    return pos

def quick_sort(lst, start, end):
    if start < end:
        pos = partition(lst, start, end)
        quick_sort(lst, start, pos - 1)
        quick_sort(lst, pos + 1, end)




liczbaElementow = 5000

#wiersz = np.random.randint(1,5001,liczbaElementow)
wiersz = np.arange(5000)

print(wiersz)

np.random.shuffle(wiersz)



print(wiersz)

wierszB=wiersz.copy()
start = datetime.datetime.now()
bobelkowo()
end = datetime.datetime.now()
print("Excecution_time bobelkowo: %s" % (end-start))
print('bobelkowo ', wierszB)

wierszS=wiersz.copy()



wierszQ=wiersz.copy()
start = datetime.datetime.now()
sortowanieSelect()
end = datetime.datetime.now()
print("Excecution_time Select: %s" % (end-start))
print('Select ', wierszS)

start = datetime.datetime.now()
quick_sort(wierszQ, 0, len(wierszQ) - 1)
end = datetime.datetime.now()
print("Excecution_time quick: %s" % (end-start))
print('quick ', wierszQ)



