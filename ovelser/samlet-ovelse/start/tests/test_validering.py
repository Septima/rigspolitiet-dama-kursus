from validering import er_gyldigt_postnummer, rens_postnummer


def test_rens_postnummer_tilfoejer_nul():
    assert rens_postnummer("800") == "0800"


def test_er_gyldigt_postnummer():
    assert er_gyldigt_postnummer("8000")
    assert not er_gyldigt_postnummer("800")
    assert not er_gyldigt_postnummer("80a0")
    assert not er_gyldigt_postnummer("")
