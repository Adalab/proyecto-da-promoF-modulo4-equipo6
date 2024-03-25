#%%
import pandas as pd
import numpy as np
from SRC import soporte
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


df_rh = pd.read_csv('SRC/data/recursos-humanos.csv', index_col=0)
df_rh =soporte.eliminar_columnas(df_rh)

df_rh=soporte.eliminando_10_filas_nulas(df_rh)

df_rh=soporte.convertir_a_datetime(df_rh, ['DateofTermination','DateofHire','LastPerformanceReview_Date', 'DOB'])
  
soporte.mayusculas_todas_palabras(df_rh,'Employee_Name')
  
soporte.nulos_a_unknown(df_rh,'Employee_Name')
    
df_rh=soporte.categorizar_department_id(df_rh)
   
soporte.nulos_999(df_rh, ['DaysLateLast30', 'Zip'], 999)
  
soporte.mediana_nulos(df_rh, 'SpecialProjectsCount')
    
df_rh=soporte.arreglando_ManagerId(df_rh)

soporte.unificar_hispaniclatino(df_rh)
   
soporte.imputar_race_desc(df_rh)

soporte.imputar_race_desc_unknown(df_rh)

df_rh=soporte.nulos_fecha(df_rh, ['DateofHire','LastPerformanceReview_Date'], '1900-01-01')

soporte.moda_nulos(df_rh, ['TermReason', 'CitizenDesc', 'RecruitmentSource'])

soporte.convertir_a_entero(df_rh, ['DaysLateLast30','SpecialProjectsCount', 'Zip', 'EmpID', 'EmpStatusID', 'Absences'])

soporte.mapear_satisfaccion_en_columna(df_rh, 'EmpSatisfaction')

soporte.mapear_genero_columna(df_rh, 'GenderID')

soporte.mapear_termd_columna(df_rh, 'Termd')

soporte.convertir_salary(df_rh, 'Salary')

soporte.columnas_a_minusculas(df_rh)

df_rh = soporte.renombrar_columna(df_rh,'dob','date_of_birth')
df_rh = soporte.renombrar_columna(df_rh,'department','xdepartment')
df_rh= soporte.renombrar_columna(df_rh,'deptid','department')

# %%
df_rh.head()
# %%
df_rh.to_csv("SRC/data/recursos-humanos_final.csv")
# %%
