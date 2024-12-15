import pandas as pd  # Importation de la bibliothèque pandas pour la manipulation des données

def search_by_name(df, nom_produit):
    # Cette fonction recherche les produits dans le DataFrame 'df' dont le nom contient 'nom_produit'
    # La recherche est insensible à la casse grâce à l'argument 'case=False'
    return df[df['Nom du produit'].str.contains(nom_produit, case=False)]

def search_by_category(df, categorie):
    # Cette fonction recherche les produits dans le DataFrame 'df' dont la catégorie contient 'categorie'
    # La recherche est insensible à la casse grâce à l'argument 'case=False'
    return df[df['Catégorie'].str.contains(categorie, case=False)]

def search_by_price_range(df, prix_min, prix_max):
    # Cette fonction recherche les produits dans le DataFrame 'df' dont le prix est compris entre 'prix_min' et 'prix_max'
    return df[(df['Prix unitaire'] >= prix_min) & (df['Prix unitaire'] <= prix_max)]

if __name__ == "__main__":
    # Si le script est exécuté directement (et non importé comme module), on lit le fichier CSV contenant l'inventaire consolidé
    df = pd.read_csv('../donnees/consolidated_inventory.csv')