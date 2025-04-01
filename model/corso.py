from dataclasses import dataclass


@dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int
    #implemento le relazioni in uno di questi due modi
    #studenti: list[Studente] = None #lazy initializazion
    #matricole: list[str] = None

    def __eq__(self, other): #due oggetti sono uguali quando le loro chiavi primarie sono uguali
        return self.codins == other.codins
    def __hash__(self):
        return hash(self.codins)

    def __str__(self):
        return f"{self.nome} ({self.codins}) - {self.crediti} CFU"
