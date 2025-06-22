import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

import unittest
from datetime import date
from models.services.service import Service
from models.services.treatment import Treatment

class TestTreatment(unittest.TestCase):
    def setUp(self):
        self.service1 = Service("Szczepienie", 80.0)
        self.service2 = Service("Badanie ogólne", 120.0)
        self.treatment = Treatment(
            treatment_date=date(2025, 6, 20),
            services=[self.service1],
            description="Wizyta kontrolna"
        )

    def test_initialization(self):
        self.assertEqual(self.treatment.treatment_date, date(2025, 6, 20))
        self.assertEqual(self.treatment.description, "Wizyta kontrolna")
        self.assertEqual(len(self.treatment.services), 1)
        self.assertEqual(self.treatment.cost, 80.0)

    def test_add_service(self):
        self.treatment.add_service(self.service2)
        self.assertEqual(len(self.treatment.services), 2)
        self.assertAlmostEqual(self.treatment.cost, 200.0)

    def test_str_representation(self):
        expected = ("Leczenie z dnia 2025-06-20: Wizyta kontrolna | "
                    "Usługi: Szczepienie | Koszt całkowity: 80.00 zł")
        self.assertEqual(str(self.treatment), expected)

        # Dodajemy drugą usługę i sprawdzamy reprezentację ponownie
        self.treatment.add_service(self.service2)
        self.assertIn("Badanie ogólne", str(self.treatment))
        self.assertIn("200.00 zł", str(self.treatment))

if __name__ == "__main__":
    unittest.main()
