import unittest
from datetime import date
from models.owner import Owner
from models.patient import Patient
from models.veterinarian import Veterinarian
from models.appointment import Appointment

class IntegrationTest1(unittest.TestCase):
    def test_appointment_flow(self):
        owner = Owner("Anna", "Kowalska", "123-456-789")
        patient = Patient(1, "Figo", "pies", "Beagle", 5, owner)
        vet = Veterinarian("Jan", "Nowak", "Chirurgia")
        appointment = Appointment(1001, patient, vet, "2025-06-25", "Kontrola po zabiegu")

        self.assertEqual(str(appointment), "Wizyta 1001: 2025-06-25 – Kontrola po zabiegu u Jan Nowak (Pacjent: Figo)")

if __name__ == '__main__':
    unittest.main()
