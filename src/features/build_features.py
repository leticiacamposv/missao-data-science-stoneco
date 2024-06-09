import pandas as pd
import datetime

def periodo_do_dia(timestamp):
    """
    Avalia a hora do timestamp fornecido e classifica o período do dia em uma das seguintes categorias: 
    - 'madrugada' (entre 00:00:01 e 05:29:59)
    - 'dia' (entre 05:30:00 e 11:59:59)
    - 'tarde' (entre 12:00:00 e 17:59:59)
    - 'noite' (entre 18:00:00 e 00:00:00)

    Parâmetros:
    timestamp -> (datetime.datetime)

    Retorno:
    str
    """
    hora = timestamp.time()
    madrugada_inicio = datetime.time(0, 0, 1)
    manha_inicio = datetime.time(5, 30, 0)
    tarde_inicio = datetime.time(12, 0, 0)
    noite_inicio = datetime.time(18, 0, 0)
    if madrugada_inicio <= hora < manha_inicio:
        return 'madrugada'
    elif manha_inicio <= hora < tarde_inicio:
        return 'dia'
    elif tarde_inicio <= hora < noite_inicio:
        return 'tarde'
    else:
        return 'noite'

def cbk_feature_engineering(df):
    """
    Realiza a criação de novas colunas a partir das existentes
    
    Parâmetros:
    df -> (pd.DataFrame) resultado do data preparation"""

    # ----------- Dados temporais --------------------------------------------------------------------------------------
    df['periodo_do_dia'] = df['transaction_timestamp'].apply(periodo_do_dia)
    df['dia_da_semana'] = pd.to_datetime(df['transaction_timestamp']).dt.day_name(locale='pt_BR')
    # df['trimestre'] = df['transaction_timestamp'].dt.quarter

    # ----------- Dados de cartão ---------------------------------------------------------------------------------------
    df['bandeira_cartao'] = df['Cartão'].str[:1]
    df['emissor_cartao'] = df['Cartão'].str[1:6]

    # ----------- Filtro de colunas -------------------------------------------------------------------------------------
    df.drop(columns=['Hora', 'transaction_timestamp', 'Dia', 'Cartão', 'bandeira_cartao'], inplace=True)

    # ----------- Afirmando dtypes --------------------------------------------------------------------------------------
    return df
    