import pandas as pd
import os
from scripts.consolider import consolidate_csv_files
from scripts.recherches import search_by_name, search_by_category, search_by_price_range
from scripts.rapport import generate_summary_report

def main():
    # Spécifier le répertoire des fichiers CSV
    directory = "donnees"
    
    # Vérifier s'il y a des fichiers CSV dans le répertoire
    all_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    if not all_files:  # Si la liste est vide
        raise ValueError("Il n'y a aucune donnée à traiter. Les fichiers .csv sont à ajouter dans le dossier 'donnees'")
    
    # Consolider les fichiers CSV
    consolidated_df = consolidate_csv_files(directory)
    consolidated_df.to_csv(os.path.join(directory, 'consolidated_inventory.csv'), index=False)
    print("Consolidation terminée. Données enregistrées dans: 'consolidated_inventory.csv'.")

    # Charger les données
    df = pd.read_csv(os.path.join(directory, 'consolidated_inventory.csv'))

    # Remplacer les valeurs NaN dans les colonnes pertinentes
    df['Nom du produit'] = df['Nom du produit'].fillna('')
    df['Catégorie'] = df['Catégorie'].fillna('')
    df['Prix unitaire'] = df['Prix unitaire'].fillna(0)  # Ou remplacer par la moyenne si nécessaire
    df['Quantité'] = df['Quantité'].fillna(0)

    # Recherche des fonctionnalités
    """
    print("Recherche par nom:")
    print(search_by_name(df, 'Produit d\'exemple'))

    print("Recherche par catégorie:")
    print(search_by_category(df, 'Catégorie d\'exemple'))

    print("Recherche par prix:")
    print(search_by_price_range(df, 10, 50))
    """

    how = '?'
    while how not in ['n', 'N', 'nom', 'Nom', 'c', 'C', 'catégorie', 'Catégorie', 'p', 'P', 'prix', 'Prix']:
        if how != '?':
            print("\nMauvais format, rééssayez \n")
        how = input("Comment souhaitez-vous rechercher ? par nom (n), catégorie (c), prix (p) \n")

    # Recherche par nom
    if how.lower() == 'n' or how.lower() == 'nom':
        pr_name = input('Nom du produit ? \n')
        print(search_by_name(df, pr_name))

    # Recherche par catégorie
    elif how.lower() == 'c' or how.lower() == 'catégorie':
        cat_name = input('Catégorie du produit ? \n')
        print(search_by_category(df, cat_name))
    
    # Recherche par prix
    elif how.lower() == 'p' or how.lower() == 'prix':
        prix_bas = int(input('Produit coûtant minimum : (en €) \n'))
        prix_haut = int(input('Produit coûtant maximum : (en €) \n'))
        print(search_by_price_range(df, prix_bas, prix_haut))
    
    else:
        print("Produit introuvable \n")

    # Générer le rapport récapitulatif
    summary_report = generate_summary_report(df)
    summary_report.to_csv(os.path.join(directory, 'summary_report.csv'), index=False)
    print("Rapport récapitulatif généré. Données enregistrées dans: 'summary_report.csv'.")

if __name__ == "__main__":
    main()
