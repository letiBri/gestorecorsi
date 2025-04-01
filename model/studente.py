from dataclasses import dataclass



@dataclass
class Studente:
    matricola: int
    cognome: str
    nome: str
    CDS: str
    # implemento le relazioni in uno di questi due modi
    #corsi: list[Corso] = None  # lazy initializazion
    #codins: list[str] = None

    def __eq__(self, other):  # due oggetti sono uguali quando le loro chiavi primarie sono uguali
        return self.matricola == other.matricola

    def __hash__(self):
        return hash(self.matricola)

    def __str__(self):
        return f"{self.cognome} {self.nome} ({self.matricola}) - {self.CDS}"
