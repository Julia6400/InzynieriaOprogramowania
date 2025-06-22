import unittest
from models.medicalhistory import MedicalHistory
from models.patient import Patient
from models.owner import Owner
from models.veterinarian import Veterinarian

class IntegrationTest3(unittest.TestCase):
    def test_medical_history_flow(self):
        owner = Owner("Anna", "Kowalska", "123-456-789")
        patient = Patient(1, "Figo", "pies", "Beagle", 5, owner)
        vet = Veterinarian("Jan", "Nowak", "Chirurgia")

        history = MedicalHistory(patient)
        history.add_record(
            date="2025-06-25",
            diagnosis="Stan stabilny",
            treatment="Szczepienie",
            veterinarian=vet.get_full_name(),
            notes="Zalecenie obserwacji"
        )

        latest = history.get_latest_record()

        self.assertEqual(latest["diagnosis"], "Stan stabilny")
        self.assertEqual(latest["veterinarian"], "Jan Nowak")
        self.assertIn("Szczepienie", latest["treatment"])
        self.assertIn("obserwacji", latest["notes"])

if __name__ == '__main__':
    unittest.main()
