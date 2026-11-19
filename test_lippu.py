"""Testit lippu.py-moduulille. Täydennä tehtävien mukaan (ks. README.md)."""

import pytest

from lippu import kokonaishinta, lippuhinta


def test_aikuisen_hinta():
    # Arrange: valmistellaan syöte
    ika = 30
    # Act: kutsutaan testattavaa funktiota
    hinta = lippuhinta(ika, opiskelija=False)
    # Assert: tarkistetaan tulos
    assert hinta == 15.0


# TEHTÄVÄ 2: Raja-arvot yhdellä parametrisoidulla testillä.
# Täydennä alla olevaan listaan pareja (ikä, odotettu hinta).
# Poista sen jälkeen rivi @pytest.mark.skip.
# @pytest.mark.skip(reason="Täydennä raja-arvot ja poista tämä rivi")
@pytest.mark.parametrize(
    "ika, odotettu",
    [
        (0, 0.0),
        (6, 0.0),
        (7, 8.0),
        (17, 8.0),
        (18, 15.0),
        (64, 15.0),
        (65, 10.0),
        (120, 10.0),
    ],
)
def test_lippuhinta_raja_arvot(ika, odotettu):
    assert lippuhinta(ika, opiskelija=False) == odotettu


# TEHTÄVÄ 3: Virheelliset iät nostavat ValueErrorin.
@pytest.mark.parametrize("ika", [-1, 121])
def test_virheellinen_ika(ika):
    with pytest.raises(ValueError):
        lippuhinta(ika, opiskelija=False)



# TEHTÄVÄ 4: Kokonaishinta ja ryhmäalennuksen raja (9 ja 10 lippua).
def test_kokonaishinta_ryhmaalennus():
    # tyhjä lista
    iat = []
    assert kokonaishinta(iat) == 0.0

    # 9 lippua, ei alennusta
    iat = [30] * 9
    assert kokonaishinta(iat) == 135.0

    # 10 lippua, alennus 10 %
    iat = [30] * 10
    assert kokonaishinta(iat) == 150.0 * 0.9

def test_opiskelija_alennus():
    assert lippuhinta(20, opiskelija=True) == 10.0