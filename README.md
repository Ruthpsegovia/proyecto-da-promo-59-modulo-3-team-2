<h1 align="center">Proyecto de Data Analytics — Análisis de Rotación de Empleados</h1>

<p align="center">
  Bootcamp de Data Analytics & IA — Adalab.
</p>

<p align="center">
  <img src="Logo el dato incomodo.jpg" width="300" alt="Análisis de Rotación de Empleados">
</p>

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

```
proyecto-da-promo-59-modulo-3-team-2/
│
├── Base_Datos/
│   ├── .env
│   ├── .gitignore
│   ├── ABC_Corporation_db.ipynb
│   ├── df_final.csv
│
├── Documentación Inicial/
│   ├── columnas_hr.md
│   ├── hr.csv
│   └── Proyecto-3 Transformando el Talento.pdf
│
├── Visualizaciones/
│   ├── visualizaciones_LIMPIO.py
│   └── Informe_Visualizaciones_Completo.pdf
│
├── README.md
├── RESUMEN_EJECUTIVO.md
└── INSIGHTS_PRINCIPALES.md
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

---

## Resultados y Hallazgos

| Métrica | Resultado |
|---------|-----------|
| Tasa global de rotación | **16.1%** de empleados abandonan la empresa. |
| Grupo de Edad con mayor rotación | **<30 años** (28%). |
| Efecto de horas extra | **Sí** triplica la probabilidad de rotación. |
| Satisfacción | Menores niveles asociados a mayor rotación. |

**Insights de negocio clave:**

* Los empleados jóvenes y los que realizan *OverTime* presentan mayor riesgo de abandonar.  
* La satisfacción laboral y con el entorno son predictores importantes de retención.  
* Diferencias significativas entre departamentos. 

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

1. **Clonar el repositorio:**
    ```bash
    git clone https://github.com/anitaromero25-bot/proyecto-da-promo-59-modulo-3-team-2.git
    ```
2. **Instalar dependencias:**
    ```bash
    pip install pandas numpy matplotlib seaborn jupyter
    ```
3. **Ejecutar el Notebook:**
    ```bash
    jupyter notebook proyecto_mod_3_team_2.ipynb
    ```
4. **Generar el informe de visualizaciones (PDF):**
    ```bash
    python Visualizaciones/visualizaciones_LIMPIO.py
    ```

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
        <img src="https://github.com/Ruthpsegovia.png" width="80" height="80" style="border-radius:50%;" alt="Ruth Perez"/>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/TamDb22">
        <img src="https://github.com/TamDb22.png" width="80" height="80" style="border-radius:50%;" alt="Tamara Diaz"/>
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
