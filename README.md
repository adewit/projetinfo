## Pour commencer
Title: reconstructing the Higgs boson at CMS and distinguishing it from background
In this project the student will use simulated data from the Compact Muon Solenoid (CMS) experiment at the CERN Large Hadron Collider (LHC) to first reconstruct the Higgs boson from its decay products, without making use of existing function libraries that were designed to this effect. Once this is implemented, the written code will be applied to both simulated signal events and simulated background events, and a program will be written to determine the optimal selection to make on the variables provided to obtain the highest signal-to-background ratio.
If time allows, a next step would be to attempt to simulate additional events, based on the information extracted from the provided samples. 


### Télécharger les données
Les données sont enregistrées dans des fichiers "root". Ils peuvent être téléchargées ici:

 - `SMHiggsToZZTo4L.root` from http://opendata.cern.ch/record/12361
 - `ZZTo4mu.root` from http://opendata.cern.ch/record/12362


### Software

Installer le code JupyterLab desktop selon les indications pour ton OS précisées ici: https://github.com/jupyterlab/jupyterlab-desktop.

Après avoir ouvert JupyterLab pour la première fois, le logiciel te demandera peut-être si tu veux installer python, il faut sélectionner 'oui'.

JupyterLab peut être utilisé pour faire tourner des jupyter notebooks, en plus ça peut être utilisé pour ouvrir un terminal (file->new->terminal) où faire tourner des fichiers .py (conseillé pour ce projet !)

### C'est (presque) parti !
Il va falloir installer quelques packages de python pour pouvoir analyser les données. Le plus facile serait de télécharger Setup.ipynb et de faire tourner la première cellule. Puis tu auras accès aux packages en utilisant 'import'. 

Le fichier 'astuces.py' contient quelques lignes de code pour commencer 
