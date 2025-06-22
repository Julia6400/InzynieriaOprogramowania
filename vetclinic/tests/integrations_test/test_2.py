import unittest
from datetime import date
from models.patient import Patient
from models.owner import Owner
from models.services.service import Service
from models.services.treatment import Treatment

class IntegrationTest2(unittest.TestCase):
    def test_treatment_services_flow(self):
        owner = Owner("Anna", "Kowalska", "123-456-789")
        patient = Patient(1, "Figo", "pies", "Beagle", 5, owner)

        s1 = Service(101, "Szczepienie", "Profilaktyka", "pies", 90.0)
        s2 = Service(102, "Badanie kontrolne", "Diagnostyka", "pies", 120.0)

        treatment = Treatment(date(2025, 6, 25), [s1], "Wizyta po zabiegu")
        treatment.add_service(s2)

        patient.add_treatment(treatment)

        self.assertEqual(len(patient.treatments), 1)
        self.assertEqual(patient.treatments[0].cost, 210.0)
        self.assertIn("Badanie kontrolne", str(treatment))

if __name__ == '__main__':
    unittest.main()
