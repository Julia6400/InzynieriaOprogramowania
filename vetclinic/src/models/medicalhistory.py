from models.patient import Patient

class MedicalHistory:
    """
    Klasa reprezentująca historię medyczną pacjenta.
    """

    def __init__(self, patient: Patient) -> None:
        """
        Inicjalizuje historię medyczną dla danego pacjenta.

        :param patient: obiekt klasy Patient
        """
        self.patient = patient
        self.owner = patient.owner.get_full_name()
        self.records: list[dict] = []
        self.list_treatment: set[str] = set()

    def add_record(self, date: str, diagnosis: str, treatment: str, veterinarian: str, notes: str = "") -> None:
        """
        Dodaje nowy wpis do historii medycznej.
        """
        record = {
            "date": date,
            "diagnosis": diagnosis,
            "treatment": treatment,
            "veterinarian": veterinarian,
            "notes": notes
        }
        self.records.append(record)
        self.list_treatment.add(treatment)

    def get_all_records(self) -> list[dict]:
        """Zwraca wszystkie wpisy historii medycznej."""
        return self.records

    def get_latest_record(self) -> dict | None:
        """Zwraca ostatni wpis, jeśli istnieje."""
        if self.records:
            return self.records[-1]
        return None

    def __str__(self) -> str:
        """Zwraca opis historii medycznej pacjenta."""
        return (
            f"Historia medyczna: {self.patient.name} ({self.patient.species}) – "
            f"{len(self.records)} wpisów, właściciel: {self.owner}"
        )
