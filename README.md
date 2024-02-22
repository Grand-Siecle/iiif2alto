# iiif2alto - Easy Notebook pour l'HTR

Ces notebooks proviennent initialement du dépôt suivant : [Fondue - Documentation](https://github.com/FoNDUE-HTR/Documentation/blob/master/notebook_pipeline.ipynb). Nous pouvons remercier Simon Gabay, Ariane Pinche, Thibault Clérice, Kelly Christensen et Floriane Goy pour ce script ainsi que les services HPC de l'Université de Genève 

## Introduction

Deux notebooks ont été produits afin de convertir des images sous le format ALTO, un prêt à utiliser pour eScriptorium. La détection des zones s'appuie sur le vocabulaire controlé [SegmOnto](https://segmonto.github.io/) via [Yolov8](https://docs.ultralytics.com/fr/), le modèle BLLA pour la segmentation des lignes, et le moteur [Kraken](https://kraken.re/main/index.html) pour la reconnaissance de caractères.

XML-ALTO est l'encodage XML reconnu pour l'HTR. Il peut être importé sur eScriptorium ou diffuser auprès de la communauté. 

- Pour convertir des images depuis un manifeste IIIF : [Notebook](https://gitlab.unige.ch/grand_siecle/iiif2alto/-/blob/main/notebook_pipeline.ipynb)
- Pour convertir des images depuis un PDF : [Notebook]()

## Utilisation 

### OpenOnDemand

OpenOnDemand est un service fournit par le service HPC de l'Université de Genève pour faciliter l'utilisation du cluster.

Le site est accessible via cette adresse : [OpenOnDemand](https://ondemand.baobab.hpc.unige.ch/). Il faut en demander l'accès au préalable via le forum : [https://hpc-community.unige.ch/t/baobab-openondemand-is-now-available/3172](https://hpc-community.unige.ch/t/baobab-openondemand-is-now-available/3172). 

### Utilisation

- **Lancer son instance *Jupyter Lab***

![Using jupyter](media/Baobab_OpenOnDemand.gif)

Pour débuter une session, il faut se connecter via SWITCH puis sélectionner l'application *Jupyter Lab*. Il faut ensuite décrire sa configuration Hardware
 - Version : GCCcore/12.3.0 JupyterLab/4.0.5
    - Partition : shared-gpu
    - Nombre d'heure : dépend du nombre de fichiers à transcrire
    - CPU : dans l'idéal 6 coeurs
    - Memory : 8 Gb 
    - GPU: 1

Il faut bien estimer le nombre d'heure d'utilisation pour ne pas surcharger le serveur, donc prendre la place aux autres. Cliquer sur *Launch* pour lancer la session.

Ensuite, il faut cliquer sur *Connect to Jupyter* pour accéder à la session. Vous pouvez déposer le fichier .ipynb (Notebook) en amont dans l'onglet *Files* -> **Upload* ou directement dans l'espace JupyterLab sur le bouton upload (en dessous de Run)

<img src="media/upload_notebook.png" alt="Upload in Jupyter" width="400"/>






