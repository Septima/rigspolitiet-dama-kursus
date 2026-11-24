from adresse import Adresse
from validering import er_gyldig, er_gyldigt_postnummer, rens_adresse, rens_postnummer


def test_rens_postnummer_tilfoejer_nul():
    assert rens_postnummer("800") == "0800"


def test_er_gyldigt_postnummer():
    assert er_gyldigt_postnummer("8000")
    assert not er_gyldigt_postnummer("800")
    assert not er_gyldigt_postnummer("80a0")
    assert not er_gyldigt_postnummer("")


def test_rens_postnummer_fjerner_mellemrum():
    assert rens_postnummer(" 800") == "0800"


def test_er_gyldig_kraever_vejnavn():
    assert er_gyldig(Adresse("Søndergade", "12", "8000"))
    assert not er_gyldig(Adresse("", "7", "8000"))
    assert not er_gyldig(Adresse("   ", "7", "8000"))


def test_rens_adresse_fjerner_mellemrum():
    adresse = Adresse(" Vestergade ", "3 ", " 800")
    assert rens_adresse(adresse) == Adresse("Vestergade", "3", "0800")
