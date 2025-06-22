from models.owner import Owner
from models.services.treatment import Treatment
from typing import List

class Patient:
    """
    Klasa reprezentująca pacjenta w klinice weterynaryjnej.
    """

    def __init__(self, patient_id: int, name: str, species: str, breed: str, age: int, owner: Owner) -> None:
        """
        Inicjalizuje nowego pacjenta.

        :param patient_id: unikalny identyfikator pacjenta
        :param name: imię zwierzęcia
        :param species: gatunek (np. pies, kot)
        :param breed: rasa
        :param age: wiek w latach
        :param owner: obiekt właściciela
        """
        self.patient_id = patient_id
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.owner = owner
        self.treatments: List[Treatment] = []
        self.medical_history: List[str] = []

    def __str__(self) -> str:
        return f"{self.name} ({self.species}, {self.breed}), {self.age} lat – Właściciel: {self.owner}"

    def add_treatment(self, treatment: Treatment) -> None:
        """Dodaje leczenie do pacjenta."""
        self.treatments.append(treatment)

    def add_medical_history(self, note: str) -> None:
        """Dodaje wpis do historii medycznej pacjenta."""
        self.medical_history.append(note)

    def get_summary(self) -> str:
        """Zwraca podsumowanie leczenia i historii medycznej pacjenta."""
        history = "\n".join(self.medical_history) if self.medical_history else "Brak wpisów"
        treatments = ", ".join(str(t) for t in self.treatments) if self.treatments else "Brak leczeń"
        return (
            f"Pacjent: {self}\n"
            f"Leczenia: {treatments}\n"
            f"Historia medyczna:\n{history}"
        )
