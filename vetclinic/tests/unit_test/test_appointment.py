import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

import unittest
from models.appointment import Appointment
from models.patient import Patient
from models.veterinarian import Veterinarian
from models.owner import Owner

class TestAppointment(unittest.TestCase):
    def setUp(self):
        self.owner = Owner("Anna", "Kowalska", "123-456-789")
        self.patient = Patient(1, "Reksio", "pies", "beagle", 4, self.owner)
        self.vet = Veterinarian("Jan", "Nowak", "Chirurgia")
        self.appointment = Appointment(100, self.patient, self.vet, "2025-06-05", "Szczepienie")

    def test_initialization(self):
        self.assertEqual(self.appointment.appointment_id, 100)
        self.assertEqual(self.appointment.patient.name, "Reksio")
        self.assertEqual(self.appointment.veterinarian.get_full_name(), "Jan Nowak")
        self.assertEqual(self.appointment.date, "2025-06-05")
        self.assertEqual(self.appointment.service, "Szczepienie")

    def test_str_representation(self):
        expected = "Wizyta 100: 2025-06-05 – Szczepienie u Jan Nowak (Pacjent: Reksio)"
        self.assertEqual(str(self.appointment), expected)

    def test_reschedule(self):
        self.appointment.reschedule("2025-06-10")
        self.assertEqual(self.appointment.date, "2025-06-10")

    def test_change_service(self):
        self.appointment.change_service("Badanie kontrolne")
        self.assertEqual(self.appointment.service, "Badanie kontrolne")

    def test_get_summary(self):
        summary = self.appointment.get_summary()
        self.assertIn("Jan Nowak", summary)
        self.assertIn("Reksio", summary)
        self.assertIn("2025-06-05", summary)

if __name__ == "__main__":
    unittest.main()
