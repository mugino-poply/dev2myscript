import unittest
import pandas as pd
from scripts.recherches import search_by_name, search_by_category, search_by_price_range

class TestRecherches(unittest.TestCase):
    def setUp(self):
        # Création d'un data frame pour le test
        self.data = {
            'Nom du produit': ['Produit A', 'Produit B', 'Produit C'],
            'Catégorie': ['Catégorie 1', 'Catégorie 1', 'Catégorie 2'],
            'Quantité': [10, 20, 30],
            'Prix unitaire': [15.5, 25.0, 35.5]
        }
        self.df = pd.DataFrame(self.data)

    def test_search_by_name(self):
        result_df = search_by_name(self.df, 'Produit A')
        self.assertEqual(len(result_df), 1)
        self.assertEqual(result_df.iloc[0]['Nom du produit'], 'Produit A')

    def test_search_by_category(self):
        result_df = search_by_category(self.df, 'Catégorie 1')
        self.assertEqual(len(result_df), 2)

    def test_search_by_price_range(self):
        result_df = search_by_price_range(self.df, 20, 40)
        self.assertEqual(len(result_df), 2)

if __name__ == '__main__':
    unittest.main()
