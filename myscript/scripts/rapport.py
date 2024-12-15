import pandas as pd  # Importation de la bibliothèque pandas pour la manipulation des données

def generate_summary_report(df):
    # Cette fonction génère un rapport récapitulatif à partir du DataFrame 'df'
    
    # Grouper les données par la colonne 'Categorie' et appliquer des agrégations sur 'Quantité' et 'Prix'
    # 'sum' est utilisée pour additionner les quantités
    # 'mean' est utilisée pour calculer la moyenne des prix
    summary = df.groupby('Catégorie').agg({
        'Quantité': 'sum',
        'Prix unitaire': 'mean'
    }).reset_index()

    summary['Prix unitaire'] = summary['Prix unitaire'].round(2)
    
    # Retourner le DataFrame récapitulatif
    return summary

if __name__ == "__main__":
    # Si le script est exécuté directement (et non importé comme module), lire le fichier CSV contenant l'inventaire consolidé
    df = pd.read_csv('../donnees/consolidated_inventory.csv')
    
    # Générer le rapport récapitulatif à partir du DataFrame 'df'
    summary_report = generate_summary_report(df)
    
    # Sauvegarder le rapport récapitulatif dans un nouveau fichier CSV
    summary_report.to_csv('../donnes/summary_report.csv', index=False)

    print("Rapport récapitulatif généré. Données sauvegardées dans: 'summary_report.csv'")
