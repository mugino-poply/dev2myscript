import unittest
import os
import pandas as pd
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from consolider import consolider

class TestConsolider(unittest.TestCase):

    def setUp(self):
        # Créer des fichiers temporaires pour les tests
        self.input_file1 = "test_input1.csv"
        self.input_file2 = "test_input2.csv"
        self.output_file = "test_output.csv"

        df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})

        df1.to_csv(self.input_file1, index=False)
        df2.to_csv(self.input_file2, index=False)

    def tearDown(self):
        # Supprimer les fichiers temporaires après les tests
        if os.path.exists(self.input_file1):
            os.remove(self.input_file1)
        if os.path.exists(self.input_file2):
            os.remove(self.input_file2)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_consolider(self):
        # Tester la consolidation de plusieurs fichiers
        consolider([self.input_file1, self.input_file2], self.output_file)

        # Vérifier que le fichier de sortie a été créé
        self.assertTrue(os.path.exists(self.output_file))

        # Vérifier le contenu du fichier consolidé
        result = pd.read_csv(self.output_file)
        self.assertEqual(len(result), 4)  # 2 lignes par fichier d'entrée
        self.assertListEqual(result["A"].tolist(), [1, 2, 5, 6])
        self.assertListEqual(result["B"].tolist(), [3, 4, 7, 8])

if __name__ == "__main__":
    unittest.main()
