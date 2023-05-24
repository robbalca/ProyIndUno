from fastapi import FastAPI
from typing import Union
import unicodedata as unicodedata
from pandas import read_csv
import pandas as pd



app = FastAPI()



d1 = pd.read_csv('d_limpio.csv')

@app.get("/")
def read_root():
    return {"Escribe lo que desees"}


@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes:str) -> dict:
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se   estrenaron ese mes historicamente'''
    
    months_translated= {
    'enero': 'January',
    'febrero': 'Febreary',
    'marzo': 'March',
    'abril': 'April',
    'mayo': 'May',
    'junio': 'June',
    'julio': 'July',
    'agosto': 'August',
    'septiembre': 'September',
    'octubre': 'October',
    'noviembre': 'November',
    'diciembre': 'December'}
    fechas = pd.to_datetime(d1['release_date'], format= '%Y-%m-%d')
    n_mes= fechas[fechas.dt.month_name(locale = 'es')==mes.capitalize()]
    respuesta = n_mes.shape[0]
    return {'mes':mes, 'cantidad':respuesta}

    

@app.get('/peliculas_dia/{dia}')
def peliculas_dia(dia:str) -> dict:
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se   estrebaron ese dia historicamente'''
    
    day_translated = {
    'lunes': 'Monday',
    'martes': 'Tuesday',
    'miercoles': 'Wednesday',
    'jueves': 'Thursday',
    'viernes': 'Friday',
    'sabado': 'Saturday',
    'domingo': 'Sunday'}
    fechas = pd.to_datetime(d1['release_date'], format= '%Y-%m-%d')
    n_dia= fechas[fechas.dt.day_name(locale = 'es')==dia.capitalize()]
    respuesta = n_dia.shape[0]
    return {'dia':dia, 'cantidad':respuesta}

    

@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total  y promedio'''
    f_bajo= franquicia.lower()
    fran= d1[['belongs_to_collection','budget','revenue']].dropna(subset=['belongs_to_collection'])
    fran= fran[fran['belongs_to_collection'].map(str.lower).apply(lambda x: f_bajo in x)]
    cantidad = fran.shape[0]
    gananciat= (fran['revenue']- fran['budget']).sum()
    gananciap= (fran['revenue']- fran['budget']).mean()
    return {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total':gananciat, 'ganancia_promedio': gananciap}


    

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo'''
    if isinstance(pais, str):
        p_bajo = pais.lower()
        cantidad = d['production_countries'].apply(lambda x: str(x).lower()).map(str.lower).apply(lambda x: p_bajo in x).sum()
        return {'pais': pais, 'cantidad': cantidad}

    

@app.get('/productoras/{productora}')
def productoras(productora:str):
    '''Ingresas la productora, retornando la ganancia toal y la cantidad de peliculas que produjeron'''
    prod = d1[['production_companies','budget', 'revenue']].dropna()
    prod['production_companies'] = prod['production_companies'].map(str.lower)
    cantidad = prod.shape[0]
    gtotal= (prod['revenue'] - prod['budget']).sum()
    return {'productora':productora, 'ganancia_total': gtotal, 'cantidad': cantidad }

    
@app.get('/retorno/{pelicula}')
def retorno(pelicula:str) -> dict:
    '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo'''
    pelicula_df = d1.loc[d1['title'] == pelicula.title()]
    inversion = pelicula_df['budget'].iloc[0].item()
    ganancia = pelicula_df['revenue'].iloc[0].item()
    retorno= pelicula_df['return'].iloc[0].item()
    anio = pelicula_df['release_year'].iloc[0].item()
    return {'pelicula': pelicula, 'inversion': inversion, 'ganancia': ganancia, 'retorno': retorno, 'anio': anio }

    
# ML
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}