# Definicao da classe "Funcao"
class Funcao():
    # Metodos privados
    # Construtor da classe
    def __init__(self, coeficientes, id):
        self.__coeficientes = coeficientes
        self.__id = id

    # Retorna o "tamanho da funcao"
    def getCoeficientes(self) -> list:
        return self.__coeficientes
    
    # Retorna o identificador da funcao
    def getId(self) -> str:
        return self.__id
    
    # Imprime a funcao
    def imprime(self) -> None:
        aux = self.getCoeficientes()
        print(f"A funcao {self.getId()} e definida como: \n")
        for x in aux:
            print(f"{aux[x]}x^{x} +")

    # Calcula a funcao derivada
    def deriva(self):
        aux = self.getCoeficientes()
        for i in aux:
            pass
        
    # Atributos privados
    __coeficientes = []     # String
    __id = None             # String