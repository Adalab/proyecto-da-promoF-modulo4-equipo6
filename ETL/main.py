#%%
import pandas as pd
import numpy as np
from SRC import soporte
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


df_rh = soporte.leer_csv('SRC/data/recursos-humanos.csv')
df_rh =eliminar_columnas(df_rh)

df_rh=eliminando_10_filas_nulas(df_rh)

df_rh=convertir_a_datetime(df_rh, ['DateofTermination','DateofHire','LastPerformanceReview_Date', 'DOB'])
  
mayusculas_todas_palabras(df_rh,'Employee_Name')
  
nulos_a_unknown(df_rh,'Employee_Name')
    
df_rh=categorizar_department_id(df_rh)
   
nulos_999(df_rh, ['DaysLateLast30', 'Zip'], 999)
  
mediana_nulos(df_rh, 'SpecialProjectsCount')
    
df_rh=arreglando_ManagerId(df_rh)

unificar_hispaniclatino(df_rh)
   
imputar_race_desc(df_rh)

imputar_race_desc_unknown(df_rh)

df_rh=nulos_fecha(df_rh, ['DateofHire','LastPerformanceReview_Date'], '1900-01-01')

moda_nulos(df_rh, ['TermReason', 'CitizenDesc', 'RecruitmentSource'])

convertir_a_entero(df_rh, ['DaysLateLast30','SpecialProjectsCount', 'Zip', 'EmpID', 'EmpStatusID', 'Absences'])

mapear_satisfaccion_en_columna(df_rh, 'EmpSatisfaction')

mapear_genero_columna(df_rh, 'GenderID')

mapear_termd_columna(df_rh, 'Termd')

convertir_salary(df_rh, 'Salary')

columnas_a_minusculas(df_rh)

df_rh = renombrar_columna(df_rh,'dob','date_of_birth')
df_rh = renombrar_columna(df_rh,'department','xdepartment')
df_rh= renombrar_columna(df_rh,'deptid','department')

   


