# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
 

# Modele um sistema orientado a objetos para representar contas correntes em do Banco Delas seguindo os requisitos abaixo.
 

# 1. Cada conta corrente pode ter um ou mais clientes como titular.

# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.

# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.

#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 

#    fizer um depósito, aumentaremos o saldo.

# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda

#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até

#    -renda_mensal.

# 5. Clientes homens por enquanto não têm direito a cheque especial.
 

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança" e "polimorfismo".

# Opcionalmente, você pode também utilizar "propriedades", "encapsulamento" e "classe abstrata".


# quando houver varios titulares e forem várias mulehres, o cheque especial vai ser uma média dos valores de cada uma na conta dividido pela quantidade de mulheres

# Cliente, Conta, Banco

class Cliente():
    def __init__(self, nome, telefone, renda_mensal, genero):
        self.__nome = nome;
        self.__telefone = telefone;
        self.__renda_mensal = renda_mensal;
        self.__genero = genero;
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone
    
    @property
    def renda_mensal(self):
        return self.__renda_mensal
    
    def __str__(self) -> str:
        return f'Informações - Cliente \nNome: {self.__nome}\n Telefone: {self.__telefone}\n Renda Mensal: {self.__renda_mensal}'

class Conta():
    def __init__(self, saldo):
        self.__saldo = saldo;
        self.__operacoes = [];
        self.__titulares = [];
    
    def saque(self, valor):
        if self.__saldo > valor:
            self.__saldo =- valor; 
            self.__operacoes.append(f'Saque - R${valor}')
        else:
            print('Saldo insuficiente...')
    
    def deposito(self, valor):
        self.__saldo += valor;
        self.__operacoes.append(f'Depósito - R&{valor}')
        

class Banco():
    def __init__(self):
        self.__clientes = []
    
    @property
    def clientes(self):
        return self.__clientes
    
    @clientes.setter
    def clientes(self, novo_cliente):
        self.__clientes.append(novo_cliente)

    def __str__(self) -> str:
        return f'Informações - Banco \nLista de clientes: {self.__clientes}'

def cadastrar_cliente_banco(banco: Banco, cliente: Cliente):
    banco.clientes()


cliente1 = Cliente('Dyana', '82389283923', 1200,'F')
cliente2 = Cliente('Allyson', '82389283923', 1200,'M')
lista_clientes = [cliente1, cliente2]
bancodelas = Banco(lista_clientes)
print(bancodelas)



        

    

    
    

