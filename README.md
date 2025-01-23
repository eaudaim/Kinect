# Kinect

Un projet Python utilisant la Kinect pour capturer et visualiser des données de profondeur en temps réel.

## Description

Ce projet a été conçu pour exploiter les capacités de la Kinect en combinant les bibliothèques OpenCV, Matplotlib, et libfreenect. Il permet :

* L'affichage en temps réel des données de profondeur capturées par le capteur infrarouge de la Kinect.
* L'application d'une colormap adaptée pour visualiser les variations de distance.
* Une installation simplifiée grâce à un script automatisé qui configure toutes les dépendances nécessaires.

## Fonctionnalités

* Capture des données de profondeur : Accède directement aux données de profondeur issues du capteur infrarouge.
* Visualisation en temps réel : Affiche les données avec une colormap intuitive, reflétant les variations de distance.
* Facilité d'installation : Un script unique installe toutes les dépendances, y compris libfreenect.

## Prérequis

Avant de commencer, assurez-vous que vous avez les éléments suivants :

* Une Kinect (modèle 360 testé)
* Python 3.7+ installé sur votre système
* Une distribution Linux (Ubuntu recommandé)

## Installation

1. Clonez le dépôt : ```
 git clone https://github.com/eaudaim/Kinect.git ```

2. Exécutez le script d'installation et de lancement : python3 setup_and_run.py
3. Interagissez avec le scanner Kinect :
* Une fenêtre s'ouvre affichant les données de profondeur capturées par le Kinect.
* Vous pouvez interrompre le script à tout moment en appuyant sur Ctrl+C.
* Le script nettoie automatiquement la mémoire et libère toutes les ressources utilisées lors de l'interruption.

## Structure du projet

* scanner3D_kinect.py : Le script principal qui gère la capture et l'affichage des données de profondeur en temps réel.
* setup_and_run.py : Un script automatisé qui installe les dépendances nécessaires (y compris libfreenect) et lance le programme principal.
* requirements.txt : Une liste des dépendances Python requises pour exécuter le projet.
* README.md : Le fichier que vous lisez actuellement, contenant les instructions et une description complète du projet.
