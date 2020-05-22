#GENERARE CUVANT POTENTIAL
def bktr(w1):
    global P,N,T,isAccepted,givenWord
    if len(w1) > len(givenWord):
        endWord(w1)
    else:
        for i in P:
            if i[0] in w1:
                if i[1] != "":
                    w2 = w1.replace(i[0],i[1])
                    bktr(w2)

#VERIFICARE DACA CUVANTUL POTENTIAL ESTE EGAL CU CEL DAT
def endWord(w1):
    global isAccepted,P,T
    for i in P:
        if i[0] in w1:
            if i[1] == "":
                w1 = w1.replace(i[0], i[1])
                if w1 == givenWord:
                    isAccepted = True
                    break
            else:
                ok = 1
                for j in T:
                    if j in i[1]:
                        ok = 0
                        break
                if ok == 1:
                    endWord(w1.replace(i[0],i[1]))


#INPUT LA P: in ordinea indexului de tuplu: neterminal, cu ce sa fie inlocuit neterminalul
# "" este epsilon

#INPUTS
N = ["S","A"]
T = ["a","b"]
P = [("S","bSbb"),
     ("S","A"),
     ("A","aA"),
     ("A","")]


isAccepted = False

print("Gramatica data este:")
print("Neterminali:")
for i in N:
    print(i, end = "  ")
print()
print("Terminali:")
for i in T:
    print(i, end = "  ")
print()
print("Productii")
for i in P:
    print(i[0],end = " - > ")
    print(i[1])

givenWord = input()

for i in N:
    if isAccepted == False :
        word = i
        bktr(word)

print("Este cuvantul acceptat de aceasta gramatica?")
print(isAccepted)