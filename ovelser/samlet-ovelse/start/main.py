from config import INPUT_STI, OUTPUT_STI
from filer import laes_raekker, skriv_raekker
from validering import er_gyldig, rens_raekke


def main() -> None:
    raekker = [rens_raekke(r) for r in laes_raekker(INPUT_STI)]
    gyldige = [r for r in raekker if er_gyldig(r)]
    skriv_raekker(OUTPUT_STI, gyldige)
    print(f"Skrev {len(gyldige)} af {len(raekker)} rækker")


if __name__ == "__main__":
    main()
