# Dev2MyScript

Ce projet est une application de gestion de produits permettant de consolider les données de produits, de rechercher par catégorie et de générer des rapports.

## Fonctionnalités

- **Consolidation de fichiers CSV** : Combine plusieurs fichiers CSV en un seul fichier consolidé.
- **Génération de rapports** : Crée des rapports basés sur des types spécifiés par l'utilisateur.
- **Recherches automatisées** : Effectue des recherches en fonction de requêtes spécifiques.
- **Tests unitaires** : Vérifie le bon fonctionnement des scripts à l'aide de `unittest`.

## Structure du projet

```
myscript/
├── scripts/                # Contient les scripts principaux
│   ├── consolider.py   # Script pour consolider des fichiers CSV
│   ├── rapport.py      # Script pour générer des rapports
│   ├── recherches.py   # Script pour effectuer des recherches
├── tests/                  # Contient les tests unitaires
│   ├── test_consolider.py  # Tests pour cli_consolider.py
│   ├── test_rapport.py     # Tests pour cli_rapport.py
│   ├── test_recherches.py  # Tests pour cli_recherches.py
└── README.md               # Documentation du projet
```

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/mugino-poply/dev2myscript.git
   cd dev2myscript/myscript
   ```
2. Assurez-vous d'avoir Python 3.7 ou supérieur installé.

3. Installez les dépendances nécessaires (si applicables) :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

Chaque script peut être exécuté depuis la ligne de commande avec des arguments spécifiques :

### Consolidation de fichiers CSV

```bash
python scripts/consolider.py --inputs file1.csv file2.csv --output consolidate.csv
```
- **`--inputs`** : Liste des fichiers CSV d'entrée.
- **`--output`** : Chemin du fichier de sortie consolidé.

### Génération de rapports

```bash
python scripts/rapport.py [-h] --input consolidate.csv --output rapport.csv
```

### Recherches

```bash
python scripts/recherches.py --query "Votre requête ici"
```
- **`--query`** : Requête ou mot-clé pour la recherche.

## Tests

Les tests unitaires pour chaque script sont disponibles dans le dossier `tests`. Pour exécuter tous les tests :

```bash
python -m unittest discover -s tests -p "*.py"
```

## Auteur:

[Hippolyte Amory](https://github.com/mugino-poply)
