# Dev2MyScript

Ce projet est une application de gestion de produits permettant de consolider les données de produits, de rechercher par catégorie et de générer des rapports.

## Prérequis

1. **Installer Python** :
    - Téléchargez et installez Python à partir de [python.org](https://www.python.org/downloads/).
    - Assurez-vous que Python est ajouté à votre variable PATH.

    Pour vérifier l'installation de Python, exécutez :
    ```bash
    python --version
    ```
    ou
    ```bash
    python3 --version
    ```

2. **Installer les dépendances** :
    - Créez un environnement virtuel et activez-le :
        ```bash
        python -m venv env
        source env/bin/activate  
        # Pour Windows : `env\Scripts\activate`
        ```
      ou
        ```bash
        python3 -m venv env
        source env/bin/activate
        # Pour Windows : `env\Scripts\activate`
        ```

    - Installez les dépendances à partir du fichier `necessaire.txt` :
        ```bash
        pip install -r necessaire.txt
        ```

## Fonctionnalités
- **Consolidation des données de produits** : Lecture de plusieurs fichiers CSV, fusion des données en un seul fichier.
- **Recherche de produits par catégorie** : Recherche de produits spécifiques dans un fichier CSV par catégorie.
- **Génération de rapports récapitulatifs** : Création de rapports récapitulatifs des produits avec des statistiques agrégées.

## Utilisation

1. **Consolidation des données** :
    ```bash
    python -m scripts.consolider input_file.csv output_file.csv
    ```
    ou
    ```bash
    python3 -m scripts.consolider input_file.csv output_file.csv
    ```
    - Consolidation des données de plusieurs fichiers CSV en un seul fichier consolidé.

2. **Recherche de produits par catégorie** :
    ```bash
    python -m scripts.recherches input_file.csv "Catégorie 1"
    ```
    ou
    ```bash
    python3 -m scripts.recherches input_file.csv "Catégorie 1"
    ```
    - Recherche de produits spécifiques dans le fichier CSV par catégorie.

3. **Génération de rapports récapitulatifs** :
    ```bash
    python -m scripts.rapport input_file.csv report_file.csv
    ```
    ou
    ```bash
    python3 -m scripts.rapport input_file.csv report_file.csv
    ```
    - Création de rapports récapitulatifs des produits avec des statistiques agrégées.

## Tests

Les tests unitaires sont inclus pour vérifier le bon fonctionnement des différentes fonctionnalités du projet.

### Exécution des tests

Pour exécuter les tests, utilisez la commande suivante :
```bash
python -m unittest discover tests
```
  ou
  ```bash
python3 -m unittest discover tests
  ```


## Contributeur:

[Hippolyte Amory](https://github.com/mugino-poply)
