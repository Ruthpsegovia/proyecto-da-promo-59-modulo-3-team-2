# 📊 Análisis de Rotación de Empleados (Employee Attrition Analysis)

<div align="center">
  
![Adalab](https://img.shields.io/badge/Adalab-Bootcamp-FF69B4?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

**Módulo 3: Análisis Exploratorio de Datos**

</div>

---

## 🎓 Proyecto del Bootcamp de Análisis de Datos - Adalab

**Módulo 3** - Análisis Exploratorio de Datos

**Equipo de Desarrollo:**
- 👩‍💻 Ana
- 👩‍💻 Ruth  
- 👩‍💻 Tamara
- 👩‍💻 Leire

## 📋 Descripción del Proyecto

Este proyecto analiza la **rotación de personal** en una organización para identificar los factores clave que influyen en que los empleados abandonen la empresa. A través del análisis de datos de recursos humanos, se busca proporcionar insights accionables para mejorar la retención del talento.

Desarrollado como parte del **Módulo 3** del Bootcamp de Análisis de Datos de **Adalab**, este trabajo pone en práctica técnicas de limpieza, transformación y análisis exploratorio de datos usando Python y sus principales librerías.

## 🎯 Objetivos del Proyecto

### Objetivos de Negocio
- Identificar los principales factores asociados con la rotación de empleados
- Analizar patrones demográficos y laborales relacionados con la salida de personal
- Evaluar la relación entre satisfacción laboral y retención de empleados
- Proporcionar métricas clave para la toma de decisiones en RRHH

### Objetivos de Aprendizaje (Módulo 3 - Adalab)
- Aplicar técnicas de limpieza y preparación de datos
- Gestionar valores nulos, duplicados y outliers
- Realizar transformaciones de datos y creación de variables derivadas
- Conducir análisis exploratorio de datos (EDA)
- Generar visualizaciones significativas
- Extraer insights accionables de los datos

## 📁 Estructura del Proyecto

```
proyecto-da-promo-59-modulo-3-team-2/
│
├── Visualizaciones/
│   ├── visualizaciones_LIMPIO.py           # Script de visualizaciones
│   └── Informe_Visualizaciones_Completo.pdf # PDF con todos los gráficos (15 páginas)
│
├── hr.csv                                   # Dataset original
├── proyecto_mod_3_team_2.ipynb              # Notebook principal de análisis
├── README.md                                # Este archivo
├── RESUMEN_EJECUTIVO.md                     # Resumen ejecutivo del proyecto
└── INSIGHTS_PRINCIPALES.md                  # Insights detallados y conclusiones
```

## 📊 Dataset

### Características del Dataset
- **Filas**: 1,470 empleados (tras limpieza)
- **Columnas**: 35 variables
- **Fuente**: Datos de recursos humanos

### Variables Principales

#### Variables Demográficas
- `Age`: Edad del empleado
- `Gender`: Género
- `MaritalStatus`: Estado civil
- `Education`: Nivel educativo
- `EducationField`: Campo de estudio

#### Variables Laborales
- `Department`: Departamento
- `JobRole`: Rol/puesto
- `JobLevel`: Nivel del puesto
- `YearsAtCompany`: Años en la empresa
- `TotalWorkingYears`: Años totales de experiencia
- `MonthlyIncome`: Ingreso mensual
- `OverTime`: Realización de horas extra

#### Variables de Satisfacción
- `JobSatisfaction`: Satisfacción laboral (1-4)
- `EnvironmentSatisfaction`: Satisfacción con el entorno (1-4)
- `WorkLifeBalance`: Balance vida-trabajo (1-4)
- `RelationshipSatisfaction`: Satisfacción con relaciones (1-4)

#### Variable Objetivo
- `Attrition`: Indica si el empleado abandonó la empresa (Yes/No)

## 🔧 Proceso de Análisis

### 1. Limpieza de Datos

#### Gestión de Duplicados
- Se identificaron y eliminaron **4 registros duplicados** basándose en `EmployeeNumber`
- Dataset final: 1,470 registros únicos

#### Tratamiento de Valores Nulos
- **Variables numéricas**: Imputación con la mediana
  - `Age`, `MonthlyIncome`, `JobSatisfaction`, `TrainingTimesLastYear`, `YearsWithCurrManager`
- **Variables categóricas**: Reemplazo con "Unknown"
  - `BusinessTravel`, `Department`, `EducationField`, `MaritalStatus`
- **StandardHours**: Imputación con la moda

#### Eliminación de Variables
Se eliminaron columnas sin variabilidad o información redundante:
- `EmployeeCount`: Valor constante (1)
- `Over18`: Todos los empleados son mayores de 18
- `StandardHours`: Sin variabilidad (todos trabajan 80 horas)

### 2. Transformación de Datos

#### Estandarización de Categorías
- Aplicación de formato **Title Case** en variables categóricas
- Eliminación de espacios y caracteres inconsistentes
- Normalización de valores en: `Department`, `EducationField`, `JobRole`, `BusinessTravel`

#### Creación de Variables Derivadas
- **`Attrition_flag`**: Variable binaria (1 = se fue, 0 = se quedó)
- **`AgeGroup`**: Grupos etarios
  - `<30`: Menores de 30 años
  - `30-40`: Entre 30 y 40 años
  - `40-50`: Entre 40 y 50 años
  - `>=50`: 50 años o más

#### Ajuste de Tipos de Datos
- Variables de satisfacción convertidas a enteros
- Variables categóricas convertidas al tipo `category` (optimización de memoria)

### 3. Análisis Exploratorio

## 📈 Resultados Principales

### Tasa Global de Rotación
- **16.1%** de los empleados abandonan la empresa

### Rotación por Grupo de Edad
| Grupo de Edad | Tasa de Rotación |
|---------------|------------------|
| <30           | 28.0%            |
| 30-40         | 14.5%            |
| 40-50         | 9.6%             |
| >=50          | 13.6%            |

**Insight**: Los empleados más jóvenes (<30 años) tienen casi el doble de probabilidad de irse.

### Rotación por Departamento
| Departamento              | Tasa de Rotación |
|---------------------------|------------------|
| Unknown                   | 34.5%            |
| Sales                     | 20.3%            |
| Human Resources           | 19.0%            |
| Research & Development    | 13.4%            |

**Insight**: Los departamentos de ventas y RRHH presentan mayor rotación.

### Rotación según Horas Extra
| OverTime | Tasa de Rotación |
|----------|------------------|
| No       | 10.2%            |
| Unknown  | 18.2%            |
| Yes      | 30.9%            |

**Insight**: Las horas extra están fuertemente asociadas con mayor rotación.

### Análisis de Satisfacción

#### Satisfacción Laboral (JobSatisfaction)
- **Empleados que permanecen**: 2.79 (promedio)
- **Empleados que se van**: 2.48 (promedio)
- **Diferencia**: -0.31 puntos

#### Satisfacción con el Entorno (EnvironmentSatisfaction)
- **Empleados que permanecen**: 2.77
- **Empleados que se van**: 2.46
- **Diferencia**: -0.31 puntos

#### Balance Vida-Trabajo (WorkLifeBalance)
- **Empleados que permanecen**: 2.78
- **Empleados que se van**: 2.66
- **Diferencia**: -0.12 puntos

**Insight**: Los empleados que abandonan la empresa tienen niveles de satisfacción consistentemente más bajos en todas las dimensiones evaluadas.

## 💡 Hipótesis Validada

✅ **La satisfacción laboral es un factor relevante en la retención de personal**

Los datos demuestran que existe una correlación entre los niveles de satisfacción (laboral, entorno, balance vida-trabajo) y la permanencia en la empresa.

## 📊 Visualizaciones

El proyecto incluye un **sistema completo de visualizaciones** que genera un PDF profesional de 15 páginas con todos los análisis gráficos.

### 📄 Informe PDF Generado

El archivo `Informe_Visualizaciones_Completo.pdf` incluye:

#### Estructura del Informe
- **Página 1:** Portada profesional
- **Página 2:** Índice de contenidos
- **Páginas 3-15:** 13 visualizaciones con resúmenes explicativos

### 📈 Visualizaciones Incluidas

#### 1. **Dashboard General de la Empresa** 📊
Vista ejecutiva con KPIs principales:
- Total de empleados: 1,470
- Tasa de rotación: 16.1%
- Salario promedio: $6,484/mes
- Satisfacción general: 2.74/4 (68.5%)
- Empleados con overtime: 405 (27.6%)

Incluye mini-gráficos de:
- Distribución por departamento
- Distribución salarial
- Grupos de edad
- Niveles de satisfacción

#### 2. **🔴 CRÍTICO: Rotación por Grupo de Edad**
**Hallazgo principal:** Los empleados <30 años tienen **28% de rotación**, casi el doble del promedio (16.1%)

Gráfico de barras comparativo mostrando:
- <30 años: 28.0% (grupo de mayor riesgo)
- 30-40 años: 14.5%
- 40-50 años: 9.6%
- ≥50 años: 13.6%

#### 3. **🔴 CRÍTICO: Rotación por Horas Extra**
**Hallazgo principal:** El overtime **triplica la rotación**: 30.9% con overtime vs 10.2% sin overtime

Incluye:
- Comparativa directa Yes vs No
- Ratio de riesgo: 3.0x más rotación
- Análisis por departamento

#### 4. **Análisis Demográfico - Edad**
- Histograma de distribución de edad
- Pie chart de grupos etarios
- Media: 37 años, Mediana: 36 años
- Composición: 45% entre 30-40 años

#### 5. **Distribución por Género y Departamento**
- Género: 60% hombres, 40% mujeres
- Departamento principal: Research & Development (65%)
- Distribución detallada por área

#### 6. **Top 8 Roles más Comunes**
Ranking de posiciones:
1. Sales Executive (326 empleados)
2. Research Scientist (292 empleados)
3. Laboratory Technician (259 empleados)
4. Manufacturing Director
5. Healthcare Representative
6. Manager
7. Sales Representative
8. Research Director

#### 7. **Distribución de Salarios**
Análisis detallado:
- Histograma con 30 bins
- Media: $6,484
- Mediana: $4,907
- Diferencia: $1,577 (indica concentración en rangos bajos-medios con outliers altos)

#### 8. **Salario Promedio por Nivel de Puesto**
Progresión salarial clara:
- Nivel 1: $2,700/mes
- Nivel 2: $5,575/mes (+106%)
- Nivel 3: $9,940/mes (+78%)
- Nivel 4: $15,468/mes (+56%)
- Nivel 5: $19,200/mes (+24%)

#### 9. **Salario Promedio por Departamento**
Comparativa de compensación:
- Sales: $7,112/mes (mejor pagado)
- Unknown: $6,865/mes
- Human Resources: $6,517/mes
- Research & Development: $5,957/mes

#### 10. **Niveles de Satisfacción (4 Dimensiones)**
Análisis completo de clima laboral:
- **Satisfacción Laboral:** 2.73/4
  - Distribución por nivel (1-4)
  - Colores: Rojo (bajo), Naranja (medio), Verde (alto)
- **Satisfacción con el Entorno:** 2.72/4
- **Balance Vida-Trabajo:** 2.76/4
- **Satisfacción con Relaciones:** 2.71/4

**Conclusión:** Satisfacción general positiva (>65%) en todas las dimensiones

#### 11. **Relación Edad-Salario-Nivel-Antigüedad**
Scatter plot multidimensional que muestra:
- Eje X: Edad
- Eje Y: Salario
- Color: Nivel del puesto (1-5)
- Tamaño: Años en la empresa

**Insight:** Correlación positiva clara - a mayor edad, experiencia y nivel → mayor salario (sistema de carrera predecible)

#### 12. **Análisis de Horas Extra (Distribución)**
- Pie chart: Proporción general (69.5% sin overtime, 27.6% con overtime)
- Barras horizontales: % con overtime por departamento
- **Conclusión:** Overtime es estructural, no excepcional

#### 13. **Distribución de Distancia del Hogar**
- Histograma de distancias
- Media: 9.2 km
- Pico en 0-2 km (mayoría vive muy cerca)
- **Conclusión:** Ubicación accesible, bajo impacto del commute

### 🎨 Características de las Visualizaciones

✅ **Profesionales:** Diseño limpio y consistente
✅ **Informativas:** Cada gráfico incluye un resumen interpretativo
✅ **Accionables:** Insights claros para toma de decisiones
✅ **Alta calidad:** 300 DPI, formato ideal para impresión
✅ **Código reproducible:** Script Python incluido

### 🚀 Generar el Informe PDF

#### Desde Terminal
```bash
cd proyecto-da-promo-59-modulo-3-team-2
python Visualizaciones/visualizaciones_LIMPIO.py
```

#### Desde Notebook
```python
import sys
sys.path.append('./Visualizaciones')

from visualizaciones_LIMPIO import generar_pdf_completo

# Generar PDF completo (15 páginas)
generar_pdf_completo(df_emp)
```

El PDF se guardará en: `Visualizaciones/Informe_Visualizaciones_Completo.pdf`

### 📌 Visualizaciones Críticas

Los gráficos marcados con 🔴 **CRÍTICO** en el índice representan los hallazgos más importantes:

1. **Rotación por Edad:** Identifica el grupo de mayor riesgo (<30 años)
2. **Rotación por Overtime:** Demuestra el factor #1 de rotación (3x más probabilidad)

Estos dos gráficos validan las conclusiones principales del resumen ejecutivo.

---

## 🛠️ Tecnologías Utilizadas

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Pandas**: Manipulación y análisis de datos
- **NumPy**: Operaciones numéricas
- **Matplotlib**: Visualización de datos y generación de gráficos
- **Seaborn**: Visualización estadística avanzada
- **Jupyter Notebook**: Entorno de desarrollo interactivo
- **Matplotlib PdfPages**: Generación de informes PDF multipágina

## 📦 Instalación y Uso

### Requisitos Previos
```bash
python >= 3.8
```

### Instalación de Dependencias
```bash
# Dependencias principales
pip install pandas numpy matplotlib seaborn jupyter

# Para generación de PDF (ya incluido en matplotlib)
# No requiere instalación adicional
```

### Ejecución del Proyecto

#### Análisis en Notebook
```bash
# Iniciar Jupyter Notebook
jupyter notebook

# Abrir proyecto_mod_3_team_2.ipynb
```

#### Generar Informe de Visualizaciones
```bash
# Desde terminal
python Visualizaciones/visualizaciones_LIMPIO.py

# Resultado: Visualizaciones/Informe_Visualizaciones_Completo.pdf
```

## 🔍 Funciones Principales

### `leer_y_explorar_df(ruta_fichero)`
Carga y realiza una exploración inicial del dataset mostrando:
- Primeras filas
- Dimensiones
- Información general
- Valores nulos
- Duplicados
- Estadísticas descriptivas

### `imputar_nulos(df)`
Gestiona valores nulos mediante:
- Mediana para variables numéricas clave
- Moda para StandardHours
- "Unknown" para variables categóricas

### `limpiar_categoricas(df)`
Estandariza variables categóricas:
- Formato Title Case
- Eliminación de espacios
- Homogeneización de valores

### `crear_variables_derivadas(df)`
Genera nuevas variables:
- `Attrition_flag`: Variable binaria de rotación
- `AgeGroup`: Grupos de edad categorizados

### `ajustar_tipos_y_columnas(df)`
Optimiza tipos de datos:
- Conversión a enteros de escalas discretas
- Conversión a category de variables categóricas
- Eliminación de columnas sin información

## 📊 Visualizaciones

El proyecto incluye visualizaciones para:
- Tasa de rotación por departamento (gráfico de barras)
- (Potencial para más visualizaciones)

## 🎓 Aprendizajes Clave

### Conceptos Aplicados del Módulo 3
1. **Limpieza de Datos**
   - Detección y eliminación de duplicados
   - Gestión de valores nulos con diferentes estrategias
   - Estandarización de variables categóricas

2. **Transformación de Datos**
   - Creación de variables derivadas
   - Codificación de variables categóricas
   - Binning y agrupación de datos numéricos

3. **Análisis Exploratorio de Datos (EDA)**
   - Análisis univariado y bivariado
   - Cálculo de métricas descriptivas
   - Identificación de patrones y tendencias

4. **Visualización de Datos**
   - Gráficos con Matplotlib y Seaborn
   - Comunicación efectiva de insights

### Insights de Negocio
1. **Edad y Rotación**: Los empleados jóvenes son un grupo de riesgo
2. **Horas Extra**: Factor crítico asociado con la rotación
3. **Satisfacción**: Predictor consistente de retención
4. **Departamentos**: Diferencias significativas entre áreas
5. **Limpieza de Datos**: Importancia de un tratamiento riguroso de valores nulos y duplicados

## 🎯 Entregables del Proyecto

### 📂 Archivos Principales

1. **`proyecto_mod_3_team_2.ipynb`**
   - Notebook con análisis completo
   - Limpieza de datos
   - Análisis exploratorio
   - Métricas y estadísticas

2. **`Informe_Visualizaciones_Completo.pdf`** (15 páginas)
   - Portada profesional
   - Índice de contenidos
   - 13 visualizaciones con resúmenes
   - Formato presentable para stakeholders

3. **`visualizaciones_LIMPIO.py`**
   - Script Python reproducible
   - Genera todas las visualizaciones
   - Documentación inline
   - Fácilmente modificable

4. **`README.md`**
   - Documentación completa del proyecto
   - Instrucciones de uso
   - Descripción de análisis

5. **`RESUMEN_EJECUTIVO.md`**
   - Resumen de 1 página
   - KPIs principales
   - Hallazgos críticos
   - Recomendaciones

6. **`INSIGHTS_PRINCIPALES.md`**
   - Análisis detallado por categorías
   - Insights de negocio
   - Banderas rojas y fortalezas
   - Recomendaciones priorizadas

### 📊 Outputs Generados

- ✅ Dataset limpio (1,470 registros)
- ✅ 13 visualizaciones profesionales
- ✅ Métricas clave calculadas
- ✅ Informe PDF ejecutivo
- ✅ Documentación completa

---

## 🚀 Próximos Pasos

## 🚀 Próximos Pasos

- [x] ~~Análisis predictivo (Machine Learning)~~ → Potencial Módulo 4
- [x] ~~Modelo de clasificación para predecir rotación~~ → Futura extensión
- [x] ~~Análisis de importancia de variables~~ → Completado en visualizaciones
- [x] ~~Dashboard interactivo~~ → PDF estático entregado
- [ ] Segmentación de empleados en grupos de riesgo (opcional)
- [ ] Análisis de tendencias temporales (requiere datos históricos)
- [ ] Presentación ejecutiva en PowerPoint (opcional para defensa)

## 🤝 Sobre el Equipo

Este proyecto ha sido desarrollado por el equipo compuesto por **Ana, Ruth, Tamara y Leire** como parte del Bootcamp de Análisis de Datos de Adalab.

### Distribución de Tareas
- **Limpieza de datos**: Trabajo colaborativo del equipo
- **Análisis exploratorio**: Trabajo colaborativo del equipo
- **Visualizaciones**: Trabajo colaborativo del equipo
- **Documentación**: Trabajo colaborativo del equipo

### Metodología de Trabajo
- Programación en pair/mob programming
- Revisiones de código en equipo
- Documentación colaborativa
- Uso de Jupyter Notebooks para análisis reproducible

## 📝 Sobre Adalab

[Adalab](https://adalab.es/) es una escuela especializada en formación digital para mujeres que ofrece bootcamps intensivos de programación web y análisis de datos, con el objetivo de aumentar la empleabilidad y diversidad en el sector tecnológico.

## 👥 Autoras

**Equipo Módulo 3 - Análisis de Datos**
- Ana
- Ruth
- Tamara
- Leire

**Promoción**: [Indicar promoción]  
**Fecha**: Enero 2025

## 📧 Contacto

Para más información sobre este proyecto, contactar a través de:
- **Adalab**: [https://adalab.es/](https://adalab.es/)
- **LinkedIn**: [Perfil del equipo o individual]

---

**Nota**: Este proyecto ha sido desarrollado con fines educativos como parte del Bootcamp de Análisis de Datos de Adalab. Los datos utilizados son de carácter público o han sido anonimizados.