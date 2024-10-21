import unittest
from auto import Auto  # importáljuk az Auto osztályt az auto.py-ból


class TestAuto(unittest.TestCase):

    def setUp(self):
        self.auto = Auto("Toyota", "Corolla", 2020, "Benzin", 180)

    def test_auto_adatok(self):
        expected_result = "Autó: Toyota Corolla, Évjárat: 2020, Üzemanyag: Benzin, Sebesség: 180 km/h"
        self.assertEqual(self.auto.adatok(), expected_result)

    def test_get_marka(self):
        self.assertEqual(self.auto.get_marka(), "Toyota")

    def test_get_modell(self):
        self.assertEqual(self.auto.get_modell(), "Corolla")

    def test_get_evjarat(self):
        self.assertEqual(self.auto.get_evjarat(), 2020)

    def test_get_uzemanyag(self):
        self.assertEqual(self.auto.get_uzemanyag(), "Benzin")

    def test_get_sebesseg(self):
        self.assertEqual(self.auto.get_sebesseg(), 180)

    def test_set_sebesseg(self):
        self.auto.set_sebesseg(200)
        self.assertEqual(self.auto.get_sebesseg(), 200)


if __name__ == '__main__':
    unittest.main()
