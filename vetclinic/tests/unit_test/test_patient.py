import unittest
from datetime import date
from models.patient import Patient
from models.owner import Owner
from models.services.treatment import Treatment
from models.services.service import Service

class TestPatient(unittest.TestCase):

    def setUp(self):
        self.owner = Owner("Anna", "Kowalska", "anna@example.com")
        self.patient = Patient(1, "Reksio", "pies", "beagle", 4, self.owner)
        self.service = Service(101, "Szczepienie", "profilaktyka", "pies", 50.0)
        self.treatment = Treatment(date(2025, 6, 20), [self.service], "Szczepienie przeciwko wściekliźnie")

    def test_initialization(self):
        self.assertEqual(self.patient.name, "Reksio")
        self.assertEqual(self.patient.species, "pies")
        self.assertEqual(self.patient.breed, "beagle")
        self.assertEqual(self.patient.age, 4)
        self.assertEqual(str(self.patient.owner), "Anna Kowalska - tel: anna@example.com")

    def test_str_representation(self):
        expected = "Reksio (pies, beagle), 4 lat – Właściciel: Anna Kowalska - tel: anna@example.com"
        self.assertEqual(str(self.patient), expected)

    def test_add_treatment(self):
        self.patient.add_treatment(self.treatment)
        self.assertEqual(len(self.patient.treatments), 1)
        self.assertEqual(self.patient.treatments[0].description, "Szczepienie przeciwko wściekliźnie")
        self.assertIn("Szczepienie", str(self.patient.treatments[0]))

    def test_add_medical_history(self):
        self.patient.add_medical_history("2025-06-21: Szczepienie")
        self.assertIn("2025-06-21: Szczepienie", self.patient.medical_history)

    def test_get_summary(self):
        self.patient.add_treatment(self.treatment)
        self.patient.add_medical_history("2025-06-21: Szczepienie")
        summary = self.patient.get_summary()
        self.assertIn("Szczepienie", summary)
        self.assertIn("2025-06-21", summary)

