import argparse
import consolider
import rapport
import recherches

# Fonction principale pour intégrer les modules
def main():
    parser = argparse.ArgumentParser(description="Programme principal pour gérer des tâches spécifiques.")
    
    parser.add_argument("--action", type=str, required=True, choices=["consolider", "rapport", "recherches"],
                        help="Choisissez l'action à exécuter : consolider, rapport ou recherches.")
    
    # Arguments spécifiques pour l'action 'consolider'
    parser.add_argument("--input", type=str, help="Chemin vers le fichier d'entrée pour la consolidation.", required=False)
    parser.add_argument("--output", type=str, help="Chemin vers le fichier de sortie pour la consolidation.", required=False)
    
    # Arguments spécifiques pour l'action 'rapport'
    parser.add_argument("--rapport-type", type=str, help="Type de rapport à générer.", required=False)
    
    # Arguments spécifiques pour l'action 'recherches'
    parser.add_argument("--query", type=str, help="Requête ou mot-clé pour effectuer des recherches.", required=False)

    args = parser.parse_args()

    # Exécution en fonction de l'action
    if args.action == "consolider":
        if not args.input or not args.output:
            parser.error("L'action 'consolider' nécessite les arguments --input et --output.")
        consolider.consolider(args.input, args.output)

    elif args.action == "rapport":
        if not args.rapport_type:
            parser.error("L'action 'rapport' nécessite l'argument --rapport-type.")
        rapport.generer_rapport(args.rapport_type)

    elif args.action == "recherches":
        if not args.query:
            parser.error("L'action 'recherches' nécessite l'argument --query.")
        recherches.effectuer_recherche(args.query)

if __name__ == "__main__":
    main()
