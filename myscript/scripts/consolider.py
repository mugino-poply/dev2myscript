import pandas as pd  # Importation de la bibliothèque pandas pour la manipulation des données
import os  # Importation de la bibliothèque os pour l'interaction avec le système de fichiers

def consolidate_csv_files(directory):
    # Cette fonction consolide tous les fichiers CSV dans le répertoire spécifié en un seul DataFrame pandas

    # Récupère la liste de tous les fichiers dans le répertoire spécifié qui se terminent par '.csv'
    all_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    
    # Initialise une liste vide pour stocker les DataFrames
    all_dataframes = []

    # Pour chaque fichier dans la liste des fichiers CSV
    for file in all_files:
        # Lit le fichier CSV et le stocke dans un DataFrame
        df = pd.read_csv(os.path.join(directory, file))
        
        # Ajoute le DataFrame à la liste des DataFrames
        all_dataframes.append(df)
    
    # Concatène tous les DataFrames en un seul, en ignorant les index pour réindexer de 0 à n-1
    consolidated_df = pd.concat(all_dataframes, ignore_index=True)
    
    # Retourne le DataFrame consolidé
    return consolidated_df

if __name__ == "__main__":
    # Spécifie le répertoire contenant les fichiers CSV
    directory = "../donnees"
    
    # Appelle la fonction pour consolider les fichiers CSV et stocke le résultat dans 'consolidated_df'
    consolidated_df = consolidate_csv_files(directory)
    
    # Sauvegarde le DataFrame consolidé dans un nouveau fichier CSV
    consolidated_df.to_csv(os.path.join(directory, 'consolidated_inventory.csv'), index=False)
    
    print("Consolidation terminée. Données sauvegardées dans 'consolidated_inventory.csv'.")