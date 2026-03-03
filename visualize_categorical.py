import json

def update_notebook_viz_categorical():
    file_path = "d:\\pc\\Documents\\telecomx\\telecomx.ipynb"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
        
    new_cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 9. Análisis de Evasión por Variables Categóricas\n",
                "\n",
                "Ahora cruzaremos nuestra variable objetivo (`Evasion`) contra variables categóricas clave (Tipo de Contrato, Servicio de Internet, Método de Pago, etc.) para buscar patrones. \n",
                "\n",
                "Utilizaremos `sns.countplot` separando los colores mediante el parámetro `hue=\"Evasion\"`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "print(\"--- EVASIÓN POR PERFIL DEL CLIENTE ---\")\n",
                "\n",
                "# Variables a analizar\n",
                "columnas_cat = ['Tipo_Contrato', 'Servicio_Internet', 'Metodo_Pago', 'Adulto_Mayor']\n",
                "nombres_titulos = ['Tipo de Contrato', 'Servicio de Internet', 'Método de Pago', 'Adulto Mayor (1=Sí)']\n",
                "\n",
                "fig, axes = plt.subplots(2, 2, figsize=(16, 12))\n",
                "fig.suptitle(\"Patrones de Evasión según Características del Servicio y Cliente\", fontsize=18, fontweight='bold', y=1.02)\n",
                "\n",
                "axes = axes.flatten() # Para iterar fácilmente sobre la grilla 2x2\n",
                "\n",
                "for i, col in enumerate(columnas_cat):\n",
                "    sns.countplot(data=df, x=col, hue='Evasion', palette=colores, ax=axes[i])\n",
                "    axes[i].set_title(f\"Evasión por {nombres_titulos[i]}\", fontsize=14)\n",
                "    axes[i].set_xlabel(\"\") # Limpiamos el texto del eje X por estética\n",
                "    axes[i].set_ylabel(\"Número de Clientes\")\n",
                "    axes[i].legend(title=\"Evasión (1=Sí)\")\n",
                "    \n",
                "    # Si es el método de pago, rotamos las etiquetas para que se lean bien\n",
                "    if col == 'Metodo_Pago':\n",
                "        axes[i].tick_params(axis='x', rotation=45)\n",
                "\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 💡 Análisis Estratégico (Insights):\n",
                "Al observar estos gráficos, los patrones estratégicos se hacen evidentes de inmediato:\n",
                "1. **Tipo de Contrato:** El contrato \"Month-to-month\" (mes a mes) es absolutamente tóxico para la retención. La gran mayoría de las fugas provienen de aquí. Los contratos de 1 y 2 años tienen fugas casi nulas en comparación.\n",
                "2. **Servicio de Internet:** Los clientes de **Fibra Óptica** tienen una tasa de abandono preocupantemente alta en contraste con el ADSL. Esto sugiere investigar fallas en el servicio, precios demasiado altos de la fibra, o competidores más agresivos en ese segmento.\n",
                "3. **Método de Pago:** Los clientes que pagan con \"Electronic check\" (Cheque electrónico) son los más propensos a irse.\n",
                "4. **Adultos Mayores:** Aunque son un grupo pequeño (1), su proporción de evasión es visiblemente mayor comparada con los clientes jóvenes (0). Podrían estar experimentando barreras tecnológicas o problemas de soporte."
            ]
        }
    ]
    
    notebook["cells"].extend(new_cells)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)

if __name__ == "__main__":
    update_notebook_viz_categorical()
