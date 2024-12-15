import unittest
import os
import pandas as pd
from scripts.consolider import consolidate_csv_files

class TestConsolider(unittest.TestCase):
    def setUp(self):
        # Creation d'un répertoire temporaire pour les tests
        os.makedirs('tests/test_data', exist_ok=True)
        df1 = pd.DataFrame({
            'Nom du produit': ['Produit A', 'Produit B'],
            'Catégorie': ['Catégorie 1', 'Catégorie 2'],
            'Quantité': [10, 20],
            'Prix unitaire': [15.5, 25.0]
        })
        df2 = pd.DataFrame({
            'Nom du produit': ['Produit C', 'Produit D'],
            'Catégorie': ['Catégorie 3', 'Catégorie 4'],
            'Quantité': [32, 42],
            'Prix unitaire': [17.5, 29.0]
        })
        df1.to_csv('tests/test_data/test1.csv', index=False)
        df2.to_csv('tests/test_data/test2.csv', index=False)

    def tearDown(self):
        # Clean up the temporary directory and CSV files
        for file in os.listdir('tests/test_data'):
            os.remove(os.path.join('tests/test_data', file))
        os.rmdir('tests/test_data')

    def test_consolidate_csv_files(self):
        result_df = consolidate_csv_files('tests/test_data')
        self.assertEqual(len(result_df), 4)
        self.assertIn('Nom du produit', result_df.columns)
        self.assertIn('Catégorie', result_df.columns)
        self.assertIn('Quantité', result_df.columns)
        self.assertIn('Prix unitaire', result_df.columns)

if __name__ == '__main__':
    unittest.main()
