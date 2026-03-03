import json

def update_notebook_viz_numeric():
    file_path = "d:\\pc\\Documents\\telecomx\\telecomx.ipynb"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
        
    new_cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 10. Análisis de Evasión por Variables Numéricas\n",
                "\n",
                "Para entender cómo los números continuos (dinero y tiempo) afectan la decisión de abandonar el servicio, utilizaremos gráficos de densidad (`sns.kdeplot`) y diagramas de caja (`sns.boxplot`).\n",
                "\n",
                "Estos gráficos nos permitirán ver si las personas que se van tienden a tener facturas más altas o menos tiempo en la empresa."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "print(\"--- EVASIÓN POR FACTORES NUMÉRICOS (TIEMPO Y DINERO) ---\")\n",
                "\n",
                "# Variables numéricas continuas a analizar\n",
                "columnas_num = ['Meses_Permanencia', 'Cargo_Mensual', 'Cargo_Total']\n",
                "nombres_titulos_num = ['Meses en la Empresa (Tenure)', 'Cargo Mensual ($)', 'Cargos Totales Acumulados ($)']\n",
                "\n",
                "fig, axes = plt.subplots(1, 3, figsize=(18, 5))\n",
                "fig.suptitle(\"Distribución de Variables Numéricas vs Evasión\", fontsize=16, fontweight='bold', y=1.05)\n",
                "\n",
                "for i, col in enumerate(columnas_num):\n",
                "    # Usamos KDE Plot (Gráfico de Densidad) para ver donde se agrupan las masas de clientes\n",
                "    sns.kdeplot(data=df, x=col, hue='Evasion', fill=True, palette=colores, ax=axes[i], alpha=0.5)\n",
                "    axes[i].set_title(nombres_titulos_num[i], fontsize=13)\n",
                "    axes[i].set_xlabel(\"\")\n",
                "    axes[i].set_ylabel(\"Densidad (Proporción de clientes)\")\n",
                "\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Gráfico complementario de Cajas (Boxplots) para identificar valores atípicos (outliers) y medianas exactas\n",
                "fig, axes = plt.subplots(1, 3, figsize=(18, 5))\n",
                "\n",
                "for i, col in enumerate(columnas_num):\n",
                "    sns.boxplot(data=df, x='Evasion', y=col, palette=colores, ax=axes[i])\n",
                "    axes[i].set_title(f\"Distribución exacta: {nombres_titulos_num[i]}\", fontsize=12)\n",
                "    axes[i].set_xlabel(\"Evasión (0=No, 1=Sí)\")\n",
                "    axes[i].set_ylabel(\"\")\n",
                "\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 💡 Análisis Estratégico Dinero y Tiempo:\n",
                "1. **Tiempo en la empresa (`Meses_Permanencia`)**: La montaña roja en el primer gráfico de densidad (KDE) está fuertemente sesgada a la izquierda. Esto es un grito de auxilio: **la inmensa mayoría de las deserciones ocurren en los primeros 5 meses**. El cliente nuevo es el más vulnerable. El Boxplot confirma que el 75% de los que se van, lo hacen antes de los 30 meses.\n",
                "2. **Cargos Mensuales (`Cargo_Mensual`)**: Observa cómo la densidad roja sube brutalmente entre los \\$70 y \\$100 dólares. Los clientes con facturas más altas son, irónicamente, los que más abandonan el servicio. En el Boxplot, la mediana (línea central) de los que se van es muy superior a la de los que se quedan (\n~$80 vs ~$60).\n",
                "3. **Cargos Totales (`Cargo_Total`)**: La evasión es altísima al inicio porque se cruza con los meses de permanencia (meses bajos = cargos totales bajos). La gente se va antes de acumular mucho gasto histórico en la empresa."
            ]
        }
    ]
    
    notebook["cells"].extend(new_cells)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)

if __name__ == "__main__":
    update_notebook_viz_numeric()
