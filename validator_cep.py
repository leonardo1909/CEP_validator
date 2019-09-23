import re


class Cep:

    def __init__(self, cep):
        self.cep = cep

    def validar(self):
        try:
            if re.match('[1-9]{1}[0-9]{5}$', self.cep):
                for part in range(int((len(self.cep))/3)+1):
                    if self.cep[part] == self.cep[part+2]:
                        return False
                return True
            else:
                return False

        except TypeError:
            print('O CEP deve ser informado como string.')
            raise TypeError
