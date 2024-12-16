import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from recherches import effectuer_recherche

class TestRecherches(unittest.TestCase):

    def test_effectuer_recherche(self):
        # Test de la fonction effectuer_recherche avec une requête valide
        query = "test_query"
        try:
            effectuer_recherche(query)
        except Exception as e:
            self.fail(f"La fonction de recherche a échoué avec l'exception : {e}")

if __name__ == "__main__":
    unittest.main()