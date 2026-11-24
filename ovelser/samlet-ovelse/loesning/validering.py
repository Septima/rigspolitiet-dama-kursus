from adresse import Adresse


def rens_postnummer(vaerdi: str) -> str:
    return vaerdi.strip().zfill(4)


def er_gyldigt_postnummer(vaerdi: str) -> bool:
    return len(vaerdi) == 4 and vaerdi.isdigit()


def rens_adresse(adresse: Adresse) -> Adresse:
    return Adresse(
        vejnavn=adresse.vejnavn.strip(),
        husnummer=adresse.husnummer.strip(),
        postnummer=rens_postnummer(adresse.postnummer),
    )


def er_gyldig(adresse: Adresse) -> bool:
    har_vejnavn = adresse.vejnavn.strip() != ""
    return har_vejnavn and er_gyldigt_postnummer(adresse.postnummer)
