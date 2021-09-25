
"""
Patika.dev / Python Temel Proje2

2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]

"""


l = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(l):
    newlist = []
    for i in l:
        i.reverse()
        newlist.append(i)
        newlist = l[::-1]
    return newlist
reverse(l)

