class Owner:
    """
    Klasa reprezentująca właściciela zwierzęcia w gabinecie weterynaryjnym.
    """

    def __init__(self, first_name: str, last_name: str, phone: str) -> None:
        """
        Inicjalizuje obiekt właściciela.

        :param first_name: imię właściciela
        :param last_name: nazwisko właściciela
        :param phone: numer telefonu właściciela
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def __str__(self) -> str:
        """
        Zwraca reprezentację tekstową właściciela.
        """
        return f"{self.first_name} {self.last_name} - tel: {self.phone}"

    def get_full_name(self) -> str:
        """
        Zwraca pełne imię i nazwisko właściciela.
        """
        return f"{self.first_name} {self.last_name}"

    def update_phone(self, new_phone: str) -> None:
        """
        Aktualizuje numer telefonu właściciela.

        :param new_phone: nowy numer telefonu
        """
        self.phone = new_phone
