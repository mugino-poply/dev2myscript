import argparse

def generer_rapport(rapport_type):
    # Exemple de logique pour générer un rapport basé sur un type donné
    print(f"Génération d'un rapport de type : {rapport_type}")
    # Ajouter ici la logique réelle pour générer le rapport

def main():
    # Définir un parseur d'arguments pour la ligne de commande
    parser = argparse.ArgumentParser(description="Générer un rapport basé sur le type spécifié.")
    
    # Ajouter un argument pour le type de rapport
    parser.add_argument("--rapport-type", type=str, required=True, help="Type de rapport à générer.")

    # Analyser les arguments de la ligne de commande
    args = parser.parse_args()
    
    # Appeler la fonction de génération de rapport avec l'argument fourni
    generer_rapport(args.rapport_type)

if __name__ == "__main__":
    main()