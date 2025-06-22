import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

import unittest
from models.medicalhistory import MedicalHistory
from models.patient import Patient
from models.owner import Owner
from models.veterinarian import Veterinarian

class TestMedicalHistory(unittest.TestCase):
    def setUp(self):
        self.owner = Owner("Anna", "Kowalska", "123-456-789")
        self.patient = Patient(1, "Reksio", "pies", "beagle", 4, self.owner)
        self.history = MedicalHistory(self.patient)

    def test_initialization(self):
        self.assertEqual(self.history.patient.name, "Reksio")
        self.assertEqual(self.history.owner, "Anna Kowalska")
        self.assertEqual(len(self.history.records), 0)
        self.assertEqual(len(self.history.list_treatment), 0)

    def test_add_record(self):
        self.history.add_record(
            date="2025-06-21",
            diagnosis="Gorączka",
            treatment="Antybiotyk",
            veterinarian="Dr Jan Nowak",
            notes="Podano zastrzyk"
        )
        self.assertEqual(len(self.history.records), 1)
        self.assertIn("Antybiotyk", self.history.list_treatment)
        record = self.history.records[0]
        self.assertEqual(record["diagnosis"], "Gorączka")
        self.assertEqual(record["notes"], "Podano zastrzyk")

    def test_get_all_records(self):
        self.history.add_record("2025-06-01", "Kaszel", "Syrop", "Dr Nowak")
        self.history.add_record("2025-06-15", "Biegunka", "Kroplówka", "Dr Kowalska")
        all_records = self.history.get_all_records()
        self.assertEqual(len(all_records), 2)
        self.assertEqual(all_records[1]["treatment"], "Kroplówka")

    def test_get_latest_record(self):
        self.assertIsNone(self.history.get_latest_record())  # brak wpisów
        self.history.add_record("2025-06-01", "Kaszel", "Syrop", "Dr Nowak")
        self.history.add_record("2025-06-15", "Biegunka", "Kroplówka", "Dr Kowalska")
        latest = self.history.get_latest_record()
        self.assertEqual(latest["diagnosis"], "Biegunka")

    def test_str_representation(self):
        self.assertIn("Historia medyczna: Reksio", str(self.history))
        self.history.add_record("2025-06-01", "Kaszel", "Syrop", "Dr Nowak")
        self.assertIn("1 wpisów", str(self.history))

if __name__ == "__main__":
    unittest.main()
