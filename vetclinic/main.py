from datetime import date
from models.owner import Owner
from models.patient import Patient
from models.veterinarian import Veterinarian
from models.services.service import Service
from models.services.treatment import Treatment
from models.medicalhistory import MedicalHistory
from models.appointment import Appointment

def main():
    # 1. Właściciel i pacjent
    owner = Owner("Anna", "Kowalska", "123-456-789")
    patient = Patient(1, "Figo", "pies", "Beagle", 5, owner)

    # 2. Weterynarz
    vet = Veterinarian("Jan", "Nowak", "Chirurgia")

    # 3. Wizyta
    appointment = Appointment(1001, patient, vet, "2025-06-25", "Kontrola po zabiegu")

    # 4. Leczenie i usługi
    service1 = Service(101, "Szczepienie", "Profilaktyka", "pies", 90.0)
    service2 = Service(102, "Badanie kontrolne", "Diagnostyka", "pies", 120.0)
    treatment = Treatment(treatment_date=date(2025, 6, 25), services=[service1], description="Wizyta po zabiegu")
    treatment.add_service(service2)
    patient.add_treatment(treatment)

    # 5. Historia medyczna
    history = MedicalHistory(patient)
    history.add_record(
        date="2025-06-25",
        diagnosis="Brak komplikacji",
        treatment="Szczepienie + Badanie kontrolne",
        veterinarian=vet.get_full_name(),
        notes="Pacjent w dobrym stanie, zalecono obserwację."
    )

    # 6. Wyświetlenie informacji
    print("===== PODSUMOWANIE PACJENTA =====")
    print(patient)
    print()
    print("===== WIZYTA =====")
    print(appointment)
    print()
    print("===== LECZENIE =====")
    print(treatment)
    print()
    print("===== HISTORIA MEDYCZNA =====")
    print(history)
    print("Ostatni wpis:")
    print(history.get_latest_record())

if __name__ == "__main__":
    main()
