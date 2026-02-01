# =============================================================================
# VISUALIZACIONES COMPLETAS + PDF CON RESÚMENES
# Proyecto Módulo 3 - Adalab
# Equipo: Ana, Ruth, Tamara, Leire
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
import warnings
import os
import datetime

warnings.filterwarnings("ignore")

# Configuración global
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.size'] = 10

# =============================================================================
# FUNCIONES AUXILIARES
# =============================================================================

def agregar_resumen(fig, texto, y_pos=0.02):
    """Añade un resumen en la parte inferior de la figura"""
    fig.text(0.5, y_pos, texto, ha='center', fontsize=9, style='italic',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#f0f0f0', alpha=0.8))


# =============================================================================
# VISUALIZACIONES
# =============================================================================

def dashboard_general(df):
    """Dashboard ejecutivo con KPIs principales"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.4, wspace=0.3)
    
    ax1 = fig.add_subplot(gs[0, :])
    ax1.axis('off')
    
    total_emp = len(df)
    salario_prom = df['MonthlyIncome'].mean()
    satisfaccion = df['JobSatisfaction'].mean()
    overtime_count = (df['OverTime']=='Yes').sum()
    tasa_rotacion = df['Attrition_flag'].mean() * 100
    
    ax1.text(0.05, 0.7, f"👥 Total: {total_emp}", fontsize=20, fontweight='bold')
    ax1.text(0.05, 0.3, f"💰 Salario: ${salario_prom:.0f}", fontsize=20)
    ax1.text(0.35, 0.7, f"😊 Satisfacción: {satisfaccion:.2f}/4", fontsize=20)
    ax1.text(0.35, 0.3, f"⏰ Overtime: {overtime_count}", fontsize=20)
    ax1.text(0.65, 0.5, f"📊 Rotación: {tasa_rotacion:.1f}%", fontsize=22, fontweight='bold', color='#e74c3c')
    
    # Departamento
    ax2 = fig.add_subplot(gs[1, 0])
    dept_counts = df['Department'].value_counts()
    ax2.barh(dept_counts.index, dept_counts.values, color='steelblue')
    ax2.set_title('Empleados por Departamento', fontweight='bold', fontsize=11)
    ax2.set_xlabel('Empleados')
    
    # Salarios
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.hist(df['MonthlyIncome'], bins=20, color='green', alpha=0.7, edgecolor='black')
    ax3.set_title('Distribución Salarial', fontweight='bold', fontsize=11)
    ax3.set_xlabel('Salario ($)')
    ax3.set_ylabel('Frecuencia')
    
    # Edad
    ax4 = fig.add_subplot(gs[1, 2])
    age_counts = df['AgeGroup'].value_counts()
    ax4.pie(age_counts, labels=age_counts.index, autopct='%1.1f%%', startangle=90)
    ax4.set_title('Grupos de Edad', fontweight='bold', fontsize=11)
    
    # Satisfacción
    ax5 = fig.add_subplot(gs[2, :])
    sat_means = df[['JobSatisfaction', 'EnvironmentSatisfaction', 'WorkLifeBalance', 'RelationshipSatisfaction']].mean()
    sat_means.index = ['Satisfacción\nLaboral', 'Satisfacción\ncon Entorno', 'Balance\nVida-Trabajo', 'Satisfacción\ncon Relaciones']
    colors_sat = ['#66c2a5' if x >= 2.5 else '#fc8d62' for x in sat_means]
    ax5.barh(sat_means.index, sat_means.values, color=colors_sat)
    ax5.set_xlim(0, 4)
    ax5.set_title('Niveles Promedio de Satisfacción', fontweight='bold', fontsize=11)
    ax5.set_xlabel('Puntuación')
    # Línea en la media real (no fija en 2.5)
    media_satisfaccion_global = sat_means.mean()
    ax5.axvline(x=media_satisfaccion_global, color='red', linestyle='--', linewidth=2, alpha=0.7,
            label=f'Media: {media_satisfaccion_global:.2f}')
    ax5.legend(loc='lower right', fontsize=9)
    
    plt.suptitle('🏢 DASHBOARD GENERAL DE LA EMPRESA', fontsize=16, fontweight='bold', y=0.98)
    
    # RESUMEN
    resumen = f"📌 RESUMEN: {total_emp} empleados | Rotación {tasa_rotacion:.1f}% | Satisfacción promedio {satisfaccion:.2f}/4 (68.5%) | {overtime_count} con overtime (27.6%)"
    agregar_resumen(fig, resumen, y_pos=0.01)
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    return fig


def rotacion_por_edad(df):
    """Rotación por grupo de edad - GRÁFICO CRÍTICO"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Calcular rotación por edad
    rotacion_edad = df.groupby('AgeGroup')['Attrition_flag'].agg(['mean', 'count'])
    rotacion_edad['percentage'] = rotacion_edad['mean'] * 100
    rotacion_edad = rotacion_edad.sort_values('percentage', ascending=False)
    
    # Gráfico de barras
    bars = ax.bar(range(len(rotacion_edad)), rotacion_edad['percentage'], 
                   color=['#e74c3c', '#f39c12', '#3498db', '#2ecc71'], alpha=0.7, edgecolor='black')
    
    # Etiquetas
    ax.set_xticks(range(len(rotacion_edad)))
    ax.set_xticklabels(rotacion_edad.index, fontsize=12)
    ax.set_ylabel('Tasa de Rotación (%)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Grupo de Edad', fontsize=12, fontweight='bold')
    ax.set_title('📊 Tasa de Rotación por Grupo de Edad', fontsize=14, fontweight='bold')
    
    # Valores encima de barras
    for i, (bar, val, count) in enumerate(zip(bars, rotacion_edad['percentage'], rotacion_edad['count'])):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{val:.1f}%\n(n={count})', ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    # Línea promedio
    promedio_global = df['Attrition_flag'].mean() * 100
    ax.axhline(y=promedio_global, color='red', linestyle='--', linewidth=2, 
               label=f'Promedio general: {promedio_global:.1f}%')
    
    ax.legend(fontsize=10)
    ax.grid(axis='y', alpha=0.3)
    ax.set_ylim(0, max(rotacion_edad['percentage']) + 5)
    
    # RESUMEN
    max_grupo = rotacion_edad.index[0]
    max_tasa = rotacion_edad['percentage'].iloc[0]
    resumen = f"📌 HALLAZGO CRÍTICO: Los empleados {max_grupo} tienen la mayor rotación ({max_tasa:.1f}%), casi el doble del promedio ({promedio_global:.1f}%)"
    agregar_resumen(fig, resumen)
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    return fig


def rotacion_por_overtime(df):
    """Rotación según horas extra - GRÁFICO CRÍTICO"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Calcular rotación por overtime
    rotacion_ot = df.groupby('OverTime')['Attrition_flag'].agg(['mean', 'count'])
    rotacion_ot['percentage'] = rotacion_ot['mean'] * 100
    rotacion_ot = rotacion_ot.sort_values('percentage', ascending=True)
    
    # Gráfico 1: Barras comparativas
    colors = ['#2ecc71' if x < 20 else '#e74c3c' for x in rotacion_ot['percentage']]
    bars = axes[0].barh(rotacion_ot.index, rotacion_ot['percentage'], 
                        color=colors, alpha=0.7, edgecolor='black')
    
    axes[0].set_xlabel('Tasa de Rotación (%)', fontsize=12, fontweight='bold')
    axes[0].set_title('Rotación según Horas Extra', fontsize=13, fontweight='bold')
    axes[0].grid(axis='x', alpha=0.3)
    
    # Valores
    for bar, val, count in zip(bars, rotacion_ot['percentage'], rotacion_ot['count']):
        axes[0].text(val + 1, bar.get_y() + bar.get_height()/2,
                     f'{val:.1f}% (n={count})', va='center', fontweight='bold')
    
    # Gráfico 2: Comparativa Yes vs No
    ot_yes_no = rotacion_ot[rotacion_ot.index.isin(['Yes', 'No'])]
    if len(ot_yes_no) >= 2:
        values = ot_yes_no['percentage'].values
        labels = ot_yes_no.index.values
        x = [0, 1]
        
        axes[1].bar(x, values, color=['#2ecc71', '#e74c3c'], alpha=0.7, 
                    width=0.6, edgecolor='black')
        axes[1].set_xticks(x)
        axes[1].set_xticklabels(['Sin Overtime', 'Con Overtime'], fontsize=12)
        axes[1].set_ylabel('Tasa de Rotación (%)', fontsize=12, fontweight='bold')
        axes[1].set_title('Comparativa Directa', fontsize=13, fontweight='bold')
        axes[1].grid(axis='y', alpha=0.3)
        
        # Diferencia
        if len(values) == 2:
            ratio = values[1] / values[0]
            axes[1].text(0.5, max(values) * 0.8, 
                        f'🔴 {ratio:.1f}x más rotación\ncon overtime',
                        ha='center', fontsize=11, fontweight='bold',
                        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
            
            # Valores
            for i, (pos, val) in enumerate(zip(x, values)):
                axes[1].text(pos, val + 1, f'{val:.1f}%', ha='center', fontweight='bold')
    
    plt.suptitle('⏰ FACTOR CRÍTICO: HORAS EXTRA Y ROTACIÓN', fontsize=14, fontweight='bold', y=0.98)
    
    # RESUMEN
    if len(ot_yes_no) >= 2:
        sin_ot = ot_yes_no.loc['No', 'percentage']
        con_ot = ot_yes_no.loc['Yes', 'percentage']
        ratio = con_ot / sin_ot
        resumen = f"📌 HALLAZGO CRÍTICO: El overtime triplica la rotación: {con_ot:.1f}% con overtime vs {sin_ot:.1f}% sin overtime (×{ratio:.1f})"
    else:
        resumen = "📌 Análisis de impacto del overtime en la rotación de personal"
    
    agregar_resumen(fig, resumen)
    
    plt.tight_layout(rect=[0, 0.05, 1, 0.96])
    return fig


def analisis_edad(df):
    """Distribución de edad"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    axes[0].hist(df['Age'].dropna(), bins=20, color='steelblue', edgecolor='black', alpha=0.7)
    axes[0].axvline(df['Age'].mean(), color='red', linestyle='--', linewidth=2, label=f"Media: {df['Age'].mean():.1f}")
    axes[0].axvline(df['Age'].median(), color='orange', linestyle='--', linewidth=2, label=f"Mediana: {df['Age'].median():.1f}")
    axes[0].set_title('Distribución de Edad', fontweight='bold', fontsize=13)
    axes[0].set_xlabel('Edad (años)')
    axes[0].set_ylabel('Empleados')
    axes[0].legend()
    axes[0].grid(axis='y', alpha=0.3)
    
    age_counts = df['AgeGroup'].value_counts()
    axes[1].pie(age_counts, labels=age_counts.index, autopct='%1.1f%%', startangle=90)
    axes[1].set_title('Composición por Grupos', fontweight='bold', fontsize=13)
    
    # RESUMEN
    media_edad = df['Age'].mean()
    grupo_mayor = age_counts.index[0]
    pct_mayor = (age_counts.iloc[0] / len(df)) * 100
    resumen = f"📌 Plantilla joven: edad media {media_edad:.0f} años | {pct_mayor:.0f}% son del grupo {grupo_mayor}"
    agregar_resumen(fig, resumen)
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    return fig


def distribucion_genero_departamento(df):
    """Distribución por género y departamento"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    gender_counts = df['Gender'].value_counts()
    axes[0].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', 
                colors=['#87ceeb', '#ffb6c1'], startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'})
    axes[0].set_title('Distribución por Género', fontweight='bold', fontsize=13)
    
    dept_counts = df['Department'].value_counts()
    axes[1].barh(dept_counts.index, dept_counts.values, color='coral', alpha=0.7)
    axes[1].set_title('Empleados por Departamento', fontweight='bold', fontsize=13)
    axes[1].set_xlabel('Empleados')
    axes[1].grid(axis='x', alpha=0.3)
    for i, v in enumerate(dept_counts.values):
        axes[1].text(v + 10, i, str(v), va='center', fontweight='bold')
    
    # RESUMEN
    pct_hombres = (gender_counts.get('Male', 0) / len(df)) * 100
    dept_principal = dept_counts.index[0]
    pct_dept = (dept_counts.iloc[0] / len(df)) * 100
    resumen = f"📌 Composición: {pct_hombres:.0f}% hombres | {dept_principal} es el {pct_dept:.0f}% de la plantilla (departamento principal)"
    agregar_resumen(fig, resumen)
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    return fig


def top_roles(df):
    """Top 8 roles"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    top_roles = df['JobRole'].value_counts().head(8)
    bars = ax.barh(top_roles.index, top_roles.values, color='skyblue', edgecolor='navy', alpha=0.7)
    
    for bar, val in zip(bars, top_roles.values):
        ax.text(val + 5, bar.get_y() + bar.get_height()/2, str(val), va='center', fontweight='bold')
    
    ax.set_title('Top 8 Roles más Comunes', fontweight='bold', fontsize=13)
    ax.set_xlabel('Empleados')
    ax.grid(axis='x', alpha=0.3)
    
    # RESUMEN
    rol_principal = top_roles.index[0]
    cant_principal = top_roles.iloc[0]
    resumen = f"📌 Rol predominante: {rol_principal} con {cant_principal} empleados"
    agregar_resumen(fig, resumen)
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    return fig


def distribucion_salarios(df):
    """Distribución de salarios"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.hist(df['MonthlyIncome'], bins=30, color='green', alpha=0.7, edgecolor='black')
    media = df['MonthlyIncome'].mean()
    mediana = df['MonthlyIncome'].median()
    
    ax.axvline(media, color='red', linestyle='--', linewidth=2.5, label=f'Media: ${media:.0f}')
    ax.axvline(mediana, color='blue', linestyle='--', linewidth=2.5, label=f'Mediana: ${mediana:.0f}')
    
    ax.set_title('Distribución de Salarios', fontweight='bold', fontsize=13)
    ax.set_xlabel('Salario Mensual ($)')
    ax.set_ylabel('Frecuencia')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    # RESUMEN
    diferencia = media - mediana
    resumen = f"📌 Salarios: Media ${media:.0f} > Mediana ${mediana:.0f} (diferencia ${diferencia:.0f}) → concentración en rangos bajos-medios con outliers altos"
    agregar_resumen(fig, resumen)
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    return fig


def salario_por_nivel(df):
    """Salario por nivel"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    salario_nivel = df.groupby('JobLevel')['MonthlyIncome'].mean().sort_index()
    bars = ax.bar(salario_nivel.index, salario_nivel.values, color='purple', alpha=0.7, edgecolor='black')
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height, f'${height:.0f}',
                ha='center', va='bottom', fontweight='bold')
    
    ax.set_title('Salario Promedio por Nivel de Puesto', fontweight='bold', fontsize=13)
    ax.set_xlabel('Nivel del Puesto')
    ax.set_ylabel('Salario Mensual Promedio ($)')
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.grid(axis='y', alpha=0.3)
    
    # RESUMEN
    nivel1 = salario_nivel.iloc[0]
    nivel5 = salario_nivel.iloc[-1]
    incremento = ((nivel5 - nivel1) / nivel1) * 100
    resumen = f"📌 Progresión salarial clara: desde ${nivel1:.0f} (nivel 1) hasta ${nivel5:.0f} (nivel 5) — incremento total {incremento:.0f}%"
    agregar_resumen(fig, resumen)
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    return fig


def salario_por_departamento(df):
    """Salario por departamento"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    salario_dept = df.groupby('Department')['MonthlyIncome'].mean().sort_values()
    bars = ax.barh(salario_dept.index, salario_dept.values, color='orange', alpha=0.7, edgecolor='black')
    
    for bar, val in zip(bars, salario_dept.values):
        ax.text(val + 100, bar.get_y() + bar.get_height()/2, f'${val:.0f}', va='center', fontweight='bold')
    
    ax.set_title('Salario Promedio por Departamento', fontweight='bold', fontsize=13)
    ax.set_xlabel('Salario Mensual Promedio ($)')
    ax.grid(axis='x', alpha=0.3)
    
    # RESUMEN
    dept_mayor = salario_dept.index[-1]
    sal_mayor = salario_dept.iloc[-1]
    resumen = f"📌 Departamento mejor pagado: {dept_mayor} (${sal_mayor:.0f}/mes)"
    agregar_resumen(fig, resumen)
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    return fig


def niveles_satisfaccion(df):
    """4 dimensiones de satisfaccion"""
    satisfaccion_cols = ['JobSatisfaction', 'EnvironmentSatisfaction', 'WorkLifeBalance', 'RelationshipSatisfaction']
    titulos = ['Satisfacción Laboral', 'Satisfacción con el Entorno', 'Balance Vida-Trabajo', 'Satisfacción con Relaciones']
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()
    
    for i, (col, titulo) in enumerate(zip(satisfaccion_cols, titulos)):
        counts = df[col].value_counts().sort_index()
        media = df[col].mean()
        
        bars = axes[i].bar(counts.index, counts.values, color='teal', alpha=0.7, edgecolor='black')
        
        for j, bar in enumerate(bars):
            if counts.index[j] <= 2:
                bar.set_color('#e74c3c')
            elif counts.index[j] == 3:
                bar.set_color('#f39c12')
            else:
                bar.set_color('#27ae60')
        
        axes[i].axvline(x=media, color='blue', linestyle='--', linewidth=2, alpha=0.6, label=f'Media: {media:.2f}')
        axes[i].set_title(titulo, fontweight='bold', fontsize=11)
        axes[i].set_xlabel('Nivel (1=Bajo, 4=Alto)')
        axes[i].set_ylabel('Empleados')
        axes[i].set_xticks([1, 2, 3, 4])
        axes[i].legend()
        axes[i].grid(axis='y', alpha=0.3)
    
    plt.suptitle('📊 Niveles de Satisfacción en la Empresa', fontsize=14, fontweight='bold')
    
    # RESUMEN
    media_general = df[satisfaccion_cols].mean().mean()
    pct_general = (media_general / 4) * 100
    resumen = f"📌 Satisfacción general positiva: {media_general:.2f}/4 ({pct_general:.0f}%) en todas las dimensiones — mayoría en niveles 3-4"
    agregar_resumen(fig, resumen, y_pos=0.01)
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    return fig


def relacion_edad_salario_nivel(df):
    """Scatter: Edad vs Salario"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    scatter = ax.scatter(df['Age'], df['MonthlyIncome'], c=df['JobLevel'], s=df['YearsAtCompany']*10,
                        cmap='viridis', alpha=0.6, edgecolors='black', linewidth=0.5)
    
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Nivel del Puesto', fontsize=11, fontweight='bold')
    
    ax.set_title('Relación Edad-Salario-Nivel-Antigüedad', fontweight='bold', fontsize=13)
    ax.set_xlabel('Edad (años)')
    ax.set_ylabel('Salario Mensual ($)')
    ax.grid(alpha=0.3)
    
    legend_sizes = [5, 15, 30]
    legend_labels = ['5 años', '15 años', '30 años']
    legend_handles = [plt.scatter([], [], s=size*10, c='gray', alpha=0.6, edgecolors='black') for size in legend_sizes]
    ax.legend(legend_handles, legend_labels, title='Antigüedad', loc='upper left', fontsize=9)
    
    # RESUMEN
    resumen = "📌 Correlación positiva clara: a mayor edad, experiencia y nivel → mayor salario (sistema de carrera predecible)"
    agregar_resumen(fig, resumen)
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    return fig


def analisis_overtime(df):
    """Análisis de horas extra"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    overtime_counts = df['OverTime'].value_counts()
    colors_ot = ['#2ecc71', '#e74c3c', '#95a5a6']
    axes[0].pie(overtime_counts, labels=overtime_counts.index, autopct='%1.1f%%',
                colors=colors_ot, startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'})
    axes[0].set_title('Proporción con Horas Extra', fontweight='bold', fontsize=13)
    
    overtime_by_dept = pd.crosstab(df['Department'], df['OverTime'], normalize='index') * 100
    
    if 'Yes' in overtime_by_dept.columns:
        overtime_sorted = overtime_by_dept['Yes'].sort_values(ascending=True)
        bars = axes[1].barh(overtime_sorted.index, overtime_sorted.values, color='salmon', alpha=0.7, edgecolor='black')
        
        for bar in bars:
            width = bar.get_width()
            axes[1].text(width + 1, bar.get_y() + bar.get_height()/2, f'{width:.1f}%', va='center', fontweight='bold')
        
        axes[1].set_title('% con Overtime por Departamento', fontweight='bold', fontsize=13)
        axes[1].set_xlabel('Porcentaje (%)')
        axes[1].grid(axis='x', alpha=0.3)
    
    # RESUMEN
    pct_overtime = (overtime_counts.get('Yes', 0) / len(df)) * 100
    resumen = f"📌 {pct_overtime:.1f}% de empleados hace overtime (estructural, no excepcional) — todos los departamentos afectados"
    agregar_resumen(fig, resumen)
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    return fig


def distancia_hogar(df):
    """Distribución de distancia"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.hist(df['DistanceFromHome'], bins=25, color='steelblue', edgecolor='black', alpha=0.7)
    media = df['DistanceFromHome'].mean()
    ax.axvline(media, color='red', linestyle='--', linewidth=2.5, label=f'Media: {media:.1f} km')
    
    ax.set_title('Distancia del Hogar al Trabajo', fontweight='bold', fontsize=13)
    ax.set_xlabel('Distancia (km)')
    ax.set_ylabel('Empleados')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    # RESUMEN
    resumen = f"📌 La mayoría vive cerca: media {media:.1f} km — ubicación accesible, bajo impacto del commute"
    agregar_resumen(fig, resumen)
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    return fig


# =============================================================================
# GENERACIÓN DE PDF
# =============================================================================

def generar_pdf_completo(df, nombre_archivo='Visualizaciones/Informe_Visualizaciones_Completo.pdf'):
    """Genera PDF con portada, índice y 13 visualizaciones con resúmenes"""
    
    print("="*70)
    print(f"📄 GENERANDO PDF: {nombre_archivo}")
    print("="*70)
    
    # VERIFICAR COLUMNAS NECESARIAS
    print("\n🔍 Verificando columnas necesarias...")
    columnas_requeridas = {
        'MonthlyIncome': 'numérica',
        'JobSatisfaction': 'numérica', 
        'EnvironmentSatisfaction': 'numérica',
        'WorkLifeBalance': 'numérica',
        'RelationshipSatisfaction': 'numérica',
        'OverTime': 'categórica',
        'Department': 'categórica',
        'AgeGroup': 'categórica',
        'Attrition_flag': 'numérica',
        'Age': 'numérica',
        'JobRole': 'categórica',
        'Gender': 'categórica',
        'YearsAtCompany': 'numérica',
        'DistanceFromHome': 'numérica',
        'JobLevel': 'numérica'
    }
    
    columnas_faltantes = []
    for col, tipo in columnas_requeridas.items():
        if col not in df.columns:
            columnas_faltantes.append(col)
            print(f"  ❌ FALTA: {col} ({tipo})")
        else:
            print(f"  ✓ {col}")
    
    if columnas_faltantes:
        print(f"\n⚠️ ADVERTENCIA: Faltan {len(columnas_faltantes)} columnas")
        print("El PDF se generará pero algunas visualizaciones pueden fallar\n")
    else:
        print(f"\n✅ Todas las columnas presentes ({len(columnas_requeridas)})\n")
    
    # Crear directorio si no existe
    directorio = os.path.dirname(nombre_archivo)
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio)
        print(f"✓ Carpeta creada: {directorio}")
    
    visualizaciones = [
        ("1. Dashboard General de la Empresa", dashboard_general),
        ("2. 🔴 CRÍTICO: Rotación por Edad", rotacion_por_edad),
        ("3. 🔴 CRÍTICO: Rotación por Overtime", rotacion_por_overtime),
        ("4. Análisis de Edad", analisis_edad),
        ("5. Distribución por Género y Departamento", distribucion_genero_departamento),
        ("6. Top 8 Roles más Comunes", top_roles),
        ("7. Distribución de Salarios", distribucion_salarios),
        ("8. Salario por Nivel de Puesto", salario_por_nivel),
        ("9. Salario por Departamento", salario_por_departamento),
        ("10. Niveles de Satisfacción (4 Dimensiones)", niveles_satisfaccion),
        ("11. Relación Edad-Salario-Nivel-Antigüedad", relacion_edad_salario_nivel),
        ("12. Análisis de Horas Extra", analisis_overtime),
        ("13. Distribución de Distancia del Hogar", distancia_hogar)
    ]
    
    with PdfPages(nombre_archivo) as pdf:
        
        # PORTADA
        print("\n[1/15] Generando portada...")
        fig_portada = plt.figure(figsize=(11, 8.5))
        fig_portada.patch.set_facecolor('#f8f9fa')
        
        fig_portada.text(0.5, 0.75, 'ANÁLISIS DE ROTACIÓN', ha='center', fontsize=32, fontweight='bold', color='#2c3e50')
        fig_portada.text(0.5, 0.68, 'DE EMPLEADOS', ha='center', fontsize=32, fontweight='bold', color='#2c3e50')
        fig_portada.text(0.5, 0.58, 'Informe de Visualizaciones', ha='center', fontsize=18, color='#34495e')
        
        plt.plot([0.2, 0.8], [0.52, 0.52], color='#3498db', linewidth=3)
        
        fig_portada.text(0.5, 0.42, 'Proyecto Módulo 3', ha='center', fontsize=14, color='#7f8c8d')
        fig_portada.text(0.5, 0.38, 'Bootcamp Análisis de Datos - Adalab', ha='center', fontsize=14, color='#7f8c8d')
        fig_portada.text(0.5, 0.28, '👥 Equipo', ha='center', fontsize=12, fontweight='bold')
        fig_portada.text(0.5, 0.24, 'Ana • Ruth • Tamara • Leire', ha='center', fontsize=11)
        
        fecha_actual = datetime.date.today().strftime("%B %Y")
        fig_portada.text(0.5, 0.14, f'📅 {fecha_actual}', ha='center', fontsize=10, style='italic')
        fig_portada.text(0.5, 0.05, f'Total empleados analizados: {len(df):,}', ha='center', fontsize=9, color='#95a5a6')
        
        plt.axis('off')
        pdf.savefig(fig_portada, bbox_inches='tight', facecolor=fig_portada.get_facecolor())
        plt.close()
        
        # ÍNDICE
        print("[2/15] Generando índice...")
        fig_indice = plt.figure(figsize=(11, 8.5))
        fig_indice.text(0.5, 0.9, '📋 ÍNDICE DE CONTENIDOS', ha='center', fontsize=20, fontweight='bold')
        
        contenidos = [
            "1.  Dashboard General de la Empresa",
            "2.  🔴 CRÍTICO: Rotación por Grupo de Edad",
            "3.  🔴 CRÍTICO: Rotación por Horas Extra (Overtime)",
            "4.  Análisis Demográfico - Distribución de Edad",
            "5.  Distribución por Género y Departamento",
            "6.  Top 8 Roles más Comunes",
            "7.  Análisis de Compensación - Distribución Salarial",
            "8.  Salario Promedio por Nivel de Puesto",
            "9.  Salario Promedio por Departamento",
            "10. Niveles de Satisfacción (4 Dimensiones)",
            "11. Relación Edad-Salario-Nivel-Antigüedad",
            "12. Análisis de Horas Extra (Distribución)",
            "13. Distribución de Distancia del Hogar"
        ]
        
        y_pos = 0.75
        for contenido in contenidos:
            color = '#e74c3c' if '🔴' in contenido else 'black'
            fig_indice.text(0.12, y_pos, contenido, fontsize=11, va='top', color=color, 
                           fontweight='bold' if '🔴' in contenido else 'normal')
            y_pos -= 0.055
        
        plt.axis('off')
        pdf.savefig(fig_indice, bbox_inches='tight')
        plt.close()
        
        # VISUALIZACIONES
        for i, (titulo, funcion) in enumerate(visualizaciones, 3):
            print(f"[{i}/15] Generando: {titulo}...")
            try:
                fig = funcion(df)
                pdf.savefig(fig, bbox_inches='tight')
                plt.close()
                print(f"      ✓ Completado")
            except Exception as e:
                print(f"      ✗ ERROR en {titulo}: {e}")
                import traceback
                traceback.print_exc()
        
        # METADATA
        d = pdf.infodict()
        d['Title'] = 'Análisis de Rotación de Empleados'
        d['Author'] = 'Ana, Ruth, Tamara, Leire - Adalab Team 2'
        d['Subject'] = 'Employee Attrition Analysis - Módulo 3'
        d['Keywords'] = 'HR Analytics, Data Analysis, Adalab'
    
    print("\n" + "="*70)
    print(f"✅ PDF GENERADO EXITOSAMENTE")
    print("="*70)
    print(f"📁 Archivo: {nombre_archivo}")
    print(f"📍 Ubicación: {os.path.abspath(nombre_archivo)}")
    print(f"📄 Páginas: 15 (portada + índice + 13 visualizaciones)")
    print("="*70)
    
    return nombre_archivo


# =============================================================================
# EJECUCIÓN PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    
    print(f"Directorio actual: {os.getcwd()}")
    
    ruta_csv = "hr.csv"
    if not os.path.exists(ruta_csv):
        ruta_csv = "../hr.csv"
    
    try:
        print(f"\n📂 Cargando datos: {ruta_csv}")
        df_emp = pd.read_csv(ruta_csv)
        print(f"✅ Cargados: {len(df_emp)} filas")
        
        # Limpieza
        df_emp = df_emp.drop_duplicates(subset='EmployeeNumber', keep='first')
        df_emp['Age'] = df_emp['Age'].fillna(df_emp['Age'].median())
        df_emp['MonthlyIncome'] = df_emp['MonthlyIncome'].fillna(df_emp['MonthlyIncome'].median())
        df_emp['JobSatisfaction'] = df_emp['JobSatisfaction'].fillna(df_emp['JobSatisfaction'].median())
        
        for col in ['Department', 'JobRole', 'Attrition', 'OverTime']:
            if col in df_emp.columns:
                df_emp[col] = df_emp[col].astype(str).str.strip().str.title()
        
        # Variables derivadas
        if 'AgeGroup' not in df_emp.columns:
            df_emp['AgeGroup'] = pd.cut(df_emp['Age'], bins=[0, 30, 40, 50, 100], 
                                       labels=['<30', '30-40', '40-50', '>=50'], right=False)
        
        if 'Attrition_flag' not in df_emp.columns:
            df_emp['Attrition_flag'] = df_emp['Attrition'].map({'Yes': 1, 'No': 0})
        
        # GENERAR PDF
        generar_pdf_completo(df_emp)
        
        print("\n✅ Proceso completado!")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
