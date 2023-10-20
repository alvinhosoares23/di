class Funcionario:
    def __init__(self, nome, bi, salario):
        self.__nome = nome
        self.__bi = bi
        self.__salario = salario

    def get_bonificacao(self):
        return self.__salario * 0.10


class Gerente(Funcionario):
    def __init__(self, nome, bi, salario, senha, qtd_funcionarios):
        super().__init__(nome, bi, salario)
        self.__senha = senha
        self.__qtd_funcionarios = qtd_funcionarios

    def autentica(self, senha):
        if self.__senha == senha:
            print('Acesso permitido!')
        else:
            print('Acesso negado!')

    def get_bonificacao(self):
        return self._Funcionario__salario * 0.15


f = Funcionario('Pedro', '00213', 563)
g = Gerente('Alvaro', '001995', 2563, senha='1234', qtd_funcionarios=25)

print(g.__dict__)
print(vars(f))
g.autentica('1234')
print(g.get_bonificacao())
