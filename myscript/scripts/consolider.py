import argparse
import pandas as pd

def consolider(input_files, output_file):
    # Consolider plusieurs fichiers CSV en un seul
    # Initialiser une liste pour stocker les DataFrames des fichiers lus
    dataframes = []
    
    # Parcourir chaque fichier d'entrée
    for input_file in input_files:
        print(f"Lecture du fichier : {input_file}")
        # Lire le fichier CSV et l'ajouter à la liste des DataFrames
        df = pd.read_csv(input_file)
        dataframes.append(df)

    # Combiner tous les DataFrames en un seul
    # Utilise pd.concat pour fusionner les fichiers en ignorant les index originaux
    result = pd.concat(dataframes, ignore_index=True)
    
    # Sauvegarder le DataFrame consolidé dans le fichier de sortie
    print(f"Enregistrement du fichier consolidé dans : {output_file}")
    result.to_csv(output_file, index=False)

def main():
    # Définir un parseur d'arguments pour la ligne de commande
    parser = argparse.ArgumentParser(description="Consolider plusieurs fichiers CSV en un fichier de sortie.")
    
    # Ajouter un argument pour les fichiers d'entrée (plusieurs fichiers acceptés)
    parser.add_argument("--inputs", nargs='+', type=str, required=True, help="Chemins des fichiers CSV d'entrée.")
    
    # Ajouter un argument pour le fichier de sortie
    parser.add_argument("--output", type=str, required=True, help="Chemin du fichier de sortie.")

    # Analyser les arguments de la ligne de commande
    args = parser.parse_args()
    
    # Appeler la fonction de consolidation avec les arguments fournis
    consolider(args.inputs, args.output)

if __name__ == "__main__":
    main()
