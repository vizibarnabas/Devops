import unittest
from auto import Auto


class TestAutoIntegration(unittest.TestCase):
    def test_auto_list_integration(self):
        autok = [
            Auto("Toyota", "Corolla", 2020, "Benzin", 180),
            Auto("Ford", "Focus", 2018, "Dízel", 190),
            Auto("BMW", "X5", 2022, "Elektromos", 220),
            Auto("Audi", "A4", 2019, "Benzin", 210)
        ]

        self.assertEqual(len(autok), 4)

        self.assertEqual(autok[0].get_marka(), "Toyota")
        self.assertEqual(autok[0].get_modell(), "Corolla")
        self.assertEqual(autok[0].get_evjarat(), 2020)
        self.assertEqual(autok[0].get_uzemanyag(), "Benzin")
        self.assertEqual(autok[0].get_sebesseg(), 180)

        autok[2].set_sebesseg(240)
        self.assertEqual(autok[2].get_sebesseg(), 240)

        expected_results = [
            ("Toyota", "Corolla", 2020, "Benzin", 180),
            ("Ford", "Focus", 2018, "Dízel", 190),
            ("BMW", "X5", 2022, "Elektromos", 240),
            ("Audi", "A4", 2019, "Benzin", 210)
        ]

        for i, auto in enumerate(autok):
            self.assertEqual(auto.get_marka(), expected_results[i][0])
            self.assertEqual(auto.get_modell(), expected_results[i][1])
            self.assertEqual(auto.get_evjarat(), expected_results[i][2])
            self.assertEqual(auto.get_uzemanyag(), expected_results[i][3])
            self.assertEqual(auto.get_sebesseg(), expected_results[i][4])


if __name__ == '__main__':
    unittest.main()
