import re


class Cep:

    def __init__(self, cep):
        self.cep = cep

    def validar(self):
        try:
            return re.match('^[1-9]+[0-9][6]$', self.cep)
        except TypeError:
            print('O CEP deve ser informado como string.')
            raise TypeError
