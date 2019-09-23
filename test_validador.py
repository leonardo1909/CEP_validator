import pytest
from validator_cep import Cep


def test_letras():
    cep = Cep('lasdko')
    assert cep.validar() is False


def test_alfanumerico():
    cep = Cep('cap123')
    assert cep.validar() is False


def test_vazio():
    cep = Cep('')
    assert cep.validar() is False


def test_None():
    with pytest.raises(TypeError):
        cep = Cep(None)
        cep.validar()


def test_int():
    with pytest.raises(TypeError):
        cep = Cep(123456)
        cep.validar()


class TestRange:

    def test_menor_6_digitos(self):
        cep = Cep('54321')
        assert cep.validar() is False

    def test_maior_9_digitos(self):
        cep = Cep('1234567890')
        assert cep.validar() is False

    def test_6_digitos_menor_100k(self):
        cep = Cep('012345')
        assert cep.validar() is False


class Testidslice:

    def test_alternado_pares(self):
        cep = Cep('121426')
        assert cep.validar() is False

    def test_valido(self):
        cep = Cep('523563')
        assert cep.validar() is True

    def test_alternado_duplo(self):
        cep = Cep('552523')
        assert cep.validar() is False
