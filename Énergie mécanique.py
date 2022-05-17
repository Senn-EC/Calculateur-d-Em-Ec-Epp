#calcul de l'energie cinetique 
print("Calculateur d'Em, d'Ec et d'Epp,\n les nombres décimaux doivent être écrit avec un point et non une virgule \n sinon le script plante.")
print (' ')
#input des valeurs nécessaire ici la masse et la vitesse 
m = float(input("masse en kg: "))
print (' ')

v = float(input("vitesse en m/s: "))
print (' ')

#def de la formule de l'énergie cinétique
def Ec(m, v): 
    return 0.5*m*v**2

#print de la réponse finale 
x = int(Ec(m, v))
answerEC = "l'EC pour m= " + str(m)+ " kg" + "\n " " et v= " + str(v) + " m/s" + " a une énergie de " + str(x) + " J."
print (answerEC)
print (' ')

#calcul de l'énergie potantielle de pesanteur

#input des valeurs nécessaire ici la constante de gravitation et l'altitude 
g = float(input("constante de gravitation: "))
print (' ')
z = float(input("altitude en m: "))
print (' ')

#def de la formule de l'énergie potentielle de pesanteur
def Epp(m, g, z):
   return m*g*z

#print de la réponse finale 
xx = int(Epp(m, g, z))
answerEpp = "l'Epp pour m= " + str(m)+ " kg" + "\n " "et pour z= " + str(z) + " m " + " a une énergie de " + str(xx) + " J."
print(answerEpp)
print (' ')

#calcul de l'energie mécanique 
Em = x + xx 
Emx = "Em= " + str(Em) + " J."
print (Emx)
print (' ')

#empeche la fermeture du script apres utilisation 
input('appuyez sur Entrée pour quitter') 