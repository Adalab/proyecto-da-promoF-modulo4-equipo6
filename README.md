# proyecto-da-promoF-modulo4-equipo6

# Proyecto Data Insights: ETL y Visualización Impactante en Tableau/Power BI

¡Bienvenidas al proyecto "Data Insights: ETL y Visualización Impactante en Tableau/Power BI" en nuestro bootcamp de Data Analytics de Adalab !

## Descripción del Proyecto
En este desafío, nos sumergiremos en el apasionante mundo del reporting de datos, adquiriendo habilidades clave para transformar datos crudos en información significativa y visualmente impactante. El proyecto se centra en el análisis de la rotación de empleados en la empresa ficticia ABC Inc.

## Conjunto de Datos de Recursos Humanos
- Información sobre los empleados (estado civil, género, rendimiento, salario, etc.). (Al final del documento quedan recogidas todas las columnas del archivo inicial)
- Problema a abordar: Análisis de la Rotación de Empleados.

### Tareas del Proyecto
- Limpieza de Datos: Abordar valores atípicos, datos faltantes y errores tipográficos.
- Exploración de perfiles de diversidad, fuentes de reclutamiento, equidad salarial, etc.

### Preguntas Clave
- Perfil de diversidad general.
- Mejores fuentes de reclutamiento para la diversidad.
- Equidad salarial en áreas específicas.
- Tasa de rotación general y por estado civil.
- Relación entre compromiso y probabilidad de abandono.
- Razones comunes para abandonar la empresa.
- Relación de asignación de proyectos especiales con rotación.

## Objetivos del Proyecto
- Consolidar conocimientos de visualización básicos.
- Implementar Scrum como marco de referencia.
- Mejorar la comunicación y habilidades de exposición.

## Planificación del Proyecto
### Sprints
- Dos sprints de 3 sesiones cada uno.
- Sprint Review al final de cada sprint.
- Sesión final de presentación y retroalimentación.

### Criterios de Aceptación
- Crear infraestructura en GitHub.
- Desarrollar un dashboard con resultados.
- Repositorio de GitHub con todo el código.

## Entrega
- Repositorio en GitHub con el formato adecuado.
- Primer sprint (sprint review): 14 Marzo.
- Segundo sprint (sprint review): 23 Marzo.
- Presentación final y retro: 27 Marzo.

## Presentación Final
- Presentación de 5 minutos por equipo.
- 5 minutos de feedback.
- Enfoque técnico y de producto.
- Practicar exposición y habilidades de comunicación.

## Librerías 
- pandas 
- numpy
pd.set_option('display.max_rows', None) # para poder visualizar todas las filas de los DataFrames
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

### Imputación de nulos usando métodos avanzados estadísticos
- sklearn
### Visualización
- matplotlib
- seaborn
### AB testing
- scipy
### Gestión de los warnings
- warnings

¡Disfruten del proyecto y demuestren sus habilidades en análisis de datos y visualización!



# Columna y descripción:

Employee_Name: Nombre completo del empleado.

EmpID: Identificador único del empleado.

MarriedID: Indica si el empleado está casado (1) o no (0).

MaritalStatusID: Identificador que representa el estado civil del empleado (por ejemplo, 0 - Soltero, 1 - Casado, 2 - Divorciado, etc.).

GenderID: Identificador del género del empleado (por ejemplo, 0 - Femenino, 1 - Masculino).

EmpStatusID: Identificador del estado del empleado (por ejemplo, 1 - Activo, 5 - Voluntariamente Terminado, etc.).

DeptID: Identificador del departamento al que pertenece el empleado.

PerfScoreID: Identificador del rendimiento del empleado (por ejemplo, 3 - Cumple completamente, 4 - Supera las expectativas, etc.).

FromDiversityJobFairID: Indica si el empleado fue reclutado a través de una feria de empleo enfocada en la diversidad (1) o no (0).

Salary: Salario del empleado.

Termd: Indica si el empleado fue terminado (1) o no (0).

PositionID: Identificador del cargo del empleado.

Position: Nombre del cargo del empleado.

State: Estado en el que reside el empleado.

Zip: Código postal de la ubicación del empleado.

DOB: Fecha de nacimiento del empleado.

Sex: Género del empleado (F - Femenino, M - Masculino).

MaritalDesc: Descripción del estado civil del empleado (por ejemplo, Soltero, Casado, Divorciado, etc.).

CitizenDesc: Descripción del estatus de ciudadanía del empleado (por ejemplo, Ciudadano de EE. UU., No ciudadano elegible, etc.).

HispanicLatino: Indica si el empleado es de origen hispano o latino.

RaceDesc: Descripción de la raza del empleado (por ejemplo, Blanco, Negro o Afroamericano, Asiático, etc.).

DateofHire: Fecha de contratación del empleado.

DateofTermination: Fecha de terminación del empleado (solo si Termd es igual a 1).

TermReason: Razón de la terminación del empleado (solo si Termd es igual a 1).

EmploymentStatus: Estado de empleo del empleado (por ejemplo, Activo, Voluntariamente Terminado, etc.).

Department: Departamento al que pertenece el empleado.

ManagerName: Nombre completo del gerente del empleado.

ManagerID: Identificador único del gerente del empleado.

RecruitmentSource: Fuente de reclutamiento del empleado (por ejemplo, LinkedIn, Indeed, Búsqueda en línea, etc.).

PerformanceScore: Puntuación de rendimiento del empleado (por ejemplo, Cumple, Supera las expectativas, Necesita mejorar, etc.).

EngagementSurvey: Puntuación de la encuesta de compromiso del empleado.

EmpSatisfaction: Puntuación de satisfacción del empleado.

SpecialProjectsCount: Número de proyectos especiales en los que ha participado el empleado.

LastPerformanceReview_Date: Fecha de la última revisión de rendimiento del empleado.

DaysLateLast30: Número de días de retraso en el último mes.

Absences: Número de ausencias del empleado.