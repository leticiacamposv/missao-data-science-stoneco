import pandas as pd
import datetime
def correct_hour_format(x):
    """
    Esta função tenta converter o valor de entrada `x` para um objeto `timedelta` do pandas. 
    Se a conversão falhar, a função assume que a entrada é uma hora inteira (0-23) e formata essa hora como 'HH:00:00'.

    Parâmetros:
    x(str ou int)->int: O valor de entrada representando a hora.

    Retorno:
    pandas.Timedelta -> Valor da hora convertido em um objeto `timedelta` do pandas.
    """
    try:
        hour = pd.to_timedelta(str(x))
    except: 
        hour = pd.to_timedelta(f'{int(x):02d}:00:00')
    return hour


def data_preparation(df):
    """
    Esta função aplica correções de dtypes, limpeza de nulos e outros tratamentos de acordo com os dados da tabela de CBK, além da criação da coluna transaction_timestamp
    
    Parâmetros:
    df(pd.Dataframe): Dataframe contendo as colunas Dia, Hora, Valor, Cartão e CBK
    
    Retorno:
    clean_df(pd.Dataframe) -> Dataframe limpo e corrigido"""

    # ---------- Dados temporais ---------------------------------------------------------------------
    # Correção dos dtypes
    df['Hora'] = df['Hora'].apply(correct_hour_format)
    df['Dia'] = pd.to_datetime(df['Dia'], errors='coerce', format='%Y-%m-%d %H:%M:%S')

    # Limpeza de anos 'absurdos' (muito no passado ou futuro)
    current_year = datetime.datetime.now().year
    df = df[(df['Dia'].dt.year >= 1900) & (df['Dia'].dt.year <= current_year)]

    df['transaction_timestamp'] = df['Dia'] + df['Hora']

    #Limpeza de transaction_timestamps com horas fora do range aceitável (dentro das 24 horas)
    df = df[(df['transaction_timestamp'].dt.hour >= 0) & (df['transaction_timestamp'].dt.hour < 24)]

    # --------- Dados numéricos ----------------------------------------------------------------------
    df = df[pd.to_numeric(df['Valor'], errors='coerce').notnull()]
    df['Valor'] = df['Valor'].astype('float')

    # --------- Coluna target ------------------------------------------------------------------------
    df = df.dropna(subset=['CBK'])
    df['CBK'] = df['CBK'].map({'Não': 0, 'Sim': 1}).fillna(df['CBK'])

    return df
    
