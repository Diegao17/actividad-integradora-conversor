import pytest
from converter import (
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    kilometros_a_millas,
    millas_a_kilometros,
    pesos_a_dolares,
    dolares_a_pesos,
)

@pytest.mark.unit
@pytest.mark.parametrize(
    "celsius, esperado",
    [
        (0, 32),
        (100, 212),
        (25, 77),
    ],
)
def test_celsius_a_fahrenheit(celsius, esperado):
    resultado = celsius_a_fahrenheit(celsius)
    assert resultado == pytest.approx(esperado)


@pytest.mark.unit
def test_fahrenheit_a_celsius():
    resultado = fahrenheit_a_celsius(32)
    assert resultado == pytest.approx(0)


@pytest.mark.unit
def test_kilometros_a_millas():
    resultado = kilometros_a_millas(10)
    assert resultado == pytest.approx(6.21371)


@pytest.mark.unit
def test_millas_a_kilometros():
    resultado = millas_a_kilometros(10)
    assert resultado == pytest.approx(16.09344, rel=1e-5)


@pytest.mark.unit
def test_pesos_a_dolares():
    resultado = pesos_a_dolares(173)
    assert resultado == pytest.approx(10)


@pytest.mark.unit
def test_dolares_a_pesos():
    resultado = dolares_a_pesos(10)
    assert resultado == pytest.approx(173)
