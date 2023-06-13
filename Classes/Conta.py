from datetime import datetime 
import datetime as dt
class Conta:
    def __init__(self,n_conta:str="",dataleitura:datetime=datetime.now(),n_leitura:str="",valor:float=0,kw_gasto:int=0)->None:
        self.__n_conta = n_conta
        self.__dataleitura = dataleitura
        self.__kw_gasto = kw_gasto
        self.__n_leitura = n_leitura
        self.__valor_pagar = valor
        self.__data_pgto = dt.timedelta(days=20)+dataleitura

    def getDataLeitura(self):
        return self.__dataleitura.strftime(" %d/%m/%Y ")
    def getKwGasto(self):
        return self.__kw_gasto
    def getValorPagar(self):
        return self.__valor_pagar
    
    def getDadosConta(self):
        print(f"{self.__n_conta}".center(20),f"{self.getDataLeitura()}".center(20),f"{self.__n_leitura}".center(20),f"R$ {self.__valor_pagar:.2f}".center(20),f"{self.__kw_gasto}".center(20))
        return ('-' *100)
