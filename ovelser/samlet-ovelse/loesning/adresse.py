from dataclasses import dataclass


@dataclass
class Adresse:
    vejnavn: str
    husnummer: str
    postnummer: str


def fra_raekke(raekke: list[str]) -> Adresse:
    vejnavn, husnummer, postnummer = raekke
    return Adresse(vejnavn, husnummer, postnummer)


def til_raekke(adresse: Adresse) -> list[str]:
    return [adresse.vejnavn, adresse.husnummer, adresse.postnummer]
