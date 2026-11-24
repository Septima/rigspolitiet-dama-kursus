import logging
from pathlib import Path

from adresse import fra_raekke, til_raekke
from config import INPUT_STI, OUTPUT_STI
from filer import laes_raekker, skriv_raekker
from validering import er_gyldig, rens_adresse

logger = logging.getLogger(__name__)


def koer_job(input_sti: Path, output_sti: Path) -> int:
    try:
        raekker = laes_raekker(input_sti)
    except FileNotFoundError:
        logger.error("Inputfil findes ikke: %s", input_sti)
        raise

    gyldige = []
    for raekke in raekker:
        adresse = rens_adresse(fra_raekke(raekke))
        if er_gyldig(adresse):
            gyldige.append(adresse)
        else:
            logger.warning("Afvist række: %s", raekke)

    skriv_raekker(output_sti, [til_raekke(a) for a in gyldige])
    logger.info("Skrev %d af %d rækker", len(gyldige), len(raekker))
    return len(gyldige)


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    koer_job(INPUT_STI, OUTPUT_STI)


if __name__ == "__main__":
    main()
