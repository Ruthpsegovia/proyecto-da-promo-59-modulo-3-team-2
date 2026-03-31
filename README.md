<h1 align="center">Proyecto de Data Analytics — Análisis de Rotación de Empleados</h1>

<p align="center">
  Bootcamp de Data Analytics & IA — Adalab.
</p>

<p align="center">
  <img src="Logo el dato incomodo.jpg" width="300" alt="Análisis de Rotación de Empleados">
</p>

---

## Resumen ejecutivo (para qué sirve)

**Pregunta:** ¿Qué factores están más asociados a la rotación (attrition) y en qué segmentos es más alta?  
**Objetivo:** identificar palancas accionables para mejorar **retención** y apoyar decisiones basadas en datos.  

**Entregables clave (en este repo):**
- 📄 **Resumen ejecutivo:** `Resumen ejecutivo.pdf`
- 🧼 **Limpieza/transformación:** `Transformacion y limpieza.ipynb`
- 📊 **Dataset final:** `Visualizaciones/df_final.csv`
- 📈 **Storytelling / visual:** `Visualizaciones/Visual_Storytelling.ipynb`
- 🗃️ **Base de datos / materiales:** carpeta `Base_Datos/`

**Aplicación (empleabilidad / impacto):** el mismo enfoque de segmentación + KPIs sirve para detectar “puntos de fuga”, abandono y adherencia en programas, y ajustar intervenciones con mejora continua.

---

## Índice de Contenidos

- [Índice de Contenidos](#índice-de-contenidos)
- [Resumen y Alcance del Proyecto](#resumen-y-alcance-del-proyecto)
- [Objetivos](#objetivos)
  - [Objetivos de Negocio](#objetivos-de-negocio)
  - [Objetivos de Aprendizaje](#objetivos-de-aprendizaje)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Proceso de Análisis](#proceso-de-análisis)
  - [1. Limpieza de Datos](#1-limpieza-de-datos)
  - [2. Transformación de Datos](#2-transformación-de-datos)
  - [3. Exploración de Datos (EDA)](#3-exploración-de-datos-eda)
  - [4. Creación de la Base de Datos](#4-creación-de-la-base-de-datos)
- [Resultados y Hallazgos](#resultados-y-hallazgos)
- [Herramientas](#herramientas)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Autoría](#autoría)

---

## Resumen y Alcance del Proyecto

Este repositorio contiene la **Evaluación Final del Módulo 3 (Análisis Exploratorio de Datos)** del Bootcamp de Data Analytics de Adalab.

El objetivo principal del proyecto es **analizar la rotación de empleados (employee attrition)** con el fin de identificar patrones y factores demográficos y laborales que influyen en la salida de trabajadores de la empresa.

El proyecto abarca:
* Limpieza y transformación de datos
* Análisis exploratorio (EDA)
* Visualización de resultados
* Generación de *insights* accionables para RRHH

---

## Objetivos

### Objetivos de Negocio

* Identificar factores asociados a la rotación de empleados.
* Analizar el impacto de variables como edad, departamento, horas extra y satisfacción laboral.
* Apoyar la toma de decisiones estratégicas en gestión de talento.

### Objetivos de Aprendizaje

* Limpieza y preprocesamiento de datos con Python.
* Tratamiento de valores nulos, duplicados y outliers.
* Análisis estadístico descriptivo.
* Visualización efectiva de datos.
* Comunicación de resultados técnicos en lenguaje de negocio.

---

## Estructura del Proyecto

```text
proyecto-da-promo-59-modulo-3-team-2/
├── Base_Datos/
│   ├── .gitignore
│   ├── ABC_Corporation_db.ipynb
│   └── .env   (recomendación: no versionar credenciales)
├── Documentación Inicial/
│   ├── Proyecto-3 Transformando el Talento.pdf
│   ├── columnas_hr.md
│   └── hr.csv
├── Visualizaciones/
│   ├── Visual_Storytelling.ipynb
│   └── df_final.csv
├── Transformacion y limpieza.ipynb
├── Resumen ejecutivo.pdf
└── README.md
```

---

## Proceso de Análisis

### 1. Limpieza de Datos

* Eliminación de duplicados (basado en `EmployeeNumber`).  
* Tratamiento de valores nulos:  
  * Imputación por mediana para variables numéricas.  
  * Reemplazo por “Unknown” para variables categóricas.  
* Eliminación de columnas sin variabilidad relevante. 

### 2. Transformación de Datos

* Normalización de categorías (Title Case).  
* Creación de variables derivadas:  
  * `Attrition_flag`: binaria para indicar rotación.  
  * `AgeGroup`: segmentos etarios.  
* Ajuste de tipos de datos para eficiencia.

### 3. Exploración de Datos (EDA)

* Análisis univariado y bivariado.  
* Identificación de patrones en relación a rotación (edad, departamento, horas extra, satisfacción, etc.).  
* Visualización de métricas clave para stakeholders.

### 4. Creación de la Base de Datos

* Diseño de la estructura de la base de datos a partir del dataset original de RRHH.
* Organización y consolidación de la información en un dataset final limpio (`df_final.csv`).
* Preparación de los datos para su uso en análisis exploratorio y visualización.
* Almacenamiento y versionado de los archivos dentro del repositorio para garantizar trazabilidad y reproducibilidad.

---

## Resultados y Hallazgos

| Métrica | Resultado |
|---|---|
| Tasa global de rotación | 16,1% de empleados abandonan la empresa |
| Grupo de edad con mayor rotación | <30 años (28%) |
| Efecto de horas extra (OverTime) | “Sí” triplica la probabilidad de rotación |
| Satisfacción | Menores niveles asociados a mayor rotación |

**Insights de negocio clave:**
- Los empleados jóvenes y quienes realizan OverTime presentan mayor riesgo de abandono.
- La satisfacción laboral y con el entorno son predictores importantes de retención.
- Existen diferencias relevantes entre departamentos.

---

## Herramientas

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="55"/>
  &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="55"/>
  &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="55"/>
  &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg" width="55"/>
  &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/matplotlib/matplotlib-original.svg" width="55"/>
  &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="55"/>
</p>

* **Python:** Lenguaje base para análisis de datos.  
* **Pandas / NumPy:** Manipulación y cálculo numérico.  
* **Matplotlib / Seaborn:** Visualización de datos.  
* **Jupyter Notebook:** Entorno de análisis interactivo.

---

## Instalación y Ejecución

1) Clonar el repositorio:

```bash
git clone https://github.com/Ruthpsegovia/proyecto-da-promo-59-modulo-3-team-2.git
cd proyecto-da-promo-59-modulo-3-team-2
```

2) Instalar dependencias:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

3) Ejecutar los notebooks:

```bash
jupyter notebook
```

Luego abre desde el navegador:
- `Transformacion y limpieza.ipynb`
- `Visualizaciones/Visual_Storytelling.ipynb`

---

## Autoría

Proyecto desarrollado por el **Equipo 2 del Módulo 3 – Análisis de Datos** del Bootcamp de Adalab:

<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/anitaromero25-bot">
        <img src="https://github.com/anitaromero25-bot.png" width="80" height="80" style="border-radius:50%;" alt="Ana Romero"/>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/leiremarinas-sys">
        <img src="https://github.com/leiremarinas-sys.png" width="80" height="80" style="border-radius:50%;" alt="Leire Marinas"/>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Ruthpsegovia">
        <img src="https://github.com/Ruthpsegovia.png" width="80" height="80" style="border-radius:50%;" alt="Ruth Pérez"/>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/TamDb22">
        <img src="https://github.com/TamDb22.png" width="80" height="80" style="border-radius:50%;" alt="Tamara Díaz"/>
      </a>
    </td>
  </tr>
  <tr>
    <td align="center"><b>Ana Romero</b></td>
    <td align="center"><b>Leire Marinas</b></td>
    <td align="center"><b>Ruth Pérez</b></td>
    <td align="center"><b>Tamara Díaz</b></td>
  </tr>
</table>

✨ **¡Gracias por explorar nuestro análisis!** ✨
