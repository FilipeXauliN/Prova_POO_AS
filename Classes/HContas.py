from .Conta import Conta

class HContas:
    def __init__(self) -> None:
        self.__contas = []
    def getMediaKw(self):
        media = 0
        for conta in self.__contas:
            media+=conta.getKwGasto()
        media = media / len(self.__contas)
        return print(f"A média do consumo de kw é de {media :.2f}" )
    def getValorMediaContas(self):
        mediac = 0
        for conta in self.__contas:
            mediac+=conta.getValorPagar()
        mediac = mediac / len(self.__contas)
        return print(f"A média do valor da conta é de {mediac :.2f}" )
    def getMesMaiorConsumo(self):
        lkw=[]
        for conta in self.__contas:
            lkw.append(conta.getKwGasto())
        maior=max(lkw)
        '''maior = 0
        for conta in self.__contas:
            if conta.getKwGasto() > maior:
                maior = conta.getKwGasto()'''
        return print(f"O maior consumo mensal foi de {maior} Kw")
    def getMesMenorConsumo(self):
        lkw=[]
        for conta in self.__contas:
            lkw.append(conta.getKwGasto())
        menor=min(lkw)
        '''menor = 0
        for conta in self.__contas:
            if menor == 0 or conta.getKwGasto() < menor:
                menor = conta.getKwGasto()'''
        return print(f"O menor consumo mensal foi de {menor} Kw")
    def setConta(self, conta: Conta):
        self.__contas.append(conta)
    
    def getContasHistory(self):
        print('-' * 100)
        print('Nº da conta'.center(20),"Data de Leitura".center(20),"Nº de Leitura".center(20),"Valor".center(20),"Kw".center(20))
        print('-' * 100)
        for conta in self.__contas:
            print(conta.getDadosConta())
        

