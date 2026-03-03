import json

def update_notebook_viz_churn():
    file_path = "d:\\pc\\Documents\\telecomx\\telecomx.ipynb"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
        
    new_cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 8. Análisis de la Variable Objetivo (Evasión / Churn)\n",
                "\n",
                "El primer paso en la exploración visual es entender nuestro problema principal: ¿Cuántos clientes se están yendo frente a los que se quedan? \n",
                "Para esto, utilizaremos las librerías `matplotlib` y `seaborn` para crear gráficos de barras y de pastel."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "\n",
                "# Configuración visual general para que los gráficos se vean modernos y limpios\n",
                "sns.set_theme(style=\"whitegrid\")\n",
                "plt.rcParams['figure.figsize'] = (10, 5)\n",
                "colores = [\"#2ecc71\", \"#e74c3c\"] # Verde (Permanece), Rojo (Evasión)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "print(\"--- DISTRIBUCIÓN DE EVASIÓN (CHURN) ---\")\n",
                "\n",
                "fig, axes = plt.subplots(1, 2, figsize=(14, 6))\n",
                "fig.suptitle(\"Análisis de Retención vs Evasión de Clientes\", fontsize=16, fontweight='bold')\n",
                "\n",
                "# GRÁFICO 1: Gráfico de barras (Conteo absoluto)\n",
                "sns.countplot(data=df, x='Evasion', palette=colores, ax=axes[0])\n",
                "axes[0].set_title(\"Cantidad de Clientes por Estado\", fontsize=14)\n",
                "axes[0].set_xlabel(\"Evasión (0 = No, 1 = Sí)\", fontsize=12)\n",
                "axes[0].set_ylabel(\"Número de Clientes\", fontsize=12)\n",
                "\n",
                "# Agregar las etiquetas de datos sobre las barras\n",
                "for p in axes[0].patches:\n",
                "    axes[0].annotate(f'{int(p.get_height())}', \n",
                "                     (p.get_x() + p.get_width() / 2., p.get_height()), \n",
                "                     ha = 'center', va = 'bottom', \n",
                "                     fontsize=11)\n",
                "    \n",
                "# GRÁFICO 2: Gráfico de Pastel (Proporción relativa)\n",
                "evasion_counts = df['Evasion'].value_counts()\n",
                "axes[1].pie(evasion_counts, \n",
                "            labels=[\"Permanecen (0)\", \"Se dan de baja (1)\"], \n",
                "            autopct='%1.1f%%', \n",
                "            startangle=90, \n",
                "            colors=colores, \n",
                "            explode=(0, 0.1),  # Separar un poco el 'Sí' para resaltarlo\n",
                "            shadow=True)\n",
                "axes[1].set_title(\"Proporción de Evasión\", fontsize=14)\n",
                "\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Conclusiones del Gráfico:\n",
                "Este gráfico de pastel y barras revela el desbalance de nuestro dataset. Notarás que la proporción de personas que se han ido (alrededor del 26%) es considerablemente menor a las que se quedan. Esto se llama **clases desbalanceadas** en Machine Learning, algo vital de considerar al entrenar modelos predictivos para que no se sesguen a predecir siempre que el cliente se queda."
            ]
        }
    ]
    
    notebook["cells"].extend(new_cells)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)

if __name__ == "__main__":
    update_notebook_viz_churn()
