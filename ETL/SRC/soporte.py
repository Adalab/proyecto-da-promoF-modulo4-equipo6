import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Imputación de nulos usando métodos avanzados estadísticos
# -----------------------------------------------------------------------
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder

# AB testing
# -----------------------------------------------------------------------
from scipy.stats import ttest_ind
from scipy.stats import levene

# Librerías de visualización
# -----------------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt



df_rh = pd.read_csv("data/recursos-humanos.csv", index_col=0)

def eliminar_columnas(df_col_sucio):
    """
    Elimina columnas del Dataframe
    parametros:
    dataframe del que sacamos las columnas
    return:
    dataframe modificado
    """
    columnas_nulos=['Date_of_Birth', 'Age', 'date', 'MarriedID','FromDiversityJobFairID','MaritalStatusID', 'Remuneration','Sex', 'PerfScoreID', 'PositionID', 'Department']
    df_col_sucio.drop(columns=columnas_nulos, inplace=True)
    return df_col_sucio

def eliminando_10_filas_nulas(df_sucio):
    """
    Elimina filas nulas del Dataframe
    parametros:
    Dataframe del que sacamos las columnas
    return:
    Dataframe modificado
    """
    filas_nulas = df_sucio[(df_sucio["EmpID"].isnull())].index
    df_sucio.drop(filas_nulas, axis = 0, inplace=True)
    return df_sucio

def convertir_a_datetime(df, columnas):
    """
    Cambia el tipo de datos de una columna a fecha
    parametros:
    Dataframe del que sacamos las columnas
    columnas: lista de columnas que queremos cambiar
    return:
    dataframe modificado
    """
    for columna in columnas:
        df[columna] = pd.to_datetime(df[columna], errors='coerce')
    return df

def mayusculas_todas_palabras(df,columna):
    """
    Convierte la primera letra de la columna a mayúscula.
    parametros:
    Dataframe 
    Columna que queremos cambiar
    """
    df[columna] = df[columna].str.title()
    
def nulos_a_unknown(df,columna):
    """
    Convierte la primera letra de la columna a mayúscula.
    parametros:
    Dataframe 
    Columna que queremos cambiar
    """
    df[columna] = df[columna].fillna("Unknown")

def categorizar_department_id(df):
    """
    Esta función asigna valores a las siguientes columnas del dataframe()
    
    Parámetros:
    Recibe un dataframe
    Returns:
    Devuelve el dataframe modificado
    """
    mapping = {
        1: 'Admin Offices',
        2: 'Executive Officer',
        3: 'IT/IS',
        4: 'Software Engineering',
        5: 'Production',
        6: 'Sales'
    }
    df['DeptID'] = df['DeptID'].map(mapping)
    return df



def nulos_999(df, columns, value):
    """
    Esta función asigna valores a las siguientes columnas del dataframe()
    parametros:
    Dataframe del que sacamos las columnas
    columnas: lista de columnas que queremos cambiar
    value : el valor que queremos poner en la columna
    
    """
    for column in columns:
        df[column].fillna(value, inplace=True)
        


def mediana_nulos(df, column):
    '''
    Imputacion de los nulos de una columna con el valor de su mediana
    Parametros: 
    Dataframe
    columna: Columna a imputar los nulos
    '''
    mediana_value = df[column].median()
    df[column].fillna(mediana_value, inplace=True)



def arreglando_ManagerId(df):
    """
    Funcion que asigna especificamente el valor 39.0 a los nulos de la columna ManagerId
    Parametros:
    Dataframe
    Return:
    Dataframe modificado
    """
    #Hemos comprobado que los nulos de ManagerID corresponden al empleado Webster Butler con ID 39.0
    df["ManagerID"] = df["ManagerID"].fillna(39.0)
    #Cambiamos la columna de ManagerID para tener los nombres de los Managers
    managers = {1.0:'Brandon R. LeBlanc', 
                2.0:'Janet King', 
                3.0:'Brandon R. LeBlanc', 
                4.0:'Simon Roup', 
                5.0:'Jennifer Zamora',
                6.0:'Eric Dougall',
                7.0:'Peter Monroe',
                9.0:'Board of Directors',
                10.0:'Alex Sweetwater',
                11.0:'Amy Dunn',
                12.0:'Brannon Miller',
                13.0:'Brian Champaigne',
                14.0:'David Stanley',
                15.0:'Debra Houlihan',
                16.0:'Elijiah Gray',
                17.0:'John Smith',
                18.0:'Kelley Spirea',
                19.0:'Ketsia Liebig',
                20.0:'Kissy Sullivan',
                21.0:'Lynn Daneault',
                22.0:'Michael Albert',
                30.0:'Michael Albert',
                39.0:'Webster Butler'
                }
    #Sobreescribimos la columna ManagerName para eliminar los valores nulos usando la columna ManagerID
    df["ManagerName"] = df["ManagerID"].map(managers)
    return df



def unificar_hispaniclatino(df):
    # Unificar valores 'Yes' y 'yes' como 'Yes' y 'No' y 'no' como 'No' en la columna 'HispanicLatino'
    df['HispanicLatino'] = df['HispanicLatino'].str.lower().replace({'yes': 'Yes', 'no': 'No'})

def imputar_race_desc(df):
    # Si en la columna RaceDesc hay un nulo y en la columna HispanicLatino hay un Yes, imputa un "Hispanic"
    df['RaceDesc'] = df.apply(lambda row: 'Hispanic' if row['HispanicLatino'] == 'Yes' and pd.isnull(row['RaceDesc']) else row['RaceDesc'], axis=1)

def imputar_race_desc_unknown(df):
    # A los nulos restantes, les meto una etiqueta de "Unknown"
    df['RaceDesc'].fillna('Unknown', inplace=True)
    


def nulos_fecha(df, columnas, fecha_reemplazo):
    for columna in columnas:
        df[columna] = df[columna].fillna(pd.to_datetime(fecha_reemplazo))
    return df



def moda_nulos(df, column):
    """
    Funcion que imputa los nulos de una columna con la moda
    Parametros:
    Dataframe
    Columna : Columna a tratar los nulos
    """
    for columna in column: 
        moda_value = df[columna].mode().iloc[0]
        df[columna].fillna(moda_value, inplace=True)
        

def convertir_a_entero(df, columnas):
    """
    Convierte el tipo de columnas a integer.
    Parametros: 
    Dataframe
    Columnas: lista de columnas a convertir.
    """
    for columna in columnas:
        df[columna] = df[columna].astype('Int64', errors='ignore')








def mapear_satisfaccion_en_columna(df, columna):
    """
  Funcion que recibe un Dataframe y una columna y categoriza sus valores
  Parametros:
  Dataframe
  Columna; Columna que se quiere categorizar
   """
    
    if columna == 1.0:
        return 'Very Dissatisfied'
    elif columna == 2.0:
        return 'Dissatisfied'
    elif columna == 3.0:
        return 'Neutral'
    elif columna == 4.0:
        return 'Satisfied'
    elif columna == 5.0:
        return 'Very Satisfied'
    else:
        return 'No answer'



def mapear_genero_columna(df, columna):
    """
    Funcion que recibe un Dataframe y una columna y categoriza sus valores, de tal 
    manera que si el valor es 1.0 lo cambia a Masculine y si no es 1.0 lo cambia a Femenine.
    Parametros:
    Dataframe
    Columna; Columna que se quiere categorizar
    """
   
    if columna == 1.0:
        return 'Masculine'
    else: 
        return 'Femenine'




def mapear_termd_columna(df, columna):
    """
    Funcion que recibe un Dataframe y una columna y categoriza sus valores, de tal 
    manera que si el valor es 1.0 lo cambia a Yes y si no es 1.0 lo cambia a No.
    Parametros:
    Dataframe
    Columna; Columna que se quiere categorizar
    """

    if columna == 1.0:
        return 'Yes'
    else: 
        return 'No'

def convertir_salary(df, columna):
    """
    Funcion que quita ',' y convierte la columna a typo float
    Parametros:
    Dataframe
    columna: columna que se quiere tratar
    """
    df[columna]=df[columna].str.replace(',', '')
    df[columna] = df[columna].astype(float)
 
def columnas_a_minusculas(df):
    """
    Cambia los nombres de las columnas a minusculas
    parametros:
    dataframe del que sacamos las columnas
    diccionario_columnas:Diccionario que mapea nombres de columnas a sus nuevos nombres
    return:
    dataframe modificado
    """
    df.columns = map(str.lower, df.columns)

def renombrar_columna(df, nombre_anterior, nombre_nuevo):
    """
    Renombra una columna en el DataFrame
    Parametros:
    - df: DataFrame
    - nombre_anterior: Nombre actual de la columna que va a ser renombrada.
    - nombre_nuevo: Nombre nuevo de la columna.

    Returns:
    - DataFrame actualizado.
    """
    if nombre_anterior in df.columns:   
        df.rename(columns={nombre_anterior: nombre_nuevo}, inplace=True)
        return df
    else:
        return df
    