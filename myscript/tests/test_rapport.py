import unittest
import pandas as pd
from scripts.rapport import generate_summary_report

class TestRapport(unittest.TestCase):
    def setUp(self):
        # Création d'un data frame pour le test
        self.data = {
            'Nom du produit': ['Produit A', 'Produit B'],
            'Catégorie': ['Catégorie 1', 'Catégorie 1'],
            'Quantité': [10, 20],
            'Prix unitaire': [15.5, 25.0]
        }
        self.df = pd.DataFrame(self.data)


    def test_generate_summary_report(self):
        result_df = generate_summary_report(self.df)
        self.assertEqual(len(result_df), 1)
        self.assertIn('Catégorie', result_df.columns)
        self.assertIn('Quantité', result_df.columns)
        self.assertIn('Prix unitaire', result_df.columns)

if __name__ == '__main__':
    unittest.main()
