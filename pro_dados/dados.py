from random import randint as rd

class Dados():
    def __init__(self, opcao):
        self.opcao = opcao

    def dado_faces(self):
        num = rd(1, self.opcao)
        return num

    def __str__(self):
        return f'Resultado sorteado do dado de {self.opcao} faces é: {self.opcoes()}'

    def opcoes(self):
        if self.opcao == 6:
            return self.dado_faces()
        elif self.opcao == 8:
            return self.dado_faces()
        elif self.opcao == 10:
            return self.dado_faces()
        elif self.opcao == 12:
            return self.dado_faces()
        elif self.opcao == 20:
            return self.dado_faces()
        else:
            raise ValueError('Opção inválida')
    
dd = Dados(20)
print(dd)