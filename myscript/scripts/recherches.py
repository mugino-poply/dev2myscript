import argparse
import csv

def effectuer_recherche(query):
    # Charger le fichier contenant les données produits
    data_file = "donnees/output_file.csv"  # Spécifiez le chemin de votre fichier
    try:
        with open(data_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            results = []

            # Parcourir les lignes et chercher la requête
            for row in reader:
                if any(query.lower() in str(value).lower() for value in row.values()):
                    results.append(row)

            # Afficher les résultats
            if not results:
                print(f"Aucun produit trouvé pour la requête : {query}")
            else:
                print(f"Produits trouvés pour la requête : {query}")
                for result in results:
                    print(result)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {data_file} est introuvable.")

def main():
    # Définir un parseur d'arguments pour la ligne de commande
    parser = argparse.ArgumentParser(description="Effectuer une recherche basée sur une requête spécifiée.")
    
    # Ajouter un argument pour la requête de recherche
    parser.add_argument("--query", type=str, required=True, help="Requête ou mot-clé à rechercher.")

    # Analyser les arguments de la ligne de commande
    args = parser.parse_args()
    
    # Appeler la fonction de recherche avec l'argument fourni
    effectuer_recherche(args.query)

if __name__ == "__main__":
    main()
