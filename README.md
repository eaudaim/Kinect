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

2. Déplacez vous dans le dossier : ```
cd Kinect ```


3. Exécutez le script d'installation et de lancement : ```
 python3 setup_and_run.py ```

4. Interagissez avec le scanner Kinect :
* Une fenêtre s'ouvre affichant les données de profondeur capturées par le Kinect.
* Vous pouvez interrompre le script à tout moment en appuyant sur Ctrl+C.
* Le script nettoie automatiquement la mémoire et libère toutes les ressources utilisées lors de l'interruption.

## Structure du projet

* scanner3D_kinect.py : Le script principal qui gère la capture et l'affichage des données de profondeur en temps réel.
* setup_and_run.py : Un script automatisé qui installe les dépendances nécessaires (y compris libfreenect) et lance le programme principal.
* requirements.txt : Une liste des dépendances Python requises pour exécuter le projet.
* README.md : Le fichier que vous lisez actuellement, contenant les instructions et une description complète du projet.


---------------------------------------------------------------------------------------------------------------------------------------


# Kinect
A Python project using the Kinect to capture and visualize real-time depth data.

## Description
This project was designed to leverage the capabilities of the Kinect by combining the OpenCV, Matplotlib, and libfreenect libraries. It provides:

Real-time display of depth data captured by the Kinect's infrared sensor.
Application of an adapted colormap to visualize distance variations.
Simplified installation via an automated script that configures all necessary dependencies.
## Features
Depth data capture: Directly accesses depth data from the infrared sensor.
Real-time visualization: Displays the data with an intuitive colormap, reflecting distance variations.
Easy installation: A single script installs all dependencies, including libfreenect.
## Prerequisites
Before getting started, make sure you have the following:

A Kinect (tested on the 360 model)
Python 3.7+ installed on your system
A Linux distribution (Ubuntu recommended)
Installation
Clone the repository: git clone https://github.com/eaudaim/Kinect.git

Navigate to the folder: cd Kinect

Run the installation and launch script: python3 setup_and_run.py

Interact with the Kinect scanner:

A window will open, displaying the depth data captured by the Kinect.
You can interrupt the script at any time by pressing Ctrl+C.
The script automatically clears memory and releases all used resources upon interruption.
Project Structure
scanner3D_kinect.py: The main script that handles depth data capture and real-time visualization.
setup_and_run.py: An automated script that installs the required dependencies (including libfreenect) and launches the main program.
requirements.txt: A list of Python dependencies required to run the project.
README.md: This file you are currently reading, containing instructions and a complete project description.
