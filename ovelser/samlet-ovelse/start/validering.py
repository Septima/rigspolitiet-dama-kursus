from config import POSTNUMMER_KOLONNE


def rens_postnummer(vaerdi: str) -> str:
    return vaerdi.zfill(4).strip()


def er_gyldigt_postnummer(vaerdi: str) -> bool:
    return len(vaerdi) == 4 and vaerdi.isdigit()


def rens_raekke(raekke: list[str]) -> list[str]:
    renset = list(raekke)
    renset[POSTNUMMER_KOLONNE] = rens_postnummer(renset[POSTNUMMER_KOLONNE])
    return renset


def er_gyldig(raekke: list[str]) -> bool:
    return er_gyldigt_postnummer(raekke[POSTNUMMER_KOLONNE])
