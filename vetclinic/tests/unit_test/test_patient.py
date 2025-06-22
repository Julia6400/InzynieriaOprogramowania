# test/unit_tests/patient_test.py
import unittest
from models.patient import Patient
from models.owner import Owner
from models.services.treatment import Treatment

class TestPatient(unittest.TestCase):

    def setUp(self):
        self.owner = Owner("Anna", "Kowalska", "anna@example.com")
        self.patient = Patient(1, "Reksio", "pies", "beagle", 4, self.owner)

    def test_initialization(self):
        self.assertEqual(self.patient.name, "Reksio")
        self.assertEqual(self.patient.species, "pies")
        self.assertEqual(self.patient.breed, "beagle")
        self.assertEqual(self.patient.age, 4)
        self.assertEqual(str(self.patient.owner), "Anna Kowalska")

    def test_str_representation(self):
        expected = "Reksio (pies, beagle), 4 lat – Właściciel: Anna Kowalska"
        self.assertEqual(str(self.patient), expected)

    def test_add_treatment(self):
        treatment = Treatment("Szczepienie", 50)
        self.patient.add_treatment(treatment)
        self.assertEqual(len(self.patient.treatments), 1)
        self.assertEqual(self.patient.treatments[0].name, "Szczepienie")

    def test_add_medical_history(self):
        self.patient.add_medical_history("2025-06-21: Szczepienie")
        self.assertIn("2025-06-21: Szczepienie", self.patient.medical_history)

    def test_get_summary(self):
        treatment = Treatment("Szczepienie", 50)
        self.patient.add_treatment(treatment)
        self.patient.add_medical_history("2025-06-21: Szczepienie")
        summary = self.patient.get_summary()
        self.assertIn("Szczepienie", summary)
        self.assertIn("2025-06-21", summary)
