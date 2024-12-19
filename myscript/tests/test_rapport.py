import unittest
import os
import csv
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from rapport import generer_rapport

class TestRapport(unittest.TestCase):

    def setUp(self):
        # Créer un fichier CSV temporaire pour les tests
        self.input_file = "test_input.csv"
        self.output_file = "test_output.csv"

        with open(self.input_file, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Catégorie", "Quantité", "Prix Unitaire"])
            writer.writerow(["Fruits", 10, 2.5])
            writer.writerow(["Fruits", 5, 3.0])
            writer.writerow(["Légumes", 8, 1.5])

    def tearDown(self):
        # Supprimer les fichiers temporaires après les tests
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_generer_rapport(self):
        # Tester la génération de rapport avec des données valides
        try:
            generer_rapport(self.input_file, self.output_file)

            # Vérifier que le fichier de sortie est créé
            self.assertTrue(os.path.exists(self.output_file))

            # Vérifier le contenu du fichier de sortie
            with open(self.output_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                rows = list(reader)

                # Vérifier les colonnes
                self.assertListEqual(reader.fieldnames, ["Catégorie", "Quantité", "Prix unitaire moyen"])

                # Vérifier les données
                self.assertEqual(len(rows), 2)  # Deux catégories : Fruits et Légumes
                self.assertEqual(rows[0]["Catégorie"], "Fruits")
                self.assertEqual(int(rows[0]["Quantité"]), 15)
                self.assertAlmostEqual(float(rows[0]["Prix unitaire moyen"]), 2.67, places=2)

                self.assertEqual(rows[1]["Catégorie"], "Légumes")
                self.assertEqual(int(rows[1]["Quantité"]), 8)
                self.assertAlmostEqual(float(rows[1]["Prix unitaire moyen"]), 1.5, places=2)

        except Exception as e:
            self.fail(f"La génération de rapport a échoué avec l'exception : {e}")

if __name__ == "__main__":
    unittest.main()
