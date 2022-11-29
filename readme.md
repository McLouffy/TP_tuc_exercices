# README

## Préparer son environnement

Installer le paquet virtualenv

> pip install virtualenv

Créer l'environnement virtuel

> python -m virtualenv venv

venv correspond au chemin/dossier dans lequel sera activé votre environnement virtuel
(Dans notre cas, dans le dossier où est exécuté la commande, dans le dossier venv)

> Activer l'environnement virtuel

./venv/Scripts/activate.ps1

Installer les paquets

> pip install -r requirements.txt

Exécuter dans le dossier application

## Pytest

> python -m pytest

## Coverage

> coverage run -m pytest --profile 

## Pylint

> pylint application/ tests/

## Développement du code
Sofiane et moi-même avons travaillé ensemble sur le developpement des fonctions, des tests unitaires ainsi que sur les workflow. Nous n'avons pas réussi à résoudre l'erreur 403 qui nous refusait de faire des push sur la branche principale. 

## Data
Fichier au format .csv pour récupérer des doonées.

