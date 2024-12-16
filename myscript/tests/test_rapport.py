import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from rapport import generer_rapport

class TestRapport(unittest.TestCase):

    def test_generer_rapport(self):
        # Test de la génération d'un rapport de type valide
        rapport_type = "type_test"
        try:
            generer_rapport(rapport_type)
        except Exception as e:
            self.fail(f"La génération de rapport a échoué avec l'exception : {e}")

if __name__ == "__main__":
    unittest.main()
