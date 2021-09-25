"""
Patika.dev / Python Temel Proje1

1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

"""

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output = []
def flat(l):
    for i in l:
        if type(i) == list:
            flat(i)
        else:
            output.append(i)
  
flat(l)
print (output)

