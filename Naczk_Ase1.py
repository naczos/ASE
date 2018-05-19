import numpy as np

liczbaElementow = 5000

#wiersz = np.random.randint(1,5001,liczbaElementow)
wiersz = np.arange(5000)

print(wiersz)

np.random.shuffle(wiersz)



print(wiersz)

wierszB=wiersz.copy()

posortowana=True
while(posortowana):
    posortowana=False
    for i in range(1,liczbaElementow):
        if wierszB[liczbaElementow-i]<wierszB[liczbaElementow-i-1]:
            temp=wierszB[liczbaElementow-i]
            wierszB[liczbaElementow - i]=wierszB[liczbaElementow-i-1]
            wierszB[liczbaElementow - i - 1] = temp
            posortowana=True

print(wierszB)

wierszS=wiersz.copy()
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

print(wierszS)

# wierszQ=wiersz.copy()
#
#
#
# index=liczbaElementow/2-1
# indexL=0
# indexP=liczbaElementow-1
# odnosnia = wierszQ[index]
# while indexL!=indexP:
#     if wierszQ[indexL]>odnosnia or wierszQ[indexL]<odnosnia:
#         temp=wierszQ[indexL]
#         wierszQ[indexL]=wierszQ[indexP]
#         wierszQ[indexP]=temp
#     indexL=indexL+1
#     indexP=indexL-1



