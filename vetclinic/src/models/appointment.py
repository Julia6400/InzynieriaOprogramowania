from models.patient import Patient
from models.veterinarian import Veterinarian

class Appointment:
    """
    Klasa reprezentująca wizytę w klinice weterynaryjnej.
    """

    def __init__(self, appointment_id: int, patient: Patient, veterinarian: Veterinarian, date: str, service: str) -> None:
        self.appointment_id = appointment_id
        self.patient = patient
        self.veterinarian = veterinarian
        self.date = date
        self.service = service

    def __str__(self) -> str:
        return f"Wizyta {self.appointment_id}: {self.date} – {self.service} u {self.veterinarian.get_full_name()} (Pacjent: {self.patient.name})"

    def reschedule(self, new_date: str) -> None:
        """Zmienia datę wizyty."""
        self.date = new_date

    def change_service(self, new_service: str) -> None:
        """Zmienia usługę przypisaną do wizyty."""
        self.service = new_service

    def get_summary(self) -> str:
        """Zwraca szczegóły wizyty w formacie tekstowym."""
        return (
            f"--- Podsumowanie wizyty ---\n"
            f"ID: {self.appointment_id}\n"
            f"Data: {self.date}\n"
            f"Lekarz: {self.veterinarian.get_full_name()} ({self.veterinarian.specialization})\n"
            f"Pacjent: {self.patient.name} ({self.patient.species})\n"
            f"Usługa: {self.service}"
        )