

class Cliente:

    def __init__(self, nome, cpf, telefone, email):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email
        self.posicao_na_lista = " "

    def __str__(self):
        return f'\nnome = "{self.__nome}"    \n' \
               f'cpf = "{self.__cpf}"    \n' \
               f'telefone = "{self.__telefone}"    \n' \
               f'email = "{self.__email} "   \n'

    def mostrar_sem_pular_linha(self):
        return f'\nnome:{self.__nome}   ' \
               f'cpf:{self.__cpf}   ' \
               f'telefone:{self.__telefone}   ' \
               f'email:{self.__email}   '

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email






