import argparse
import csv
from collections import defaultdict

def generer_rapport(input_file, output_file):
    try:
        # Charger les données du fichier CSV d'entrée
        with open(input_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Initialiser les données pour le rapport
            categories = defaultdict(lambda: {'quantite': 0, 'prix_total': 0})

            # Parcourir les lignes et agréger les données
            for row in reader:
                categorie = row['Catégorie']
                quantite = int(row['Quantité'])
                prix_unitaire = float(row['Prix unitaire'])

                categories[categorie]['quantite'] += quantite
                categories[categorie]['prix_total'] += quantite * prix_unitaire

            # Générer le rapport avec les colonnes souhaitées
            with open(output_file, mode='w', encoding='utf-8', newline='') as out_file:
                writer = csv.writer(out_file)
                writer.writerow(['Catégorie', 'Quantité', 'Prix unitaire moyen'])

                for categorie, data in categories.items():
                    quantite_totale = data['quantite']
                    prix_moyen = data['prix_total'] / quantite_totale if quantite_totale > 0 else 0
                    writer.writerow([categorie, quantite_totale, round(prix_moyen, 2)])

        print(f"Rapport généré avec succès dans {output_file}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier {input_file} est introuvable.")
    except KeyError as e:
        print(f"Erreur : Colonne manquante dans le fichier d'entrée - {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

def main():
    parser = argparse.ArgumentParser(description="Générer un rapport résumé à partir d'un fichier CSV d'entrée.")
    parser.add_argument("--input", type=str, required=True, help="Chemin du fichier CSV d'entrée.")
    parser.add_argument("--output", type=str, required=True, help="Chemin du fichier CSV de sortie.")

    args = parser.parse_args()
    generer_rapport(args.input, args.output)

if __name__ == "__main__":
    main()
