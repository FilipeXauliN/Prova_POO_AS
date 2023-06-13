from Classes import Conta,HContas
from datetime import datetime

if __name__ == "__main__":
    history = HContas()
        
  
    history.setConta(Conta(n_conta="0016634",dataleitura=datetime.strptime("01/02/2021", "%d/%m/%Y"),n_leitura="002",valor=250.0,kw_gasto=150))
    history.setConta(Conta(n_conta="0017634",dataleitura=datetime.strptime("01/03/2021", "%d/%m/%Y"),n_leitura="003",valor=170.0,kw_gasto=130))
    history.setConta(Conta(n_conta="0018634",dataleitura=datetime.strptime("01/04/2021", "%d/%m/%Y"),n_leitura="004",valor=210.0,kw_gasto=140))
    history.setConta(Conta(n_conta="0019634",dataleitura=datetime.strptime("01/05/2021", "%d/%m/%Y"),n_leitura="005",valor=70.0,kw_gasto=90))
    history.setConta(Conta(n_conta="0019034",dataleitura=datetime.strptime("01/06/2021", "%d/%m/%Y"),n_leitura="006",valor=180.0,kw_gasto=135))
    history.setConta(Conta(n_conta="0019134",dataleitura=datetime.strptime("01/07/2021", "%d/%m/%Y"),n_leitura="007",valor=300.0,kw_gasto=185))
    

    history.getMediaKw()
    history.getValorMediaContas()
    history.getMesMaiorConsumo()
    history.getMesMenorConsumo()
    history.getContasHistory()
    
    