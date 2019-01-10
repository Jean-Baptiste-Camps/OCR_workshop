# Atelier OCR et HTR des masters Humanités numériques et Technologies numériques appliquées à l'histoire (École nationale des chartes | PSL)

Ce dépôt contient les données nécessaires pour l'atelier.

## Installations et préparations de la séance

Cette procédure d'installation est conçue pour une distribution Linux Ubuntu >=
16.04

Tout d'abord, il faut récupérer ce dossier, soit en clonant avec Git,

```bash
    git clone https://github.com/Jean-Baptiste-Camps/OCR_workshop.git
```

soit en le téléchargeant et en extrayant l'archive.

### Installation de ScanTailor

```bash
    sudo apt-get install scantailor
```
    
### Installation de Kraken

Tout d'abord, il vous faut une installation de Python >= à 3.6, et installer les paquets
suivants:

```bash
    sudo apt-get install python3.6 python3.6-dev python3-pip virtualenv
```

Une fois cela fait, il est possible de passer à l'installation de Kraken, ce
que je vous suggère de faire dans un environnement virtuel, selon les étapes suivantes:

```bash
    # Créer un environnement virtuel (optionnel)
    virtualenv env -p /usr/bin/python3.6
    # l'activer (optionnel)
    source env/bin/activate
    # installer
    pip3 install kraken
```

