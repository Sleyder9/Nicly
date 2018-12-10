'''
fruits = ["Banane", "Cerises", "Poire", "Quennette"]
fruits.append("Corossol")
'''
'''
for f in fruits:
    print f
'''

'''
i = 0
while i < len(fruits): #len calcule la taille du tableau
    print fruits[i]
    i += 1
'''
import os
def SayHello(name):
    if name:
        print("Hello " + name)
    else:
        name = raw_input("Vous n'avez pas saisi de nom, merci d'en saisir un: ")
        SayHello(name)

SayHello('')
