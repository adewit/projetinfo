import uproot

#Pour ouvrir le fichier root, qui contient un 'TTree', nommé 'Events'
events = uproot.open("SMHiggsToZZTo4L.root:Events")

#On peut voir le contenu du TTree Events - chaque ligne est ce qu'on nomme une 'branche'. Une branche peut contenir plusieurs données dans un seul évènement, selon le type de branche (par exemple, 'nMuon' est un seul numéro par évènement, mais s'il y a N muons dans l'évènement, 'Muon_pt' contiendra N quantités 
print(events.show())

# Pour extraire les données du fichier
branches = events.arrays()

#Le plus facile sera d'utiliser les arrays crées ainsi et faire une boucle dessus. Le code peut être développé sur une petite partie du fichier, mais dès qu'il fonctionne il devrait être tourné sur tout le fichier. Ici pour n'utiliser que 10 évènements:  
for i in range(0,10):
    #Imprimer sur l'écran que quelques infos liées aux muons. 
    print(branches["nMuon"][i])
    print(branches["Muon_pt"][i])
    print(branches["Muon_eta"][i])
    print(branches["Muon_phi"][i])


#Voilà on regarde des évènements H->ZZ*->4l. A toi de réconstituer les bosons de Higgs et leur quantités kinématiques (pt, eta, phi, masse), sans utiliser des fonctions d'un python library qui à été conçu pour faire cela. A noter: le boson de Higgs désintegre en 4 leptons, passant par deux bosons Z. C'est-à-dire: les 4 leptons peuvent être 2 paires de muons, 2 paires d'électrons, soit une paire de muons et une paire d'électrons (où les deux muons ou électrons d'une paire doivent avoir des charges électriques opposées). Après avoir reconstitué les bosons de Higgs, fais des plots des quantités principales de ce particule, et ajoute-y le bruit de fond (fichier ZZTo4Mu.root). Je t'ai fait installer quelques packages qui peuvent être utile pour faire des plots, mais tu peux les faire avec n'importe quel package de plots

#Deuxième partie du projet (après avoir réconstituté les bosons de Higgs et avoir fait la même réconstitution sur le fichier contentant du bruit de fond): écrire un programme pour trouver des sélections sur les leptons/le candidat de boson de Higgs réconstitué/autres variables qui optimisent S/sqrt(B), où S indique le nombre d'évènements de boson de Higgs séléctionnés et B le nombre d'évènements du fichier de bruit de fond sélectionnés. 

#Troisième partie: s'il reste du temps, tu peux essayer d'écrire un programme qui produit plus d'évènements, à partir des données qui se trouvent dans les fichiers. Quand tu arrives à ce stade il faut d'abord qu'on en parle pour voir si ça en vaut la peine, ou s'il vaut mieux utiliser le temps qui reste pour autre chose